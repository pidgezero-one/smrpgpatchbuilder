"""Based on patcdr's original battle disassembler"""

import os
import shutil
from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import shortify, writeline

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
    "BobombHenchman",
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
    "BahamuttMagikoopa",
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

TARGETS = [
    "MARIO",
    "TOADSTOOL",
    "BOWSER",
    "GENO",
    "MALLOW",
    "UNKNOWN_5",
    "UNKNOWN_6",
    "UNKNOWN_7",
    "UNKNOWN_8",
    "UNKNOWN_9",
    "UNKNOWN_10",
    "UNKNOWN_11",
    "UNKNOWN_12",
    "UNKNOWN_13",
    "UNKNOWN_14",
    "UNKNOWN_15",
    "SLOT_1",
    "SLOT_2",
    "SLOT_3",
    "MONSTER_1_SET",
    "MONSTER_2_SET",
    "MONSTER_3_SET",
    "MONSTER_4_SET",
    "MONSTER_5_SET",
    "MONSTER_6_SET",
    "MONSTER_7_SET",
    "MONSTER_8_SET",
    "SELF",
    "ALL_ALLIES_EXCLUDING_SELF",
    "RANDOM_ALLY_EXCLUDING_SELF_OPPONENT_IF_SOLO",
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
ATTACKS = [
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
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "AttackDoNothing",
]
SPELLS = [
    "Jump",
    "FireOrb",
    "SuperJump",
    "SuperFlame",
    "UltraJump",
    "UltraFlame",
    "Therapy",
    "GroupHug",
    "SleepyTime",
    "ComeBack",
    "Mute",
    "PsychBomb",
    "Terrorize",
    "PoisonGas",
    "Crusher",
    "BowserCrush",
    "GenoBeam",
    "GenoBoost",
    "GenoWhirl",
    "GenoBlast",
    "GenoFlash",
    "Thunderbolt",
    "HPRain",
    "Psychopath",
    "Shocker",
    "Snowy",
    "StarRain",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
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
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "SpellDoNothing",
]

BATTLE_EVENTS = [
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
    "BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT_RANDOMIZER_ONLY",
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
]
COMMANDS = ["COMMAND_ATTACK", "COMMAND_SPECIAL", "COMMAND_ITEM"]

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
VARIABLES = [
    "0x7EE000",
    "0x7EE001",
    "0x7EE002",
    "0x7EE003",
    "0x7EE004",
    "DESIGNATED_RANDOM_NUM_VAR",
    "ATTACK_PHASE_COUNTER",
    "0x7EE007",
    "0x7EE008",
    "0x7EE009",
    "0x7EE00A",
    "0x7EE00B",
    "0x7EE00C",
    "0x7EE00D",
    "0x7EE00E",
    "0x7EE00F",
]


battle_lengths = [
    1, #00
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
    1, #10
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
    1, #20
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
    1, #30
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
    1, #40
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
    1, #50
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
    1, #60
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
    1, #70
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
    1, #80
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
    1, #90
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
    1, #A0
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
    1, #B0
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
    1, #C0
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
    1, #D0
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
    4, #E0
    0,
    2,
    2,
    0,
    2,
    3,
    4,
    2,
    0,
    4,
    3,
    1,
    2,
    0,
    2, 
    4, #F0
    2,
    3,
    3,
    4,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    4,
    1,
    1,
    1,
]

def tokenize(rom, start):
    dex = start
    ff_seen = False
    acc = []
    while True:
        cmd = rom[dex]
        if cmd == 0xFF:
            if ff_seen:
                break
            ff_seen = True
        l = battle_lengths[cmd]
        acc.append((rom[dex : dex + l], dex))
        dex += l
    return acc

def pythonize(command):
    opcode = command[0]
    args = {}
    cls = None
    include_argnames = True
    
    match opcode:
        case 0xE0:
            cls = "Attack"
            args["attack_1"] = ATTACKS[command[1]]
            args["attack_2"] = ATTACKS[command[2]]
            args["attack_3"] = ATTACKS[command[3]]
            include_argnames = False
        case 0xE2:
            cls = "SetTarget"
            args["target"] = TARGETS[command[1]]
            include_argnames = False
        case 0xE3:
            cls = "RunBattleDialog"
            args["dialog_id"] = str(command[1])
            include_argnames = False
        case 0xE5:
            cls = "RunBattleEvent"
            assert 0 <= command[1] <= 102
            args["event_id"] = BATTLE_EVENTS[command[1]]
            include_argnames = False
        case 0xE6:
            match command[1]:
                case 0x00:
                    cls = "IncreaseVarBy1"
                case 0x01:
                    cls = "DecreaseVarBy1"
                case _:
                    raise Exception("invalid byte")
            args["variable"] = VARIABLES[command[2] & 0x0F]
            include_argnames = False
        case 0xE7:
            match command[1]:
                case 0x00:
                    cls = "SetVarBits"
                case 0x01:
                    cls = "ClearVarBits"
                case _:
                    raise Exception("invalid byte")
            args["variable"] = VARIABLES[command[2] & 0x0F]
            bits = []
            for i in range(0, 8):
                comp = 1 << i
                if command[3] & comp == comp:
                    bits.append(i)
            args["bits"] = "%r" % bits
            include_argnames = False
        case 0xE8:
            cls = "ClearVar"
            args["variable"] = VARIABLES[command[1] & 0x0F]
            include_argnames = False
        case 0xEA:
            match command[1]:
                case 0x00:
                    cls = "RemoveTarget"
                case 0x01:
                    cls = "CallTarget"
                case _:
                    raise Exception("invalid byte")
            args["target"] = TARGETS[command[3]]
            include_argnames = False
        case 0xEB:
            match command[1]:
                case 0x00:
                    cls = "MakeInvulnerable"
                case 0x01:
                    cls = "MakeVulnerable"
                case _:
                    raise Exception("invalid byte")
            args["target"] = TARGETS[command[2]]
            include_argnames = False
        case 0xEC:
            cls = "ExitBattle"
        case 0xED:
            cls = "Set7EE005ToRandomNumber"
            args["upper_bound"] = str(command[1])
        case 0xEF:
            cls = "CastSpell"
            args["spell_1"] = SPELLS[command[1]]
            include_argnames = False
        case 0xF0:
            cls = "CastSpell"
            args["spell_1"] = SPELLS[command[1]]
            args["spell_2"] = SPELLS[command[2]]
            args["spell_3"] = SPELLS[command[3]]
            include_argnames = False
        case 0xF1:
            cls = "DoMonsterBehaviour"
            args["animation_id"] = str(command[1])
            include_argnames = False
        case 0xF2:
            match command[1]:
                case 0x00:
                    cls = "SetUntargetable"
                case 0x01:
                    cls = "SetTargetable"
                case _:
                    raise Exception("invalid byte")
            if command[2] == 0:
                args["target"] = TARGETS[0x1B]
            else:
                args["target"] = TARGETS[command[2] + 0x12]
            include_argnames = False
        case 0xF3:
            match command[1]:
                case 0x00:
                    cls = "EnableCommand"
                case 0x01:
                    cls = "DisableCommand"
                case _:
                    raise Exception("invalid byte")
            commands_set = []
            if command[2] & 0x01 == 0x01:
                commands_set.append("COMMAND_ATTACK")
            if command[2] & 0x02 == 0x02:
                commands_set.append("COMMAND_SPECIAL")
            if command[2] & 0x04 == 0x04:
                commands_set.append("COMMAND_ITEM")
            args["commands"] = "[%s]" % ", ".join(commands_set)
            include_argnames = False
        case 0xF4:
            match command[1]:
                case 0x00:
                    cls = "RemoveAllInventory"
                case 0x01:
                    cls = "RestoreInventory"
                case _:
                    raise Exception("invalid byte")
        case 0xFB:
            cls = "DoNothing"
        case 0xFC:
            match command[1]:
                case 0x01:
                    cls = "IfTargetedByCommand"
                    include_argnames = False
                    if command[2] == command[3]:
                        args["commands"] = "[%s]" % COMMANDS[command[2] - 2]
                    else:
                        args["commands"] = "[%s]" % ", ".join(
                            COMMANDS[command[2] - 2], COMMANDS[command[3] - 2]
                        )
                case 0x02:
                    cls = "IfTargetedBySpell"
                    include_argnames = False
                    nums = []
                    for a in command[2:]:
                        nums.append(a)
                    if nums[0] == nums[1]:
                        args["spells"] = "[%s]" % SPELLS[nums[0]]
                    else:
                        args["spells"] = "[%s]" % ", ".join(SPELLS[nums[0]], SPELLS[nums[1]])
                case 0x03:
                    cls = "IfTargetedByItem"
                    include_argnames = False
                    nums = []
                    for a in command[2:]:
                        nums.append(a)
                    if nums[0] == nums[1]:
                        args["items"] = "[%s]" % ITEMS[nums[0]]
                    else:
                        args["items"] = "[%s]" % ", ".join(ITEMS[nums[0]], ITEMS[nums[1]])
                case 0x04:
                    cls = "IfTargetedByElement"
                    include_argnames = False
                    elements = []
                    if command[2] & 0x10 == 0x10:
                        elements.append("Element.ICE")
                    if command[2] & 0x20 == 0x20:
                        elements.append("Element.THUNDER")
                    if command[2] & 0x40 == 0x40:
                        elements.append("Element.FIRE")
                    if command[2] & 0x80 == 0x80:
                        elements.append("Element.Jump")
                    args["elements"] = "[%s]" % ", ".join(elements)
                case 0x05:
                    cls = "IfTargetedByRegularAttack"
                case 0x06:
                    cls = "IfTargetHPBelow"
                    include_argnames = False
                    args["target"] = TARGETS[command[2]]
                    args["threshold"] = str(command[3])
                case 0x07:
                    cls = "IfHPBelow"
                    include_argnames = False
                    args["threshold"] = str(shortify(command, 2))
                case 0x08:
                    cls = "IfTargetAfflictedBy"
                    include_argnames = False
                    elements = []
                    args["target"] = TARGETS[command[2]]
                    if command[3] & 0x01 == 0x01:
                        elements.append("Status.MUTE")
                    if command[3] & (1 << 1) == (1 << 1):
                        elements.append("Status.SLEEP")
                    if command[3] & (1 << 2) == (1 << 2):
                        elements.append("Status.POISON")
                    if command[3] & (1 << 3) == (1 << 3):
                        elements.append("Status.FEAR")
                    if command[3] & (1 << 4) == (1 << 4):
                        elements.append("Status.BERSERK")
                    if command[3] & (1 << 5) == (1 << 5):
                        elements.append("Status.MUSHROOM")
                    if command[3] & (1 << 6) == (1 << 6):
                        elements.append("Status.SCARECROW")
                    if command[3] & (1 << 7) == (1 << 7):
                        elements.append("Status.INVINCIBLE")
                    args["statuses"] = "[%s]" % ", ".join(elements)
                case 0x09:
                    cls = "IfTargetNotAfflictedBy"
                    include_argnames = False
                    elements = []
                    args["target"] = TARGETS[command[2]]
                    if command[3] & 0x01 == 0x01:
                        elements.append("Status.MUTE")
                    if command[3] & (1 << 1) == (1 << 1):
                        elements.append("Status.SLEEP")
                    if command[3] & (1 << 2) == (1 << 2):
                        elements.append("Status.POISON")
                    if command[3] & (1 << 3) == (1 << 3):
                        elements.append("Status.FEAR")
                    if command[3] & (1 << 4) == (1 << 4):
                        elements.append("Status.BERSERK")
                    if command[3] & (1 << 5) == (1 << 5):
                        elements.append("Status.MUSHROOM")
                    if command[3] & (1 << 6) == (1 << 6):
                        elements.append("Status.SCARECROW")
                    if command[3] & (1 << 7) == (1 << 7):
                        elements.append("Status.INVINCIBLE")
                    args["statuses"] = "[%s]" % ", ".join(elements)
                case 0x0A:
                    cls = "IfTurnCounterEquals"
                    include_argnames = False
                    args["phase"] = str(command[2])
                case 0x0C:
                    cls = "IfVarLessThan"
                    include_argnames = False
                    args["variable"] = VARIABLES[command[2] & 0x0F]
                    args["threshold"] = str(command[3])
                case 0x0D:
                    cls = "IfVarEqualOrGreaterThan"
                    include_argnames = False
                    args["variable"] = VARIABLES[command[2] & 0x0F]
                    args["threshold"] = str(command[3])
                case 0x10:
                    match command[2]:
                        case 0x00:
                            cls = "IfTargetAlive"
                        case 0x01:
                            cls = "IfTargetKOed"
                    include_argnames = False
                    args["target"] = TARGETS[command[3]]
                case 0x11:
                    cls = "IfVarBitsSet"
                    include_argnames = False
                    args["variable"] = VARIABLES[command[2] & 0x0F]
                    bits = []
                    for i in range(0, 8):
                        comp = 1 << i
                        if command[3] & comp == comp:
                            bits.append(i)
                    args["bits"] = "%r" % bits
                case 0x12:
                    cls = "IfVarBitsClear"
                    include_argnames = False
                    args["variable"] = VARIABLES[command[2] & 0x0F]
                    bits = []
                    for i in range(0, 8):
                        comp = 1 << i
                        if command[3] & comp == comp:
                            bits.append(i)
                    args["bits"] = "%r" % bits
                case 0x13:
                    cls = "IfCurrentlyInFormationID"
                    include_argnames = False
                    args["formation_id"] = str(command[2])
                case 0x14:
                    cls = "IfLastMonsterStanding"
                case _:
                    raise Exception("invalid byte")
        case 0xFD:
            cls = "Wait1Turn"
        case 0xFE:
            cls = "Wait1TurnandRestartScript"
        case 0xFF:
            cls = "StartCounterCommands"
        case _:
            if battle_lengths[opcode] == 1 and (opcode <= 128 or opcode == 251):
                cls = "Attack"
                args["attack_1"] = ATTACKS[opcode]
                include_argnames = False
            else:
                cls = "Db"
                args["bytes"] = "%r" % command
                include_argnames = False
    arg_strings = []
    for key in args:
        if include_argnames:
            arg_strings.append("%s=%s" % (key, args[key]))
        else:
            arg_strings.append(args[key])
    arg_string = ", ".join(arg_strings)
    output = "%s(%s%s)" % (cls, arg_string, "")
    return output
    

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):
        output_path = "./src/disassembler_output/monster_ai"

        shutil.rmtree(output_path, ignore_errors=True)

        os.makedirs(f"{output_path}/scripts", exist_ok=True)
        open(f"{output_path}/__init__.py", "w")
        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        start = 0x390000
        for monster_id in range(256):
            ptr_location = start + 0x30AA + monster_id * 2
            ptr = shortify(rom, ptr_location)
            script_location = start + ptr
            script = tokenize(rom, script_location)
            
            output = "# %i - %s" % (monster_id, ENEMIES[monster_id])
            output += "\n\nfrom smrpgpatchbuilder.datatypes.enemies.implementations import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.items.implementations import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.monster_scripts import *"
            output += "\nfrom smrpgpatchbuilder.datatypes.battle_animation_scripts.ids.battle_events import *"
            output += "\n\nscript = MonsterScript([\n\t"

            output += ",\n\t".join([pythonize(entry[0]) for entry in script])

            output += "\n])"
            file = open(f"{output_path}/scripts/script_{monster_id}.py", "w")
            file.write(output)
            file.close()
        open(f"{output_path}/scripts/__init__.py", "w")
        open(f"{output_path}/__init__.py", "w")
        module = open(f"{output_path}/monster_scripts.py", "w")
        writeline(module, f"from smrpgpatchbuilder.datatypes.monster_scripts.types import MonsterScriptBank")
        for monster_id in range(256):
            writeline(module, f"from .scripts.script_{monster_id} import script as script_{monster_id}")
        writeline(module, "monster_scripts = MonsterScriptBank([")
        for monster_id in range(256):
            writeline(module, f"\tscript_{monster_id},")
        writeline(module, "])")
        module.close()
            
