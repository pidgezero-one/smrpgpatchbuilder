# pylint: disable=C0301

"""Individual item class definitions."""

from typing import List

from .classes import (
    RegularItem,
    Weapon,
    Armor,
    Accessory,
)
from smrpgpatchbuilder.datatypes.numbers.classes import UInt16
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.classes import PartyCharacter
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MARIO,
    MALLOW,
    GENO,
    TOADSTOOL,
    BOWSER,
)
from smrpgpatchbuilder.datatypes.spells.classes import Element, Status, TempStatBuff


class Hammer(Weapon):
    """Hammer item class"""

    _item_id: int = 5
    _description: str = "Pounds\x01enemies"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 10
    _variance: int = 1
    _price: int = 70


class FroggieStick(Weapon):
    """FroggieStick item class"""

    _item_id: int = 6
    _description: str = "Frogfucius\x01made it"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 20
    _variance: int = 2
    _price: int = 180


class NokNokShell(Weapon):
    """NokNokShell item class"""

    _item_id: int = 7
    _description: str = "Kick to attack"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 20
    _variance: int = 2
    _price: int = 20


class PunchGlove(Weapon):
    """PunchGlove item class"""

    _item_id: int = 8
    _description: str = "Knock out\x01power!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 30
    _variance: int = 3
    _price: int = 36


class FingerShot(Weapon):
    """FingerShot item class"""

    _item_id: int = 9
    _description: str = "Fingers shoot\x01bullets"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 12
    _variance: int = 3
    _price: int = 50


class Cymbals(Weapon):
    """Cymbals item class"""

    _item_id: int = 10
    _description: str = "Scare enemies\x01with a clash"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 30
    _variance: int = 3
    _price: int = 42


class Chomp(Weapon):
    """Chomp item class"""

    _item_id: int = 11
    _description: str = "Just spin me\x01at an enemy!"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 10
    _variance: int = 4
    _price: int = 140


class Masher(Weapon):
    """Masher item class"""

    _item_id: int = 12
    _description: str = "Makes monster\x01mash!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 30
    _price: int = 160


class ChompShell(Weapon):
    """ChompShell item class"""

    _item_id: int = 13
    _description: str = "It~s a\x01Kinklink shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 9
    _variance: int = 3
    _price: int = 60


class SuperHammer(Weapon):
    """SuperHammer item class"""

    _item_id: int = 14
    _description: str = "The standard\x01for hammers!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 40
    _variance: int = 4
    _price: int = 70


class HandGun(Weapon):
    """HandGun item class"""

    _item_id: int = 15
    _description: str = "It packs a kick"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 24
    _variance: int = 4
    _price: int = 75


class WhompGlove(Weapon):
    """WhompGlove item class"""

    _item_id: int = 16
    _description: str = "The old double\x01whammie!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 40
    _variance: int = 4
    _price: int = 72


class SlapGlove(Weapon):
    """SlapGlove item class"""

    _item_id: int = 17
    _description: str = "It slaps ~em\x01silly"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 40
    _variance: int = 4
    _price: int = 100


class TroopaShell(Weapon):
    """TroopaShell item class"""

    _item_id: int = 18
    _description: str = "Kick with it!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 50
    _variance: int = 5
    _price: int = 90


class Parasol(Weapon):
    """Parasol item class"""

    _item_id: int = 19
    _description: str = "Inflicts\x01serious pain!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 50
    _variance: int = 5
    _price: int = 84


class HurlyGloves(Weapon):
    """HurlyGloves item class"""

    _item_id: int = 20
    _description: str = "A classic\x01Mario}toss\x01attack"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 20
    _variance: int = 5
    _price: int = 92


class DoublePunch(Weapon):
    """DoublePunch item class"""

    _item_id: int = 21
    _description: str = "A handy double\x01rocket punch"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 35
    _variance: int = 5
    _price: int = 88


class RibbitStick(Weapon):
    """RibbitStick item class"""

    _item_id: int = 22
    _description: str = "It~ll come\x01in handy"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 50
    _variance: int = 5
    _price: int = 86


class SpikedLink(Weapon):
    """SpikedLink item class"""

    _item_id: int = 23
    _description: str = "A studded ball\x01and chain!"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 30
    _variance: int = 6
    _price: int = 94


class MegaGlove(Weapon):
    """MegaGlove item class"""

    _item_id: int = 24
    _description: str = "Packs a mega\x01wallop!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 60
    _variance: int = 6
    _price: int = 102


class WarFan(Weapon):
    """WarFan item class"""

    _item_id: int = 25
    _description: str = "A mysterious\x01battle fan!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 60
    _variance: int = 6
    _price: int = 100


class HandCannon(Weapon):
    """HandCannon item class"""

    _item_id: int = 26
    _description: str = "Shoots bullets\x01from elbow!"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 45
    _variance: int = 6
    _price: int = 105


class StickyGlove(Weapon):
    """StickyGlove item class"""

    _item_id: int = 27
    _description: str = "Launches a\x01punch attack."
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 60
    _variance: int = 6
    _price: int = 98


class UltraHammer(Weapon):
    """UltraHammer item class"""

    _item_id: int = 28
    _description: str = "The ultimate\x01hammer!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 70
    _variance: int = 7
    _price: int = 115


class SuperSlap(Weapon):
    """SuperSlap item class"""

    _item_id: int = 29
    _description: str = "The Princess~\x01mega}slap!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 70
    _variance: int = 7
    _price: int = 110


class DrillClaw(Weapon):
    """DrillClaw item class"""

    _item_id: int = 30
    _description: str = "A drilling\x01claw!"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _attack: int = 40
    _variance: int = 7
    _price: int = 118


class StarGun(Weapon):
    """StarGun item class"""

    _item_id: int = 31
    _description: str = "Try shooting\x01stars!"
    _equip_chars: List[PartyCharacter] = [GENO]
    _attack: int = 57
    _variance: int = 7
    _price: int = 120


class SonicCymbal(Weapon):
    """SonicCymbal item class"""

    _item_id: int = 32
    _description: str = "Puts noise to\x01work for you!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _attack: int = 70
    _variance: int = 7
    _price: int = 108


class LazyShellWeapon(Weapon):
    """LazyShellWeapon item class"""

    _item_id: int = 33
    _description: str = "Toss a shell\x01at an enemy!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 90
    _variance: int = 40
    _price: int = 200


class FryingPan(Weapon):
    """FryingPan item class"""

    _item_id: int = 34
    _description: str = "Enough iron to\x01be dangerous!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _attack: int = 90
    _variance: int = 20
    _price: int = 300


class LuckyHammer(Weapon):
    """LuckyHammer item class"""

    _item_id: int = 35
    _description: str = "A lucky hammer!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 123


class Shirt(Armor):
    """Shirt item class"""

    _item_id: int = 37
    _description: str = "It~s a\x01shirt!"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 6
    _magic_defense: int = 6
    _price: int = 7


class Pants(Armor):
    """Pants item class"""

    _item_id: int = 38
    _description: str = "It~s a pair\x01of pants!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 7


class ThickShirt(Armor):
    """ThickShirt item class"""

    _item_id: int = 39
    _description: str = "A padded shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 12
    _magic_defense: int = 8
    _price: int = 14


class ThickPants(Armor):
    """ThickPants item class"""

    _item_id: int = 40
    _description: str = "Padded pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 14


class MegaShirt(Armor):
    """MegaShirt item class"""

    _item_id: int = 41
    _description: str = "Durable stay}\x01pressed shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 18
    _magic_defense: int = 10
    _price: int = 22


class MegaPants(Armor):
    """MegaPants item class"""

    _item_id: int = 42
    _description: str = "Durable work\x01pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 22


class WorkPants(Armor):
    """WorkPants item class"""

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

    _item_id: int = 44
    _description: str = "Durable\x01pressed cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 22


class HappyShirt(Armor):
    """HappyShirt item class"""

    _item_id: int = 45
    _description: str = "A lucky shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyPants(Armor):
    """HappyPants item class"""

    _item_id: int = 46
    _description: str = "A lucky\x01pair of pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 38


class HappyCape(Armor):
    """HappyCape item class"""

    _item_id: int = 47
    _description: str = "A lucky cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 38


class HappyShell(Armor):
    """HappyShell item class"""

    _item_id: int = 48
    _description: str = "A lucky shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 6
    _magic_defense: int = 3
    _price: int = 38


class PolkaDress(Armor):
    """PolkaDress item class"""

    _item_id: int = 49
    _description: str = "A flashy dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 160


class SailorShirt(Armor):
    """SailorShirt item class"""

    _item_id: int = 50
    _description: str = "A sailor~s\x01suit"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorPants(Armor):
    """SailorPants item class"""

    _item_id: int = 51
    _description: str = "A sailor~s\x01pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class SailorCape(Armor):
    """SailorCape item class"""

    _item_id: int = 52
    _description: str = "A sailor~s\x01cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 50


class NauticaDress(Armor):
    """NauticaDress item class"""

    _item_id: int = 53
    _description: str = "A female\x01sailor~s dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 50


class CourageShell(Armor):
    """CourageShell item class"""

    _item_id: int = 54
    _description: str = "A stout shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 12
    _magic_defense: int = 6
    _price: int = 60


class FuzzyShirt(Armor):
    """FuzzyShirt item class"""

    _item_id: int = 55
    _description: str = "A fuzzy shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyPants(Armor):
    """FuzzyPants item class"""

    _item_id: int = 56
    _description: str = "Fuzzy pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FuzzyCape(Armor):
    """FuzzyCape item class"""

    _item_id: int = 57
    _description: str = "A fuzzy cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 70


class FuzzyDress(Armor):
    """FuzzyDress item class"""

    _item_id: int = 58
    _description: str = "A fuzzy dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 70


class FireShirt(Armor):
    """FireShirt item class"""

    _item_id: int = 59
    _description: str = "Determined\x01person~s shirt"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class FirePants(Armor):
    """FirePants item class"""

    _item_id: int = 60
    _description: str = "Determined\x01person~s pants"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90
    _elemental_immunities: List[Element] = []


class FireCape(Armor):
    """FireCape item class"""

    _item_id: int = 61
    _description: str = "Determined\x01person~s cape"
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 30
    _magic_defense: int = 15
    _price: int = 90


class FireShell(Armor):
    """FireShell item class"""

    _item_id: int = 62
    _description: str = "Determined\x01person~s shell"
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 18
    _magic_defense: int = 9
    _price: int = 90


class FireDress(Armor):
    """FireDress item class"""

    _item_id: int = 63
    _description: str = "Determined\x01woman~s dress"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 42
    _magic_defense: int = 21
    _price: int = 90


class HeroShirt(Armor):
    """HeroShirt item class"""

    _item_id: int = 64
    _description: str = "A legendary\x01shirt."
    _equip_chars: List[PartyCharacter] = [MARIO]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class PrincePants(Armor):
    """PrincePants item class"""

    _item_id: int = 65
    _description: str = "Legendary\x01pants!"
    _equip_chars: List[PartyCharacter] = [MALLOW]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class StarCape(Armor):
    """StarCape item class"""

    _item_id: int = 66
    _description: str = "A legendary\x01cape."
    _equip_chars: List[PartyCharacter] = [GENO]
    _defense: int = 36
    _magic_defense: int = 18
    _price: int = 100


class HealShell(Armor):
    """HealShell item class"""

    _item_id: int = 67
    _description: str = "A legendary\x01shell."
    _equip_chars: List[PartyCharacter] = [BOWSER]
    _defense: int = 24
    _magic_defense: int = 12
    _price: int = 100


class RoyalDress(Armor):
    """RoyalDress item class"""

    _item_id: int = 68
    _description: str = "A legendary\x01dress!"
    _equip_chars: List[PartyCharacter] = [TOADSTOOL]
    _defense: int = 48
    _magic_defense: int = 24
    _price: int = 100


class SuperSuit(Armor):
    """SuperSuit item class"""

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


class LazyShellArmor(Armor):
    """LazyShellArmor item class"""

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


class ZoomShoes(Accessory):
    """ZoomShoes item class"""

    _item_id: int = 74
    _description: str = "Speed up by 10!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 100


class SafetyBadge(Accessory):
    """SafetyBadge item class"""

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


class JumpShoes(Accessory):
    """JumpShoes item class"""

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


class Amulet(Accessory):
    """Amulet item class"""

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

    _item_id: int = 79
    _description: str = "Cuts FP use\x01in half\x01during battle"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 50
    _frog_coin_item: bool = True
    _arbitrary_value: UInt16 = UInt16(1)


class ExpBooster(Accessory):
    """ExpBooster item class"""

    _item_id: int = 80
    _description: str = "Doubles Exp.\x01when equipped"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _price: int = 22
    _frog_coin_item: bool = True
    _arbitrary_value: UInt16 = UInt16(10)


class AttackScarf(Accessory):
    """AttackScarf item class"""

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

    _item_id: int = 82
    _description: str = "Raises defense\x01power!"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 15
    _magic_defense: int = 15
    _price: int = 150


class BtubRing(Accessory):
    """BtubRing item class"""

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

    _item_id: int = 84
    _description: str = "Prevents\x01poison damage"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 2
    _magic_defense: int = 2
    _status_immunities: List[Status] = [Status.POISON]
    _price: int = 28


class WakeUpPin(Accessory):
    """WakeUpPin item class"""

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


class FearlessPin(Accessory):
    """FearlessPin item class"""

    _item_id: int = 86
    _description: str = "Prevents Fear\x01attacks"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _defense: int = 5
    _magic_defense: int = 5
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 130


class TrueformPin(Accessory):
    """TrueformPin item class"""

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


class CoinTrick(Accessory):
    """CoinTrick item class"""

    _item_id: int = 88
    _description: str = "Doubles the\x01coins you win\x01in battle"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _price: int = 36
    _frog_coin_item: bool = True
    _arbitrary_value: UInt16 = UInt16(2)


class GhostMedal(Accessory):
    """GhostMedal item class"""

    _item_id: int = 89
    _description: str = "Raises defense\x01while attacking"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 1600


class JinxBelt(Accessory):
    """JinxBelt item class"""

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

    _item_id: int = 91
    _description: str = "Speed up by 20"
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _defense: int = 5
    _magic_defense: int = 5
    _price: int = 666


class TroopaPin(Accessory):
    """TroopaPin item class"""

    _item_id: int = 92
    _description: str = 'Grants "Troopa#\x01confidence!'
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 20
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 1000


class SignalRing(Accessory):
    """SignalRing item class"""

    _item_id: int = 93
    _description: str = "Noise indicates\x01a hidden chest."
    _equip_chars: List[PartyCharacter] = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]
    _speed: int = 10
    _price: int = 600


class QuartzCharm(Accessory):
    """QuartzCharm item class"""

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


class Mushroom(RegularItem):
    """Mushroom item class"""

    _item_id: int = 96
    _description: str = "Recovers 30 HP"
    _consumable: bool = True
    _price: int = 4


class MidMushroom(RegularItem):
    """MidMushroom item class"""

    _item_id: int = 97
    _description: str = "Recovers 80 HP"
    _consumable: bool = True
    _price: int = 20


class MaxMushroom(RegularItem):
    """MaxMushroom item class"""

    _item_id: int = 98
    _description: str = "Recovers all HP"
    _consumable: bool = True
    _price: int = 78


class HoneySyrup(RegularItem):
    """HoneySyrup item class"""

    _item_id: int = 99
    _description: str = "Recovers 10 FP"
    _consumable: bool = True
    _price: int = 10


class MapleSyrup(RegularItem):
    """MapleSyrup item class"""

    _item_id: int = 100
    _description: str = "Recovers 40 FP"
    _consumable: bool = True
    _price: int = 30


class RoyalSyrup(RegularItem):
    """RoyalSyrup item class"""

    _item_id: int = 101
    _description: str = "Recovers all FP"
    _consumable: bool = True
    _price: int = 101


class PickMeUp(RegularItem):
    """PickMeUp item class"""

    _item_id: int = 102
    _description: str = "Revives downed\x01allies"
    _consumable: bool = True
    _price: int = 5


class AbleJuice(RegularItem):
    """AbleJuice item class"""

    _item_id: int = 103
    _description: str = "Heal status\x01ailments"
    _consumable: bool = True
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


class Bracer(RegularItem):
    """Bracer item class"""

    _item_id: int = 104
    _description: str = "Raises ally~s\x01def. in battle"
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 50
    _frog_coin_item: bool = True
    _rank_value: int = 10


class Energizer(RegularItem):
    """Energizer item class"""

    _item_id: int = 105
    _description: str = "Raises ally~s\x01battle power\x01during battle"
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 50
    _frog_coin_item: bool = True


class YoshiAde(RegularItem):
    """YoshiAde item class"""

    _item_id: int = 106
    _description: str = "Power raised\x01during battle"
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 200


class RedEssence(RegularItem):
    """RedEssence item class"""

    _item_id: int = 107
    _description: str = "Become invincible\x01for 3 turns"
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.INVINCIBLE]
    _price: int = 400


class KerokeroCola(RegularItem):
    """KerokeroCola item class"""

    _item_id: int = 108
    _description: str = "All members\x01recover fully"
    _consumable: bool = True
    _price: int = 400


class YoshiCookie(RegularItem):
    """YoshiCookie item class"""

    _item_id: int = 109
    _description: str = "Summons Yoshi\x01during battle"
    _consumable: bool = True
    _price: int = 100


class PureWater(RegularItem):
    """PureWater item class"""

    _item_id: int = 110
    _description: str = "Defeats ghosts\x01in a wink"
    _consumable: bool = True
    _price: int = 150


class SleepyBomb(RegularItem):
    """SleepyBomb item class"""

    _item_name: str = "Sleepy Bomb"
    _item_id: int = 111
    _description: str = "Puts enemies\x01to sleep"
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.SLEEP]
    _price: int = 25
    _frog_coin_item: bool = True


class BadMushroom(RegularItem):
    """BadMushroom item class"""

    _item_name: str = "Bad Mushroom"
    _item_id: int = 112
    _description: str = "Poisons\x01an enemy"
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 30


class FireBomb(RegularItem):
    """FireBomb item class"""

    _item_name: str = "Fire Bomb"
    _item_id: int = 113
    _description: str = "Hit all\x01enemies w/fire"
    _consumable: bool = True
    _price: int = 200


class IceBomb(RegularItem):
    """IceBomb item class"""

    _item_name: str = "Ice Bomb"
    _item_id: int = 114
    _description: str = "Hit all\x01enemies w/ice"
    _consumable: bool = True
    _price: int = 250


class FlowerTab(RegularItem):
    """FlowerTab item class"""

    _item_id: int = 115
    _description: str = "Raise FP by 1"
    _consumable: bool = True
    _price: int = 200


class FlowerJar(RegularItem):
    """FlowerJar item class"""

    _item_id: int = 116
    _description: str = "Raise FP by 3"
    _consumable: bool = True
    _price: int = 600


class FlowerBox(RegularItem):
    """FlowerBox item class"""

    _item_id: int = 117
    _description: str = "Raise FP by 5"
    _consumable: bool = True
    _price: int = 1000


class YoshiCandy(RegularItem):
    """YoshiCandy item class"""

    _item_id: int = 118
    _description: str = "Heals 100 HP"
    _consumable: bool = True
    _price: int = 140


class FroggieDrink(RegularItem):
    """FroggieDrink item class"""

    _item_id: int = 119
    _description: str = "Party heals\x0130 HP"
    _consumable: bool = True
    _price: int = 16


class MukuCookie(RegularItem):
    """MukuCookie item class"""

    _item_id: int = 120
    _description: str = "Party heals\x0169 HP"
    _consumable: bool = True
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


class Elixir(RegularItem):
    """Elixir item class"""

    _item_id: int = 121
    _description: str = "Party heals\x0180 HP"
    _consumable: bool = True
    _price: int = 48


class Megalixir(RegularItem):
    """Megalixir item class"""

    _item_id: int = 122
    _description: str = "Party heals\x01150 HP"
    _consumable: bool = True
    _price: int = 120


class SeeYa(RegularItem):
    """SeeYa item class"""

    _item_id: int = 123
    _description: str = "Run away from\x01battles"
    _price: int = 250
    _frog_coin_item: bool = True


class TempleKey(RegularItem):
    """TempleKey item class"""

    _item_id: int = 124


class GoodieBag(RegularItem):
    """GoodieBag item class"""

    _item_id: int = 125
    _price: int = 1110
    _description: str = "It's packed\x01full of coins"


class EarlierTimes(RegularItem):
    """EarlierTimes item class"""

    _item_id: int = 126
    _description: str = "Use it to start\x01a battle over"
    _price: int = 375
    _frog_coin_item: bool = True


class FreshenUp(RegularItem):
    """FreshenUp item class"""

    _item_id: int = 127
    _description: str = "Heals party\x01status ailments"
    _consumable: bool = True
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


class RareFrogCoin(RegularItem):
    """RareFrogCoin item class"""

    _item_id: int = 128


class Wallet(RegularItem):
    """Wallet item class"""

    _item_id: int = 129
    _description: str = "A fat wallet"
    _price: int = 246


class CricketPie(RegularItem):
    """CricketPie item class"""

    _item_id: int = 130


class RockCandy(RegularItem):
    """RockCandy item class"""

    _item_name: str = "Rock Candy"
    _item_id: int = 131
    _description: str = "Attack all\x01enemies"
    _consumable: bool = True
    _price: int = 400


class CastleKey1(RegularItem):
    """CastleKey1 item class"""

    _item_id: int = 132


class CastleKey2(RegularItem):
    """CastleKey2 item class"""

    _item_id: int = 134


class BambinoBomb(RegularItem):
    """BambinoBomb item class"""

    _item_id: int = 135


class SheepAttack(RegularItem):
    """SheepAttack item class"""

    _item_id: int = 136
    _description: str = "Baah, baah..."
    _price: int = 150


class CarboCookie(RegularItem):
    """CarboCookie item class"""

    _item_id: int = 137
    _description: str = "Kid's love 'em"
    _price: int = 2


class ShinyStone(RegularItem):
    """ShinyStone item class"""

    _item_id: int = 138
    _description: str = "A pretty stone!"
    _price: int = 4


class RoomKey(RegularItem):
    """RoomKey item class"""

    _item_id: int = 140


class ElderKey(RegularItem):
    """ElderKey item class"""

    _item_id: int = 141


class ShedKey(RegularItem):
    """ShedKey item class"""

    _item_id: int = 142


class LambsLure(RegularItem):
    """LambsLure item class"""

    _item_id: int = 143
    _description: str = "Baa, baa..."
    _price: int = 40


class FrightBomb(RegularItem):
    """FrightBomb item class"""

    _item_name: str = "Fright Bomb"
    _item_id: int = 144
    _description: str = "Inflict fear\x01on one enemy"
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.FEAR]
    _price: int = 100


class MysteryEgg(RegularItem):
    """MysteryEgg item class"""

    _item_id: int = 145
    _description: str = "A product of\x01pure love..."
    _price: int = 200


class BeetleBox(RegularItem):
    """BeetleBox item class"""

    _item_id: int = 146


class BeetleBox2(RegularItem):
    """BeetleBox2 item class"""

    _item_id: int = 147


class LuckyJewel(RegularItem):
    """LuckyJewel item class"""

    _item_id: int = 148
    _description: str = "Summons Luck\x01at will"
    _price: int = 100


class SopranoCard(RegularItem):
    """SopranoCard item class"""

    _item_id: int = 150


class AltoCard(RegularItem):
    """AltoCard item class"""

    _item_id: int = 151


class TenorCard(RegularItem):
    """TenorCard item class"""

    _item_id: int = 152


class Crystalline(RegularItem):
    """Crystalline item class"""

    _item_id: int = 153
    _description: str = "Raises party's\x01Defense in\x01battle"
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.DEFENSE,
        TempStatBuff.MAGIC_DEFENSE,
    ]
    _price: int = 125
    _frog_coin_item: bool = True


class PowerBlast(RegularItem):
    """PowerBlast item class"""

    _item_id: int = 154
    _description: str = "Raises party's\x01Attack Power\x01in battle"
    _consumable: bool = True
    _temp_buffs: List[TempStatBuff] = [
        TempStatBuff.ATTACK,
        TempStatBuff.MAGIC_ATTACK,
    ]
    _price: int = 125
    _frog_coin_item: bool = True


class WiltShroom(RegularItem):
    """WiltShroom item class"""

    _item_id: int = 155
    _description: str = "It's wilted..."
    _consumable: bool = True
    _price: int = 8


class RottenMush(RegularItem):
    """RottenMush item class"""

    _item_id: int = 156
    _description: str = "Eeew,\x01it's rotten!"
    _consumable: bool = True
    _price: int = 4


class MoldyMush(RegularItem):
    """MoldyMush item class"""

    _item_id: int = 157
    _description: str = "Gross!\x01There's mold\x01growing on it."
    _consumable: bool = True
    _price: int = 2


class Seed(RegularItem):
    """Seed item class"""

    _item_id: int = 158


class Fertilizer(RegularItem):
    """Fertilizer item class"""

    _item_id: int = 159


class WasteBasket(RegularItem):
    """WasteBasket item class"""

    _item_id: int = 160


class BigBooFlag(RegularItem):
    """BigBooFlag item class"""

    _item_id: int = 161


class DryBonesFlag(RegularItem):
    """DryBonesFlag item class"""

    _item_id: int = 162


class GreaperFlag(RegularItem):
    """GreaperFlag item class"""

    _item_id: int = 163


class CricketJam(RegularItem):
    """CricketJam item class"""

    _item_id: int = 166


class Fireworks(RegularItem):
    """Fireworks item class"""

    _item_id: int = 172
    _description: str = "A gorgeous\x01firework"
    _price: int = 500


class BrightCard(RegularItem):
    """BrightCard item class"""

    _item_id: int = 174


class Mushroom2(RegularItem):
    """Mushroom2 item class"""

    _item_id: int = 175
    _description: str = "Recoers 30 HP,\x01but..."
    _consumable: bool = True
    _status_immunities: List[Status] = [Status.MUSHROOM]
    _price: int = 4


class StarEgg(RegularItem):
    """StarEgg item class"""

    _item_id: int = 176
    _description: str = "Reusable battle\x01item"
    _price: int = 700

