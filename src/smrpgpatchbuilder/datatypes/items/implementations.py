# pylint: disable=C0301

"""Individual item class definitions."""

from typing import List

from .classes import (
    RegularItem,
    Weapon,
    Armor,
    Accessory,
)
from .enums import (
    EffectType, 
    InflictFunction, 
    OverworldMenuBehaviour
)
from smrpgpatchbuilder.datatypes.numbers.classes import UInt16, UInt8
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import PartyCharacter
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MARIO,
    MALLOW,
    GENO,
    TOADSTOOL,
    BOWSER,
)
from smrpgpatchbuilder.datatypes.spells.classes import Element, Status, TempStatBuff


class DummyWeapon(Weapon):
    """Placeholder slot 0 item class"""
    _item_name: str = "Weapon"

    _item_id: int = 0
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [MARIO]
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(8)
    _perfect_window_ends = UInt8(14)
    _half_time_window_ends = UInt8(22)


class DummyArmor(Weapon):
    """Placeholder slot 1 item class"""
    _item_name: str = "Armor"

    _item_id: int = 1
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(36)


class DummyAccessory(Weapon):
    """Placeholder slot 2 item class"""
    _item_name: str = "Accessory"

    _item_id: int = 2
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(16)
    _perfect_window_ends = UInt8(24)
    _half_time_window_ends = UInt8(36)


class Empty3(Weapon):
    """Placeholder slot 3 item class"""
    _item_name: str = "Space"

    _item_id: int = 3
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [GENO]
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(56)


class Empty4(Weapon):
    """Placeholder slot 3 item class"""
    _item_name: str = "Space"

    _item_id: int = 4
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(22)


class Hammer(Weapon):
    """Hammer item class"""
    _item_name: str = "Hammer"

    _item_id: int = 5
    _description: str = "Pounds\x01enemies"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 10
    _variance: int = 1
    _price: int = 70
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(14)
    _perfect_window_ends = UInt8(20)
    _half_time_window_ends = UInt8(38)


class FroggieStick(Weapon):
    """FroggieStick item class"""
    _item_name: str = "FroggieStick"

    _item_id: int = 6
    _description: str = "Frogfucius\x01made it"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 20
    _variance: int = 2
    _price: int = 180
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(18)
    _perfect_window_ends = UInt8(24)
    _half_time_window_ends = UInt8(36)


class NokNokShell(Weapon):
    """NokNokShell item class"""
    _item_name: str = "NokNok Shell"

    _item_id: int = 7
    _description: str = "Kick to attack"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 20
    _variance: int = 2
    _price: int = 20
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)


class PunchGlove(Weapon):
    """PunchGlove item class"""
    _item_name: str = "Punch Glove"

    _item_id: int = 8
    _description: str = "Knock out\x01power!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 30
    _variance: int = 3
    _price: int = 36
    _half_time_window_begins = UInt8(4)
    _perfect_window_begins = UInt8(8)
    _perfect_window_ends = UInt8(14)
    _half_time_window_ends = UInt8(22)


class FingerShot(Weapon):
    """FingerShot item class"""
    _item_name: str = "Finger Shot"

    _item_id: int = 9
    _description: str = "Fingers shoot\x01bullets"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 12
    _variance: int = 3
    _price: int = 50
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(16)
    _perfect_window_ends = UInt8(22)
    _half_time_window_ends = UInt8(26)


class Cymbals(Weapon):
    """Cymbals item class"""
    _item_name: str = "Cymbals"

    _item_id: int = 10
    _description: str = "Scare enemies\x01with a clash"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 30
    _variance: int = 3
    _price: int = 42
    _half_time_window_begins = UInt8(4)
    _perfect_window_begins = UInt8(5)
    _perfect_window_ends = UInt8(11)
    _half_time_window_ends = UInt8(30)


class Chomp(Weapon):
    """Chomp item class"""
    _item_name: str = "Chomp"

    _item_id: int = 11
    _description: str = "Just spin me\x01at an enemy!"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 10
    _variance: int = 4
    _price: int = 140
    _half_time_window_begins = UInt8(40)
    _perfect_window_begins = UInt8(50)
    _perfect_window_ends = UInt8(56)
    _half_time_window_ends = UInt8(60)


class Masher(Weapon):
    """Masher item class"""
    _item_name: str = "Masher"

    _item_id: int = 12
    _description: str = "Makes monster\x01mash!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 30
    _price: int = 160
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(14)
    _perfect_window_ends = UInt8(20)
    _half_time_window_ends = UInt8(38)


class ChompShell(Weapon):
    """ChompShell item class"""
    _item_name: str = "Chomp Shell"

    _item_id: int = 13
    _description: str = "It~s a\x01Kinklink shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 9
    _variance: int = 3
    _price: int = 60
    _half_time_window_begins = UInt8(40)
    _perfect_window_begins = UInt8(50)
    _perfect_window_ends = UInt8(56)
    _half_time_window_ends = UInt8(60)


class SuperHammer(Weapon):
    """SuperHammer item class"""
    _item_name: str = "Super Hammer"

    _item_id: int = 14
    _description: str = "The standard\x01for hammers!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 40
    _variance: int = 4
    _price: int = 70
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(40)
    _perfect_window_ends = UInt8(46)
    _half_time_window_ends = UInt8(50)


class HandGun(Weapon):
    """HandGun item class"""
    _item_name: str = "Hand Gun"

    _item_id: int = 15
    _description: str = "It packs a kick"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 24
    _variance: int = 4
    _price: int = 75
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(34)


class WhompGlove(Weapon):
    """WhompGlove item class"""
    _item_name: str = "Whomp Glove"

    _item_id: int = 16
    _description: str = "The old double\x01whammie!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 40
    _variance: int = 4
    _price: int = 72
    _half_time_window_begins = UInt8(2)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(22)


class SlapGlove(Weapon):
    """SlapGlove item class"""
    _item_name: str = "Slap Glove"

    _item_id: int = 17
    _description: str = "It slaps ~em\x01silly"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 40
    _variance: int = 4
    _price: int = 100
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(36)


class TroopaShell(Weapon):
    """TroopaShell item class"""
    _item_name: str = "Troopa Shell"

    _item_id: int = 18
    _description: str = "Kick with it!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 5
    _price: int = 90
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)


class Parasol(Weapon):
    """Parasol item class"""
    _item_name: str = "Parasol"

    _item_id: int = 19
    _description: str = "Inflicts\x01serious pain!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 50
    _variance: int = 5
    _price: int = 84
    _half_time_window_begins = UInt8(5)
    _perfect_window_begins = UInt8(8)
    _perfect_window_ends = UInt8(14)
    _half_time_window_ends = UInt8(24)


class HurlyGloves(Weapon):
    """HurlyGloves item class"""
    _item_name: str = "Hurly Gloves"

    _item_id: int = 20
    _description: str = "A classic\x01Mario}toss\x01attack"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 20
    _variance: int = 5
    _price: int = 92
    _half_time_window_begins = UInt8(12)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(36)


class DoublePunch(Weapon):
    """DoublePunch item class"""
    _item_name: str = "Double Punch"

    _item_id: int = 21
    _description: str = "A handy double\x01rocket punch"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 35
    _variance: int = 5
    _price: int = 88
    _half_time_window_begins = UInt8(6)
    _perfect_window_begins = UInt8(26)
    _perfect_window_ends = UInt8(32)
    _half_time_window_ends = UInt8(36)


class RibbitStick(Weapon):
    """RibbitStick item class"""
    _item_name: str = "Ribbit Stick"

    _item_id: int = 22
    _description: str = "It~ll come\x01in handy"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 50
    _variance: int = 5
    _price: int = 86
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(18)
    _perfect_window_ends = UInt8(24)
    _half_time_window_ends = UInt8(36)


class SpikedLink(Weapon):
    """SpikedLink item class"""
    _item_name: str = "Spiked Link"

    _item_id: int = 23
    _description: str = "A studded ball\x01and chain!"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 30
    _variance: int = 6
    _price: int = 94
    _half_time_window_begins = UInt8(40)
    _perfect_window_begins = UInt8(50)
    _perfect_window_ends = UInt8(56)
    _half_time_window_ends = UInt8(60)


class MegaGlove(Weapon):
    """MegaGlove item class"""
    _item_name: str = "Mega Glove"

    _item_id: int = 24
    _description: str = "Packs a mega\x01wallop!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 60
    _variance: int = 6
    _price: int = 102
    _half_time_window_begins = UInt8(6)
    _perfect_window_begins = UInt8(12)
    _perfect_window_ends = UInt8(18)
    _half_time_window_ends = UInt8(26)


class WarFan(Weapon):
    """WarFan item class"""
    _item_name: str = "War Fan"

    _item_id: int = 25
    _description: str = "A mysterious\x01battle fan!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 60
    _variance: int = 6
    _price: int = 100
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(2)
    _perfect_window_ends = UInt8(8)
    _half_time_window_ends = UInt8(22)


class HandCannon(Weapon):
    """HandCannon item class"""
    _item_name: str = "Hand Cannon"

    _item_id: int = 26
    _description: str = "Shoots bullets\x01from elbow!"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 45
    _variance: int = 6
    _price: int = 105
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(46)
    _perfect_window_ends = UInt8(52)
    _half_time_window_ends = UInt8(64)


class StickyGlove(Weapon):
    """StickyGlove item class"""
    _item_name: str = "Sticky Glove"

    _item_id: int = 27
    _description: str = "Launches a\x01punch attack."
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 60
    _variance: int = 6
    _price: int = 98
    _half_time_window_begins = UInt8(5)
    _perfect_window_begins = UInt8(12)
    _perfect_window_ends = UInt8(18)
    _half_time_window_ends = UInt8(26)


class UltraHammer(Weapon):
    """UltraHammer item class"""
    _item_name: str = "Ultra Hammer"

    _item_id: int = 28
    _description: str = "The ultimate\x01hammer!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 70
    _variance: int = 7
    _price: int = 115
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(14)
    _perfect_window_ends = UInt8(20)
    _half_time_window_ends = UInt8(38)


class SuperSlap(Weapon):
    """SuperSlap item class"""
    _item_name: str = "Super Slap"

    _item_id: int = 29
    _description: str = "The Princess~\x01mega}slap!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 70
    _variance: int = 7
    _price: int = 110
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(10)
    _perfect_window_ends = UInt8(16)
    _half_time_window_ends = UInt8(36)


class DrillClaw(Weapon):
    """DrillClaw item class"""
    _item_name: str = "Drill Claw"

    _item_id: int = 30
    _description: str = "A drilling\x01claw!"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 40
    _variance: int = 7
    _price: int = 118
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(16)
    _perfect_window_ends = UInt8(24)
    _half_time_window_ends = UInt8(36)


class StarGun(Weapon):
    """StarGun item class"""
    _item_name: str = "Star Gun"

    _item_id: int = 31
    _description: str = "Try shooting\x01stars!"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 57
    _variance: int = 7
    _price: int = 120
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(24)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(34)


class SonicCymbal(Weapon):
    """SonicCymbal item class"""
    _item_name: str = "Sonic Cymbal"

    _item_id: int = 32
    _description: str = "Puts noise to\x01work for you!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 70
    _variance: int = 7
    _price: int = 108
    _half_time_window_begins = UInt8(4)
    _perfect_window_begins = UInt8(5)
    _perfect_window_ends = UInt8(11)
    _half_time_window_ends = UInt8(30)


class LazyShellWeapon(Weapon):
    """LazyShellWeapon item class"""
    _item_name: str = "Lazy Shell"

    _item_id: int = 33
    _description: str = "Toss a shell\x01at an enemy!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 90
    _variance: int = 40
    _price: int = 200
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)


class FryingPan(Weapon):
    """FryingPan item class"""
    _item_name: str = "Frying Pan"

    _item_id: int = 34
    _description: str = "Enough iron to\x01be dangerous!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 90
    _variance: int = 20
    _price: int = 300
    _half_time_window_begins = UInt8(0)
    _perfect_window_begins = UInt8(4)
    _perfect_window_ends = UInt8(10)
    _half_time_window_ends = UInt8(24)


class LuckyHammer(Weapon):
    """LuckyHammer item class"""
    _item_name: str = "Hammer"

    _item_id: int = 35
    _description: str = "A lucky hammer!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 123
    _half_time_window_begins = UInt8(8)
    _perfect_window_begins = UInt8(14)
    _perfect_window_ends = UInt8(20)
    _half_time_window_ends = UInt8(38)


class Spare36(Weapon):
    """Placeholder slot 36 item class"""
    _item_name: str = "Spare"

    _item_id: int = 36
    _description: str = ""
    _equip_chars: List[PartyCharacter] = []
    _price: int = 100
    _half_time_window_begins = UInt8(10)
    _perfect_window_begins = UInt8(20)
    _perfect_window_ends = UInt8(30)
    _half_time_window_ends = UInt8(40)


class Shirt(Armor):
    """Shirt item class"""
    _item_name: str = "Shirt"

    _item_id: int = 37
    _description: str = "It~s a\x01shirt!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 6
    _magic_defense: int = 6
    _price: int = 7


class Pants(Armor):
    """Pants item class"""
    _item_name: str = "Pants"

    _item_id: int = 38
    _description: str = "It~s a pair\x01of pants!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 7


class ThickShirt(Armor):
    """ThickShirt item class"""
    _item_name: str = "Thick Shirt"

    _item_id: int = 39
    _description: str = "A padded shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 12
    _magic_defense: int = 8
    _price: int = 14


class ThickPants(Armor):
    """ThickPants item class"""
    _item_name: str = "Thick Pants"

    _item_id: int = 40
    _description: str = "Padded pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 14


class MegaShirt(Armor):
    """MegaShirt item class"""
    _item_name: str = "Mega Shirt"

    _item_id: int = 41
    _description: str = "Durable stay}\x01pressed shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 18
    _magic_defense: int = 10
    _price: int = 22


class MegaPants(Armor):
    """MegaPants item class"""
    _item_name: str = "Mega Pants"

    _item_id: int = 42
    _description: str = "Durable work\x01pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 22


class WorkPants(Armor):
    """WorkPants item class"""
    _item_name: str = "Work Pants"

    _item_id: int = 43
    _description: str = "Sweaty\x01work pants!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 5
    _attack: int = 10
    _defense: int = 15
    _magic_attack: int = 10
    _magic_defense: int = 5
    _price: int = 22


class MegaCape(Armor):
    """MegaCape item class"""
    _item_name: str = "Mega Cape"

    _item_id: int = 44
    _description: str = "Durable\x01pressed cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 22


class HappyShirt(Armor):
    """HappyShirt item class"""
    _item_name: str = "Happy Shirt"

    _item_id: int = 45
    _description: str = "A lucky shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyPants(Armor):
    """HappyPants item class"""
    _item_name: str = "Happy Pants"

    _item_id: int = 46
    _description: str = "A lucky\x01pair of pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyCape(Armor):
    """HappyCape item class"""
    _item_name: str = "Happy Cape"

    _item_id: int = 47
    _description: str = "A lucky cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 38


class HappyShell(Armor):
    """HappyShell item class"""
    _item_name: str = "Happy Shell"

    _item_id: int = 48
    _description: str = "A lucky shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 38


class PolkaDress(Armor):
    """PolkaDress item class"""
    _item_name: str = "Polka Dress"

    _item_id: int = 49
    _description: str = "A flashy dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 160


class SailorShirt(Armor):
    """SailorShirt item class"""
    _item_name: str = "Sailor Shirt"

    _item_id: int = 50
    _description: str = "A sailor~s\x01suit"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorPants(Armor):
    """SailorPants item class"""
    _item_name: str = "Sailor Pants"

    _item_id: int = 51
    _description: str = "A sailor~s\x01pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorCape(Armor):
    """SailorCape item class"""
    _item_name: str = "Sailor Cape"

    _item_id: int = 52
    _description: str = "A sailor~s\x01cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 50


class NauticaDress(Armor):
    """NauticaDress item class"""
    _item_name: str = "NauticaDress"

    _item_id: int = 53
    _description: str = "A female\x01sailor~s dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class CourageShell(Armor):
    """CourageShell item class"""
    _item_name: str = "Courage Shell"

    _item_id: int = 54
    _description: str = "A stout shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 60


class FuzzyShirt(Armor):
    """FuzzyShirt item class"""
    _item_name: str = "Fuzzy Shirt"

    _item_id: int = 55
    _description: str = "A fuzzy shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyPants(Armor):
    """FuzzyPants item class"""
    _item_name: str = "Fuzzy Pants"

    _item_id: int = 56
    _description: str = "Fuzzy pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyCape(Armor):
    """FuzzyCape item class"""
    _item_name: str = "Fuzzy Cape"

    _item_id: int = 57
    _description: str = "A fuzzy cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 70


class FuzzyDress(Armor):
    """FuzzyDress item class"""
    _item_name: str = "Fuzzy Dress"

    _item_id: int = 58
    _description: str = "A fuzzy dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FireShirt(Armor):
    """FireShirt item class"""
    _item_name: str = "Fire Shirt"

    _item_id: int = 59
    _description: str = "Determined\x01person~s shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class FirePants(Armor):
    """FirePants item class"""
    _item_name: str = "Fire Pants"

    _item_id: int = 60
    _description: str = "Determined\x01person~s pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _elemental_immunities: List[Element] = []


class FireCape(Armor):
    """FireCape item class"""
    _item_name: str = "Fire Cape"

    _item_id: int = 61
    _description: str = "Determined\x01person~s cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 90


class FireShell(Armor):
    """FireShell item class"""
    _item_name: str = "Fire Shell"

    _item_id: int = 62
    _description: str = "Determined\x01person~s shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 90


class FireDress(Armor):
    """FireDress item class"""
    _item_name: str = "Fire Dress"

    _item_id: int = 63
    _description: str = "Determined\x01woman~s dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class HeroShirt(Armor):
    """HeroShirt item class"""
    _item_name: str = "Hero Shirt"

    _item_id: int = 64
    _description: str = "A legendary\x01shirt."
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class PrincePants(Armor):
    """PrincePants item class"""
    _item_name: str = "Prince Pants"

    _item_id: int = 65
    _description: str = "Legendary\x01pants!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class StarCape(Armor):
    """StarCape item class"""
    _item_name: str = "Star Cape"

    _item_id: int = 66
    _description: str = "A legendary\x01cape."
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 100


class HealShell(Armor):
    """HealShell item class"""
    _item_name: str = "Heal Shell"

    _item_id: int = 67
    _description: str = "A legendary\x01shell."
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 100


class RoyalDress(Armor):
    """RoyalDress item class"""
    _item_name: str = "Royal Syrup"

    _item_id: int = 68
    _description: str = "A legendary\x01dress!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class SuperSuit(Armor):
    """SuperSuit item class"""
    _item_name: str = "Super Suit"

    _item_id: int = 69
    _description: str = "A truly fine\x01suit!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 30
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 50
    _magic_defense: int = 50
    _elemental_immunities: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 700
    _effect_type: EffectType = EffectType.PROTECTION


class LazyShellArmor(Armor):
    """LazyShellArmor item class"""
    _item_name: str = "Lazy Shell"

    _item_id: int = 70
    _description: str = "A stout and\x01durable shell."
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = -50
    _attack: int = -50
    _defense: int = 127
    _magic_attack: int = -50
    _magic_defense: int = 127
    _elemental_immunities: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 222
    _effect_type: EffectType = EffectType.PROTECTION


class Spare71(Armor):
    """Placeholder slot 71 item class"""
    _item_name: str = "Spare"

    _item_id: int = 71
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 100


class Spare72(Armor):
    """Placeholder slot 72 item class"""
    _item_name: str = "Spare"

    _item_id: int = 72
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 100


class Spare73(Armor):
    """Placeholder slot 73 item class"""
    _item_name: str = "Spare"

    _item_id: int = 73
    _description: str = ""
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 100


class ZoomShoes(Accessory):
    """ZoomShoes item class"""
    _item_name: str = "Zoom Shoes"

    _item_id: int = 74
    _description: str = "Speed up by 10!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 100


class SafetyBadge(Accessory):
    """SafetyBadge item class"""
    _item_name: str = "Safety Badge"

    _item_id: int = 75
    _description: str = "Prevents Mute \x9c\x01Poison attacks"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 5
    _magic_defense: int = 5
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 500
    _effect_type: EffectType = EffectType.PROTECTION


class JumpShoes(Accessory):
    """JumpShoes item class"""
    _item_name: str = "Jump Shoes"

    _item_id: int = 76
    _description: str = "Use jump attacks\x01against any foe"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _speed: int = 2
    _defense: int = 1
    _magic_attack: int = 5
    _magic_defense: int = 1
    _price: int = 30
    _arbitrary_value: UInt16 = UInt16(1)


class SafetyRing(Accessory):
    """SafetyRing item class"""
    _item_name: str = "Safety Ring"

    _item_id: int = 77
    _description: str = "Guards against\x01mortal blows."
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 5
    _defense: int = 5
    _magic_defense: int = 5
    _prevent_ko: bool = True
    _elemental_immunities: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 800
    _effect_type: EffectType = EffectType.PROTECTION


class Amulet(Accessory):
    """Amulet item class"""
    _item_name: str = "Amulet"

    _item_id: int = 78
    _description: str = "Great item,\x01bad smell!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = -5
    _attack: int = 7
    _defense: int = 7
    _magic_attack: int = 7
    _magic_defense: int = 7
    _elemental_resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _price: int = 200


class ScroogeRing(Accessory):
    """ScroogeRing item class"""
    _item_name: str = "Scrooge Ring"

    _item_id: int = 79
    _description: str = "Cuts FP use\x01in half\x01during battle"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 50
    _frog_coin_item: bool = True
    _arbitrary_value: UInt16 = UInt16(1)


class ExpBooster(Accessory):
    """ExpBooster item class"""
    _item_name: str = "Exp. Booster"

    _item_id: int = 80
    _description: str = "Doubles Exp.\x01when equipped"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 22
    _frog_coin_item: bool = True
    _arbitrary_value: UInt16 = UInt16(10)


class AttackScarf(Accessory):
    """AttackScarf item class"""
    _item_name: str = "Attack Scarf"

    _item_id: int = 81
    _description: str = "So comfy it~ll\x01make you jump!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _speed: int = 30
    _attack: int = 30
    _defense: int = 30
    _magic_attack: int = 30
    _magic_defense: int = 30
    _prevent_ko: bool = True
    _price: int = 1500


class RareScarf(Accessory):
    """RareScarf item class"""
    _item_name: str = "Rare Scarf"

    _item_id: int = 82
    _description: str = "Raises defense\x01power!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 15
    _magic_defense: int = 15
    _price: int = 150


class BtubRing(Accessory):
    """BtubRing item class"""
    _item_name: str = "Btub Ring"

    _item_id: int = 83
    _description: str = "You~ll win her\x01heart with this!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _elemental_resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
        Element.JUMP,
    ]
    _price: int = 145
    _arbitrary_value: UInt16 = UInt16(1)


class AntidotePin(Accessory):
    """AntidotePin item class"""
    _item_name: str = "Antidote Pin"

    _item_id: int = 84
    _description: str = "Prevents\x01poison damage"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 2
    _magic_defense: int = 2
    _status_immunities: List[Status] = [Status.POISON]
    _price: int = 28
    _effect_type: EffectType = EffectType.PROTECTION


class WakeUpPin(Accessory):
    """WakeUpPin item class"""
    _item_name: str = "Wake Up Pin"

    _item_id: int = 85
    _description: str = "Prevents Mute \x9c\x01Sleep attacks"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 3
    _magic_defense: int = 3
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _price: int = 42
    _effect_type: EffectType = EffectType.PROTECTION


class FearlessPin(Accessory):
    """FearlessPin item class"""
    _item_name: str = "Fearless Pin"

    _item_id: int = 86
    _description: str = "Prevents Fear\x01attacks"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 5
    _magic_defense: int = 5
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 130
    _effect_type: EffectType = EffectType.PROTECTION


class TrueformPin(Accessory):
    """TrueformPin item class"""
    _item_name: str = "Trueform Pin"

    _item_id: int = 87
    _description: str = "You won~t be\x01turned into\x01Mushrooms or\x01Scarecrows!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 4
    _magic_defense: int = 4
    _status_immunities: List[Status] = [
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 60
    _effect_type: EffectType = EffectType.PROTECTION


class CoinTrick(Accessory):
    """CoinTrick item class"""
    _item_name: str = "Coin Trick"
    _item_id: int = 88
    _description: str = "Doubles the\x01coins you win\x01in battle"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 36
    _frog_coin_item: bool = True
    _arbitrary_value: UInt16 = UInt16(2)


class GhostMedal(Accessory):
    """GhostMedal item class"""
    _item_name: str = "Ghost Medal"

    _item_id: int = 89
    _description: str = "Raises defense\x01while attacking"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 1600
    _effect_type: EffectType = EffectType.INFLICTION


class JinxBelt(Accessory):
    """JinxBelt item class"""
    _item_name: str = "Jinx Belt"

    _item_id: int = 90
    _description: str = "Jinx~s emblem\x01of power!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 12
    _attack: int = 27
    _defense: int = 27
    _prevent_ko: bool = True
    _price: int = 1998


class Feather(Accessory):
    """Feather item class"""
    _item_name: str = "Feather"

    _item_id: int = 91
    _description: str = "Speed up by 20"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 666


class TroopaPin(Accessory):
    """TroopaPin item class"""
    _item_name: str = "Troopa Pin"

    _item_id: int = 92
    _description: str = 'Grants "Troopa#\x01confidence!'
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 1000
    _effect_type: EffectType = EffectType.INFLICTION


class SignalRing(Accessory):
    """SignalRing item class"""
    _item_name: str = "Signal Ring"

    _item_id: int = 93
    _description: str = "Noise indicates\x01a hidden chest."
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _price: int = 600


class QuartzCharm(Accessory):
    """QuartzCharm item class"""
    _item_name: str = "Quartz Charm"

    _item_id: int = 94
    _description: str = "Shining source\x01of power!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _prevent_ko: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 7
    _effect_type: EffectType = EffectType.INFLICTION


class Spare95(RegularItem):
    """Placeholder slot 95 item class"""
    _item_name: str = "Spare"

    _item_id: int = 95
    _description: str = ""
    _equip_chars: List[PartyCharacter] = []
    _price: int = 65535
    _usable_overworld: bool = True


class Mushroom(RegularItem):
    """Mushroom item class"""
    _item_name: str = "Mushroom"

    _item_id: int = 96
    _description: str = "Recovers 30 HP"
    
    _price: int = 4
    _inflict: int = 30

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _can_target_others: bool = True 
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    


class MidMushroom(RegularItem):
    """MidMushroom item class"""
    _item_name: str = "Mid Mushroom"

    _item_id: int = 97
    _description: str = "Recovers 80 HP"
    
    _price: int = 20
    _inflict: int = 80

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _can_target_others: bool = True 
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    


class MaxMushroom(RegularItem):
    """MaxMushroom item class"""
    _item_name: str = "Max Mushroom"

    _item_id: int = 98
    _description: str = "Recovers all HP"
    
    _price: int = 78
    _inflict: int = 255

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _can_target_others: bool = True 
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    


class HoneySyrup(RegularItem):
    """HoneySyrup item class"""
    _item_name: str = "Honey Syrup"

    _item_id: int = 99
    _description: str = "Recovers 10 FP"
    
    _price: int = 10
    _inflict: int = 10

    _inflict_type: InflictFunction = InflictFunction.RESTORE_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_fp: bool = True
    


class MapleSyrup(RegularItem):
    """MapleSyrup item class"""
    _item_name: str = "Maple Syrup"

    _item_id: int = 100
    _description: str = "Recovers 40 FP"
    
    _price: int = 30
    _inflict: int = 40

    _inflict_type: InflictFunction = InflictFunction.RESTORE_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_fp: bool = True
    


class RoyalSyrup(RegularItem):
    """RoyalSyrup item class"""
    _item_name: str = "Royal Syrup"

    _item_id: int = 101
    _description: str = "Recovers all FP"
    
    _price: int = 101
    _inflict: int = 99

    _inflict_type: InflictFunction = InflictFunction.RESTORE_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_fp: bool = True
    


class PickMeUp(RegularItem):
    """PickMeUp item class"""
    _item_name: str = "Pick Me Up"

    _item_id: int = 102
    _description: str = "Revives downed\x01allies"
    
    _price: int = 5

    _inflict_type: InflictFunction = InflictFunction.REVIVE
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True 
    _koed_target_only: bool = True
    


class AbleJuice(RegularItem):
    """AbleJuice item class"""
    _item_name: str = "Able Juice"

    _item_id: int = 103
    _description: str = "Heal status\x01ailments"
    
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 4

    _effect_type: EffectType = EffectType.NULLIFICATION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True 
    


class Bracer(RegularItem):
    """Bracer item class"""
    _item_name: str = "Bracer"

    _item_id: int = 104
    _description: str = "Raises ally~s\x01def. in battle"
    
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 50
    _frog_coin_item: bool = True
    _rank_value: int = 10

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True 
    


class Energizer(RegularItem):
    """Energizer item class"""
    _item_name: str = "Energizer"

    _item_id: int = 105
    _description: str = "Raises ally~s\x01battle power\x01during battle"
    
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 50
    _frog_coin_item: bool = True

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True 
    _overworld_menu_fill_fp: bool = True
    


class YoshiAde(RegularItem):
    """YoshiAde item class"""
    _item_name: str = "Yoshi-Ade"

    _item_id: int = 106
    _description: str = "Power raised\x01during battle"
    
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 200

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True 
    


class RedEssence(RegularItem):
    """RedEssence item class"""
    _item_name: str = "Red Essence"

    _item_id: int = 107
    _description: str = "Become invincible\x01for 3 turns"
    
    _status_immunities: List[Status] = [Status.INVINCIBLE]
    _price: int = 400

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True 
    


class KerokeroCola(RegularItem):
    """KerokeroCola item class"""
    _item_name: str = "KerokeroCola"

    _item_id: int = 108
    _description: str = "All members\x01recover fully"
    
    _price: int = 400

    _inflict_type: InflictFunction = InflictFunction.RESTORE_ALL_HP_FP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    

    _overworld_menu_fill_fp: bool = True 
    _overworld_menu_fill_hp: bool = True


class YoshiCookie(RegularItem):
    """YoshiCookie item class"""
    _item_name: str = "Yoshi Cookie"

    _item_id: int = 109
    _description: str = "Summons Yoshi\x01during battle"
    
    _price: int = 100

    _inflict_type: InflictFunction = InflictFunction.ITEM_MORPH
    _usable_battle: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    


class PureWater(RegularItem):
    """PureWater item class"""
    _item_name: str = "Pure Water"

    _item_id: int = 110
    _description: str = "Defeats ghosts\x01in a wink"
    
    _price: int = 150

    _hide_damage: bool = True
    _usable_battle: bool = True
    _can_target_others: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    


class SleepyBomb(RegularItem):
    """SleepyBomb item class"""

    _item_name: str = "Sleepy Bomb"
    _item_id: int = 111
    _description: str = "Puts enemies\x01to sleep"
    
    _status_immunities: List[Status] = [Status.SLEEP]
    _price: int = 25
    _frog_coin_item: bool = True

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _target_all: bool = True
    


class BadMushroom(RegularItem):
    """BadMushroom item class"""

    _item_name: str = "Bad Mushroom"
    _item_id: int = 112
    _description: str = "Poisons\x01an enemy"
    
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 30
    _inflict: int = 50

    _effect_type: EffectType = EffectType.INFLICTION
    _usable_battle: bool = True
    _can_target_others: bool = True 
    _target_enemies: bool = True
    _one_side_only: bool = True
    

class FireBomb(RegularItem):
    """FireBomb item class"""

    _item_name: str = "Fire Bomb"
    _item_id: int = 113
    _description: str = "Hit all\x01enemies w/fire"
    
    _price: int = 200
    _inflict: 120

    _inflict_element: Element.FIRE
    _usable_battle: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _target_all: bool = True
    


class IceBomb(RegularItem):
    """IceBomb item class"""

    _item_name: str = "Ice Bomb"
    _item_id: int = 114
    _description: str = "Hit all\x01enemies w/ice"
    
    _price: int = 250
    _inflict: int = 140

    _inflict_element: Element.ICE
    _usable_battle: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _target_all: bool = True
    


class FlowerTab(RegularItem):
    """FlowerTab item class"""
    _item_name: str = "Flower Tab"

    _item_id: int = 115
    _description: str = "Raise FP by 1"
    
    _price: int = 200
    _inflict: int = 1

    _inflict_type: InflictFunction = InflictFunction.RAISE_MAX_FP
    _usable_overworld: bool = True 
    _can_target_others: bool = True
    _one_side_only: bool = True
    

    _overworld_menu_behaviour: OverworldMenuBehaviour.LEAD_TO_FP


class FlowerJar(RegularItem):
    """FlowerJar item class"""
    _item_name: str = "Flower Jar"

    _item_id: int = 116
    _description: str = "Raise FP by 3"
    
    _price: int = 600
    _inflict: int = 3

    _inflict_type: InflictFunction = InflictFunction.RAISE_MAX_FP
    _usable_overworld: bool = True 
    _can_target_others: bool = True
    _one_side_only: bool = True
    

    _overworld_menu_behaviour: OverworldMenuBehaviour.LEAD_TO_FP


class FlowerBox(RegularItem):
    """FlowerBox item class"""
    _item_name: str = "Flower Box"

    _item_id: int = 117
    _description: str = "Raise FP by 5"
    
    _price: int = 1000
    _inflict: int = 5

    _inflict_type: InflictFunction = InflictFunction.RAISE_MAX_FP
    _usable_overworld: bool = True 
    _can_target_others: bool = True
    _one_side_only: bool = True
    

    _overworld_menu_behaviour: OverworldMenuBehaviour.LEAD_TO_FP


class YoshiCandy(RegularItem):
    """YoshiCandy item class"""
    _item_name: str = "Yoshi Candy"

    _item_id: int = 118
    _description: str = "Heals 100 HP"
    
    _price: int = 140
    _inflict: int = 100

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    


class FroggieDrink(RegularItem):
    """FroggieDrink item class"""
    _item_name: str = "FroggieDrink"

    _item_id: int = 119
    _description: str = "Party heals\x0130 HP"
    
    _price: int = 16
    _inflict: int = 30

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    

class MukuCookie(RegularItem):
    """MukuCookie item class"""
    _item_name: str = "Muku Cookie"

    _item_id: int = 120
    _description: str = "Party heals\x0169 HP"
    
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 69
    _inflict: int = 69
    _effect_type: EffectType = EffectType.NULLIFICATION
    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    

    _overworld_menu_fill_hp: bool = True


class Elixir(RegularItem):
    """Elixir item class"""
    _item_name: str = "Elixir"

    _item_id: int = 121
    _description: str = "Party heals\x0180 HP"
    
    _price: int = 48
    _inflict: int = 80

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    


class Megalixir(RegularItem):
    """Megalixir item class"""
    _item_name: str = "Megalixir"

    _item_id: int = 122
    _description: str = "Party heals\x01150 HP"
    
    _price: int = 120
    _inflict: int = 150

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True
    


class SeeYa(RegularItem):
    """SeeYa item class"""
    _item_name: str = "See Ya"

    _item_id: int = 123
    _description: str = "Run away from\x01battles"
    _price: int = 10
    _frog_coin_item: bool = True

    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _reusable: bool = True


class TempleKey(RegularItem):
    """TempleKey item class"""
    _item_name: str = "Temple Key"
    _description: str = "It's a\x01Temple Key"

    _item_id: int = 124
    


class GoodieBag(RegularItem):
    """GoodieBag item class"""
    _item_name: str = "Goodie Bag"

    _item_id: int = 125
    _price: int = 1110
    _description: str = "It's packed\x01full of coins"
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _reusable: bool = True


class EarlierTimes(RegularItem):
    """EarlierTimes item class"""
    _item_name: str = "EarlierTimes"

    _item_id: int = 126
    _description: str = "Use it to start\x01a battle over"
    _price: int = 375
    _frog_coin_item: bool = True
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _reusable: bool = True


class FreshenUp(RegularItem):
    """FreshenUp item class"""
    _item_name: str = "Freshen Up"

    _item_id: int = 127
    _description: str = "Heals party\x01status ailments"
    
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _price: int = 50

    _effect_type: EffectType = EffectType.NULLIFICATION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _target_all: bool = True


class RareFrogCoin(RegularItem):
    """RareFrogCoin item class"""
    _item_name: str = "RareFrogCoin"
    _description: str = "It's a Frog Coin\x01from Frogfucius!"

    _item_id: int = 128
    


class Wallet(RegularItem):
    """Wallet item class"""
    _item_name: str = "Wallet"

    _item_id: int = 129
    _description: str = "A fat wallet"
    _price: int = 246
    


class CricketPie(RegularItem):
    """CricketPie item class"""
    _item_name: str = "Cricket Pie"
    _description: str = "A tasty looking\x01pie"

    _item_id: int = 130
    


class RockCandy(RegularItem):
    """RockCandy item class"""

    _item_name: str = "Rock Candy"
    _item_id: int = 131
    _description: str = "Attack all\x01enemies"
    _inflict: int = 200
    
    _price: int = 400

    _usable_battle: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _target_all: bool = True


class CastleKey1(RegularItem):
    """CastleKey1 item class"""
    _item_name: str = "Castle Key 1"
    _description: str = "It's a\x01Castle Key"

    _item_id: int = 132
    


class DebugBomb(RegularItem):
    """DebugBomb item class"""

    _item_name: str = "Debug Bomb"
    _item_id: int = 133
    _description: str = ""
    _inflict: int = 255
    
    _price: int = 2

    _usable_battle: bool = True
    _reusable: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _target_all: bool = True


class CastleKey2(RegularItem):
    """CastleKey2 item class"""
    _item_name: str = "Castle Key 2"
    _description: str = "It's a\x01Castle Key"

    _item_id: int = 134


class BambinoBomb(RegularItem):
    """BambinoBomb item class"""
    _item_name: str = "Bambino Bomb"
    _description: str = "Handle with\x01care!"

    _item_id: int = 135


class SheepAttack(RegularItem):
    """SheepAttack item class"""
    _item_name: str = "Sheep Attack"

    _item_id: int = 136
    _description: str = "Baah, baah..."
    _price: int = 2

    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _target_all: bool = True

    _inflict_type: InflictFunction = InflictFunction.INSTANT_DEATH


class CarboCookie(RegularItem):
    """CarboCookie item class"""
    _item_name: str = "Carbo Cookie"

    _item_id: int = 137
    _description: str = "Kid's love 'em"
    _price: int = 2


class ShinyStone(RegularItem):
    """ShinyStone item class"""
    _item_name: str = "Shiny Stone"

    _item_id: int = 138
    _description: str = "A pretty stone!"
    _price: int = 4


class Dummy139(RegularItem):
    """Dummy139 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 139


class RoomKey(RegularItem):
    """RoomKey item class"""
    _item_name: str = "Room Key"
    _description: str = "The key to\x01the mine room!"

    _item_id: int = 140


class ElderKey(RegularItem):
    """ElderKey item class"""
    _item_name: str = "Elder Key"
    _description: str = "The key to the\x01Ancestor Hall"

    _item_id: int = 141


class ShedKey(RegularItem):
    """ShedKey item class"""
    _item_name: str = "Shed Key"
    _description: str = "The key\x01to the shed\x01in Seaside Town"

    _item_id: int = 142


class LambsLure(RegularItem):
    """LambsLure item class"""
    _item_name: str = "Lamb's Lure"

    _item_id: int = 143
    _description: str = "Baa, baa..."
    _price: int = 2

    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True

    _inflict_type: InflictFunction = InflictFunction.INSTANT_DEATH


class FrightBomb(RegularItem):
    """FrightBomb item class"""

    _item_name: str = "Fright Bomb"
    _item_id: int = 144
    _description: str = "Inflict fear\x01on one enemy"
    _inflict: int = 100
    
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 100

    _effect_type: EffectType = EffectType.INFLICTION
    _usable_battle: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True


class MysteryEgg(RegularItem):
    """MysteryEgg item class"""
    _item_name: str = "Mystery Egg"

    _item_id: int = 145
    _description: str = "A product of\x01pure love..."
    _price: int = 200

    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _one_side_only: bool = True


class BeetleBox(RegularItem):
    """BeetleBox item class"""
    _item_name: str = "Beetle Box"
    _description: str = "It's an insect\x01cage"

    _item_id: int = 146


class BeetleBox2(RegularItem):
    """BeetleBox2 item class"""
    _item_name: str = "Beetle Box"
    _description: str = "There are\x01beetles inside"

    _item_id: int = 147


class LuckyJewel(RegularItem):
    """LuckyJewel item class"""
    _item_name: str = "Lucky Jewel"

    _item_id: int = 148
    _description: str = "Summons Luck\x01at will"
    _price: int = 100

    _hide_damage: bool = True
    _usable_battle: bool = True 
    _reusable: bool = True
    _one_side_only: bool = True


class Dummy149(RegularItem):
    """Dummy149 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 149


class SopranoCard(RegularItem):
    """SopranoCard item class"""
    _item_name: str = "Soprano Card"
    _description: str = "A membership\x01card for the\x01juice bar"

    _item_id: int = 150


class AltoCard(RegularItem):
    """AltoCard item class"""
    _item_name: str = "Alto Card"
    _description: str = "A membership\x01card for the\x01juice bar"

    _item_id: int = 151


class TenorCard(RegularItem):
    """TenorCard item class"""
    _item_name: str = "Tenor Card"
    _description: str = "A membership\x01card for the\x01juice bar"

    _item_id: int = 152


class Crystalline(RegularItem):
    """Crystalline item class"""
    _item_name: str = "Crystalline"

    _item_id: int = 153
    _description: str = "Raises party's\x01Defense in\x01battle"
    
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 5
    _frog_coin_item: bool = True

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _target_all: bool = True


class PowerBlast(RegularItem):
    """PowerBlast item class"""
    _item_name: str = "Power Blast"

    _item_id: int = 154
    _description: str = "Raises party's\x01Attack Power\x01in battle"
    
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 5
    _frog_coin_item: bool = True

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _one_side_only: bool = True
    _target_all: bool = True


class WiltShroom(RegularItem):
    """WiltShroom item class"""
    _item_name: str = "Wilt Shroom"

    _item_id: int = 155
    _description: str = "It's wilted..."
    
    _price: int = 8
    _inflict: int = 10

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_overworld: bool = True
    _can_target_others: bool = True 
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True


class RottenMush(RegularItem):
    """RottenMush item class"""
    _item_name: str = "Rotten Mush"

    _item_id: int = 156
    _description: str = "Eeew,\x01it's rotten!"
    
    _price: int = 4
    _inflict: int = 5

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_overworld: bool = True
    _can_target_others: bool = True 
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True


class MoldyMush(RegularItem):
    """MoldyMush item class"""
    _item_name: str = "Moldy Mush"

    _item_id: int = 157
    _description: str = "Gross!\x01There's mold\x01growing on it."
    
    _price: int = 2
    _inflict: int = 1

    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_overworld: bool = True
    _can_target_others: bool = True 
    _one_side_only: bool = True
    _overworld_menu_fill_hp: bool = True


class Seed(RegularItem):
    """Seed item class"""
    _item_name: str = "Seed"
    _description: str = "A fast-growing\x01deed"

    _item_id: int = 158
    _price: int = 300


class Fertilizer(RegularItem):
    """Fertilizer item class"""
    _item_name: str = "Fertilizer"
    _description: str = "Nutrients!"

    _item_id: int = 159
    _price: int = 200


class WasteBasket(RegularItem):
    """WasteBasket item class"""
    _item_name: str = "Waste Basket"
    _description: str = "You can throw\x01away unwanted\x01items"

    _item_id: int = 160
    _price: int = 65535
    _usable_overworld: bool = True


class BigBooFlag(RegularItem):
    """BigBooFlag item class"""
    _item_name: str = "Big Boo Flag"
    _description: str = "It's a\x01Big Boo Flag"

    _item_id: int = 161


class DryBonesFlag(RegularItem):
    """DryBonesFlag item class"""
    _item_name: str = "DryBonesFlag"
    _description: str = "It's a\x01Dry Bones' Flag"

    _item_id: int = 162


class GreaperFlag(RegularItem):
    """GreaperFlag item class"""
    _item_name: str = "Greaper Flag"
    _description: str = "It's a\x01Greaper Flag"

    _item_id: int = 163


class SecretGame(RegularItem):
    """GreaperFlag item class"""
    _item_name: str = "Secret Game"
    _description: str = "A super\x01popular video\x01game!"

    _item_id: int = 164
    _price: int = 1998

class SCrowBomb(RegularItem):
    """S.Crow Bomb item class"""
    _item_name: str = "S.Crow Bomb"
    _item_id: int = 165
    _price: int = 2
    _status_immunities: List[Status] = [Status.SCARECROW]
    _effect_type: EffectType = EffectType.INFLICTION 
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True


class CricketJam(RegularItem):
    """CricketJam item class"""

    _item_name: str = "Cricket Jam"
    _description: str = "Delicious jam!"
    _item_id: int = 166

class BaneBomb(RegularItem):
    """Bane Bomb item class"""
    _item_name: str = "Bane Bomb"
    _item_id: int = 167
    _status_immunities: List[Status] = [Status.POISON]
    _effect_type: EffectType = EffectType.INFLICTION 
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True

class DoomBomb(RegularItem):
    """Doom Bomb item class"""
    _item_name: str = "Doom Bomb"
    _item_id: int = 168
    _price: int = 2
    _inflict: int = 255
    _usable_battle: bool = True
    _reusable: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True

class FearBomb(RegularItem):
    """FearBomb item class"""

    _item_name: str = "Fear Bomb"
    _item_id: int = 169
    _inflict: int = 100
    
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 100

    _effect_type: EffectType = EffectType.INFLICTION
    _usable_battle: bool = True
    _target_enemies: bool = True
    _one_side_only: bool = True
    _can_target_others: bool = True

class SleepBomb(RegularItem):
    """SleepBomb item class"""

    _item_name: str = "Sleep Bomb"
    _item_id: int = 170
    
    _status_immunities: List[Status] = [Status.SLEEP]

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    
    _one_side_only: bool = True
    _can_target_others: bool = True

class MuteBomb(RegularItem):
    """MuteBomb item class"""

    _item_name: str = "Mute Bomb"
    _item_id: int = 171
    
    _status_immunities: List[Status] = [Status.MUTE]

    _effect_type: EffectType = EffectType.INFLICTION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _reusable: bool = True
    
    _one_side_only: bool = True
    _can_target_others: bool = True


class Fireworks(RegularItem):
    """Fireworks item class"""

    _item_name: str = "Fireworks"
    _item_id: int = 172
    _description: str = "A gorgeous\x01firework"
    _price: int = 500

class Bomb(RegularItem):
    """Bomb item class"""
    _item_name: str = "Bomb"
    _item_id: int = 173
    _inflict: int = 255
    _usable_battle: bool = True
    _reusable: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _target_enemies: bool = True


class BrightCard(RegularItem):
    """BrightCard item class"""
    _item_name: str = "Bright Card"
    _description: str = "A member's card\x01for the casino"

    _item_id: int = 174


class Mushroom2(RegularItem):
    """Mushroom2 item class"""

    _item_name: str = "Mushroom"
    _item_id: int = 175
    _description: str = "Recoers 30 HP,\x01but..."
    _inflict: int = 30
    _effect_type: EffectType = EffectType.INFLICTION
    _inflict_type: InflictFunction = InflictFunction.RESTORE_HP
    _usable_battle: bool = True
    _usable_overworld: bool = True
    _can_target_others: bool = True
    _one_side_only: bool = True
    _can_target_self: bool = False
    
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 4
    _overworld_menu_fill_hp: bool = True


class StarEgg(RegularItem):
    """StarEgg item class"""
    _item_name: str = "Star Egg"

    _item_id: int = 176
    _description: str = "Reusable battle\x01item"
    _price: int = 2 
    _inflict: int = 100 
    _usable_battle: bool = True
    _reusable: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True

class Dummy177(RegularItem):
    """Dummy177 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 177

class Dummy178(RegularItem):
    """Dummy178 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 178

class Dummy179(RegularItem):
    """Dummy179 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 179

class Dummy180(RegularItem):
    """Dummy180 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 180

class Dummy181(RegularItem):
    """Dummy181 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 181

class Dummy182(RegularItem):
    """Dummy182 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 182

class Dummy183(RegularItem):
    """Dummy183 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 183

class Dummy184(RegularItem):
    """Dummy184 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 184

class Dummy185(RegularItem):
    """Dummy185 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 185

class Dummy186(RegularItem):
    """Dummy186 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 186

class Dummy187(RegularItem):
    """Dummy187 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 187

class Dummy188(RegularItem):
    """Dummy188 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 188

class Dummy189(RegularItem):
    """Dummy189 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 189

class Dummy190(RegularItem):
    """Dummy190 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 190

class Dummy191(RegularItem):
    """Dummy191 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 191

class Dummy192(RegularItem):
    """Dummy192 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 192

class Dummy193(RegularItem):
    """Dummy193 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 193

class Dummy194(RegularItem):
    """Dummy194 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 194

class Dummy195(RegularItem):
    """Dummy195 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 195

class Dummy196(RegularItem):
    """Dummy196 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 196

class Dummy197(RegularItem):
    """Dummy197 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 197

class Dummy198(RegularItem):
    """Dummy198 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 198

class Dummy199(RegularItem):
    """Dummy199 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 199

class Dummy200(RegularItem):
    """Dummy200 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 200

class Dummy201(RegularItem):
    """Dummy201 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 201

class Dummy202(RegularItem):
    """Dummy202 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 202

class Dummy203(RegularItem):
    """Dummy203 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 203

class Dummy204(RegularItem):
    """Dummy204 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 204

class Dummy205(RegularItem):
    """Dummy205 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 205

class Dummy206(RegularItem):
    """Dummy206 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 206

class Dummy207(RegularItem):
    """Dummy207 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 207

class Dummy208(RegularItem):
    """Dummy208 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 208

class Dummy209(RegularItem):
    """Dummy209 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 209

class Dummy210(RegularItem):
    """Dummy210 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 210

class Dummy211(RegularItem):
    """Dummy211 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 211

class Dummy212(RegularItem):
    """Dummy212 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 212

class Dummy213(RegularItem):
    """Dummy213 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 213

class Dummy214(RegularItem):
    """Dummy214 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 214

class Dummy215(RegularItem):
    """Dummy215 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 215

class Dummy216(RegularItem):
    """Dummy216 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 216

class Dummy217(RegularItem):
    """Dummy217 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 217

class Dummy218(RegularItem):
    """Dummy218 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 218

class Dummy219(RegularItem):
    """Dummy219 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 219

class Dummy220(RegularItem):
    """Dummy220 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 220

class Dummy221(RegularItem):
    """Dummy221 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 221

class Dummy222(RegularItem):
    """Dummy222 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 222

class Dummy223(RegularItem):
    """Dummy223 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 223

class Dummy224(RegularItem):
    """Dummy224 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 224

class Dummy225(RegularItem):
    """Dummy225 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 225

class Dummy226(RegularItem):
    """Dummy226 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 226

class Dummy227(RegularItem):
    """Dummy227 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 227

class Dummy228(RegularItem):
    """Dummy228 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 228

class Dummy229(RegularItem):
    """Dummy229 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 229

class Dummy230(RegularItem):
    """Dummy230 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 230

class Dummy231(RegularItem):
    """Dummy231 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 231

class Dummy232(RegularItem):
    """Dummy232 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 232

class Dummy233(RegularItem):
    """Dummy233 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 233

class Dummy234(RegularItem):
    """Dummy234 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 234

class Dummy235(RegularItem):
    """Dummy235 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 235

class Dummy236(RegularItem):
    """Dummy236 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 236

class Dummy237(RegularItem):
    """Dummy237 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 237

class Dummy238(RegularItem):
    """Dummy238 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 238

class Dummy239(RegularItem):
    """Dummy239 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 239

class Dummy240(RegularItem):
    """Dummy240 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 240

class Dummy241(RegularItem):
    """Dummy241 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 241

class Dummy242(RegularItem):
    """Dummy242 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 242

class Dummy243(RegularItem):
    """Dummy243 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 243

class Dummy244(RegularItem):
    """Dummy244 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 244

class Dummy245(RegularItem):
    """Dummy245 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 245

class Dummy246(RegularItem):
    """Dummy246 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 246

class Dummy247(RegularItem):
    """Dummy247 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 247

class Dummy248(RegularItem):
    """Dummy248 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 248

class Dummy249(RegularItem):
    """Dummy249 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 249

class Dummy250(RegularItem):
    """Dummy250 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 250

class Dummy251(RegularItem):
    """Dummy251 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 251

class Dummy252(RegularItem):
    """Dummy252 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 252

class Dummy253(RegularItem):
    """Dummy253 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 253

class Dummy254(RegularItem):
    """Dummy254 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 254

class Dummy255(RegularItem):
    """Dummy255 item class"""
    _item_name: str = "DUMMY"

    _item_id: int = 255
