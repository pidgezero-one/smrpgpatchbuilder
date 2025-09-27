from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import (
    shortify,
    shortify_signed,
    byte_signed,
    writeline,
)
import re
import os
import shutil
from smrpgpatchbuilder.datatypes.sprites.ids.sprite_ids import *
from copy import deepcopy
from typing import List, Tuple, Dict, Optional, Union
from dataclasses import dataclass, field
import numpy as np

# TODO: this game is hellbent on ruining my life
# ally run away animation has a jump that targets partway through another command (0x35053C)
# need to do something like specify an optional mid-command offset for jump targets

ORIGINS = [
    "ABSOLUTE_POSITION",
    "CASTER_INITIAL_POSITION",
    "TARGET_CURRENT_POSITION",
    "CASTER_CURRENT_POSITION",
]

EFFECTS = [
    "EF0000____DUMMY",
    "EF0001____DUMMY",
    "EF0002_THUNDERSHOCK",
    "EF0003_THUNDERSHOCK__BG_MASK_",
    "EF0004_CRUSHER",
    "EF0005_METEOR_BLAST",
    "EF0006_BOLT",
    "EF0007_STAR_RAIN",
    "EF0008_FLAME__FIRE_ENGULF_",
    "EF0009_MUTE__BALLOON_",
    "EF0010_FLAME_STONE",
    "EF0011_BOWSER_CRUSH",
    "EF0012_SPELL_CAST_SPADE",
    "EF0013_SPELL_CAST_HEART",
    "EF0014_SPELL_CAST_CLUB",
    "EF0015_SPELL_CAST_DIAMOND",
    "EF0016_SPELL_CAST_STAR",
    "EF0017_TERRORIZE",
    "EF0018_SNOWY__SNOW_BG__4BPP_",
    "EF0019_SNOWY__SNOW_FG__2BPP_",
    "EF0020_ENDOBUBBLE__BLACK_BALL_ORB_",
    "EF0021____DUMMY",
    "EF0022_SOLIDIFY",
    "EF0023____DUMMY",
    "EF0024____DUMMY",
    "EF0025_PSYCH_BOMB__BG_",
    "EF0026____DUMMY",
    "EF0027_DARK_STAR",
    "EF0028_WILLY_WISP__BLUE_ORB_BALL_BG_",
    "EF0029____DUMMY",
    "EF0030____DUMMY",
    "EF0031____DUMMY",
    "EF0032_GENO_WHIRL",
    "EF0033____DUMMY",
    "EF0034____DUMMY",
    "EF0035____DUMMY",
    "EF0036_BLANK_WHITE_FLASH__2BPP_",
    "EF0037_BLANK_WHITE_FLASH__4BPP_",
    "EF0038_BOULDER",
    "EF0039_BLACK_BALL_ORB",
    "EF0040_BLANK_BLUE_FLASH__2BPP_",
    "EF0041_BLANK_RED_FLASH__2BPP_",
    "EF0042_BLANK_BLUE_FLASH__4BPP_",
    "EF0043_BLANK_RED_FLASH__4BPP_",
    "EF0044____DUMMY",
    "EF0045_BLANK_DARK_BLUE_FLASH__2BPP_",
    "EF0046_BLANK_DARK_BLUE_FLASH__4BPP_",
    "EF0047_METEOR_SHOWER__SNOW_CONFETTI_",
    "EF0048_PURPLE_VIOLET_FLASH__4BPP_",
    "EF0049_BROWN_FLASH__4BPP_",
    "EF0050_DARK_RED_BLAST",
    "EF0051_DARK_BLUE_BLAST",
    "EF0052_SNOW_CONFETTI__GREEN",
    "EF0053_LIGHT_BLUE_BLAST",
    "EF0054_BLACK_BALL_ORB",
    "EF0055_RED_BALL_ORB",
    "EF0056_GREEN_BALL_ORB",
    "EF0057_SNOW_CONFETTI__SLATE_GREEN",
    "EF0058_SNOW_CONFETTI__RED",
    "EF0059_ORANGE_RED_BLAST__FIRE_BOMB_",
    "EF0060_ICE_BOMB_SOLIDIFY_BG__BLUE_FREEZE_",
    "EF0061_STATIC_E___ELECTRIC_BLAST_",
    "EF0062_GREEN_STAR_BUNCHES",
    "EF0063_BLUE_STAR_BUNCHES",
    "EF0064_PINK_STAR_BUNCHES",
    "EF0065_YELLOW_STAR_BUNCHES",
    "EF0066_AURORA_FLASH",
    "EF0067_STORM",
    "EF0068_ELECTROSHOCK",
    "EF0069_SMITHY_TREASURE_HEAD_SPELL__RED",
    "EF0070_SMITHY_TREASURE_HEAD_SPELL__GREEN",
    "EF0071_SMITHY_TREASURE_HEAD_SPELL__BLUE",
    "EF0072_SMITHY_TREASURE_HEAD_SPELL__YELLOW",
    "EF0073____DUMMY",
    "EF0074____DUMMY",
    "EF0075____DUMMY",
    "EF0076_FLAME_WALL__ORANGE_RED_FIRE_",
    "EF0077_PETAL_BLAST_1",
    "EF0078_PETAL_BLAST_2",
    "EF0079_DRAIN_BEAM_BG__4BPP_",
    "EF0080_DRAIN_BEAM_FG__2BPP_",
    "EF0081____DUMMY",
    "EF0082_ELECTRIC_BOLT",
    "EF0083_SAND_STORM_BG__2BPP_",
    "EF0084____DUMMY",
    "EF0085_POLLEN_NAP__YELLOW_POLLEN_",
    "EF0086_GENO_BEAM__BLUE",
    "EF0087_GENO_BEAM__RED",
    "EF0088_GENO_BEAM__GOLD",
    "EF0089_GENO_BEAM__YELLOW",
    "EF0090_GENO_BEAM__GREEN",
    "EF0091_THUNDERBOLT",
    "EF0092_LIGHT_BEAM",
    "EF0093_METEOR_SHOWER",
    "EF0094_S__CROW_DUST__PURPLE_POLLEN_",
    "EF0095_HP_RAIN_BG",
    "EF0096_HP_RAIN_FG",
    "EF0097_WAVY_DARK_BLUE_LINES",
    "EF0098_WAVY_BLUE_LINES",
    "EF0099_WAVY_RED_LINES",
    "EF0100_WAVY_BROWN_LINES",
    "EF0101_SAND_STORM_FG__4BPP_",
    "EF0102_SLEDGE",
    "EF0103_ARROW_RAIN",
    "EF0104_SPEAR_RAIN",
    "EF0105_SWORD_RAIN",
    "EF0106_LIGHTNING_ORB__BG_WAVES_",
    "EF0107_ECHOFINDER",
    "EF0108_POISON_GAS_FG_1",
    "EF0109_POISON_GAS_FG_2",
    "EF0110_POISON_GAS_BG",
    "EF0111_SMITHY_TRANSFORMS__BEAM_EFFECT_",
    "EF0112_SMELTER__S_MOLTEN_METAL",
    "EF0113____DUMMY",
    "EF0114____DUMMY",
    "EF0115____DUMMY",
    "EF0116____DUMMY",
    "EF0117____DUMMY",
    "EF0118____DUMMY",
    "EF0119____DUMMY",
    "EF0120____DUMMY",
    "EF0121____DUMMY",
    "EF0122____DUMMY",
    "EF0123____DUMMY",
    "EF0124____DUMMY",
    "EF0125____DUMMY",
    "EF0126____DUMMY",
    "EF0127____DUMMY",
]

FLASH_COLOURS = ["NO_COLOUR", "RED", "GREEN", "YELLOW", "BLUE", "PINK", "AQUA", "WHITE"]

BONUS_MESSAGES = [
    "BM_ATTACK",
    "BM_DEFENSE",
    "BM_UP",
    "BM_HPMAX",
    "BM_ONCE",
    "BM_AGAIN",
    "BM_LUCKY",
]

SCREEN_EFFECTS = [
    "SEF0000_GENO_FLASH",
    "SEF0001_SNOWY",
    "SEF0002_TERRORIZE",
    "SEF0003_SHOCKER",
    "SEF0004_UNKNOWN",
    "SEF0005_SLASH_INSTANT_DEATH",
    "SEF0006_SCREEN_FLASHES_WHITE",
    "SEF0007_CHANGE_BATTLEFIELD",
    "SEF0008_COME_BACK",
    "SEF0009_GENO_BEAM",
    "SEF0010_GENO_BLAST",
    "SEF0011_HOWL",
    "SEF0012_WIN_BATTLE_WINDOW",
    "SEF0013_SET_BATTLEFIELD_COORDS",
    "SEF0014_SQUASH_BIG_STAR",
    "SEF0015_UNKNOWN",
    "SEF0016_UNKNOWN",
    "SEF0017_CORONA",
    "SEF0018_MEGA_DRAIN",
    "SEF0019_UNKNOWN",
    "SEF0020_UNKNOWN",
]

SOUNDS = [
    "S0000_SILENCE",
    "S0001_MENU_SELECT",
    "S0002_MENU_CANCEL",
    "S0003_MENU_SCROLL",
    "S0004_JUMP",
    "S0005_BIRDIE_TWEET",
    "S0006_BONUS_FLOWER_STATUS_UP",
    "S0007_ERROR_INCORRECT_ANSWER",
    "S0008_GET_DIZZY",
    "S0009_ARROW_SLING",
    "S0010_MALLOW_PUNCH_1",
    "S0011_SWOOSH_RUN_AWAY",
    "S0012_BOMB_EXPLOSION",
    "S0013_COIN",
    "S0014_ITEM_GET",
    "S0015_SPIKE_STING",
    "S0016_BITE",
    "S0017_STAR_GUN_SHOOT",
    "S0018_SUPER_JUMP_HIT_1",
    "S0019_DRAIN_BEAM",
    "S0020_AURORA_FLASH",
    "S0021_SCARECROW_BIRDIES",
    "S0022_CORONA_DESCENDS",
    "S0023_SMALL_LASER",
    "S0024_NULL",
    "S0025_SLAP_BIG",
    "S0026_FLAME_WALL",
    "S0027_ITEM_1_UP",
    "S0028_FLAME",
    "S0029_FIRE_SHOOT",
    "S0030_FIRE_THROW",
    "S0031_FIRE_HIT",
    "S0032_FIRE_BURN",
    "S0033_INSERT",
    "S0034_",
    "S0035_SPELL_POWER_UP",
    "S0036_SNOW",
    "S0037_MONSTER_ITEM_TOSS",
    "S0038_FRYING_PAN_HIT_2",
    "S0039_CLAW",
    "S0040_PIERCE",
    "S0041_SUPER_JUMP_HIT_4",
    "S0042_BLADE",
    "S0043_COIN_SHOWERS_INTO_FOUNTAIN",
    "S0044_BOLT",
    "S0045_HP_RAIN_CLOUD",
    "S0046_PLASMA_BOUNCE",
    "S0047_DRY_CLUNK",
    "S0048_MALLOW_PUNCH_2",
    "S0049_CYMBAL_CRASH",
    "S0050_SUPER_JUMP_HIT_5",
    "S0051_FIRE_THROW_BIG",
    "S0052_FINGER_SHOT_BULLETS",
    "S0053_THWOMP_HIT_GROUND",
    "S0054_HAMMER_HIT_1",
    "S0055_HAMMER_HIT_2",
    "S0056_SUPER_JUMP_HIT_1_UP",
    "S0057_FIRE_SPOUT",
    "S0058_SUPER_JUMP_HIT_2",
    "S0059_SUPER_JUMP_HIT_3",
    "S0060_CYMBAL_RESONANCE",
    "S0061_ITEM_USE",
    "S0062_MONSTER_RUN_AWAY",
    "S0063_GENO_BLAST_IGNITION",
    "S0064_EGG_HATCH",
    "S0065_YOSHI_CANT_MAKE_COOKIE",
    "S0066_RECOVER_HP",
    "S0067_RECOVER_FP",
    "S0068_RECOVER_DRINK",
    "S0069_GENO_POWER_UP",
    "S0070_GENO_BEAM",
    "S0071_PSYCHOPATH_DRUM_ROLL",
    "S0072_PSYCHOPATH_CLOUD_APPEARS",
    "S0073_SPELL_NAME",
    "S0074_QUACK",
    "S0075_YOSHI_TALK",
    "S0076_STAT_BOOST_SINGLE",
    "S0077_STAT_BOOST_MULTI",
    "S0078_TIMED_STAT_BOOST",
    "S0079_RUMBLE_SINGLE",
    "S0080_WALLOP_1",
    "S0081_WALLOP_2",
    "S0082_WALLOP_3",
    "S0083_FRYING_PAN_HIT_1",
    "S0084_WALLOP_4",
    "S0085_WALLOP_5",
    "S0086_LONG_FALL",
    "S0087_BIG_BOUNCE",
    "S0088_TICKING_BOMB",
    "S0089_COMMON_MONSTER_EXPLOSION",
    "S0090_BIRDIE_CALL",
    "S0091_NULL",
    "S0092_SPEAR_RAIN_SINGLE",
    "S0093_BOWYER_ARROW_LOCK_BUTTON",
    "S0094_SHOCKER",
    "S0095_BOWSERS_CRUSHER",
    "S0096_RUMBLE_MULTI",
    "S0097_PLASMA_TOSS",
    "S0098_CLICK",
    "S0099_WILLY_WISP",
    "S0100_ELECTROSHOCK_SPARKS",
    "S0101_STENCH",
    "S0102_STATIC_E",
    "S0103_CRYSTAL_HITS",
    "S0104_BLIZZARD",
    "S0105_ROCK_CANDY",
    "S0106_LIGHT_BEAM",
    "S0107_BUBBLE_POP",
    "S0108_HOWL",
    "S0109_GENO_HAND_CANNON_SHOOT",
    "S0110_HUGE_EXPLOSION",
    "S0111_SLEDGE",
    "S0112_SWING",
    "S0113_GENO_FINGER_SHOT_HIT",
    "S0114_SPIKEY_ATTACK",
    "S0115_TRANSFORM",
    "S0116_TERRAPIN_SWING",
    "S0117_STING",
    "S0118_GENO_BLAST_END",
    "S0119_METEOR_SWARM",
    "S0120_DEEP_SWALLOW",
    "S0121_BIG_SWING",
    "S0122_POISONED",
    "S0123_CHOMP_BITE",
    "S0124_GOOMBA_ROLL",
    "S0125_SPIKE_SHOT",
    "S0126_FLOPPING_HIT",
    "S0127_LIQUID_DROPLET",
    "S0128_AMANITA_CURLS",
    "S0129_THROW",
    "S0130_VALOR_UP_VIGOR_UP",
    "S0131_ECHOING_BUBBLE",
    "S0132_STINGER_POISON",
    "S0133_LULLABY_SAD_SONG",
    "S0134_BOO_DISAPPEARS",
    "S0135_BOO_APPEARS",
    "S0136_BOO_APPROACHES",
    "S0137_BOWSER_CRUSH_STOMP",
    "S0138_ENDOBUBBLE",
    "S0139_GUITAR_STRING",
    "S0140_S_CROW_BELL",
    "S0141_LULLABY_MARIO_THEME",
    "S0142_DRY_BONES_ATTACK",
    "S0143_TOSS",
    "S0144_LIGHTNING_ORB",
    "S0145_ARTICHOKER_SPINES",
    "S0146_SLAP",
    "S0147_NULL",
    "S0148_SMITHY_BULLET_FINGERS",
    "S0149_ENEMY_JUMPS_HIGH",
    "S0150_ENEMY_TAUNTS_THEN_HITS",
    "S0151_SPORES",
    "S0152_HIT",
    "S0153_GUERRILLA_THINKS",
    "S0154_BUZZING_BEE",
    "S0155_SPARKY_HIT",
    "S0156_CHOMP_BITE",
    "S0157_ENIGMA_SCATTERS",
    "S0158_YELP",
    "S0159_BIG_DEEP_HIT",
    "S0160_SLAP",
    "S0161_SPORE_CHIMES_DOOM_REVERB",
    "S0162_NULL",
    "S0163_NULL",
    "S0164_CARROBOSCIS_ATTACK",
    "S0165_SKY_TROOPA_FLAPS",
    "S0166_TAPPING_FEET",
    "S0167_BELOME_EATS",
    "S0168_TERRAPIN_ATTACK",
    "S0169_TELEPORT_ATTACK",
    "S0170_SUBMERGED_UNDER",
    "S0171_SLAP_POWERFUL",
    "S0172_WEAPON_TIMING",
    "S0173_TERRORIZE",
    "S0174_SOLIDIFY",
    "S0175_DEATHSICKLE",
    "S0176_BOSS_FADE_OUT_DEATH",
    "S0177_POISON_GAS_1",
    "S0178_POISON_GAS_2",
    "S0179_SLEEPY_BOMB",
    "S0180_SLEEPY_TIME_TIMED",
    "S0181_LAMB_S_LURE_SINGLE",
    "S0182_SHEEP_ATTACK_1",
    "S0183_FLOATING_LAMB",
    "S0184_SHEEP_ATTACK_2_MULTI",
    "S0185_GENO_FLASH_SHOOT",
    "S0186_GENO_FLASH_EXPLOSION",
    "S0187_MUTE_BALLOON_RISES",
    "S0188_PETAL_BLAST",
    "S0189_POLLEN_NAP",
    "S0190_COME_BACK",
    "S0191_MUTE_BALLOON_FAILS",
    "S0192_BIG_SHELL_KICK",
    "S0193_BIG_SHELL_HIT_1",
    "S0194_BIG_SHELL_HIT_2",
    "S0195_EXPLOSIVE_HIT",
    "S0196_GENO_FLASH_TRANSFORMATION",
    "S0197_GENO_STAR_GUN_HIT",
    "S0198_ICE_ROCK",
    "S0199_ARROW_RAIN",
    "S0200_SPEAR_RAIN_MULTI",
    "S0201_SWORD_RAIN",
    "S0202_CORONA_FLASH",
    "S0203_MEGA_DRAIN_SINGLE",
    "S0204_CHOMPING",
    "S0205_JINXED",
    "S0206_MONSTER_SWING",
    "S0207_MONSTER_TAUNT",
    "S0208_SMITHY_FORM_1_LIGHT_UP",
    "S0209_SMITHY_FORM_1_TRANSFORM",
    "S0210_BOOSTER_EXPRESS_TRAIN_HORN",
]
MUSIC = [
    "M0000_CURRENT",
    "M0001_DODO_SCOMING",
    "M0002_MUSHROOMKINGDOM",
    "M0003_FIGHTAGAINSTSTRONGERMONSTER",
    "M0004_YO_STERISLAND",
    "M0005_SEASIDETOWN",
    "M0006_FIGHTAGAINSTMONSTERS",
    "M0007_PIPEVAULT",
    "M0008_INVINCIBLESTAR",
    "M0009_VICTORY",
    "M0010_INTHEFLOWERGARDEN",
    "M0011_BOWSER_SCASTLE_1STTIME",
    "M0012_FIGHTAGAINSTBOWSER",
    "M0013_ROADISFULLOFDANGERS",
    "M0014_MARIO_SPAD",
    "M0015_HERE_SSOMEWEAPONS",
    "M0016_LET_SRACE",
    "M0017_TADPOLEPOND",
    "M0018_ROSETOWN",
    "M0019_RACETRAINING",
    "M0020_SHOCK",
    "M0021_SADSONG",
    "M0022_MIDASRIVER",
    "M0023_GOTASTARPIECE_PART1",
    "M0024_GOTASTARPIECE_PART2",
    "M0025_FIGHTAGAINSTANARMEDBOSS",
    "M0026_FORESTMAZE",
    "M0027_DUNGEONISFULLOFMONSTERS",
    "M0028_LET_SPLAYGENO",
    "M0029_STARTSLOTMENU",
    "M0030_LONGLONGAGO",
    "M0031_BOOSTER_STOWER",
    "M0032_ANDMYNAME_SBOOSTER",
    "M0033_MOLEVILLE",
    "M0034_STARHILL",
    "M0035_MOUNTAINRAILROAD",
    "M0036_EXPLANATION",
    "M0037_BOOSTERHILL_START",
    "M0038_BOOSTERHILL",
    "M0039_MARRYMORE",
    "M0040_NEWPARTNER",
    "M0041_SUNKENSHIP",
    "M0042_STILLTHEROADISFULLOFMONSTERS",
    "M0043_SILENCE",
    "M0044_SEA",
    "M0045_HEARTBEATINGALITTLEFASTER_PART1",
    "M0046_HEARTBEATINGALITTLEFASTER_PART2",
    "M0047_GRATEGUY_SCASINO",
    "M0048_GENOAWAKENS",
    "M0049_CELEBRATIONAL",
    "M0050_NIMBUSLAND",
    "M0051_MONSTROTOWN",
    "M0052_TOADOFSKY",
    "M0053_SILENCE",
    "M0054_HAPPYADVENTURE_DELIGHFULADVENTURE",
    "M0055_WORLDMAP",
    "M0056_FACTORY",
    "M0057_SWORDCRASHESANDSTARSSCATTER",
    "M0058_CONVERSATIONWITHCULEX",
    "M0059_FIGHTAGAINSTCULEX",
    "M0060_VICTORYAGAINSTCULEX",
    "M0061_VALENTINA",
    "M0062_BARRELVOLCANO",
    "M0063_AXEMRANGERSDROPIN",
    "M0064_THEEND",
    "M0065_GATE",
    "M0066_BOWSER_SCASTLE_2NDTIME",
    "M0067_WEAPONSFACTORY",
    "M0068_FIGHTAGAINSTSMITHY1",
    "M0069_FIGHTAGAINSTSMITHY2",
    "M0070_ENDINGPART1",
    "M0071_ENDINGPART2",
    "M0072_ENDINGPART3",
    "M0073_ENDINGPART4",
]

TARGETS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "UNKNOWN_05",
    "UNKNOWN_06",
    "UNKNOWN_07",
    "UNKNOWN_08",
    "UNKNOWN_09",
    "UNKNOWN_10",
    "UNKNOWN_11",
    "UNKNOWN_12",
    "UNKNOWN_13",
    "UNKNOWN_14",
    "UNKNOWN_15",
    "CHARACTER_IN_SLOT_1",
    "CHARACTER_IN_SLOT_2",
    "CHARACTER_IN_SLOT_3",
    "MONSTER_1_SET",
    "MONSTER_2_SET",
    "MONSTER_3_SET",
    "MONSTER_4_SET",
    "MONSTER_5_SET",
    "MONSTER_6_SET",
    "MONSTER_7_SET",
    "MONSTER_8_SET",
    "SELF",
    "ALL_ALLIES_NOT_SELF",
    "RANDOM_ALLY_NOT_SELF",
    "ALL_ALLIES_AND_SELF",
    "RANDOM_ALLY_OR_SELF",
    "UNKNOWN_32",
    "UNKNOWN_33",
    "UNKNOWN_34",
    "ALL_OPPONENTS",
    "AT_LEAST_ONE_OPPONENT",
    "RANDOM_OPPONENT",
    "UNKNOWN_38",
    "AT_LEAST_ONE_ALLY",
    "MONSTER_1_CALL",
    "MONSTER_2_CALL",
    "MONSTER_3_CALL",
    "MONSTER_4_CALL",
    "MONSTER_5_CALL",
    "MONSTER_6_CALL",
    "MONSTER_7_CALL",
    "MONSTER_8_CALL",
]

ITEMS = [
    None,
    None,
    None,
    None,
    None,
    "Hammer",
    "FroggieStick",
    "NokNokShell",
    "PunchGlove",
    "FingerShot",
    "Cymbals",
    "Chomp",
    "Masher",
    "ChompShell",
    "SuperHammer",
    "HandGun",
    "WhompGlove",
    "SlapGlove",
    "TroopaShell",
    "Parasol",
    "HurlyGloves",
    "DoublePunch",
    "RibbitStick",
    "SpikedLink",
    "MegaGlove",
    "WarFan",
    "HandCannon",
    "StickyGlove",
    "UltraHammer",
    "SuperSlap",
    "DrillClaw",
    "StarGun",
    "SonicCymbal",
    "LazyShellWeapon",
    "FryingPan",
    "LuckyHammer",
    None,
    "Shirt",
    "Pants",
    "ThickShirt",
    "ThickPants",
    "MegaShirt",
    "MegaPants",
    "WorkPants",
    "MegaCape",
    "HappyShirt",
    "HappyPants",
    "HappyCape",
    "HappyShell",
    "PolkaDress",
    "SailorShirt",
    "SailorPants",
    "SailorCape",
    "NauticaDress",
    "CourageShell",
    "FuzzyShirt",
    "FuzzyPants",
    "FuzzyCape",
    "FuzzyDress",
    "FireShirt",
    "FirePants",
    "FireCape",
    "FireShell",
    "FireDress",
    "HeroShirt",
    "PrincePants",
    "StarCape",
    "HealShell",
    "RoyalDress",
    "SuperSuit",
    "LazyShellArmor",
    None,
    None,
    None,
    "ZoomShoes",
    "SafetyBadge",
    "JumpShoes",
    "SafetyRing",
    "Amulet",
    "ScroogeRing",
    "ExpBooster",
    "AttackScarf",
    "RareScarf",
    "BtubRing",
    "AntidotePin",
    "WakeUpPin",
    "FearlessPin",
    "TrueformPin",
    "CoinTrick",
    "GhostMedal",
    "JinxBelt",
    "Feather",
    "TroopaPin",
    "SignalRing",
    "QuartzCharm",
    None,
    "Mushroom",
    "MidMushroom",
    "MaxMushroom",
    "HoneySyrup",
    "MapleSyrup",
    "RoyalSyrup",
    "PickMeUp",
    "AbleJuice",
    "Bracer",
    "Energizer",
    "YoshiAde",
    "RedEssence",
    "KerokeroCola",
    "YoshiCookie",
    "PureWater",
    "SleepyBomb",
    "BadMushroom",
    "FireBomb",
    "IceBomb",
    "FlowerTab",
    "FlowerJar",
    "FlowerBox",
    "YoshiCandy",
    "FroggieDrink",
    "MukuCookie",
    "Elixir",
    "Megalixir",
    "SeeYa",
    "TempleKey",
    "GoodieBag",
    "EarlierTimes",
    "FreshenUp",
    "RareFrogCoin",
    "Wallet",
    "CricketPie",
    "RockCandy",
    "CastleKey1",
    None,
    "CastleKey2",
    "BambinoBomb",
    "SheepAttack",
    "CarboCookie",
    "ShinyStone",
    None,
    "RoomKey",
    "ElderKey",
    "ShedKey",
    "LambsLure",
    "FrightBomb",
    "MysteryEgg",
    None,
    None,
    "LuckyJewel",
    None,
    "SopranoCard",
    "AltoCard",
    "TenorCard",
    "Crystalline",
    "PowerBlast",
    "WiltShroom",
    "RottenMush",
    "MoldyMush",
    "Seed",
    "Fertilizer",
    "WasteBasket",
    "BigBooFlag",
    "DryBonesFlag",
    "GreaperFlag",
    None,
    None,
    "CricketJam",
    None,
    None,
    None,
    None,
    None,
    "Fireworks",
    None,
    "BrightCard",
    "Mushroom2",
    "StarEgg",
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "Shoes",
    "Brooch",
    "Ring",
    "Crown",
]

MASKS = [
    "NO_MASK",
    "INCLINE_1",
    "INCLINE_2",
    "CIRCLE_MASK",
    "DOME_MASK",
    "POLYGON_MASK",
    "WAVY_CIRCLE_MASK",
    "CYLINDER_MASK",
]

ENEMIES = [
    "Terrapin",
    "Spikey",
    "Skytroopa",
    "MadMallet",
    "Shaman",
    "Crook",
    "Goomba",
    "PiranhaPlant",
    "Amanita",
    "Goby",
    "Bloober",
    "BandanaRed",
    "Lakitu",
    "Birdy",
    "Pinwheel",
    "Ratfunk",
    "K9",
    "Magmite",
    "TheBigBoo",
    "DryBones",
    "Greaper",
    "Sparky",
    "Chomp",
    "Pandorite",
    "ShyRanger",
    # "BobombHenchman", # TODO rando shold reaplce all of these Bobombs
    "Bobomb",
    "Spookum",
    "HammerBro",
    "Buzzer",
    "Ameboid",
    "Gecko",
    "Wiggler",
    "Crusty",
    "Magikoopa",
    "Leuko",
    "Jawful",
    "Enigma",
    "Blaster",
    "Guerrilla",
    "Babayaga",
    "Hobgoblin",
    "Reacher",
    "Shogun",
    "Orbuser",
    "HeavyTroopa",
    "Shadow",
    "Cluster",
    # "BahamuttMagikoopa",
    "Bahamutt",  # same as bobombhenchman
    "Octolot",
    "Frogog",
    "Clerk",
    "Gunyolk",
    "Boomer",
    "Remocon",
    "Snapdragon",
    "Stumpet",
    "Dodo",
    "Jester",
    "Artichoker",
    "Arachne",
    "Carriboscis",
    "Hippopo",
    "Mastadoom",
    "Corkpedite",
    "Terracotta",
    "Spikester",
    "Malakoopa",
    "Pounder",
    "Poundette",
    "Sackit",
    "GuGoomba",
    "Chewy",
    "Fireball",
    "CrookHenchman",
    "MrKipper",
    "FactoryChief",
    "BandanaBlue",
    "Manager",
    "Bluebird",
    "AlleyRat",
    "Chow",
    "Magmus",
    "LilBoo",
    "Vomer",
    "GlumReaper",
    "Pyrosphere",
    "ChompChomp",
    "Hidon",
    "SlingShy",
    "Robomb",
    "ShyGuy",
    "Ninja",
    "Stinger",
    "Goombette",
    "Geckit",
    "Jabit",
    "Starcruster",
    "Merlin",
    "Muckle",
    "Forkies",
    "Gorgon",
    "BigBertha",
    "ChainedKong",
    "Fautso",
    "Strawhead",
    "Juju",
    "ArmoredAnt",
    "Orbison",
    "TuboTroopa",
    "Doppel",
    "Pulsar",
    "Bobomb",
    "Octovader",
    "Ribbite",
    "Director",
    "SnifitHenchman",
    "None",
    "Puppox",
    "FinkFlower",
    "Lumbler",
    "Springer",
    "Harlequin",
    "Kriffid",
    "Spinthra",
    "Radish",
    "Crippo",
    "MastaBlasta",
    "Piledriver",
    "Apprentice",
    "ApprenticeHenchman",
    "BandanaRedHenchman",
    "PiranhaPlantHenchman",
    "None",
    "MadMalletHenchman",
    "BoxBoy",
    "Shelly",
    "Superspike",
    "DodoSolo",
    "Oerlikon",
    "Chester",
    "CorkpediteBody",
    "BluebirdHenchman",
    "Torte",
    "Shyaway",
    "JinxClone",
    "MachineMadeShyster",
    "MachineMadeDrillBit",
    "Formless",
    "Mokura",
    "FireCrystal",
    "WaterCrystal",
    "EarthCrystal",
    "WindCrystal",
    "MarioClone",
    "PeachClone",
    "BowserClone",
    "GenoClone",
    "MallowClone",
    "Shyster",
    "Kinklink",
    "BirdyHenchman",
    "HanginShy",
    "Smelter",
    "MachineMadeMack",
    "MachineMadeBowyer",
    "MachineMadeYaridovich",
    "MachineMadeAxemPink",
    "MachineMadeAxemBlack",
    "MachineMadeAxemRed",
    "MachineMadeAxemYellow",
    "MachineMadeAxemGreen",
    "BahamuttChester",
    "BlooberHenchman",
    "MachineMadeAxemBlackHenchman",
    "MachineMadeAxemPinkHenchman",
    "AeroSmithy",
    "Starslap",
    "Mukumuku",
    "Zeostar",
    "Jagger",
    "EmptyEnemy",
    "Smithy2TankHead",
    "Smithy2SafeHead",
    "PyrosphereHenchman",
    "Microbomb",
    "ShyGuyHenchman",
    "Grit",
    "Neosquid",
    "YaridovichMirage",
    "Helio",
    "RightEye",
    "LeftEye",
    "KnifeGuy",
    "GrateGuy",
    "Bundt",
    "Jinx1",
    "Jinx2",
    "CountDown",
    "DingALing",
    "Belome1",
    "Belome2",
    "MachineMadeAxemRedHenchman",
    "Smilax",
    "Thrax",
    "Megasmilax",
    "Birdo",
    "Eggbert",
    "AxemYellow",
    "Punchinello",
    "TentaclesRight",
    "AxemRed",
    "AxemGreen",
    "KingBomb",
    "MezzoBomb",
    "MachineMadeShysterHenchman",
    "Raspberry",
    "KingCalamari",
    "TentaclesLeft",
    "Jinx3",
    "Zombone",
    "CzarDragon",
    "Cloaker",
    "Domino",
    "MadAdder",
    "Mack",
    "Bodyguard",
    "Yaridovich",
    "DrillBit",
    "AxemPink",
    "AxemBlack",
    "Bowyer",
    "AeroBowyer",
    "MachineMadeAxemGreenHenchman",
    "Exor",
    "Smithy1",
    "Shyper",
    "Smithy2Body",
    "Smithy2Head",
    "Smithy2MageHead",
    "Smithy2ChestHead",
    "Croco1",
    "Croco2",
    "MachineMadeAxemYellowHenchman",
    "Earthlink",
    "YaridovichDrillBit",
    "AxemRangers",
    "Booster",
    "Booster2",
    "Snifit",
    "Johnny",
    "JohnnySolo",
    "Valentina",
    "Cloaker2",
    "Domino2",
    "Candle",
    "Culex",
]

SCRIPT_NAMES = {
    "battle_events": [
        "BE0000_UNUSED",
        "BE0001_UNUSED",
        "BE0002_BELOME_SWALLOWS_MALLOW",
        "BE0003_UNUSED",
        "BE0004_MACK_JUMPS_OUT_OF_BATTLE_OFF_SCREEN",
        "BE0005_MACK_RETURNS_TO_BATTLE",
        "BE0006_BELOME_SPITS_OUT_MALLOW",
        "BE0007_COUNTDOWN_RUNS_SCHEDULE_1_00_3_00_5_00_6_00_7_00",
        "BE0008_COUNTDOWN_RUNS_SCHEDULE_6_00_9_00_10_00_12_00",
        "BE0009_PUNCHINELLO_INTERLUDES_AND_PREPARES_TO_SUMMON_BOB_OMBS",
        "BE0010_PUNCHINELLO_INTERLUDES_AND_PREPARES_TO_SUMMON_MEZZO_BOMBS",
        "BE0011_SOLO_EARTH_CRYSTAL_APPEARS",
        "BE0012_DIALOGUE_FROM_BOOSTER_FIGHT",
        "BE0013_UNKNOWN",
        "BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT",
        "BE0015_CROCO_STEALS_ITEMS_YOU_WANT_THEM_BACK",
        "BE0016_CROCO_RETURNS_ITEMS_ENOUGH_HERE_S_YOUR_JUNK",
        "BE0017_UNUSED",
        "BE0018_KNIFE_GUY_GRATE_GUY_PAIR_UP_PIGGY_BACK",
        "BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH",
        "BE0020_SOLO_WATER_CRYSTAL_APPEARS",
        "BE0021_JOHNNY_CHALLENGES_MARIO_TO_A_ONE_ON_ONE",
        "BE0022_YARIDOVICH_MIRAGE_ATTACK",
        "BE0023_YARIDOVICH_MIRAGE_IS_DESTROYED_RETURN_TO_SINGLE_FORM",
        "BE0024_MACHINE_MADE_YARIDOVICH_MULTIPLIER",
        "BE0025_DRILL_BIT",
        "BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES",
        "BE0027_BEAT_TENTACLES_MOVE_ON_TO_NEXT",
        "BE0028_BEAT_TENTACLES_MOVE_ON_TO_KING_CALAMARI",
        "BE0029_UNUSED",
        "BE0030_UNUSED",
        "BE0031_UNUSED",
        "BE0032_BUNDT_MOVES_AGAIN_BOTH_COOKS_RUN_AWAY",
        "BE0033_CANDLES_APPEAR_ON_BUNDT",
        "BE0034_BLOW_THOSE_CANDLES_OUT",
        "BE0035_SOLO_WIND_CRYSTAL_APPEARS",
        "BE0036_TENTACLES_THROW_CHARACTER_OFF_SCREEN",
        "BE0037_UNUSED",
        "BE0038_UNUSED",
        "BE0039_UNUSED",
        "BE0040_UNUSED",
        "BE0041_UNUSED",
        "BE0042_BB_BOMBS_EXPLODE",
        "BE0043_UNUSED",
        "BE0044_CZAR_DRAGON_DIES",
        "BE0045_ZOMBONE_DIES",
        "BE0046_CZAR_DRAGON_SUMMONS_HELIOS",
        "BE0047_UNKNOWN",
        "BE0048_VALENTINA_SUMMONS_DODO_DODO_CARRIES_OFF_MIDDLE_CHARACTER",
        "BE0049_DODO_FLUTTERS_AND_LEAVES_BATTLE",
        "BE0050_DODO_RETURNS_TO_VALENTINA_S_FORMATION",
        "BE0051_UNUSED",
        "BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION",
        "BE0053_DOMINO_TEAMS_UP_WITH_MAD_ADDER",
        "BE0054_CLOAKER_TEAMS_UP_WITH_EARTHLINK",
        "BE0055_SHY_AWAY_WATERS_SMILAX_PART_1",
        "BE0056_SHY_AWAY_WATERS_SMILAX_PART_2",
        "BE0057_SHY_AWAY_WATERS_SMILAX_PART_3",
        "BE0058_THRAX_IS_THERE",
        "BE0059_BELOME_CONFRONTS_A_CHARACTER_YOU_ALL_LOOK_DELICIOUS",
        "BE0060_BELOME_CLONES_SOMEONE",
        "BE0061_ONLY_MARIO_IS_THERE",
        "BE0062_UNUSED",
        "BE0063_UNUSED",
        "BE0064_UNUSED",
        "BE0065_UNUSED",
        "BE0066_UNUSED",
        "BE0067_AXEM_RANGERS_GROUP_FORMATION",
        "BE0068_UNUSED",
        "BE0069_AXEM_RANGERS_ARE_DEFEATED",
        "BE0070_JINX_USES_JINXED",
        "BE0071_JINX_USES_TRIPLE_KICK",
        "BE0072_JINX_USES_QUICKSILVER",
        "BE0073_JINX_USES_BOMBS_AWAY",
        "BE0074_CULEX_SUMMONS_CRYSTALS",
        "BE0075_FORMLESS_CHANGES_INTO_MOKURA",
        "BE0076_SOLO_FIRE_CRYSTAL_APPEARS",
        "BE0077_SCREEN_FLASHES_WHITE",
        "BE0078_DODO_FLUTTERS_AND_EXITS_BATTLE",
        "BE0079_MAGIKOOPA_SUMMONS_MONSTER",
        "BE0080_EXOR_FIGHT_BEGINS",
        "BE0081_EXOR_IS_DEFEATED_CRIES_AND_OPENS_MOUTH",
        "BE0082_SMITHY_1ST_FORM_IS_BEATEN_GROUND_SHAKES_ETC",
        "BE0083_SCREEN_FLASHES_WHITE",
        "BE0084_SCREEN_FLASHES_WHITE",
        "BE0085_FEAR_ROULETTE",
        "BE0086_SMELTER_POURS_MOLTEN_LIQUID_SMITHY_WELDS",
        "BE0087_SMITHY_TRANSFORMS_INTO_TANK_HEAD",
        "BE0088_SMITHY_TRANSFORMS_INTO_MAGIC_HEAD",
        "BE0089_SMITHY_TRANSFORMS_INTO_CHEST_HEAD",
        "BE0090_SMITHY_TRANSFORMS_INTO_BOX_HEAD",
        "BE0091_SMITHY_S_HEAD_FADES_BEFORE_TRANSFORMING_INTO_OTHER_HEAD",
        "BE0092_SHELLY_BREAKS",
        "BE0093_BEAM_OF_LIGHT_FORMS_AROUND_SMITHY_HEAD_BEFORE_BODY_APPEARS",
        "BE0094_PUNCHINELLO_S_BOMBS_EXPLODE_IF_STILL_ALIVE",
        "BE0095_BOMBS_EXPLODE",
        "BE0096_NOTHING",
        "BE0097_SMITHY_WAITS_BEFORE_TRANSFORMING_HEAD",
        "BE0098_SMITHY_IS_DEFEATED",
        "BE0099_UNKNOWN",
        "BE0100_EARTHLINK_MAD_ADDER_COLLAPSES_AND_DIES",
        "BE0101_MAGIKOOPA_IS_THERE",
        "BE0102_NONE",
    ],
    
    "ally_spells": [
        "Jump",
        "Fire Orb",
        "Super Jump",
        "Super Flame",
        "Ultra Jump",
        "Ultra Flame",
        "Therapy",
        "Group Hug",
        "Sleepy Time",
        "Come Back",
        "Mute",
        "Psych Bomb",
        "Terrorize",
        "Poison Gas",
        "Crusher",
        "Bowser Crush",
        "Geno Beam",
        "Geno Boost",
        "Geno Whirl",
        "Geno Blast",
        "Geno Flash",
        "Thunderbolt",
        "HP Rain",
        "Psychopath",
        "Shocker",
        "Snowy",
        "Star Rain",
    ],
    "flower_bonus": [
        "(empty flower bonus message)",
        "Attack Up!",
        "Defense Up!",
        "HP Max!",
        "Once Again!",
        "Lucky!",
    ],
    "items": [  # offset 96
        "Mushroom",
        "MidMushroom",
        "MaxMushroom",
        "HoneySyrup",
        "MapleSyrup",
        "RoyalSyrup",
        "PickMeUp",
        "AbleJuice",
        "Bracer",
        "Energizer",
        "YoshiAde",
        "RedEssence",
        "KerokeroCola",
        "YoshiCookie",
        "PureWater",
        "SleepyBomb",
        "BadMushroom",
        "FireBomb",
        "IceBomb",
        "FlowerTab",
        "FlowerJar",
        "FlowerBox",
        "YoshiCandy",
        "FroggieDrink",
        "MukuCookie",
        "Elixir",
        "Megalixir",
        "SeeYa",
        "TempleKey",
        "GoodieBag",
        "EarlierTimes",
        "FreshenUp",
        "RareFrogCoin",
        "Wallet",
        "CricketPie",
        "RockCandy",
        "CastleKey1",
        "DebugBomb",
        "CastleKey2",
        "BambinoBomb",
        "SheepAttack",
        "CarboCookie",
        "ShinyStone",
        "DUMMY_43" "RoomKey",
        "ElderKey",
        "ShedKey",
        "LambsLure",
        "FrightBomb",
        "MysteryEgg",
        "BeetleBox",
        "BeetleBox2",
        "LuckyJewel",
        "DUMMY_53" "SopranoCard",
        "AltoCard",
        "TenorCard",
        "Crystalline",
        "PowerBlast",
        "WiltShroom",
        "RottenMush",
        "MoldyMush",
        "Seed",
        "Fertilizer",
        "WasteBasket",
        "BigBooFlag",
        "DryBonesFlag",
        "GreaperFlag",
        "SecretGame",
        "ScrowBomb",
        "CricketJam",
        "BaneBomb",
        "DoomBomb",
        "FearBomb",
        "SleepBomb",
        "MuteBomb",
        "Fireworks",
        "Bomb",
        "BrightCard",
        "Mushroom2",
        "StarEgg",
    ],
    "ally_behaviours": [
        'Ally behaviour unindexed: unknown 0x350462',
        'Ally behaviour 0: flinch animation',
        'Ally behaviour unindexed: unknown 0x350484',
        'Ally behaviour unindexed: Mario/DUMMY A attack',
        'Ally behaviour unindexed: Mario/DUMMY Y attack',
        'Ally behaviour unindexed: Mario/DUMMY X item',
        'Ally behaviour unindexed: victory pose',
        'Ally behaviour 1: run away attempt',

        'Ally behaviour unindexed: unknown 0x350462',
        'Ally behaviour 0: flinch animation',
        'Ally behaviour unindexed: unknown 0x350484',
        'Ally behaviour unindexed: Peach A attack',
        'Ally behaviour unindexed: Peach Y attack',
        'Ally behaviour unindexed: Peach X item',
        'Ally behaviour unindexed: victory pose',
        'Ally behaviour 1: run away attempt',

        'Ally behaviour unindexed: unknown 0x350462',
        'Ally behaviour 0: flinch animation',
        'Ally behaviour unindexed: unknown 0x350484',
        'Ally behaviour unindexed: Bowser A attack',
        'Ally behaviour unindexed: Bowser Y attack',
        'Ally behaviour unindexed: Bowser X item',
        'Ally behaviour unindexed: victory pose',
        'Ally behaviour 1: run away attempt',

        'Ally behaviour unindexed: unknown 0x350462',
        'Ally behaviour 0: flinch animation',
        'Ally behaviour unindexed: unknown 0x350484',
        'Ally behaviour unindexed: Geno A attack',
        'Ally behaviour unindexed: Geno Y attack',
        'Ally behaviour unindexed: Geno X item',
        'Ally behaviour unindexed: victory pose',
        'Ally behaviour 1: run away attempt',

        'Ally behaviour unindexed: unknown 0x350462',
        'Ally behaviour 0: flinch animation',
        'Ally behaviour unindexed: unknown 0x350484',
        'Ally behaviour unindexed: Mallow A attack',
        'Ally behaviour unindexed: Mallow Y attack',
        'Ally behaviour unindexed: Mallow X item',
        'Ally behaviour unindexed: victory pose',
        'Ally behaviour 1: run away attempt',

        'Ally behaviour unindexed: unknown 0x350462',
        'Ally behaviour 0: flinch animation',
        'Ally behaviour unindexed: unknown 0x350484',
        'Ally behaviour unindexed: unknown 0x350488 (mario/dummy)',
        'Ally behaviour unindexed: unknown 0x3504AB (mario/dummy)',
        'Ally behaviour unindexed: unknown 0x3504CE (mario/dummy)',
        'Ally behaviour unindexed: victory pose',
        'Ally behaviour 1: run away attempt',
    ],
    "monster_behaviours_1": [  # 5
        'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit'
        'Monster behaviour 1: flinch animation of sprite behaviours: no movement for "Escape"',
        'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 8: escape animation of sprite behaviours: no movement for "Escape", no reaction when hit',
        'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
        'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 2: flinch animation of sprite behaviours: slide backward when hit",
        'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 9: escape animation of sprite behaviours: slide backward when hit, Bowser Clone sprite, Mario Clone sprite",
        'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
        'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 3: flinch animation of sprite behaviours: Bowser Clone sprite",
        'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 9: escape animation of sprite behaviours: slide backward when hit, Bowser Clone sprite, Mario Clone sprite",
        'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
        'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 4: flinch animation of sprite behaviours: Mario Clone sprite",
        'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 9: escape animation of sprite behaviours: slide backward when hit, Bowser Clone sprite, Mario Clone sprite",
        'Monster behaviour 10: KO animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite',
        'Monster behaviour 0: entrance animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        "Monster behaviour 5: flinch animation of sprite behaviours: no reaction when hit",
        'Monster behaviour 6: initiate spell animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 7: initiate attack animation of sprite behaviours: no movement for "Escape", slide backward when hit, Bowser Clone sprite, Mario Clone sprite, no reaction when hit',
        'Monster behaviour 8: escape animation of sprite behaviours: no movement for "Escape", no reaction when hit',
        "Monster behaviour 11: KO animation of sprite behaviours: no reaction when hit",
    ],
    "monster_behaviours_2": [  # 1
        "Monster behaviour 12: entrance animation of sprite behaviours: sprite shadow",
        "Monster behaviour 13: flinch animation of sprite behaviours: sprite shadow",
        "Monster behaviour 14: initiate spell animation of sprite behaviours: sprite shadow",
        "Monster behaviour 15: initiate attack animation of sprite behaviours: sprite shadow",
        "Monster behaviour 16: escape animation of sprite behaviours: sprite shadow",
        "Monster behaviour 17: KO animation of sprite behaviours: sprite shadow",
    ],
    "monster_behaviours_3": [  # 2
        "Monster behaviour 18: entrance animation of sprite behaviours: floating, sprite shadow",
        "Monster behaviour 20: flinch animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 21: initiate spell animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 22: initiate attack animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 23: escape animation of sprite behaviours: floating, sprite shadow",
        "Monster behaviour 25: KO animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 19: entrance animation of sprite behaviours: floating",
        "Monster behaviour 20: flinch animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 21: initiate spell animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 22: initiate attack animation of sprite behaviours: floating, sprite shadow, floating",
        "Monster behaviour 24: escape animation of sprite behaviours: floating",
        "Monster behaviour 25: KO animation of sprite behaviours: floating, sprite shadow, floating",
    ],
    "monster_behaviours_4": [  # 3
        "Monster behaviour 26: entrance animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 27: flinch animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
        "Monster behaviour 29: initiate spell animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
        "Monster behaviour 31: initiate attack animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 32: escape animation of sprite behaviours: floating, slide backward when hit (1)",
        "Monster behaviour 35: KO animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 26: entrance animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 27: flinch animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
        "Monster behaviour 29: initiate spell animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2)",
        "Monster behaviour 31: initiate attack animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 33: escape animation of sprite behaviours: floating, slide backward when hit (2)",
        "Monster behaviour 35: KO animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 26: entrance animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 28: flinch animation of sprite behaviours: fade out death, floating",
        "Monster behaviour 30: initiate spell animation of sprite behaviours: fade out death, floating",
        "Monster behaviour 31: initiate attack animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
        "Monster behaviour 34: escape animation of sprite behaviours: fade out death, floating",
        "Monster behaviour 35: KO animation of sprite behaviours: floating, slide backward when hit (1), floating, slide backward when hit (2), fade out death, floating",
    ],
    "monster_behaviours_5": [  # 4
        'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 39: initiate spell aanimation of sprite behaviours: fade out death (1), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        "Monster behaviour 41: escape animation of sprite behaviours: fade out death (1), fade out death (2)",
        'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        "Monster behaviour 38: initiate spell aanimation of sprite behaviours: fade out death (2)",
        'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        "Monster behaviour 41: escape animation of sprite behaviours: fade out death (1), fade out death (2)",
        'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 39: initiate spell aanimation of sprite behaviours: fade out death (1), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        "Monster behaviour 42: escape animation of sprite behaviours: fade out death, Smithy spell cast",
        'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 36: entrance animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 37: flinch animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 39: initiate spell aanimation of sprite behaviours: fade out death (1), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 40: initiate attack animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
        'Monster behaviour 43: escape animation of sprite behaviours: fade out death, no "Escape" movement',
        'Monster behaviour 44: KO animation of sprite behaviours: fade out death (1), fade out death (2), fade out death, Smithy spell cast, fade out death, no "Escape" movement',
    ],
    "monster_behaviours_6": [  # 3
        'Monster behaviour 45: entrance animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 46: flinch animation of sprite behaviours: fade out death, no "Escape" transition',
        'Monster behaviour 49: initiate spell animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 50: initiate attack animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 51: escape animation of sprite behaviours: fade out death, no "Escape" transition',
        'Monster behaviour 53: KO animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 45: entrance animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        "Monster behaviour 47: flinch animation of sprite behaviours: (normal)",
        'Monster behaviour 49: initiate spell animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 50: initiate attack animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        "Monster behaviour 52: escape animation of sprite behaviours: (normal), no reaction when hit",
        'Monster behaviour 53: KO animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 45: entrance animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        "Monster behaviour 48: flinch animation of sprite behaviours: no reaction when hit",
        'Monster behaviour 49: initiate spell animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        'Monster behaviour 50: initiate attack animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
        "Monster behaviour 52: escape animation of sprite behaviours: (normal), no reaction when hit",
        'Monster behaviour 53: KO animation of sprite behaviours: fade out death, no "Escape" transition, (normal), no reaction when hit',
    ],
    "misses": [
        "Weapon",
        "Armor",
        "Accessory",
        "Space",
        "Space",
        "Hammer",
        "FroggieStick",
        "NokNokShell",
        "PunchGlove",
        "FingerShot",
        "Cymbals",
        "Chomp",
        "Masher",
        "ChompShell",
        "SuperHammer",
        "HandGun",
        "WhompGlove",
        "SlapGlove",
        "TroopaShell",
        "Parasol",
        "HurlyGloves",
        "DoublePunch",
        "RibbitStick",
        "SpikedLink",
        "MegaGlove",
        "WarFan",
        "HandCannon",
        "StickyGlove",
        "UltraHammer",
        "SuperSlap",
        "DrillClaw",
        "StarGun",
        "SonicCymbal",
        "LazyShellWeapon",
        "FryingPan",
        "LuckyHammer",
    ],
    "weapons": [
        "Weapon",
        "Armor",
        "Accessory",
        "Space",
        "Space",
        "Hammer",
        "FroggieStick",
        "NokNokShell",
        "PunchGlove",
        "FingerShot",
        "Cymbals",
        "Chomp",
        "Masher",
        "ChompShell",
        "SuperHammer",
        "HandGun",
        "WhompGlove",
        "SlapGlove",
        "TroopaShell",
        "Parasol",
        "HurlyGloves",
        "DoublePunch",
        "RibbitStick",
        "SpikedLink",
        "MegaGlove",
        "WarFan",
        "HandCannon",
        "StickyGlove",
        "UltraHammer",
        "SuperSlap",
        "DrillClaw",
        "StarGun",
        "SonicCymbal",
        "LazyShellWeapon",
        "FryingPan",
        "LuckyHammer",
    ],
    "weapon_misses": [
        "Weapon",
        "Armor",
        "Accessory",
        "Space",
        "Space",
        "Hammer",
        "FroggieStick",
        "NokNokShell",
        "PunchGlove",
        "FingerShot",
        "Cymbals",
        "Chomp",
        "Masher",
        "ChompShell",
        "SuperHammer",
        "HandGun",
        "WhompGlove",
        "SlapGlove",
        "TroopaShell",
        "Parasol",
        "HurlyGloves",
        "DoublePunch",
        "RibbitStick",
        "SpikedLink",
        "MegaGlove",
        "WarFan",
        "HandCannon",
        "StickyGlove",
        "UltraHammer",
        "SuperSlap",
        "DrillClaw",
        "StarGun",
        "SonicCymbal",
        "LazyShellWeapon",
        "FryingPan",
        "LuckyHammer",
    ],
    "weapon_sounds": [
        "Weapon",
        "Armor",
        "Accessory",
        "Space",
        "Space",
        "Hammer",
        "FroggieStick",
        "NokNokShell",
        "PunchGlove",
        "FingerShot",
        "Cymbals",
        "Chomp",
        "Masher",
        "ChompShell",
        "SuperHammer",
        "HandGun",
        "WhompGlove",
        "SlapGlove",
        "TroopaShell",
        "Parasol",
        "HurlyGloves",
        "DoublePunch",
        "RibbitStick",
        "SpikedLink",
        "MegaGlove",
        "WarFan",
        "HandCannon",
        "StickyGlove",
        "UltraHammer",
        "SuperSlap",
        "DrillClaw",
        "StarGun",
        "SonicCymbal",
        "LazyShellWeapon",
        "FryingPan",
        "LuckyHammer",
    ],
    "monster_attacks": [
        "PhysicalAttack0",
        "PhysicalAttack1",
        "PhysicalAttack2",
        "PhysicalAttack3",
        "PhysicalAttack4",
        "PhysicalAttack5",
        "PhysicalAttack6",
        "PhysicalAttack7",
        "PhysicalAttack8",
        "PhysicalAttack9",
        "PhysicalAttack10",
        "PhysicalAttack11",
        "PhysicalAttack12",
        "PhysicalAttack13",
        "PhysicalAttack14",
        "PhysicalAttack15",
        "PhysicalAttack16",
        "Thornet",
        "PhysicalAttack18",
        "Funguspike",
        "PhysicalAttack20",
        "PhysicalAttack21",
        "FullHouse",
        "WildCard",
        "RoyalFlush",
        "PhysicalAttack25",
        "SpritzBomb",
        "PhysicalAttack27",
        "PhysicalAttack28",
        "PhysicalAttack29",
        "Blazer",
        "PhysicalAttack31",
        "PhysicalAttack32",
        "Echofinder",
        "ScrowBell",
        "DoomReverb",
        "SporeChimes",
        "InkBlast",
        "GunkBall",
        "Endobubble",
        "PhysicalAttack40",
        "SleepSauce",
        "VenomDrool",
        "MushFunk",
        "ScrowFunk",
        "Stench",
        "PhysicalAttack46",
        "PhysicalAttack47",
        "ViroPlasm",
        "PsychoPlasm",
        "PhysicalAttack50",
        "PhysicalAttack51",
        "PollenNap",
        "ScrowDust",
        "Sporocyst",
        "Toxicyst",
        "PhysicalAttack56",
        "PhysicalAttack57",
        "LullaBye",
        "Elegy",
        "Backfire",
        "VaVaVoom",
        "FunRun",
        "BodySlam",
        "Howl",
        "Scream",
        "IronMaiden",
        "Fangs",
        "Poison",
        "CarniKiss",
        "Claw",
        "Grinder",
        "DarkClaw",
        "Scythe",
        "Sickle",
        "Deathsickle",
        "EerieJig",
        "SomnusWaltz",
        "DahliaDance",
        "Skewer",
        "Pierce",
        "PhysicalAttack81",
        "Magnum",
        "Psyche",
        "Migraine",
        "PhysicalAttack85",
        "PhysicalAttack86",
        "Multistrike",
        "FlutterHush",
        "PhysicalAttack89",
        "PhysicalAttack90",
        "PhysicalAttack91",
        "FearRoulette",
        "PhysicalAttack93",
        "PhysicalAttack94",
        "PhysicalAttack95",
        "HammerTime",
        "ValorUp",
        "PhysicalAttack98",
        "LastShot",
        "PhysicalAttack100",
        "PhysicalAttack101",
        "PhysicalAttack102",
        "PhysicalAttack103",
        "PhysicalAttack104",
        "PhysicalAttack105",
        "Gnight",
        "PhysicalAttack107",
        "PhysicalAttack108",
        "Chomp",
        "GetTough",
        "PhysicalAttack111",
        "Missedme",
        "PhysicalAttack113",
        "LocoExpress",
        "PhysicalAttack115",
        "PhysicalAttack116",
        "PhysicalAttack117",
        "PhysicalAttack118",
        "Jinxed",
        "TripleKick",
        "Quicksilver",
        "BombsAway",
        "Vigorup",
        "PhysicalAttack124",
        "SilverBullet",
        "Terrapunch",
        "ScrowFangs",
        "Shaker",
    ],
    "monster_entrances": [
        "ENT0000_NONE",
        "ENT0001_SLIDE_IN",
        "ENT0002_LONG_JUMP",
        "ENT0003_HOP_3_TIMES",
        "ENT0004_DROP_FROM_ABOVE",
        "ENT0005_ZOOM_IN_FROM_RIGHT",
        "ENT0006_ZOOM_IN_FROM_LEFT",
        "ENT0007_SPREAD_OUT_FROM_BACK",
        "ENT0008_HOVER_IN",
        "ENT0009_READY_TO_ATTACK",
        "ENT0010_FADE_IN",
        "ENT0011_SLOW_DROP_FROM_ABOVE",
        "ENT0012_WAIT_THEN_APPEAR",
        "ENT0013_SPREAD_FROM_FRONT",
        "ENT0014_SPREAD_FROM_MIDDLE",
        "ENT0015_READY_TO_ATTACK",
    ],
    "monster_spells": [  # offset: 64
        "Drain",
        "LightningOrb",
        "Flame",
        "Bolt",
        "Crystal",
        "FlameStone",
        "MegaDrain",
        "WillyWisp",
        "DiamondSaw",
        "Electroshock",
        "Blast",
        "Storm",
        "IceRock",
        "Escape",
        "DarkStar",
        "Recover",
        "MegaRecover",
        "FlameWall",
        "StaticE",
        "SandStorm",
        "Blizzard",
        "DrainBeam",
        "MeteorBlast",
        "LightBeam",
        "WaterBlast",
        "Solidify",
        "PetalBlast",
        "AuroraFlash",
        "Boulder",
        "Corona",
        "MeteorSwarm",
        "KnockOut",
        "WeirdMushroom",
        "BreakerBeam",
        "Shredder",
        "Sledge",
        "SwordRain",
        "SpearRain",
        "ArrowRain",
        "BigBang",
        "ChestScrow",
        "ChestFear",
        "ChestMute",
        "ChestPoison",
        "ChainSaw",
    ],

}


searchable_vars = globals()


def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] == obj]


def get_var_name_string(id, prefix):
    candidates = namestr(id, searchable_vars)
    r = re.compile("^%s.*" % prefix)
    newlist = list(filter(r.match, candidates))
    if len(newlist) != 1:
        raise Exception(newlist)
    return newlist[0]


def get_sprite_name(id):
    return get_var_name_string(id, "SPR")


# Monster behaviours are pretty much just object queues.
# The "Sprite behaviour" dropdown is a pointer to an object queue.
# 0x350202 + (enemy index * 2) = at this address you will find the address of the object queue the monster uses
monster_behaviour_oq_offsets = [
    0x35058A,  # no movement for "Escape"
    0x350596,  # slide backward when hit
    0x3505A2,  # Bowser Clone sprite
    0x3505AE,  # Mario Clone sprite
    0x3505BA,  # no reaction when hit
    0x350898,  # sprite shadow
    0x350985,  # floating, sprite shadow
    0x350991,  # floating
    0x350AD3,  # floating, slide backward when hit
    0x350ADF,  # floating, slide backward when hit
    0x350AEB,  # fade out death, floating
    0x350CF2,  # fade out death
    0x350CFE,  # fade out death
    0x350D0A,  # fade out death, Smithy spell cast
    0x350D16,  # fade out death, no "Escape" movement
    0x350E60,  # fade out death, no "Escape" transition
    0x350E6C,  # (normal)
    0x350E78,  # no reaction when hit
]


@dataclass
class Bank:
    pointer_table_start: Optional[int]
    pointer_table_end: Optional[int]
    start: int
    end: int

    @property
    def has_pointers(self) -> bool:
        return (
            self.pointer_table_end is not None and self.pointer_table_start is not None
        )

    def __init__(
        self,
        start: int,
        end: int,
        pointer_table_start: Optional[int] = None,
        pointer_table_end: Optional[int] = None,
    ):
        self.pointer_table_start = pointer_table_start
        self.pointer_table_end = pointer_table_end
        self.start = start
        self.end = end

    def __str__(self):
        return "Bank(start=0x%06X, end=0x%06X, pointer_table_start=%s, pointer_table_end=%s)" % (
            self.start,
            self.end,
            "0x%06X" % self.pointer_table_start
            if self.pointer_table_start is not None
            else "None",
            "0x%06X" % self.pointer_table_end
            if self.pointer_table_end is not None
            else "None",
        )


banks: Dict[str, Bank] = {

    "flower_bonus": Bank(0x02F461, 0x02F4A0, 0x02F455, 0x02F460),
    # gap
    "toad_tutorial": Bank(0x02F4BF, 0x02F50D),
    "ally_behaviours": Bank(0x350462, 0x35054D, 0x350402, 0x350461),
    "monster_behaviours_1": Bank(0x3505C6, 0x350897, 0x35058A, 0x3505C5),
    "monster_behaviours_2": Bank(0x3508A4, 0x350984, 0x350898, 0x3508A3),
    "monster_behaviours_3": Bank(0x35099E, 0x350AD2, 0x350985, 0x35099D),
    "monster_behaviours_4": Bank(0x350AF7, 0x350CF1, 0x350AD3, 0x350AF6),
    "monster_behaviours_5": Bank(0x350D22, 0x350E5F, 0x350CF2, 0x350D21),
    "monster_behaviours_6": Bank(0x350E84, 0x351025, 0x350E60, 0x350E83),
    "monster_spells": Bank(0x351080, 0x351492, 0x351026, 0x35107F),
    "monster_attacks": Bank(0x351595, 0x352127, 0x351493, 0x351594),
    "monster_entrances": Bank(0x352148, 0x3523C3, 0x352128, 0x352147),
    # gap
    "weapon_misses": Bank(0x3581B7, 0x35826E, 0x35816D, 0x3581B6),
    # gap (2 bytes, ptr table header)
    "weapon_sounds": Bank(0x3582BB, 0x35831C, 0x358271, 0x3582BA),
    # gap
    "weapon_wrapper_mario": Bank(0x358916, 0x358935),
    # gap
    "weapon_wrapper_toadstool": Bank(0x3589D5, 0x358A07),
    # gap
    "weapon_wrapper_bowser": Bank(0x358AC6, 0x358A9A),
    # gap
    "weapon_wrapper_geno": Bank(0x358B57, 0x358B8C),
    # gap
    "weapon_wrapper_mallow": Bank(0x358BEC, 0x358C2A),
    # gap
    "items": Bank(0x35C803, 0x35C967, 0x35C761, 0x35C802),
    # gap
    "ally_spells": Bank(
        0x35C9C8, 0x35CAAB, 0x35C992, 0x35C9C7
    ),  # NOTE: Adjusted due to clone spells!
    # gap
    "weapons": Bank(0x35ECEA, 0x35F111, 0x35ECA2, 0x35ECE9),
    "battle_events": Bank(0x3A6000, 0x3A705C),

    #"battle_events": Bank(0x3A60D0, 0x3A705C, 0x3A6004, 0x3A60CF),
}

BATTLE_EVENT_INDEXES_START_AT = 0x3A6004
UNKNOWN_BATTLE_EVENT_SIBLING_STARTS_AT = 0x3AECF7


command_lens = [
    9,
    8,
    1,
    6,
    4,
    1,
    6,
    1,
    8,
    3,
    1,
    8,
    6,
    1,
    1,
    1,  # 0x00
    3,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    2,
    2,
    2,
    1,
    2,
    2,  # 0x10
    4,
    4,
    4,
    4,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    6,
    4,
    4,
    4,
    4,  # 0x20
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    3,
    5,
    5,
    1,
    1,
    3,
    1,
    1,
    6,  # 0x30
    3,
    3,
    8,
    2,
    2,
    1,
    1,
    4,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0x40
    3,
    3,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    5,
    1,
    1,  # 0x50
    1,
    1,
    1,
    2,
    3,
    1,
    1,
    1,
    4,
    1,
    3,
    4,
    1,
    1,
    1,
    1,  # 0x60
    1,
    1,
    3,
    1,
    3,
    3,
    1,
    2,
    2,
    5,
    3,
    1,
    1,
    1,
    2,
    1,  # 0x70
    4,
    1,
    1,
    2,
    3,
    3,
    7,
    1,
    1,
    1,
    2,
    5,
    1,
    1,
    3,
    2,  # 0x80
    1,
    1,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    5,
    9,
    2,
    3,
    1,  # 0x90
    1,
    1,
    5,
    2,
    1,
    1,
    1,
    3,
    3,
    1,
    1,
    2,
    1,
    1,
    2,
    1,  # 0xA0
    2,
    4,
    1,
    1,
    1,
    1,
    3,
    1,
    1,
    1,
    0,
    2,
    3,
    3,
    3,
    2,  # 0xB0
    5,
    1,
    1,
    2,
    1,
    1,
    0,
    2,
    2,
    2,
    1,
    2,
    1,
    1,
    8,
    6,  # 0xC0
    4,
    1,
    2,
    4,
    6,
    4,
    1,
    1,
    3,
    1,
    1,
    2,
    1,
    6,
    1,
    1,  # 0xD0
    1,
    4,
    1,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0xE0
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,  # 0xF0
]

# command_lens = [
#   9, 8, 1, 6, 4, 1, 6, 1, 8, 3, 1, 8, 6, 1, 1, 1, # 0x00
#   3, 1, 2, 1, 1, 1, 1, 1, 3, 1, 2, 2, 2, 1, 2, 2, # 0x10
#   4, 4, 4, 4, 6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, # 0x20
#   2, 2, 2, 2, 2, 2, 3, 3, 5, 5, 1, 1, 3, 1, 1, 6, # 0x30
#   3, 3, 8, 2, 2, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, # 0x40
#   3, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 5, 1, 1, # 0x50
#   1, 1, 1, 2, 3, 1, 1, 1, 4, 1, 3, 4, 1, 1, 1, 1, # 0x60
#   1, 1, 3, 1, 3, 3, 1, 2, 2, 5, 3, 1, 1, 1, 2, 1, # 0x70
#   4, 1, 1, 2, 3, 3, 7, 1, 1, 1, 2, 5, 1, 1, 3, 2, # 0x80
#   1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 5, 9, 2, 3, 1, # 0x90
#   1, 1, 5, 2, 1, 1, 1, 3, 3, 1, 1, 2, 1, 1, 2, 1, # 0xA0
#   2, 4, 1, 1, 1, 1, 3, 1, 1, 1, 4, 2, 3, 3, 3, 2, # 0xB0
#   5, 1, 1, 2, 1, 1,10, 2, 2, 2, 1, 2, 1, 1, 8, 6, # 0xC0
#   4, 1, 2, 4, 6, 4, 1, 1, 3, 1, 1, 2, 1, 6, 1, 1, # 0xD0
#   1, 4, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, # 0xE0
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  # 0xF0
# ]

rom_coverage = [None] * 0x400000
addresses_to_track = []


class AMEM(list):
    """Base class representing a battlefield layout as a list of 16 lists of ints."""

    def __new__(cls, data):
        # Validate the outer list length
        if not isinstance(data, list) or len(data) != 16:
            raise ValueError("AMEM must be a list of 16 lists.")

        # Validate each inner list
        for i, inner in enumerate(data):
            if not isinstance(inner, list):
                raise TypeError(f"Element at index {i} is not a list.")
            if not all(isinstance(x, int) for x in inner):
                raise TypeError(f"Element at index {i} contains non-integer values.")

        # Create the list instance (empty; contents set in __init__)
        return super().__new__(cls)

    def __init__(self, data):
        # Initialize list contents
        super().__init__(data)

    def __reduce_ex__(self, protocol):
        # Tell pickle/deepcopy how to reconstruct us: call AMEM(list(self))
        return (self.__class__, (list(self),))

@dataclass
class OQRef:
    addr: int
    amem: AMEM
    relevant_indexes: List[int]
    label: str
    length: int
    pointers: List[int]

    def __init__(self, addr: int, amem: AMEM, relevant_indexes: List[int], label: str = ""):
        self.addr = addr
        self.amem = deepcopy(amem)
        self.relevant_indexes = deepcopy (relevant_indexes)
        self.label = label

    def __repr__(self) -> str:
        return f"OQRef(addr=0x{self.addr:06X}, label={self.label}, length={self.length if hasattr(self, 'length') else None}, pointers={[f'0x{p:06X}' for p in self.pointers] if hasattr(self, 'pointers') else None}, relevant_indexes={self.relevant_indexes}, amem={self.amem})"


def tok(rom: bytearray, start: int, end: int, oq_starts: List[OQRef], oq_idx_starts: List[OQRef]) -> List[Tuple[bytearray, int, bool]]:
    dex = start
    script: List[Tuple[bytearray, int, bool]] = []
    combo_oq = oq_starts + oq_idx_starts
    while dex < end:
        if dex in [s.addr for s in combo_oq]:
            oq = next((s for s in combo_oq if s.addr == dex), None)
            if oq is None:
                raise Exception("how did you get here?")
            script.append((rom[dex : dex + oq.length], dex, True))
            dex += oq.length
        else:
            cmd = rom[dex]
            l = command_lens[cmd]
            if cmd == 0xC6 and l == 0:
                l = 2 + rom[dex + 1]
            elif cmd == 0xBA and l == 0:
                l = 2 + rom[dex + 1] * 2
            script.append((rom[dex : dex + l], dex, False))
            dex += l
    return script


jmp_cmds = [
    0x09,
    0x10,
    0x24,
    0x25,
    0x26,
    0x27,
    0x28,
    0x29,
    0x2A,
    0x2B,
    0x38,
    0x39,
    0x50,
    0x51,
    0x5D,
    0x64,
    0x68,
    0xA7,
    0xCE,
    0xCF,
    0xD0,
    0xD8,
]

jmp_cmds_1 = [0x68]

SPECIAL_CASE_BREAKS = [
    0x356076,
    0x356087,
    0x3560A9,
    0x3560CD,
    0x3560FE,
    0x356131,
    0x356152,
    0x35617A,
    0x3561AD,
    0x3561E0,
    0x356213,
    0x35624B,
    0x3A8A68,
    0x3A8AC0,
    0x3A8C8A,
]


@dataclass
class Addr:
    offset: int
    amem: AMEM
    ref_label: str
    _referenced_by: list[str]

    @property
    def referenced_by(self) -> List[str]:
        return [r for r in self._referenced_by if r != ""]

    def __init__(self, offset: int, amem: AMEM, ref_label: str, refs: Optional[List[str]] = None):
        self.offset = offset
        self.amem = amem
        self.ref_label = ref_label
        self._referenced_by = deepcopy(refs) if refs is not None else []

    def __str__(self) -> str:
        return (
            f"Addr(offset=0x{self.offset:06X}, amem={self.amem}, "
            f"ref_label={self.ref_label}, referenced_by={self.referenced_by})"
        )


@dataclass
class ObjectQueue:
    offset: int
    destination_offsets: List[int]

    def __init__(self, offset: int, destination_offsets: List[int]):
        self.offset = offset
        self.destination_offsets = destination_offsets


@dataclass
class ObjectQueueWithIndex:
    offset: int
    destination_offsets: List[List[int]]

    def __init__(self, offset: int, destination_offsets: List[List[int]]):
        self.offset = offset
        self.destination_offsets = destination_offsets

@dataclass
class ProtoCommand:
    id: str 
    addr: int
    raw_data: bytearray
    parsed_data: List[Union[int, str]]
    length: Optional[int]
    oq: bool

    def __init__(
        self,
        id: str,
        addr: int,
        data: bytearray,
        oq: bool = False,
        length: Optional[int] = None
    ):
        self.id = id
        self.addr = addr
        self.raw_data = data
        self.oq = oq
        self.length = length
        self.parsed_data = []

    def __repr__(self) -> str:
        return (
            f"ProtoCommand(id={self.id!r}, addr=0x{self.addr:06X}, "
            f"raw_data=[{" ".join([f'0x{b:02X}' for b in self.raw_data])}], parsed_data=[{" ".join([str(d) for d in self.parsed_data])}], oq={self.oq}, length={self.length})"
        )

@dataclass
class ContiguousBlock:
    start: int
    contents: bytearray

    @property
    def size(self):
        return len(self.contents)
    
    @property
    def end(self):
        return self.start + self.size
    
    def __init__(self, start: int, contents: bytearray):
        self.start = start
        self.contents = contents

    def __str__(self) -> str:
        return f"ContiguousBlock(start=0x{self.start:06X}, size={self.size}, end=0x{self.end:06X})"


def string_byte(word):
    if type(word) == str:
        return '''"%s"''' % word
    else:
        return "0x%02x" % word


INIT_AMEM: AMEM = AMEM([[0]] * 16)

BATTLE_EVENTS_WITH_QUEUE_POINTER_TABLE = [22]
BATTLE_EVENTS_WITH_DOUBLE_QUEUE_POINTER_TABLE = [70, 85]

def get_third_byte_as_string(bank_name: str) -> str:
    if "subroutine" in bank_name:
        return bank_name[-6:-4].upper()
    elif bank_name == "battle_events":
        return "3A"
    elif bank_name in ["toad_tutorial", "flower_bonus"]:
        return "02"
    else:
        return "35"

BATTLE_EVENTS_ROOT_LABEL = "battle_events_root"

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):
        output_path = "./src/disassembler_output/battle_animation"

        shutil.rmtree(output_path, ignore_errors=True)

        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w")

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        jump_pointers = []

        oq_starts: List[OQRef] = []
        oq_idx_starts: List[OQRef] = []

        known_addresses_covered = {
            "02": [False] * 0x10000,
            "35": [False] * 0x10000,
            "3A": [False] * 0x10000,
        }

        collective_data: Dict[str, List[List[ProtoCommand]]] = {"35": [], "3A": [], "02": []}
        
        references: Dict[int, List[str]] = {}

        for bank_id, blocks in banks.items():
            #print(f'Processing bank: {bank_id}')
            third_byte_as_string = get_third_byte_as_string(bank_id)
            reference_label = bank_id

            bank_as_upper_byte = blocks.start & 0xFF0000

            bank_pointer_addresses: List[int] = []
            script_sizes: List[int] = []

            # This is the list of every address in the animation code that can be touched, recursively, from a top-level pointer
            branches: List[Addr] = []
            amem: AMEM = deepcopy(INIT_AMEM)

            # To start, all of the bank's pointers (or just the bank start, if there are no pointers) need to be added to the branch array.
            if blocks.has_pointers:
                for pointer_table_index, pointer in enumerate(
                    range(blocks.pointer_table_start, blocks.pointer_table_end, 2) # type: ignore - these can never be None if has_pointers is True
                ):
                    three_byte_pointer: int = (
                        shortify(rom, pointer) + bank_as_upper_byte
                    )
                    # This is a string that tells us what the script does, i.e. froggiestick miss, ice bomb, etc.
                    ref_label = "%s %s" % (
                        reference_label,
                        (
                            str(pointer_table_index)
                            if pointer_table_index >= len(SCRIPT_NAMES[bank_id])
                            else SCRIPT_NAMES[bank_id][pointer_table_index]
                        ),
                    )
                    bank_pointer_addresses.append(three_byte_pointer)
                    #print(f"    adding {bank_id} pointer {pointer_table_index} 0x{bank_as_upper_byte + pointer:06X}")
                    branches.append(
                        Addr(three_byte_pointer, deepcopy(amem), ref_label, [])
                    )
            elif bank_id == "battle_events":
                tertiary_cursor = blocks.start
                tertiary_cursor_short = tertiary_cursor & 0xFFFF
                tertiary_end = 0x10000
                while tertiary_cursor_short < tertiary_end:
                    tertiary_points_to = shortify(rom, tertiary_cursor)
                    known_addresses_covered[third_byte_as_string][tertiary_cursor & 0xFFFF] = True
                    known_addresses_covered[third_byte_as_string][(tertiary_cursor & 0xFFFF) + 1] = True
                    if tertiary_points_to < tertiary_end:
                        tertiary_end = tertiary_points_to
                    #print("    reading battle_events root iterator addr", f"0x{tertiary_cursor:06X}", "points to", f"0x{bank_as_upper_byte + tertiary_points_to:06X}")
                    tertiary_cursor += 2
                    tertiary_cursor_short = tertiary_cursor & 0xFFFF
                    oq_idx_starts.append(
                        OQRef(
                            bank_as_upper_byte + tertiary_points_to,
                            deepcopy(INIT_AMEM),
                            [0],
                        )
                    )
                    branches.append(Addr(bank_as_upper_byte + tertiary_points_to, deepcopy(INIT_AMEM), BATTLE_EVENTS_ROOT_LABEL, []))
                # force 0x3A6000 to be processed as ptr table, do not treat it as a branch
                o = OQRef(
                        0x3A6000,
                        deepcopy(INIT_AMEM),
                        [0],
                    )
                o.length = 4
                oq_idx_starts.append(
                    o
                )
            else:
                #print(f"    adding {bank_id} 0x{blocks.start:06X}")
                branches.append(Addr(blocks.start, deepcopy(INIT_AMEM), bank_id, []))
            # Now we're going to process every item in the branch array, adding any more branches we find from jumps, object queues, subroutines, etc.
            branch_index: int = 0
            this_branch = branches[branch_index]
            while True:
                #print(f'    Tracing branch index {branch_index}/{len(branches)} of {bank_id} (0x{this_branch.offset:06X}): {this_branch}')
                # AMEM can control where the code branches to.
                amem = deepcopy(this_branch.amem)
                absolute_offset = this_branch.offset 

                # Keep a running, recursive list of what top-level scripts ultimately reference this code.
                # This will ultimatley be displayed in the output python file as an annotation.
                cursor = absolute_offset
                if absolute_offset not in references:
                    references[absolute_offset] = []
                references[absolute_offset].extend(this_branch.referenced_by)
                references[absolute_offset] = list(set(references[absolute_offset]))

                # Process every command in the script until we find a terminating byte.
                end_found = False
                while not end_found:
                    #print(f'        current_addr: 0x{cursor:06X}')
                    def validate_addr(offs: int, am: AMEM, lbl: str = "", important_amem_indexes_raw: Optional[List[int]] = None):
                        if important_amem_indexes_raw is None:
                            important_amem_indexes_raw = [0]
                        important_amem_indexes = list(set(important_amem_indexes_raw))

                        # ?
                        jump_voided = False

                        # exit if the branch destination is somehow not in this bank
                        if offs & 0xFF0000 != bank_as_upper_byte:
                            raise Exception("illegal addr 0x%06x" % offs)

                        # add this branch's label to the list of references the destination branch will receive
                        dc = deepcopy(this_branch.referenced_by)
                        if (
                            this_branch.ref_label != ""
                            and this_branch.ref_label != BATTLE_EVENTS_ROOT_LABEL
                        ):
                            dc.append(this_branch.ref_label)

                        # separately, maintain an address<->references dict for easier lookup
                        if offs not in references:
                            references[offs] = []
                        references[offs].append(this_branch.ref_label)
                        references[offs] = list(set(references[offs]))

                        destination_branch = Addr(
                            offs, deepcopy(am), lbl, deepcopy(dc)
                        )

                        # if the destination branch already exists, verify that we don't have an exact copy with the same amem
                        for t in [t for t in branches if t.offset == offs]:
                            same_amem_count = 0
                            for a in important_amem_indexes:
                                capped_amem = list(set([min(65535, b) for b in t.amem[a]]))
                                capped_amem_comp = list(set([min(65535, b) for b in am[a]]))
                                if set(capped_amem) == set(capped_amem_comp):
                                    same_amem_count += 1
                            if same_amem_count == len(important_amem_indexes):
                                jump_voided = True
                                break

                        if not jump_voided:
                            branches.append(destination_branch)
                            #print(f'            --> adding new branch entry for 0x{destination_branch.offset:06X}: {destination_branch}')

                        return destination_branch

                    def create_object_queue(base_addr: int, label_override: Optional[str] = None) -> int:
                        temp_cursor_addr = base_addr
                        length = 0
                        for s in [s for s in oq_starts if s.addr == base_addr]:
                            temp_cursor_addr = base_addr
                            tbl_ends_at = 0x10000
                            temp_cursor_addr_short = temp_cursor_addr & 0xFFFF
                            i = 0
                            length = 0
                            ptrs: List[int] = []
                            if label_override is not None:
                                label = label_override
                            while temp_cursor_addr_short < tbl_ends_at:
                                cursor_points_to = shortify(rom, temp_cursor_addr)
                                known_addresses_covered[third_byte_as_string][temp_cursor_addr_short] = True
                                known_addresses_covered[third_byte_as_string][temp_cursor_addr_short + 1] = True
                                if cursor_points_to < tbl_ends_at:
                                    tbl_ends_at = cursor_points_to
                                # print("            reading base_iterator_addr", f"0x{temp_cursor_addr:06X}", "points to", f"0x{bank_as_upper_byte + cursor_points_to:06X}")
                                temp_cursor_addr += 2
                                temp_cursor_addr_short = temp_cursor_addr & 0xFFFF
                                amem = deepcopy(INIT_AMEM)
                                amem[0] = [i]
                                if label_override is None:
                                    label = ""
                                if i in s.relevant_indexes:
                                    amem = s.amem
                                    if label_override is None:
                                        label = s.label
                                ref = bank_as_upper_byte + cursor_points_to
                                validate_addr(ref, amem, label)
                                ptrs.append(ref)
                                i += 1
                                length += 2
                                if not (temp_cursor_addr_short < tbl_ends_at):
                                    break
                            s.length = length
                            s.pointers = ptrs
                        return length

                    # Get the bytes for whatever command begins at current_addr.
                    # Check first if this is the start of an OQ pointer table. Add branches if so, and mark table range as used.
                    if cursor in [s.addr for s in oq_starts]:
                        s = next((s for s in oq_starts if s.addr == cursor), None)
                        if not s:
                            raise ValueError("how did you get here?")
                        # print("        THIS IS A ONE-TIER OQ")
                        cursor += create_object_queue(s.addr)
                        continue
                    elif cursor in [s.addr for s in oq_idx_starts]:
                        #print("        THIS IS A TWO-TIER OQ")
                        complex_oq = next((s for s in oq_idx_starts if s.addr == cursor), None)
                        if not complex_oq:
                            raise ValueError("how did you get here?")
                        tbl_ends_at = 0x10000
                        cursor_short = cursor & 0xFFFF
                        i = 0
                        if not hasattr(complex_oq, "pointers"):
                            complex_oq.pointers = []
                        length = 0
                        while cursor_short < tbl_ends_at:
                            length += 2
                            # figure out where every basic OQ in the complex OQ starts
                            # by iterating through short pointers until we hit the start of a basic OQ
                            if i in complex_oq.relevant_indexes:
                                # relevant indexes are ones that we know are actually referenced by a script
                                # and therefore need to carry possible AMEM values and a label
                                # other indexes are probably unused but we should know them if they are parts of OQs
                                amem = complex_oq.amem
                                label = complex_oq.label
                            else:
                                amem = deepcopy(INIT_AMEM)
                                amem[0] = [i]
                                label = ""
                            # if this basic OQ is a lower pointer than any others, it's probably where the complex OQ table ends
                            cursor_points_to = shortify(rom, cursor)
                            if cursor_points_to < tbl_ends_at:
                                tbl_ends_at = cursor_points_to
                            # we know these bytes are used because they point to a basic OQ
                            known_addresses_covered[third_byte_as_string][cursor_short] = True
                            known_addresses_covered[third_byte_as_string][cursor_short + 1] = True
                            # add a branch to the branch array for the basic OQ
                            # relevant indexes based on the amem being passed in
                            relevant_indexes = list(set([x for sub in amem for x in sub]))
                            pointed_addr = bank_as_upper_byte + cursor_points_to
                            ref = OQRef(pointed_addr, amem, relevant_indexes, label)
                            oq_starts.append(ref)
                            complex_oq.pointers.append(pointed_addr)
                            # parse the basic OQ to add its branches
                            # print("        reading at 0x%06x: points to 0x%04x" % (cursor, shortify(rom, cursor)))  
                            if this_branch.offset == BATTLE_EVENT_INDEXES_START_AT:
                                battle_event_index = (cursor - BATTLE_EVENT_INDEXES_START_AT) // 2
                                label = SCRIPT_NAMES["battle_events"][battle_event_index]
                                create_object_queue(pointed_addr, label_override=label)
                            elif this_branch.offset == UNKNOWN_BATTLE_EVENT_SIBLING_STARTS_AT:
                                #print(f"cursor: 0x{cursor:06X}, base to: 0x{UNKNOWN_BATTLE_EVENT_SIBLING_STARTS_AT:06X}")
                                label = f"unknown_battle_event_adjacent"
                                create_object_queue(pointed_addr, label_override=label)
                            else:
                                create_object_queue(pointed_addr)
                            cursor += 2
                            cursor_short = cursor & 0xFFFF
                            i += 1
                        complex_oq.length = length
                        continue

                    opcode = rom[cursor]
                    length = command_lens[opcode]
                    # print(f'            opcode: {opcode:02X}, length: {length}, data: {" ".join([f"0x{b:02X}" for b in rom[cursor:cursor+length]])}')
                    if opcode == 0xC6:
                        length = rom[cursor + 1] + 2
                    elif opcode == 0xBA:    
                        length = rom[cursor + 1] * 2 + 2
                    command = rom[cursor : cursor + length]
                    cvr_range = cursor & 0xFFFF

                    if command == bytearray([0,0,0,0,0,0,0,0,0]):
                        end_found = True
                        break
                    # I have no idea why the branch array length is being compared to the script size length, but it worked before
                    # Here we're flagging each byte in the command as "used", as in we know some script definitely accesses it
                    elif blocks.has_pointers and (branch_index < len(script_sizes)):
                        for tok_output in range(
                            cvr_range, cvr_range + length
                        ):
                            known_addresses_covered[third_byte_as_string][tok_output] = True
                    else:
                        for tok_output in range(cvr_range, cvr_range + length):
                            known_addresses_covered[third_byte_as_string][tok_output] = True

                    # If this is a command that changes AMEM $60-$6F, or COULD change them, we need to keep track of what its possible values could be in case an AMEM-based object queue comes up.
                    if opcode in [0x20, 0x21]:  # set amem 8 bit to...
                        if command[1] & 0xF0 == 0x30:  # copy
                            src = command[2] & 0x0F
                            dst = command[1] & 0x0F
                            amem[dst] = amem[src]
                        elif command[1] & 0xF0 == 0x00 and command[1] <= 0x0F:  # const
                            amem[command[1]] = [shortify(command, 2)]
                        # impossible to evaluate other value sources
                    elif (
                        opcode in [0x22, 0x23] and command[1] & 0xF0 == 0x30
                    ):  # copy, other way around
                        dst = command[2] & 0x0F
                        src = command[1] & 0x0F
                        amem[dst] = amem[src]
                    elif opcode in [0x2C, 0x2D]:  # inc
                        if command[1] & 0xF0 == 0x30:  # by amem
                            index1 = command[2] & 0x0F
                            index2 = command[1] & 0x0F
                            consolidated: List[int] = []
                            for x in amem[index2]:
                                for y in amem[index1]:
                                    consolidated.append(x + y)
                            amem[index2] = list(set(consolidated))
                        elif (
                            command[1] & 0xF0 == 0x00 and command[1] <= 0x0F
                        ):  # by const
                            amem[command[1]] = list(
                                set(
                                    [
                                        (a + shortify(command, 2))
                                        for a in amem[command[1]]
                                    ]
                                )
                            )
                    elif opcode in [0x2E, 0x2F]:  # dec
                        if command[1] & 0xF0 == 0x30:  # by amem
                            index1 = command[2] & 0x0F
                            index2 = command[1] & 0x0F
                            consolidated: List[int] = []
                            for x in amem[index2]:
                                for y in amem[index1]:
                                    consolidated.append(max(0, x - y))
                            amem[index2] = list(set(consolidated))
                        elif (
                            command[1] & 0xF0 == 0x00 and command[1] <= 0x0F
                        ):  # by const
                            amem[command[1]] = list(
                                set(
                                    [
                                        max(0, a - shortify(command, 2))
                                        for a in amem[command[1]]
                                    ]
                                )
                            )
                    elif opcode in [0x30, 0x31] and command[1] <= 0x0F:
                        amem[command[1]] = list(set([a + 1 for a in amem[command[1]]]))
                    elif opcode in [0x32, 0x33] and command[1] <= 0x0F:
                        amem[command[1]] = list(set([a - 1 for a in amem[command[1]]]))
                    elif opcode in [0x34, 0x35] and command[1] <= 0x0F:
                        amem[command[1]] = [0]
                    elif opcode in [0x6A, 0x6B] and command[1] <= 0x0F:
                        amem[command[1]] = list(range(command[2]))

                    amem_was = deepcopy(amem)

                    # If this command includes a GOTO, need to add the destinations to the branch array and process them separately
                    if opcode in jmp_cmds or opcode in jmp_cmds_1:
                        if opcode in jmp_cmds_1:
                            address_byte = command[-3:-1]
                        else:
                            address_byte = command[-2:]

                        branch_addr = (
                            bank_as_upper_byte
                            + (address_byte[1] << 8)
                            + address_byte[0]
                        )

                        # Which of AMEM $60-$6F are part of the branch condition? ie if AMEM $64 bit 1 = ... then ...
                        # Clean up what the AMEMs can be at the target branch, and then add it to the array.
                        # Only really tracking constants and other AMEM. Not really possible to track $7Exxxx and $7Fxxxx or OMEM
                        important_amem_indexes = [0]

                        if opcode in [0x24, 0x25]:  # if amem =
                            index1 = command[1] & 0x0F
                            important_amem_indexes.append(index1)
                            var_type = (command[1] & 0xF0) >> 4
                            if var_type == 0:
                                amem[index1] = [shortify(command, 2)]
                            elif var_type == 3:
                                index2 = command[2] & 0x0F
                                amem[index1] = amem[index2]
                        elif opcode in [0x26, 0x27]:  # if amem !=
                            index1 = command[1] & 0x0F
                            important_amem_indexes.append(index1)
                            var_type = (command[1] & 0xF0) >> 4
                            if var_type == 0:
                                amem[index1] = [a for a in amem[index1] if a != shortify(command, 2)]
                            elif var_type == 3:
                                index2 = command[2] & 0x0F
                                if amem[index1] == amem[index2]:
                                    amem[index1] = []
                        elif opcode in [0x28, 0x29]:  # if amem <
                            index1 = command[1] & 0x0F
                            important_amem_indexes.append(index1)
                            var_type = (command[1] & 0xF0) >> 4
                            if var_type == 0:
                                amem[index1] = [a for a in amem[index1] if a < shortify(command, 2)]
                            elif var_type == 3:
                                index2 = command[2] & 0x0F
                                amem[index1] = [a for a in amem[index1] if a < max([0] if not amem[index2] else amem[index2])]
                        elif opcode in [0x2A, 0x2B]:  # if amem >=
                            index1 = command[1] & 0x0F
                            important_amem_indexes.append(index1)
                            var_type = (command[1] & 0xF0) >> 4
                            if var_type == 0:
                                amem[index1] = [a for a in amem[index1] if a >= shortify(command, 2)]
                            elif var_type == 3:
                                index2 = command[2] & 0x0F
                                amem[index1] = [a for a in amem[index1] if a >= max([0] if not amem[index2] else amem[index2])]
                        elif opcode == 0x38:  # if amem bits set
                            index1 = command[1] & 0x0F
                            important_amem_indexes.append(index1)
                            amem[index1] = [a for a in amem[index1] if a & command[2] == command[2]]
                        elif opcode == 0x39:  # if amem bits clear
                            index1 = command[1] & 0x0F
                            important_amem_indexes.append(index1)
                            amem[index1] = [a for a in amem[index1] if ~a & command[2] == command[2]]
                        elif opcode == 0x64:  # object queue, command index = amem 60
                            oq_starts.append(OQRef(branch_addr, amem, amem[0], this_branch.ref_label))
                        elif (
                            opcode == 0x68
                        ):  # object queue, pointer table index = amem $60, command index is an arg
                            oq_idx_starts.append(OQRef(branch_addr, amem, amem[0], this_branch.ref_label))


                        validate_addr(branch_addr, amem, important_amem_indexes_raw=important_amem_indexes)

                        amem = deepcopy(amem_was)

                    # terminating conditions
                    if opcode in [0x09, 0x11, 0x07, 0x5E]:
                        end_found = True
                    elif (
                        branch_index < len(script_sizes)
                        and (cursor + length >= absolute_offset + script_sizes[branch_index])
                    ):
                        end_found = True
                    elif cursor + length in SPECIAL_CASE_BREAKS:
                        end_found = True
                    elif 0x3A0000 <= cursor + length < 0x3A60D0:
                        end_found = True

                    # if not terminated, move on to the next command
                    cursor += length

                # move on to the next branch
                branch_index += 1
                if branch_index >= len(branches):
                    break
                this_branch = branches[branch_index]

        # print("Done tracing branches, collecting data...")
        # Collect contiguous known bytes
        used: Dict[str, List[ContiguousBlock]] = {
            "02": [],
            "35": [],
            "3A": [],
        }
        for bank_id, bank_contents in known_addresses_covered.items():
            # bank_name: str (02, 35, 3A)
            # bank_contents: List[bool] (0x10000 length)
            started: Optional[int] = None
            upper = (int(bank_id, 16)) << 16
            # upper: 0x020000, 0x350000, 0x3A0000
            for index, value in enumerate(bank_contents):
                # index: 4 digit ROM position
                # value: used or not
                if value and started is None:
                    started = index
                    # started: 4 digit ROM position at which current block started
                elif started is not None and not value:
                    used[bank_id].append(ContiguousBlock(started + upper, rom[(upper+started):(upper+index)]))
                    started = None
            if started is not None:
                used[bank_id].append(ContiguousBlock(started + upper, rom[(upper+started):(upper+0x10000)]))

        # turn contiguous blocks into proto-commands
        for bank_id, blocks in used.items():
            data: List[List[ProtoCommand]] = []
            for block in blocks:
                # print(f'block.start, block.end: 0x{block.start:06X}, 0x{block.end:06X} (size {block.size})')
                split_block = tok(
                    rom, block.start, block.end, oq_starts, oq_idx_starts
                )
                offset_within_block = 0
                this_script: List[ProtoCommand] = []
                for tok_output in split_block:
                    #print(tok_output)
                    absolute_offset = block.start + offset_within_block
                    identifier = f"command_0x{absolute_offset:06X}"
                    possible_rename = [b.ref_label for b in branches if b.offset == absolute_offset and b.ref_label != ""]
                    if len(possible_rename) > 0:
                        identifier = f"{possible_rename[0].lower().replace(" ", "_").replace("-", "_")}_0x{absolute_offset:06X}"
                    named_proto_command = ProtoCommand(identifier, absolute_offset, tok_output[0], tok_output[2], len(tok_output[0]))
                    this_script.append(named_proto_command)
                    #print(f'    parsed command {named_proto_command}')
                    offset_within_block += len(tok_output[0])
                data.append(this_script)
            #print(data)
            collective_data[bank_id].extend(data)

        # associate jump pointers with command IDs
        for bank_id, script in collective_data.items():

            third_byte_as_string = get_third_byte_as_string(bank_id)

            # when reassembling battle scripts: before each script body, need to insert 2 bytes
            # that are a pointer to its own start
            # ie: values in pointer bank @ 3A6004 for script 0: 0xD0 0x60
            # actual value at 3A60D0: 0xD2 0x60
            # actual script 0 begins at 3A60D2

            # replace jump addresses with IDs if in the same bank
            for index, commands in enumerate(script):
                for cmd_index, command in enumerate(commands):
                    address_data = None
                    if command.oq:
                        address_data = deepcopy(command.raw_data)
                        #print([f"0x{b:02X}" for b in address_data])
                        del command.raw_data[0:]
                    elif (
                        command.raw_data[0] in jmp_cmds_1
                    ):
                        address_data = command.raw_data[-3:-1]
                        del command.raw_data[-3:-1]
                    elif (
                        command.raw_data[0] in jmp_cmds
                    ):
                        address_data = command.raw_data[-2:]
                        del command.raw_data[-2:]
                        # print(2)
                    # print(address_data)

                    if address_data is None:
                        continue

                    addresses: List[List[int]] = np.array(address_data).reshape(-1, 2)
                    #print("")
                    #print(addresses)
                    for address in addresses:
                        #print(address)
                        dest = (
                            (command.addr & 0xFF0000)
                            + (int(address[1]) << 8)
                            + int(address[0])
                        )

                        found = None
                        if dest in [0x35053C]:
                            found = f"ILLEGAL_JUMP_{(dest & 0xFFFF):04X}"
                        else:
                            for search_script in script:
                                for search_command in search_script:
                                    # print (f'searching for 0x{dest:06X}, checking command {search_command.id} at 0x{search_command.addr:06X}')
                                    if search_command.addr == dest:
                                        found = search_command.id
                                        break
                                if found is not None:
                                    break
                        if found is not None:
                            command.parsed_data.append(found)
                            jump_pointers.append(found)
                        else:
                            raise Exception("couldn't find jump target 0x%06x" % dest)

                        script[index][cmd_index].raw_data = command.raw_data
        
        # do the same but for pointer tables
        # treat pointers as OQs with no AMEM
        for bank_id, blocks in banks.items():
            if not blocks.has_pointers:
                continue
            this_script: List[ProtoCommand] = []
            makeshift_oq = ProtoCommand(f"{bank_id}_pointer_table", blocks.pointer_table_start, bytearray(), True, 0)
            third_byte_as_string = get_third_byte_as_string(bank_id)
            for pointer_table_index, pointer in enumerate(
                range(blocks.pointer_table_start, blocks.pointer_table_end, 2) # type: ignore - these can never be None if has_pointers is True
            ):
                three_byte_pointer: int = (
                    shortify(rom, pointer) + (int(third_byte_as_string, 16) << 16)
                )
                found = None
                for search_script in collective_data[bank_id]:
                    for search_command in search_script:
                        if search_command.addr == three_byte_pointer:
                            found = search_command.id
                            break
                    if found is not None:
                        break
                if found is not None:
                    jump_pointers.append(found)
                    makeshift_oq.parsed_data.append(found)
                else:
                    raise Exception("couldn't find pointer target 0x%06x" % three_byte_pointer)
            this_script.append(makeshift_oq)
            collective_data[bank_id].insert(0, this_script)

        # TODO: Comprehensive parser seems to be working
        # Now we need to re-do how the output files are written
        # Also need to adjust how OQ command classes work. IDX type is just a pointer collection

        for bank_id, blocks in collective_data.items():
            #print(f"Exporting {bank_id}...")

            third_byte_as_string = get_third_byte_as_string(bank_id)

            export_dest = f"{output_path}/{bank_id}"
            os.makedirs(export_dest, exist_ok=True)

            open(f"{export_dest}/__init__.py", "w")
            export_file = open("%s/export.py" % export_dest, "w")

            import_body = ""
            export_body = ""

            # when reassembling battle scripts: before each script body, need to insert 2 bytes
            # that are a pointer to its own start
            # ie: values in pointer bank @ 3A6004 for script 0: 0xD0 0x60
            # actual value at 3A60D0: 0xD2 0x60
            # actual script 0 begins at 3A60D2

            for script in blocks:

                script_alias = ""

                dest = f"{output_path}/{bank_id}"
                os.makedirs(f"{dest}/contents", exist_ok=True)
                open(f"{dest}/__init__.py", "w")
                open(f"{dest}/contents/__init__.py", "w")
                script_alias = f"script_0x{script[0].addr:06X}"
                file = open(f"{dest}/contents/{script_alias}.py", "w")
                import_body += "\nfrom .contents.%s import script as %s" % (
                    script_alias,
                    script_alias,
                )

                size = sum([c.length for c in script])

                output = (
                    "from smrpgpatchbuilder.datatypes.items.implementations import *"
                )
                output += "\nfrom smrpgpatchbuilder.datatypes.battle_animation_scripts import *"
                output += "\nfrom smrpgpatchbuilder.datatypes.enemies.implementations import *"
                
                output += f"\n\nscript = AnimationScriptBlock(expected_size={size}, expected_beginning=0x{script[0].addr:06X}, script=[\n\t"

                contents = get_script(script, jump_pointers)

                output += ",\n\t".join(contents)

                output += "\n])"

                writeline(file, output)

                export_body += "\n\t\t%s," % script_alias
            export_output = "from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import AnimationScriptBank"
            export_output += import_body
            export_output += "\n\nbank = AnimationScriptBank("
            export_output += "\n\tname = \"0x%s\"," % bank_id.upper()
            export_output += "\n\tscripts = ["
            export_output += export_body

            export_output += "\n\t]"
            export_output += "\n)"
            writeline(export_file, export_output)


def get_script(script, valid_identifiers):

    new_script = []

    for cmd in script:
        identifier = ""
        cls, args, use_identifier, include_argnames = convert_event_script_command(
            cmd, valid_identifiers
        )

        if cls is not None:
            arg_strings = []
            for key in args:
                if include_argnames:
                    arg_strings.append("%s=%s" % (key, args[key]))
                else:
                    arg_strings.append(args[key])
            try:
                arg_string = ", ".join(arg_strings)
            except:
                raise Exception(cls)

            if use_identifier:
                if len(arg_string) > 0:
                    arg_string += ", "
                identifier = 'identifier="%s"' % cmd.id

            output = "%s(%s%s)" % (cls, arg_string, identifier)
            new_script.append(output)

    return new_script


def convert_event_script_command(command, valid_identifiers):
    cmd = command.raw_data
    use_identifier: bool = (
        command.id in valid_identifiers or "queuestart" in command.id
    )
    # use_identifier: bool = False
    args = {}
    cls = None
    include_argnames = True

    if command.oq:
        args["destinations"] = '[%s]' %  ", ".join(f"\"{a}\"" for a in command.parsed_data)
        return "DefineObjectQueue", args, True, False

    opcode = cmd[0]

    if opcode == 0x00:
        cls = "NewSpriteAtCoords"
        args["sprite_id"] = get_sprite_name(shortify(cmd, 3) & 0x3FF)
        args["sequence"] = str(cmd[5] & 0x0F)
        args["priority"] = str((cmd[6] & 0x30) >> 4)
        args["vram_address"] = f"0x{shortify(cmd, 7):04X}"
        args["palette_row"] = str(cmd[6] & 0x0F)
        if (cmd[1] & 0x01) == 0x01:
            args["overwrite_vram"] = "True"
        if (cmd[2] & 0x08) == 0x08:
            args["looping"] = "True"
        if (cmd[2] & 0x10) == 0x10:
            args["param_2_and_0x10"] = "True"
        if (cmd[2] & 0x20) == 0x20:
            args["overwrite_palette"] = "True"
        if (cmd[6] & 0x40) == 0x40:
            args["mirror_sprite"] = "True"
        if (cmd[6] & 0x80) == 0x80:
            args["invert_sprite"] = "True"
        if (cmd[1] & 0x40) == 0x40:
            args["behind_all_sprites"] = "True"
        if (cmd[1] & 0x80) == 0x80:
            args["overlap_all_sprites"] = "True"
    elif opcode == 0x01 or opcode == 0x0B:
        if opcode == 0x01:
            cls = "SetAMEM32ToXYZCoords"
        elif opcode == 0x0B:
            cls = "SetAMEM40ToXYZCoords"
        args["origin"] = ORIGINS[((cmd[1] >> 4) & 0b11)]
        args["x"] = str(shortify_signed(cmd, 2))
        args["y"] = str(shortify_signed(cmd, 4))
        args["z"] = str(shortify_signed(cmd, 6))
        if (cmd[1] & 0x01) == 0x01:
            args["set_x"] = "True"
        if (cmd[1] & 0x02) == 0x02:
            args["set_y"] = "True"
        if (cmd[1] & 0x04) == 0x04:
            args["set_z"] = "True"
    elif opcode == 0x03:
        cls = "DrawSpriteAtAMEM32Coords"
        args["sprite_id"] = get_sprite_name(shortify(cmd, 3) & 0x3FF)
        args["sequence"] = cmd[5] & 0x0F
        if (cmd[1] & 0x01) == 0x01:
            args["store_to_vram"] = "True"
        if (cmd[2] & 0x08) == 0x08:
            args["looping"] = "True"
        if (cmd[2] & 0x20) == 0x20:
            args["store_palette"] = "True"
        if (cmd[1] & 0x40) == 0x40:
            args["behind_all_sprites"] = "True"
        if (cmd[1] & 0x80) == 0x80:
            args["overlap_all_sprites"] = "True"
    elif opcode == 0x04:
        cls = "PauseScriptUntil"
        if cmd[1] == 6:
            args["condition"] = "SPRITE_SHIFT_COMPLETE"
        elif cmd[1] == 8:
            args["condition"] = "BUTTON_PRESSED"
        elif cmd[1] == 0x10:
            args["condition"] = "FRAMES_ELAPSED"
            args["frames"] = str(shortify(cmd, 2))
        elif cmd[1] in [1, 2, 4, 7]:
            args["condition"] = f"UNKNOWN_PAUSE_{cmd[1]}"
        else:
            args["condition"] = f"0x{cmd[1]:02X}"
    elif opcode == 0x05:
        cls = "RemoveObject"
    elif opcode == 0x07:
        cls = "ReturnObjectQueue"
    elif opcode == 0x08:
        cls = "MoveObject"
        args["speed"] = str(shortify_signed(cmd, 6))
        args["start_position"] = str(shortify_signed(cmd, 2))
        args["end_position"] = str(shortify_signed(cmd, 4))
        if (cmd[1] & 0x04) == 0x04:
            args["apply_to_x"] = "True"
        if (cmd[1] & 0x02) == 0x02:
            args["apply_to_y"] = "True"
        if (cmd[1] & 0x01) == 0x01:
            args["apply_to_z"] = "True"
        if (cmd[1] & 0x20) == 0x20:
            args["should_set_start_position"] = "True"
        if (cmd[1] & 0x40) == 0x40:
            args["should_set_end_position"] = "True"
        if (cmd[1] & 0x80) == 0x80:
            args["should_set_speed"] = "True"
    elif opcode == 0x09:
        cls = "Jmp"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode == 0x0A:
        cls = "Pause1Frame"
    elif opcode == 0x0C:
        cls = "MoveSpriteToCoords"
        if cmd[1] & 0x0E == 0:
            args["shift_type"] = "SHIFT_TYPE_0X00"
        elif cmd[1] & 0x0E == 2:
            args["shift_type"] = "SHIFT_TYPE_SHIFT"
        elif cmd[1] & 0x0E == 4:
            args["shift_type"] = "SHIFT_TYPE_TRANSFER"
        elif cmd[1] & 0x0E == 6:
            args["shift_type"] = "SHIFT_TYPE_0X04"
        elif cmd[1] & 0x0E == 8:
            args["shift_type"] = "SHIFT_TYPE_0X08"
        else:
            raise Exception("invalid shift type: %r" % command)
        args["speed"] = str(shortify_signed(cmd, 2))
        args["arch_height"] = str(shortify_signed(cmd, 4))
    elif opcode == 0x0E:
        cls = "ResetTargetMappingMemory"
    elif opcode == 0x0F:
        cls = "ResetObjectMappingMemory"
    elif opcode == 0x10:
        cls = "RunSubroutine"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode == 0x11:
        cls = "ReturnSubroutine"
    elif opcode == 0x1A:
        cls = "VisibilityOn"
    elif opcode == 0x1B:
        cls = "VisibilityOff"
    elif (
        opcode
        in [
            0x20,
            0x21,
            0x24,
            0x25,
            0x26,
            0x27,
            0x28,
            0x29,
            0x2A,
            0x2B,
            0x2C,
            0x2D,
            0x2E,
            0x2F,
        ]
        and cmd[1] & 0xF0 <= 0xB0
    ) or (opcode in [0x22, 0x23] and 0x10 <= cmd[1] & 0xF0 <= 0x60):
        byte2 = cmd[1] & 0xF0
        include_argnames = False
        if opcode == 0x20:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "SetAMEM8BitToConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "SetAMEM8BitTo7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "SetAMEM8BitTo7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEM8BitToAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetAMEM8BitToOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "SetAMEM8BitTo7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetAMEM8BitToOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "SetAMEM8BitToUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
        elif opcode == 0x21:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "SetAMEM16BitToConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "SetAMEM16BitTo7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "SetAMEM16BitTo7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEM16BitToAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetAMEM16BitToOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "SetAMEM16BitTo7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetAMEM16BitToOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "SetAMEM16BitToUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
        elif opcode == 0x22:
            if byte2 == 0x10:
                cls = "Set7E1xToAMEM8Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "Set7FToAMEM8Bit"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEMToAMEM8Bit"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["dest_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetOMEMCurrentToAMEM8Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "Set7E5xToAMEM8Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetOMEMMainToAMEM8Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "SetUnknownShortToAMEM8Bit"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        elif opcode == 0x23:
            if byte2 == 0x10:
                cls = "Set7E1xToAMEM16Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "Set7FToAMEM16Bit"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "SetAMEMToAMEM16Bit"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["dest_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "SetOMEMCurrentToAMEM16Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "Set7E5xToAMEM16Bit"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "SetOMEMMainToAMEM16Bit"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "SetUnknownShortToAMEM16Bit"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        elif opcode == 0x24:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitEqualsAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitEqualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            else:
                cls = "JmpIfAMEM8BitEqualsUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x25:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitEqualsAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitEqualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM16BitEqualsUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x26:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitNotEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitNotEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitNotEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitNotEqualsAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitNotEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitNotEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitNotEqualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM8BitNotEqualsUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x27:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitNotEqualsConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitNotEquals7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitNotEquals7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitNotEqualsAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitNotEqualsOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitNotEquals7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitNotEq16BitualsOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM16BitNotEqualsUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x28:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitLessThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitLessThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitLessThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitLessThanAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitLessThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitLessThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitLessThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM8BitLessThanUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x29:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitLessThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitLessThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitLessThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitLessThanAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitLessThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitLessThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitLessThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM16BitLessThanUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x2A:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM8BitGreaterOrEqualThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM8BitGreaterOrEqualThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM8BitGreaterOrEqualThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM8BitGreaterOrEqualThanUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x2B:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "JmpIfAMEM16BitGreaterOrEqualThan7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "JmpIfAMEM16BitGreaterOrEqualThan7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "JmpIfAMEM16BitGreaterOrEqualThan7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "JmpIfAMEM16BitGreaterOrEqualThanUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        elif opcode == 0x2C:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "IncAMEM8BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "IncAMEM8BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "IncAMEM8BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "IncAMEM8BitByAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "IncAMEM8BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "IncAMEM8BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "IncAMEM8BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "IncAMEM8BitByUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
        elif opcode == 0x2D:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "IncAMEM16BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "IncAMEM16BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "IncAMEM16BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "IncAMEM16BitByAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "IncAMEM16BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "IncAMEM16BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "IncAMEM16BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "IncAMEM16BitByUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
        elif opcode == 0x2E:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "DecAMEM8BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "DecAMEM8BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "DecAMEM8BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "DecAMEM8BitByAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "DecAMEM8BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "DecAMEM8BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "DecAMEM8BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "DecAMEM8BitByUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
        elif opcode == 0x2F:
            args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
            if byte2 == 0:
                cls = "DecAMEM16BitByConst"
                args["value"] = str(shortify(cmd, 2))
            elif byte2 == 0x10:
                cls = "DecAMEM16BitBy7E1x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x20:
                cls = "DecAMEM16BitBy7F"
                args["address"] = f"0x7F{shortify(cmd, 2):04X}"
            elif byte2 == 0x30:
                cls = "DecAMEM16BitByAMEM"
                src = cmd[2] & 0x0F
                upper = cmd[2] & 0xF0
                args["source_amem"] = f"0x{(src + 0x60):02X}"
                args["upper"] = f"0x{(upper):02X}"
                include_argnames = True
            elif byte2 == 0x40:
                cls = "DecAMEM16BitByOMEMCurrent"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 == 0x50:
                cls = "DecAMEM16BitBy7E5x"
                args["address"] = f"0x7E{shortify(cmd, 2):04X}"
            elif byte2 == 0x60:
                cls = "DecAMEM16BitByOMEMMain"
                args["omem"] = f"0x{cmd[2]:02X}"
                include_argnames = True
            elif byte2 <= 0xB0:
                cls = "DecAMEM16BitByUnknownShort"
                args["type"] = f"0x{(byte2 >> 4):01X}"
                args["value"] = f"0x{shortify(cmd, 2):04X}"
                include_argnames = True
            else:
                raise Exception("invalid amem shift type: %r" % command)
    elif opcode in [0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B]:
        cls = "UnknownJmp%02X" % opcode
        args["byte_1"] = str(cmd[1])
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode in [0x30, 0x31, 0x32, 0x33, 0x34, 0x35]:
        if opcode == 0x30:
            cls = "IncAMEM8Bit"
        elif opcode == 0x31:
            cls = "IncAMEM16Bit"
        elif opcode == 0x32:
            cls = "DecAMEM8Bit"
        elif opcode == 0x33:
            cls = "DecAMEM16Bit"
        elif opcode == 0x34:
            cls = "ClearAMEM8Bit"
        elif opcode == 0x35:
            cls = "ClearAMEM16Bit"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        include_argnames = False
    elif opcode in [0x36, 0x37, 0x38, 0x39, 0x40, 0x41]:
        if opcode == 0x36:
            cls = "SetAMEMBits"
        elif opcode == 0x37:
            cls = "ClearAMEMBits"
        elif opcode == 0x38:
            cls = "JmpIfAMEMBitsSet"
        elif opcode == 0x39:
            cls = "JmpIfAMEMBitsClear"
        elif opcode == 0x40:
            cls = "PauseScriptUntilAMEMBitsSet"
        elif opcode == 0x41:
            cls = "PauseScriptUntilAMEMBitsClear"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        bits = []
        for b in range(0, 8):
            if cmd[2] & (1 << b) != 0:
                bits.append(b)
        args["bits"] = "%r" % bits
        if opcode in [0x38, 0x39]:
            args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode == 0x3A:
        cls = "AttackTimerBegins"
    elif opcode == 0x43:
        cls = "SpriteSequence"
        args["sequence"] = str(cmd[1] & 0x0F)
        if cmd[1] & 0x10 == 0x10:
            args["looping_on"] = "True"
        if cmd[1] & 0x20 == 0x20:
            args["looping_off"] = "True"
        if cmd[1] & 0x40 == 0x40:
            args["bit_6"] = "True"
        if cmd[1] & 0x80 == 0x80:
            args["mirror"] = "True"
    elif opcode == 0x45:
        cls = "SetAMEM60ToCurrentTarget"
    elif opcode == 0x46:
        cls = "GameOverIfNoAlliesStanding"
    elif opcode == 0x4E:
        cls = "PauseScriptUntilSpriteSequenceDone"
    elif opcode == 0x50:
        cls = "JmpIfTargetDisabled"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode == 0x51:
        cls = "JmpIfTargetEnabled"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode == 0x5D:
        cls = "UseSpriteQueue"
        args["field_object"] = str(cmd[2])
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        if cmd[1] & 0x01 == 0x01:
            args["bit_0"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["bit_1"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["bit_2"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["character_slot"] = "True"
        if cmd[1] & 0x10 == 0x10:
            args["bit_4"] = "True"
        if cmd[1] & 0x20 == 0x20:
            args["bit_5"] = "True"
        if cmd[1] & 0x40 == 0x40:
            args["current_target"] = "True"
        if cmd[1] & 0x80 == 0x80:
            args["bit_7"] = "True"
    elif opcode == 0x5E:
        cls = "ReturnSpriteQueue"
    elif opcode == 0x63 and 0 <= cmd[1] <= 2:
        cls = "DisplayMessageAtOMEM60As"
        if cmd[1] == 0:
            args["type"] = "ATTACK_NAME"
        elif cmd[1] == 1:
            args["type"] = "SPELL_NAME"
        elif cmd[1] == 2:
            args["type"] = "ITEM_NAME"
        elif cmd[1] == 3:
            args["type"] = "UNKNOWN_MESSAGE_TYPE_3"
        elif cmd[1] == 4:
            args["type"] = "UNKNOWN_MESSAGE_TYPE_4"
        elif cmd[1] == 5:
            args["type"] = "UNKNOWN_MESSAGE_TYPE_5"
        include_argnames = False
    elif opcode == 0x64:
        cls = "UseObjectQueueAtOffsetWithAMEM60Index"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
    elif opcode == 0x68:
        cls = "UseObjectQueueAtOffsetWithAMEM60PointerOffset"
        args["index"] = str(cmd[1])
        args["destinations"] = '["%s"]' % command.parsed_data[0]
    elif opcode == 0x69:
        cls = "SetOMEM60To072C"
    elif opcode == 0x6A:
        cls = "SetAMEMToRandomByte"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        args["upper_bound"] = str(cmd[2])
    elif opcode == 0x6B:
        cls = "SetAMEMToRandomShort"
        args["amem"] = f"0x{((cmd[1] & 0x0F) + 0x60):02X}"
        args["upper_bound"] = str(shortify(cmd, 2))
    elif opcode == 0x70:
        cls = "EnableSpritesOnSubscreen"
    elif opcode == 0x71:
        cls = "DisableSpritesOnSubscreen"
    elif opcode == 0x72:
        cls = "NewEffectObject"
        args["effect"] = EFFECTS[cmd[2]]
        if cmd[1] & 0x01 == 0x01:
            args["looping_on"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["playback_off"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["looping_off"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["bit_3"] = "True"
    elif opcode == 0x73:
        cls = "Pause2Frames"
    elif opcode == 0x74 and cmd[1:] in [
        [0x04, 0x00],
        [0x08, 0x00],
        [0x00, 0x02],
        [0x00, 0x04],
        [0x00, 0x08],
    ]:
        cls = "PauseScriptUntil"
        if cmd[1:] == [0x04, 0x00]:
            args["condition"] = "SEQ_4BPP_COMPLETE"
        elif cmd[1:] == [0x08, 0x00]:
            args["condition"] = "SEQ_2BPP_COMPLETE"
        elif cmd[1:] == [0x00, 0x02]:
            args["condition"] = "FADE_IN_COMPLETE"
        elif cmd[1:] == [0x00, 0x04]:
            args["condition"] = "FADE_4BPP_COMPLETE"
        elif cmd[1:] == [0x00, 0x08]:
            args["condition"] = "FADE_2BPP_COMPLETE"
    elif opcode == 0x75:
        cls = "PauseScriptUntilBitsClear"
        args["bits"] = f"0x{shortify(cmd, 1):04X}"
        include_argnames = False
    elif opcode == 0x76:
        cls = "ClearEffectIndex"
    elif opcode in [0x77, 0x78]:
        if opcode == 0x77:
            cls = "Layer3On"
        else:
            cls = "Layer3Off"
        if cmd[1] & 0xF0 == 0:
            args["property"] = "TRANSPARENCY_OFF"
        elif cmd[1] & 0xF0 == 0x10:
            args["property"] = "OVERLAP_ALL"
        elif cmd[1] & 0xF0 == 0x20:
            args["property"] = "OVERLAP_NONE"
        elif cmd[1] & 0xF0 == 0x30:
            args["property"] = "OVERLAP_ALL_EXCEPT_ALLIES"
        else:
            raise Exception("invalid property type at %r" % command)
        if cmd[1] & 0x01 == 0x01:
            args["bit_0"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["bpp4"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["bpp4"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["invisible"] = "True"
    elif opcode == 0x7A and 0 <= cmd[1] <= 2:
        cls = "DisplayMessage"
        if cmd[1] == 0:
            args["type"] = "ATTACK_NAME"
        elif cmd[1] == 1:
            args["type"] = "SPELL_NAME"
        elif cmd[1] == 2:
            args["type"] = "ITEM_NAME"
        args["dialog_id"] = str(cmd[2])
        include_argnames = False
    elif opcode == 0x7B:
        cls = "PauseScriptUntilDialogClosed"
    elif opcode == 0x7E:
        cls = "FadeOutObject"
        args["duration"] = str(cmd[1])
    elif opcode == 0x7F:
        cls = "ResetSpriteSequence"
    elif opcode == 0x80:
        cls = "ShineEffect"
        args["colour_count"] = str(cmd[2] & 0x0F)
        args["starting_colour_index"] = str((cmd[2] & 0xF0) >> 4)
        args["glow_duration"] = str(cmd[3])
        if cmd[1] == 1:
            args["west"] = "True"
        elif cmd[1] == 0:
            args["east"] = "True"
        else:
            raise Exception(command)
    elif opcode == 0x85:
        if cmd[1] == 0:
            cls = "FadeOutEffect"
        elif cmd[1] == 0x10:
            cls = "FadeOutSprite"
        elif cmd[1] == 0x20:
            cls = "FadeOutScreen"
        elif cmd[1] == 2:
            cls = "FadeInEffect"
        elif cmd[1] == 0x12:
            cls = "FadeInSprite"
        elif cmd[1] == 0x22:
            cls = "FadeInScreen"
        args["duration"] = cmd[2]
    elif opcode == 0x86 and cmd[1] in [1, 2, 4]:
        if cmd[1] == 1:
            cls = "ShakeScreen"
        elif cmd[1] == 2:
            cls = "ShakeSprites"
        elif cmd[1] == 4:
            cls = "ShakeScreenAndSprites"
        args["amount"] = str(cmd[4])
        args["speed"] = str(shortify(cmd, 5))
    elif opcode == 0x87:
        cls = "StopShakingObject"
    elif opcode == 0x9C:
        cls = "WaveEffect"
        param1 = cmd[2]
        if param1 & 0x01 == 0x01:
            args["layer"] = "WAVE_LAYER_BATTLEFIELD"
        elif param1 & 0x02 == 0x02:
            args["layer"] = "WAVE_LAYER_4BPP"
        elif param1 & 0x04 == 0x04:
            args["layer"] = "WAVE_LAYER_2BPP"
        if param1 & 0x40 == 0x40:
            args["direction"] = "WAVE_LAYER_HORIZONTAL"
        elif param1 & 0x80 == 0x80:
            args["direction"] = "WAVE_LAYER_VERTICAL"
        args["depth"] = str(shortify(cmd, 3))
        args["intensity"] = str(shortify(cmd, 5))
        args["speed"] = str(shortify(cmd, 7))
        if param1 & 0x08 == 0x08:
            args["bit_3"] = "True"
        if param1 & 0x10 == 0x10:
            args["bit_4"] = "True"
        if param1 & 0x20 == 0x20:
            args["bit_5"] = "True"
        if cmd[1] != 0:
            args["byte_1"] = f"0x{cmd[1]:02X}"
    elif opcode == 0x9D:
        cls = "StopWaveEffect"
        if cmd[1] & 0x80 == 0x80:
            args["bit_7"] = "True"
    elif opcode == 0xA7:
        cls = "JmpIfTimedHitSuccess"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
    elif opcode == 0x8E:
        cls = "ScreenFlashWithDuration"
        args["colour"] = FLASH_COLOURS[cmd[1] & 0x07]
        args["duration"] = str(cmd[2])
        if cmd[1] & 0xF8 != 0:
            args["unknown_upper"] = str(cmd[1] & 0xF8)
        include_argnames = False
    elif opcode == 0x8F:
        cls = "ScreenFlash"
        args["colour"] = FLASH_COLOURS[cmd[1] & 0x07]
        if cmd[1] & 0xF8 != 0:
            args["unknown_upper"] = str(cmd[1] & 0xF8)
        include_argnames = False
    elif opcode == 0x95:
        cls = "InitializeBonusMessageSequence"
    elif opcode == 0x96:
        cls = "DisplayBonusMessage"
        args["message"] = BONUS_MESSAGES[cmd[2]]
        args["x"] = str(byte_signed(cmd[3]))
        args["y"] = str(byte_signed(cmd[4]))
    elif opcode == 0x97:
        cls = "PauseScriptUntilBonusMessageComplete"
    elif opcode == 0xA3:
        cls = "ScreenEffect"
        args["message"] = SCREEN_EFFECTS[cmd[1]]
        include_argnames = False
    elif opcode in [0xAB, 0xAE]:
        cls = "PlaySound"
        args["sound"] = SOUNDS[cmd[1]]
        if opcode == 0xAE:
            args["channel"] = "4"
    elif opcode == 0xB0:
        cls = "PlayMusicAtCurrentVolume"
        args["sound"] = MUSIC[cmd[1]]
        include_argnames = False
    elif opcode == 0xB1:
        cls = "PlayMusicAtVolume"
        args["sound"] = MUSIC[cmd[1]]
        args["volume"] = str(shortify(cmd, 2))
        include_argnames = False
    elif opcode == 0xB2:
        cls = "StopCurrentSoundEffect"
    elif opcode == 0xB6:
        cls = "FadeCurrentMusicToVolume"
        args["speed"] = str(cmd[1])
        args["volume"] = str(cmd[2])
    elif opcode == 0xBB:
        cls = "SetTarget"
        args["target"] = TARGETS[cmd[1]]
        include_argnames = False
    elif opcode in [0xBC, 0xBD]:
        include_argnames = False
        if cmd[2] == 0:
            cls = (
                "AddItemToStandardInventory"
                if opcode == 0xBC
                else "AddItemToKeyItemInventory"
            )
            args["target"] = ITEMS[cmd[1]]
        elif cmd[2] == 0xFF:
            cls = (
                "RemoveItemFromStandardInventory"
                if opcode == 0xBC
                else "RemoveItemFromKeyItemInventory"
            )
            args["target"] = ITEMS[256 - cmd[1]]
        else:
            raise Exception(command)
    elif opcode == 0xBE:
        cls = "AddCoins"
        args["amount"] = str(shortify(cmd, 1))
        include_argnames = False
    elif opcode == 0xBF:
        cls = "AddYoshiCookiesToInventory"
        args["amount"] = str(cmd[1])
        include_argnames = False
    elif opcode == 0xC3:
        cls = "DoMaskEffect"
        args["effect"] = MASKS[cmd[1] & 0x07]
        if cmd[1] & 0xF8 != 0:
            args["unknown_upper"] = str(cmd[1] & 0xF8)
        include_argnames = False
    elif opcode == 0xC6:
        cls = "SetMaskCoords"
        point_bytes = byte_signed(cmd[1])
        points = []
        for i in range(2, (point_bytes // 2) * 2 + 2, 2):
            points.append("(%s, %s)" % (byte_signed(cmd[i]), byte_signed(cmd[i + 1])))
        args["points"] = f'[{",".join(points)}]'
        if point_bytes % 2 != 0:
            args["extra_byte"] = f"0x{cmd[2 + point_bytes - 1]:02x}"
    elif opcode == 0xCB:
        cls = "SetSequenceSpeed"
        args["speed"] = str(cmd[1])
        include_argnames = False
    elif opcode == 0xCC:
        cls = "StartTrackingAllyButtonInputs"
    elif opcode == 0xCD:
        cls = "EndTrackingAllyButtonInputs"
    elif opcode == 0xCE:
        cls = "TimingForOneTieredButtonPress"
        args["start_accepting_input"] = str(cmd[2])
        args["end_accepting_input"] = str(cmd[1])
        args["partial_start"] = str(cmd[3])
        args["perfect_start"] = str(cmd[4])
        args["perfect_end"] = str(cmd[5])
        args["destinations"] = '["%s"]' % command.parsed_data[0]
    elif opcode == 0xCF:
        cls = "TimingForOneBinaryButtonPress"
        args["start_accepting_input"] = str(cmd[2])
        args["end_accepting_input"] = str(cmd[1])
        args["timed_hit_ends"] = str(cmd[3])
        args["destinations"] = '["%s"]' % command.parsed_data[0]
    elif opcode == 0xD0:
        cls = "TimingForMultipleButtonPresses"
        args["start_accepting_input"] = str(cmd[1])
        args["destinations"] = '["%s"]' % command.parsed_data[0]
    elif opcode == 0xD1:
        cls = "TimingForButtonMashUnknown"
    elif opcode == 0xD2:
        cls = "TimingForButtonMashCount"
        args["max_presses"] = str(cmd[1])
    elif opcode == 0xD3:
        cls = "TimingForRotationCount"
        args["start_accepting_input"] = str(cmd[2])
        args["end_accepting_input"] = str(cmd[1])
        args["max_presses"] = str(cmd[3])
    elif opcode == 0xD4:
        cls = "TimingForChargePress"
        args["charge_level_1_end"] = str(cmd[1])
        args["charge_level_2_end"] = str(cmd[2])
        args["charge_level_3_end"] = str(cmd[3])
        args["charge_level_4_end"] = str(cmd[4])
        args["overcharge_end"] = str(cmd[5])
    elif opcode == 0xD5:
        cls = "SummonMonster"
        args["monster"] = ENEMIES[cmd[2]]
        args["position"] = cmd[3]
        if cmd[1] & 0x01 == 0x01:
            args["bit_0"] = "True"
        if cmd[1] & 0x02 == 0x02:
            args["bit_1"] = "True"
        if cmd[1] & 0x04 == 0x04:
            args["bit_2"] = "True"
        if cmd[1] & 0x08 == 0x08:
            args["bit_3"] = "True"
        if cmd[1] & 0x10 == 0x10:
            args["bit_4"] = "True"
        if cmd[1] & 0x20 == 0x20:
            args["bit_5"] = "True"
        if cmd[1] & 0x40 == 0x40:
            args["bit_6"] = "True"
        if cmd[1] & 0x80 == 0x80:
            args["bit_7"] = "True"
    elif opcode == 0xD8:
        cls = "MuteTimingJmp"
        args["destinations"] = '["%s"]' % command.parsed_data[0]
        include_argnames = False
    elif opcode == 0xD9:
        cls = "DisplayCantRunDialog"
    elif opcode == 0xE0:
        cls = "StoreOMEM60ToItemInventory"
    elif opcode == 0xE1:
        cls = "RunBattleEvent"
        args["script_id"] = SCRIPT_NAMES["battle_events"][shortify(cmd, 1)]
        if cmd[3] != 0:
            args["offset"] = str(cmd[3])
    else:
        cls = "UnknownCommand"
        include_argnames = False
        args["args"] = "%r" % bytearray(cmd)

    return cls, args, use_identifier, include_argnames


# empty space filler: 0x11

# screen flash none = 2 bytes {0x8F 0x00}
# screen flash none 0 frames = 3 bytes {0x8F 0x00 0x00}

# theoretically, could we have multiple battle events for walking on KC/CD depending on # of party members,
# and battle logic picks which of the 3 to run?
# maybe THAT'S worth disassembling for
# figure out which battle events are unused somehow

# also need to make solo crystal battle events

# also need to DA battle text to not deadname birdetta
