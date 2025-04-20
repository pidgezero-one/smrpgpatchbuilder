"""Static values for item properties"""

import enum


""" class EffectTypeOld(enum.Enum):
    # Enumeration to describe the type of effect an item will have on its target.

    NORMAL = enum.auto()
    ELEMENTAL_IMMUNITY = enum.auto()
    ELEMENTAL_RESISTANCE = enum.auto()
    STATUS_PROTECTION = enum.auto()
    FEW_EFFECTS = enum.auto()
    BUFFS = enum.auto()
 """

class EquipStats(str, enum.Enum):
    """Enumeration for numerical stats that are directly affected by equips."""

    SPEED = "speed"
    ATTACK = "attack"
    DEFENSE = "defense"
    MAGIC_ATTACK = "magic_attack"
    MAGIC_DEFENSE = "magic_defense"


class ItemTypeValue(enum.IntEnum):
    """Enumeration for distinct base classifications for items."""

    WEAPON = 0b00
    ARMOR = 0b01
    ACCESSORY = 0b10
    ITEM = 0b11

class EffectType(enum.Enum):
    INFLICTION = enum.auto()
    PROTECTION = enum.auto()
    NULLIFICATION = enum.auto()

class InflictFunction(enum.Enum):
    ITEM_MORPH = enum.auto()
    REVIVE = enum.auto()
    RESTORE_FP = enum.auto()
    INCREASE_STATS_ITEM = enum.auto()
    RESTORE_HP = enum.auto()
    RESTORE_ALL_HP_FP = enum.auto()
    RAISE_MAX_FP = enum.auto()
    INSTANT_DEATH = enum.auto()

class OverworldMenuBehaviour(enum.Enum):
    LEAD_TO_HP = enum.auto()
    LEAD_TO_FP = enum.auto()