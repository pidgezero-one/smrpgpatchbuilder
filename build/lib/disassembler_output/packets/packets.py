from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import Packet, PacketCollection
from ..variables.sprite_names import *
from ..variables.action_script_names import *

P000_FLASHING_POOF_FLOWER = Packet(
    packet_id=0,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0910_FLOWER_FLASH_THEN_POOF,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P001_FLASHING_POOF_MUSHROOM = Packet(
    packet_id=1,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0908_MUSHROOM_FLASH_THEN_POOF,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P002_BRIEF_KEY = Packet(
    packet_id=2,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0913_KEY_APPEARS_BRIEFLY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P003_BRIEF_STAR = Packet(
    packet_id=3,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0909_STAR_APPEARS_BRIEFLY,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x02, 0x04, 0x01, 0x00, 0x00]),
)

P004_MIMIC_POOF_ON_DEFEAT = Packet(
    packet_id=4,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0912_POOF_WHEN_MIMIC_3_DEFEATED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x02, 0x03, 0x01, 0x00, 0x00]),
)

P005_BRIEF_POOF_BAG = Packet(
    packet_id=5,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0127_BAG_APPEARS_BRIEFLY_THEN_POOFS,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P006_STATIC_SIDEWAYS_SPARKLE = Packet(
    packet_id=6,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P007_STATIC_SIDEWAYS_SPARKLE = Packet(
    packet_id=7,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P008_STATIC_EXPLOSION = Packet(
    packet_id=8,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P009_STATIC_BLUE_CLOUD = Packet(
    packet_id=9,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P010_STATIC_SMALL_FROG_COIN = Packet(
    packet_id=10,
    sprite_id=SPR0202_SHOES,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P011_STATIC_LEVELUP_TEXT = Packet(
    packet_id=11,
    sprite_id=SPR0203_LEVEL_UP_TEXT_FROM_INVINCIBLE_STAR,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P012_STATIC_GREY_EXPLOSION = Packet(
    packet_id=12,
    sprite_id=SPR0204_GREY_EXPLOSION_WHEN_ENCOUNTERING_FIREBALLS,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P013_STATIC_MICROBOMB = Packet(
    packet_id=13,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P014_UNUSED = Packet(
    packet_id=14,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0914_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x03, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P015_UNUSED = Packet(
    packet_id=15,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0915_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x03, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P016_BIG_COIN_BEING_COLLECTED = Packet(
    packet_id=16,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0904_COIN_GETS_COLLECTED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x05, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P017_SMALL_MINIGAME_COIN = Packet(
    packet_id=17,
    sprite_id=SPR0193_SMALL_COIN,
    shadow=False,
    action_script_id=A0171_MINIGAME_COIN_SPINS,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x05, 0x03, 0x04, 0x01, 0x00, 0x00]),
)

P018_SMALL_COIN_BEING_COLLECTED = Packet(
    packet_id=18,
    sprite_id=SPR0193_SMALL_COIN,
    shadow=False,
    action_script_id=A0904_COIN_GETS_COLLECTED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x05, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P019_FROG_COIN_BEING_COLLECTED = Packet(
    packet_id=19,
    sprite_id=SPR0194_FROG_COIN,
    shadow=False,
    action_script_id=A0911_FROG_COIN_GETS_COLLECTED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x05, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P020_WATER_DROPLETS_USE_7016_701A = Packet(
    packet_id=20,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0167_SPAWN_AT_7016_701A_CALCULATED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P021_FLASHING_SMALL_EXPLOSION = Packet(
    packet_id=21,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0623_SMALL_EXPLOSION_FLASH_7_TIMES,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P022_RECURSIVE_SPARKLES = Packet(
    packet_id=22,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0446_SUMMON_EXTRA_SPARKLES,
    unknown_bits=[True, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x03, 0x00, 0x00]),
)

P023_LOOPING_SINGLE_SPARKLE = Packet(
    packet_id=23,
    sprite_id=SPR0197_SPARKLE_SIDEWAYS,
    shadow=False,
    action_script_id=A0447_LOOPING_SINGLE_SPARKLE,
    unknown_bits=[True, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x03, 0x00, 0x00]),
)

P024_REGULAR_SOUND_EXPLOSION = Packet(
    packet_id=24,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x02, 0x03, 0x01, 0x00, 0x00]),
)

P025_UNUSED = Packet(
    packet_id=25,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P026_UNUSED = Packet(
    packet_id=26,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=False,
    action_script_id=A0621_SEQ_10_STORE_BUTTON_INPUT_AND_MAKE_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x06, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P027_UNUSED = Packet(
    packet_id=27,
    sprite_id=SPR0237_EGG,
    shadow=False,
    action_script_id=A0622_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x04, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P028_MUSHROOM_THROWN_SOUTHWEST = Packet(
    packet_id=28,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0907_MUSHROOM_THROWN_SOUTHWEST,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P029_SPARKLE_LINE_LOOPED = Packet(
    packet_id=29,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    shadow=False,
    action_script_id=A0507_SPARKLE_LINE_LOOPED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P030_WATER_SPLASH_DROPS_SFX = Packet(
    packet_id=30,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0720_WATER_SPLASH_DROPS_SFX,
    unknown_bits=[True, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x02, 0x03, 0x03, 0x00, 0x00]),
)

P031_LEVELUP_TEXT = Packet(
    packet_id=31,
    sprite_id=SPR0203_LEVEL_UP_TEXT_FROM_INVINCIBLE_STAR,
    shadow=False,
    action_script_id=A0620_LEVELUP_TEXT,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P032_BLUE_CLOUD = Packet(
    packet_id=32,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0651_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x03, 0x01, 0x00, 0x00]),
)

P033_BOMB_EXPLOSION = Packet(
    packet_id=33,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0303_BOMB_EXPLOSION,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x03, 0x01, 0x00, 0x00]),
)

P034_GREY_EXPLOSION_SFX = Packet(
    packet_id=34,
    sprite_id=SPR0204_GREY_EXPLOSION_WHEN_ENCOUNTERING_FIREBALLS,
    shadow=False,
    action_script_id=A0063_EXPLOSION_WITH_SOUND,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x02, 0x03, 0x01, 0x00, 0x00]),
)

P035_FLOWER_FALL = Packet(
    packet_id=35,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0917_SEQ_0_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P036_MUSHROOM_FALL = Packet(
    packet_id=36,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0916_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P037_ITEM_BAG_FALL = Packet(
    packet_id=37,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0918_SEQ_5_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P038_MUSHROOM_FALL_DEFAULT_PRIORITY = Packet(
    packet_id=38,
    sprite_id=SPR0195_FLOWER,
    shadow=True,
    action_script_id=A0921_SEQ_1_FALLING,
    unknown_bits=[False, True, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P039_UNUSED = Packet(
    packet_id=39,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0915_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x01, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P040_UNUSED = Packet(
    packet_id=40,
    sprite_id=SPR0208_HAMMER_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x00, 0x00, 0x00]),
)

P041_UNUSED = Packet(
    packet_id=41,
    sprite_id=SPR0209_STICK_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x00, 0x00, 0x00]),
)

P042_UNUSED = Packet(
    packet_id=42,
    sprite_id=SPR0210_CHOMP_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x00, 0x00, 0x00]),
)

P043_UNUSED = Packet(
    packet_id=43,
    sprite_id=SPR0211_FAN_PACKET,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x00, 0x00, 0x00]),
)

P044_UNUSED = Packet(
    packet_id=44,
    sprite_id=SPR0212_RED_MUSHROOM_ITEM,
    shadow=False,
    action_script_id=A0929_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x00, 0x00, 0x00]),
)

P045_TELEPORTATION_SHINE = Packet(
    packet_id=45,
    sprite_id=SPR0213_AXEM_RED_TELEPORT,
    shadow=False,
    action_script_id=A0940_TELEPORTATION_SHINE,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x00, 0x00, 0x00]),
)

P046_UNUSED = Packet(
    packet_id=46,
    sprite_id=SPR0205_MICROBOMB_PACKET,
    shadow=False,
    action_script_id=A0939_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x01, 0x00, 0x01, 0x03, 0x00, 0x00, 0x00]),
)

P047_BLUE_FIRE_TRAIL = Packet(
    packet_id=47,
    sprite_id=SPR0201_MOKURA_S_CLOUD_BLUE,
    shadow=False,
    action_script_id=A0943_BLUE_FIRE_TRAIL,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x02, 0x04, 0x01, 0x00, 0x00]),
)

P048_UNUSED = Packet(
    packet_id=48,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    shadow=False,
    action_script_id=A0938_UNUSED,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P049_HAMMER_SPARKS_SFX = Packet(
    packet_id=49,
    sprite_id=SPR0198_SPARKLE_DOWNWARDS,
    shadow=False,
    action_script_id=A0952_HAMMER_SPARKS_SFX,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x03, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P050_WATER_BLAST_SFX = Packet(
    packet_id=50,
    sprite_id=SPR0242_WHITE_GAS_CLOUD,
    shadow=False,
    action_script_id=A0249_WATER_BLAST_SFX,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P051_DRILL_BIT = Packet(
    packet_id=51,
    sprite_id=SPR0243_MACHINE_MADE_DRILL_BIT,
    shadow=False,
    action_script_id=A0250_DRILL_BIT,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x07, 0x01, 0x04, 0x02, 0x00, 0x00]),
)

P052_BOMB_EXPLOSION_FASTER = Packet(
    packet_id=52,
    sprite_id=SPR0200_EXPLOSION,
    shadow=False,
    action_script_id=A0195_BOMB_EXPLOSION_FASTER,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x01, 0x03, 0x01, 0x00, 0x00]),
)

P053_UNUSED = Packet(
    packet_id=53,
    sprite_id=SPR0194_FROG_COIN,
    shadow=False,
    action_script_id=A0196_EMPTY,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x05, 0x03, 0x03, 0x01, 0x00, 0x00]),
)

P054_LEVELUP_BONUS_POW = Packet(
    packet_id=54,
    sprite_id=SPR0230_LEVEL_UP_BONUS_POW_POWER,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P055_LEVELUP_BONUS_S = Packet(
    packet_id=55,
    sprite_id=SPR0231_LEVEL_UP_BONUS_STAR_MAGIC,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P056_LEVELUP_BONUS_HP = Packet(
    packet_id=56,
    sprite_id=SPR0232_LEVEL_UP_BONUS_HP,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P057_UNUSED = Packet(
    packet_id=57,
    sprite_id=SPR0233_GREEN_BOMB,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P058_UNUSED = Packet(
    packet_id=58,
    sprite_id=SPR0234_YELLOW_BOMB,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P059_UNUSED = Packet(
    packet_id=59,
    sprite_id=SPR0235_BLUE_BOMB,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P060_UNUSED = Packet(
    packet_id=60,
    sprite_id=SPR0236_GREEN_JUICE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P061_UNUSED = Packet(
    packet_id=61,
    sprite_id=SPR0237_EGG,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P062_UNUSED = Packet(
    packet_id=62,
    sprite_id=SPR0238_RED_JUICE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P063_UNUSED = Packet(
    packet_id=63,
    sprite_id=SPR0239_BLUE_R_DRINK,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P064_COIN_SHOWER_E = Packet(
    packet_id=64,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0896_COIN_SHOWER_E,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P065_COIN_SHOWER_SE = Packet(
    packet_id=65,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0897_COIN_SHOWER_SE,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P066_COIN_SHOWER_S = Packet(
    packet_id=66,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0898_COIN_SHOWER_S,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P067_COIN_SHOWER_SW = Packet(
    packet_id=67,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0899_COIN_SHOWER_SW,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P068_COIN_SHOWER_W = Packet(
    packet_id=68,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0900_COIN_SHOWER_W,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P069_COIN_SHOWER_NW = Packet(
    packet_id=69,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0901_COIN_SHOWER_NW,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P070_COIN_SHOWER_N = Packet(
    packet_id=70,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0902_COIN_SHOWER_N,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P071_COIN_SHOWER_NE = Packet(
    packet_id=71,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0903_COIN_SHOWER_NE,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P072_COIN_SHOWER_E_DB = Packet(
    packet_id=72,
    sprite_id=SPR0192_COIN,
    shadow=False,
    action_script_id=A0905_COIN_SHOWER_E_DB,
    unknown_bits=[False, True, True],
    unknown_bytes=bytearray([0x00, 0x03, 0x01, 0x04, 0x01, 0x00, 0x00]),
)

P073_UNUSED = Packet(
    packet_id=73,
    sprite_id=SPR0249_RED_SHELL,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P074_UNUSED = Packet(
    packet_id=74,
    sprite_id=SPR0250_GREEN_SHELL,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P075_UNUSED = Packet(
    packet_id=75,
    sprite_id=SPR0251_PARASOL_PACKET,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P076_UNUSED = Packet(
    packet_id=76,
    sprite_id=SPR0252_FEATHER,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P077_UNUSED = Packet(
    packet_id=77,
    sprite_id=SPR0253_BERRY,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P078_UNUSED = Packet(
    packet_id=78,
    sprite_id=SPR0254_YOSHI_COOKIE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P079_UNUSED = Packet(
    packet_id=79,
    sprite_id=SPR0255_BEETLE,
    shadow=False,
    action_script_id=A0000_DO_NOTHING,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]),
)

P080_FEATHER_CHEST = None

P081_STAR_PIECE_CHEST = None

P082_FEATHER_FALL = None

P083_STAR_PIECE_FALL = None

P084_FEATHER_STATIC = None

P085_STAR_PIECE_STATIC = None

P086_FLOWER_STATIC = None

P087_MUSHROOM_STATIC = None

P088_KEY_STATIC = None

P089_KEY_FALLING = None

P090_BAG_STATIC = None

P091_RING_CHEST = None

P092_RING_FALL = None

P093_RING_STATIC = None

P094_BROOCH_STATIC = None

P095_BROOCH_FALL = None

P096_BROOCH_CHEST = None

P097_SHOES_STATIC = None

P098_SHOES_FALL = None

P099_SHOES_CHEST = None

P100_BANANA_STATIC = None

P101_BANANA_FALL = None

P102_BANANA_CHEST = None

P103_CROWN_CHEST = None

P104_CROWN_FALL = None

P105_CROWN_STATIC = None

P106_COIN_FALL = None

P107_SMALL_COIN_FALL = None

P108_FROG_COIN_FALL = None

P109_COIN_STATIC = None

P110_SMALL_COIN_STATIC = None

P111_FROG_COIN_STATIC = None

P112_BOMB_STATIC = None

P113_BOMB_FALL = None

P114_BOMB_CHEST = None

P115_EGG_STATIC = None

P116_EGG_FALLING = None

P117_EGG_CHEST = None

P118_COOKIE_STATIC = None

P119_COOKIE_FALL = None

P120_COOKIE_CHEST = None

P121_BERRY_STATIC = None

P122_BERRY_FALL = None

P123_BERRY_CHEST = None

P124_CARD_STATIC = None

P125_CARD_FALL = None

P126_CARD_CHEST = None

P127_GREEN_SYRUP_STATIC = None

P128_GREEN_SYRUP_FALL = None

P129_GREEN_SYRUP_CHEST = None

P130_RED_SYRUP_STATIC = None

P131_RED_SYRUP_FALL = None

P132_RED_SYRUP_CHEST = None

P133_BLUE_SYRUP_STATIC = None

P134_BLUE_SYRUP_FALL = None

P135_BLUE_SYRUP_CHEST = None

P136_YELLOW_SYRUP_STATIC = None

P137_YELLOW_SYRUP_FALL = None

P138_YELLOW_SYRUP_CHEST = None

P139_GREEN_JUICE_STATIC = None

P140_GREEN_JUICE_FALL = None

P141_GREEN_JUICE_CHEST = None

P142_RED_JUICE_STATIC = None

P143_RED_JUICE_FALL = None

P144_RED_JUICE_CHEST = None

P145_P_DRINK_STATIC = None

P146_P_DRINK_FALL = None

P147_P_DRINK_CHEST = None

P148_D_DRINK_CHEST = None

P149_D_DRINK_FALL = None

P150_D_DRINK_STATIC = None

P151_YELLOW_MUSIC_DRINK_CHEST = None

P152_YELLOW_MUSIC_DRINK_FALL = None

P153_YELLOW_MUSIC_DRINK_STATIC = None

P154_BLUE_MUSIC_DRINK_CHEST = None

P155_BLUE_MUSIC_DRINK_FALL = None

P156_BLUE_MUSIC_DRINK_STATIC = None

P157_FROG_DRINK_CHEST = None

P158_FROG_DRINK_FALL = None

P159_FROG_DRINK_STATIC = None

P160_RED_MUSIC_DRINK_CHEST = None

P161_RED_MUSIC_DRINK_FALL = None

P162_RED_MUSIC_DRINK_STATIC = None

P163_R_DRINK_STATIC = None

P164_R_DRINK_FALL = None

P165_R_DRINK_CHEST = None

P166_MUSIC_NOTE_STATIC = None

P167_MUSIC_NOTE_FALL = None

P168_MUSIC_NOTE_CHEST = None

P169_STAR_DRINK_STATIC = None

P170_STAR_DRINK_FALL = None

P171_STAR_DRINK_CHEST = None

P172_UNUSED = None

P173_GREEN_CANDY_STATIC = None

P174_GREEN_CANDY_FALL = None

P175_GREEN_CANDY_CHEST = None

P176_BLUE_CANDY_STATIC = None

P177_BLUE_CANDY_FALL = None

P178_BLUE_CANDY_CHEST = None

P179_GREEN_BOMB_STATIC = None

P180_GREEN_BOMB_FALL = None

P181_GREEN_BOMB_CHEST = None

P182_RED_BOMB_STATIC = None

P183_RED_BOMB_FALL = None

P184_RED_BOMB_CHEST = None

P185_BLUE_BOMB_STATIC = None

P186_BLUE_BOMB_FALL = None

P187_BLUE_BOMB_CHEST = None

P188_YELLOW_BOMB_STATIC = None

P189_YELLOW_BOMB_FALL = None

P190_YELLOW_BOMB_CHEST = None

P191_BEETLE_STATIC = None

P192_BEETLE_FALL = None

P193_BEETLE_CHEST = None

P194_RED_MUSHROOM_STATIC = None

P195_RED_MUSHROOM_FALL = None

P196_RED_MUSHROOM_CHEST = None

P197_GREEN_MUSHROOM_STATIC = None

P198_GREEN_MUSHROOM_FALL = None

P199_GREEN_MUSHROOM_CHEST = None

P200_YELLOW_MUSHROOM_STATIC = None

P201_YELLOW_MUSHROOM_FALL = None

P202_YELLOW_MUSHROOM_CHEST = None

P203_FRYING_PAN_STATIC = None

P204_FRYING_PAN_FALL = None

P205_FRYING_PAN_CHEST = None

P206_HAMMER_STATIC = None

P207_HAMMER_FALL = None

P208_HAMMER_CHEST = None

P209_STICK_STATIC = None

P210_STICK_FALL = None

P211_STICK_CHEST = None

P212_CHOMP_STATIC = None

P213_CHOMP_FALL = None

P214_CHOMP_CHEST = None

P215_FAN_STATIC = None

P216_FAN_FALL = None

P217_FAN_CHEST = None

P218_RED_SHELL_STATIC = None

P219_RED_SHELL_FALL = None

P220_RED_SHELL_CHEST = None

P221_GREEN_SHELL_STATIC = None

P222_GREEN_SHELL_FALL = None

P223_GREEN_SHELL_CHEST = None

P224_PARASOL_STATIC = None

P225_PARASOL_FALL = None

P226_PARASOL_CHEST = None

P227_UNUSED = None

P228_UNUSED = None

P229_UNUSED = None

P230_UNUSED = None

P231_UNUSED = None

P232_UNUSED = None

P233_UNUSED = None

P234_UNUSED = None

P235_UNUSED = None

P236_UNUSED = None

P237_UNUSED = None

P238_UNUSED = None

P239_UNUSED = None

P240_UNUSED = None

P241_UNUSED = None

P242_UNUSED = None

P243_UNUSED = None

P244_UNUSED = None

P245_UNUSED = None

P246_UNUSED = None

P247_UNUSED = None

P248_UNUSED = None

P249_UNUSED = None

P250_UNUSED = None

P251_UNUSED = None

P252_UNUSED = None

P253_UNUSED = None

P254_UNUSED = None

P255_UNUSED = None

# Packet Collection
ALL_PACKETS = PacketCollection([
    P000_FLASHING_POOF_FLOWER,
    P001_FLASHING_POOF_MUSHROOM,
    P002_BRIEF_KEY,
    P003_BRIEF_STAR,
    P004_MIMIC_POOF_ON_DEFEAT,
    P005_BRIEF_POOF_BAG,
    P006_STATIC_SIDEWAYS_SPARKLE,
    P007_STATIC_SIDEWAYS_SPARKLE,
    P008_STATIC_EXPLOSION,
    P009_STATIC_BLUE_CLOUD,
    P010_STATIC_SMALL_FROG_COIN,
    P011_STATIC_LEVELUP_TEXT,
    P012_STATIC_GREY_EXPLOSION,
    P013_STATIC_MICROBOMB,
    P014_UNUSED,
    P015_UNUSED,
    P016_BIG_COIN_BEING_COLLECTED,
    P017_SMALL_MINIGAME_COIN,
    P018_SMALL_COIN_BEING_COLLECTED,
    P019_FROG_COIN_BEING_COLLECTED,
    P020_WATER_DROPLETS_USE_7016_701A,
    P021_FLASHING_SMALL_EXPLOSION,
    P022_RECURSIVE_SPARKLES,
    P023_LOOPING_SINGLE_SPARKLE,
    P024_REGULAR_SOUND_EXPLOSION,
    P025_UNUSED,
    P026_UNUSED,
    P027_UNUSED,
    P028_MUSHROOM_THROWN_SOUTHWEST,
    P029_SPARKLE_LINE_LOOPED,
    P030_WATER_SPLASH_DROPS_SFX,
    P031_LEVELUP_TEXT,
    P032_BLUE_CLOUD,
    P033_BOMB_EXPLOSION,
    P034_GREY_EXPLOSION_SFX,
    P035_FLOWER_FALL,
    P036_MUSHROOM_FALL,
    P037_ITEM_BAG_FALL,
    P038_MUSHROOM_FALL_DEFAULT_PRIORITY,
    P039_UNUSED,
    P040_UNUSED,
    P041_UNUSED,
    P042_UNUSED,
    P043_UNUSED,
    P044_UNUSED,
    P045_TELEPORTATION_SHINE,
    P046_UNUSED,
    P047_BLUE_FIRE_TRAIL,
    P048_UNUSED,
    P049_HAMMER_SPARKS_SFX,
    P050_WATER_BLAST_SFX,
    P051_DRILL_BIT,
    P052_BOMB_EXPLOSION_FASTER,
    P053_UNUSED,
    P054_LEVELUP_BONUS_POW,
    P055_LEVELUP_BONUS_S,
    P056_LEVELUP_BONUS_HP,
    P057_UNUSED,
    P058_UNUSED,
    P059_UNUSED,
    P060_UNUSED,
    P061_UNUSED,
    P062_UNUSED,
    P063_UNUSED,
    P064_COIN_SHOWER_E,
    P065_COIN_SHOWER_SE,
    P066_COIN_SHOWER_S,
    P067_COIN_SHOWER_SW,
    P068_COIN_SHOWER_W,
    P069_COIN_SHOWER_NW,
    P070_COIN_SHOWER_N,
    P071_COIN_SHOWER_NE,
    P072_COIN_SHOWER_E_DB,
    P073_UNUSED,
    P074_UNUSED,
    P075_UNUSED,
    P076_UNUSED,
    P077_UNUSED,
    P078_UNUSED,
    P079_UNUSED,
    P080_FEATHER_CHEST,
    P081_STAR_PIECE_CHEST,
    P082_FEATHER_FALL,
    P083_STAR_PIECE_FALL,
    P084_FEATHER_STATIC,
    P085_STAR_PIECE_STATIC,
    P086_FLOWER_STATIC,
    P087_MUSHROOM_STATIC,
    P088_KEY_STATIC,
    P089_KEY_FALLING,
    P090_BAG_STATIC,
    P091_RING_CHEST,
    P092_RING_FALL,
    P093_RING_STATIC,
    P094_BROOCH_STATIC,
    P095_BROOCH_FALL,
    P096_BROOCH_CHEST,
    P097_SHOES_STATIC,
    P098_SHOES_FALL,
    P099_SHOES_CHEST,
    P100_BANANA_STATIC,
    P101_BANANA_FALL,
    P102_BANANA_CHEST,
    P103_CROWN_CHEST,
    P104_CROWN_FALL,
    P105_CROWN_STATIC,
    P106_COIN_FALL,
    P107_SMALL_COIN_FALL,
    P108_FROG_COIN_FALL,
    P109_COIN_STATIC,
    P110_SMALL_COIN_STATIC,
    P111_FROG_COIN_STATIC,
    P112_BOMB_STATIC,
    P113_BOMB_FALL,
    P114_BOMB_CHEST,
    P115_EGG_STATIC,
    P116_EGG_FALLING,
    P117_EGG_CHEST,
    P118_COOKIE_STATIC,
    P119_COOKIE_FALL,
    P120_COOKIE_CHEST,
    P121_BERRY_STATIC,
    P122_BERRY_FALL,
    P123_BERRY_CHEST,
    P124_CARD_STATIC,
    P125_CARD_FALL,
    P126_CARD_CHEST,
    P127_GREEN_SYRUP_STATIC,
    P128_GREEN_SYRUP_FALL,
    P129_GREEN_SYRUP_CHEST,
    P130_RED_SYRUP_STATIC,
    P131_RED_SYRUP_FALL,
    P132_RED_SYRUP_CHEST,
    P133_BLUE_SYRUP_STATIC,
    P134_BLUE_SYRUP_FALL,
    P135_BLUE_SYRUP_CHEST,
    P136_YELLOW_SYRUP_STATIC,
    P137_YELLOW_SYRUP_FALL,
    P138_YELLOW_SYRUP_CHEST,
    P139_GREEN_JUICE_STATIC,
    P140_GREEN_JUICE_FALL,
    P141_GREEN_JUICE_CHEST,
    P142_RED_JUICE_STATIC,
    P143_RED_JUICE_FALL,
    P144_RED_JUICE_CHEST,
    P145_P_DRINK_STATIC,
    P146_P_DRINK_FALL,
    P147_P_DRINK_CHEST,
    P148_D_DRINK_CHEST,
    P149_D_DRINK_FALL,
    P150_D_DRINK_STATIC,
    P151_YELLOW_MUSIC_DRINK_CHEST,
    P152_YELLOW_MUSIC_DRINK_FALL,
    P153_YELLOW_MUSIC_DRINK_STATIC,
    P154_BLUE_MUSIC_DRINK_CHEST,
    P155_BLUE_MUSIC_DRINK_FALL,
    P156_BLUE_MUSIC_DRINK_STATIC,
    P157_FROG_DRINK_CHEST,
    P158_FROG_DRINK_FALL,
    P159_FROG_DRINK_STATIC,
    P160_RED_MUSIC_DRINK_CHEST,
    P161_RED_MUSIC_DRINK_FALL,
    P162_RED_MUSIC_DRINK_STATIC,
    P163_R_DRINK_STATIC,
    P164_R_DRINK_FALL,
    P165_R_DRINK_CHEST,
    P166_MUSIC_NOTE_STATIC,
    P167_MUSIC_NOTE_FALL,
    P168_MUSIC_NOTE_CHEST,
    P169_STAR_DRINK_STATIC,
    P170_STAR_DRINK_FALL,
    P171_STAR_DRINK_CHEST,
    P172_UNUSED,
    P173_GREEN_CANDY_STATIC,
    P174_GREEN_CANDY_FALL,
    P175_GREEN_CANDY_CHEST,
    P176_BLUE_CANDY_STATIC,
    P177_BLUE_CANDY_FALL,
    P178_BLUE_CANDY_CHEST,
    P179_GREEN_BOMB_STATIC,
    P180_GREEN_BOMB_FALL,
    P181_GREEN_BOMB_CHEST,
    P182_RED_BOMB_STATIC,
    P183_RED_BOMB_FALL,
    P184_RED_BOMB_CHEST,
    P185_BLUE_BOMB_STATIC,
    P186_BLUE_BOMB_FALL,
    P187_BLUE_BOMB_CHEST,
    P188_YELLOW_BOMB_STATIC,
    P189_YELLOW_BOMB_FALL,
    P190_YELLOW_BOMB_CHEST,
    P191_BEETLE_STATIC,
    P192_BEETLE_FALL,
    P193_BEETLE_CHEST,
    P194_RED_MUSHROOM_STATIC,
    P195_RED_MUSHROOM_FALL,
    P196_RED_MUSHROOM_CHEST,
    P197_GREEN_MUSHROOM_STATIC,
    P198_GREEN_MUSHROOM_FALL,
    P199_GREEN_MUSHROOM_CHEST,
    P200_YELLOW_MUSHROOM_STATIC,
    P201_YELLOW_MUSHROOM_FALL,
    P202_YELLOW_MUSHROOM_CHEST,
    P203_FRYING_PAN_STATIC,
    P204_FRYING_PAN_FALL,
    P205_FRYING_PAN_CHEST,
    P206_HAMMER_STATIC,
    P207_HAMMER_FALL,
    P208_HAMMER_CHEST,
    P209_STICK_STATIC,
    P210_STICK_FALL,
    P211_STICK_CHEST,
    P212_CHOMP_STATIC,
    P213_CHOMP_FALL,
    P214_CHOMP_CHEST,
    P215_FAN_STATIC,
    P216_FAN_FALL,
    P217_FAN_CHEST,
    P218_RED_SHELL_STATIC,
    P219_RED_SHELL_FALL,
    P220_RED_SHELL_CHEST,
    P221_GREEN_SHELL_STATIC,
    P222_GREEN_SHELL_FALL,
    P223_GREEN_SHELL_CHEST,
    P224_PARASOL_STATIC,
    P225_PARASOL_FALL,
    P226_PARASOL_CHEST,
    P227_UNUSED,
    P228_UNUSED,
    P229_UNUSED,
    P230_UNUSED,
    P231_UNUSED,
    P232_UNUSED,
    P233_UNUSED,
    P234_UNUSED,
    P235_UNUSED,
    P236_UNUSED,
    P237_UNUSED,
    P238_UNUSED,
    P239_UNUSED,
    P240_UNUSED,
    P241_UNUSED,
    P242_UNUSED,
    P243_UNUSED,
    P244_UNUSED,
    P245_UNUSED,
    P246_UNUSED,
    P247_UNUSED,
    P248_UNUSED,
    P249_UNUSED,
    P250_UNUSED,
    P251_UNUSED,
    P252_UNUSED,
    P253_UNUSED,
    P254_UNUSED,
    P255_UNUSED,
])
