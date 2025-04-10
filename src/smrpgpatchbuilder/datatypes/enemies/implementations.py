"""Individual enemy class definitions."""

from typing import List, Optional, Type, Union
from smrpgpatchbuilder.datatypes.enemies.classes import (
    Enemy,
    ApproachSound,
    HitSound,
    FlowerBonusType,
)
from smrpgpatchbuilder.datatypes.items.classes import RegularItem
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status

from smrpgpatchbuilder.datatypes.items.implementations import (
    AbleJuice,
    BadMushroom,
    Bracer,
    Crystalline,
    Elixir,
    Energizer,
    FireBomb,
    FlowerBox,
    FlowerJar,
    FlowerTab,
    FreshenUp,
    FrightBomb,
    FroggieDrink,
    HoneySyrup,
    IceBomb,
    KerokeroCola,
    MapleSyrup,
    MaxMushroom,
    Megalixir,
    MidMushroom,
    MukuCookie,
    Mushroom,
    PickMeUp,
    PowerBlast,
    PureWater,
    RockCandy,
    RoyalSyrup,
    SleepyBomb,
)


class Terrapin(Enemy):
    """Terrapin enemy class"""

    _monster_id: int = 0

    # vital status
    _hp: int = 10
    _fp: int = 100
    _attack: int = 1
    _defense: int = 8
    _magic_defense: int = 1
    _speed: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # reward attributes
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc
    _palette = 16


class Spikey(Enemy):
    """Spikey enemy class"""

    _monster_id: int = 1

    # vital status
    _hp: int = 20
    _fp: int = 100
    _attack: int = 6
    _defense: int = 11
    _magic_attack: int = 4
    _magic_defense: int = 2
    _speed: int = 14

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element nullification
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 1
    _coins: int = 2
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.75
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc


class Skytroopa(Enemy):
    """Skytroopa enemy class"""

    _monster_id: int = 2

    # vital status
    _hp: int = 10
    _fp: int = 100
    _attack: int = 4
    _defense: int = 16
    _magic_attack: int = 6
    _magic_defense: int = 4
    _speed: int = 18
    _evade: int = 8

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _coins: int = 1
    _rare_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 60

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc


class MadMallet(Enemy):
    """MadMallet enemy class"""

    _monster_id: int = 3

    # vital status
    _hp: int = 200
    _fp: int = 100
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 34
    _magic_defense: int = 85
    _speed: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc



class Shaman(Enemy):
    """Shaman enemy class"""

    _monster_id: int = 4

    # vital status
    _hp: int = 150
    _fp: int = 100
    _attack: int = 92
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 9

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 17
    _coins: int = 4
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc


class Crook(Enemy):
    """Crook enemy class"""

    _monster_id: int = 5

    # vital status
    _hp: int = 38
    _fp: int = 100
    _attack: int = 35
    _defense: int = 32
    _magic_attack: int = 12
    _magic_defense: int = 25
    _speed: int = 22
    _evade: int = 40
    _magic_evade: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0

    # misc



class Goomba(Enemy):
    """Goomba enemy class"""

    _monster_id: int = 6

    # vital status
    _hp: int = 16
    _fp: int = 100
    _attack: int = 3
    _defense: int = 3
    _magic_attack: int = 1
    _magic_defense: int = 1
    _speed: int = 13

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc


class PiranhaPlant(Enemy):
    """PiranhaPlant enemy class"""

    _monster_id: int = 7

    # vital status
    _hp: int = 168
    _fp: int = 4
    _attack: int = 45
    _defense: int = 14
    _magic_attack: int = 20
    _magic_defense: int = 22
    _speed: int = 6

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 5
    _coins: int = 5
    _common_item_drop: "Type[RegularItem]" = MapleSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY


class Amanita(Enemy):
    """Amanita enemy class"""

    _monster_id: int = 8

    # vital status
    _hp: int = 52
    _fp: int = 100
    _attack: int = 35
    _defense: int = 30
    _magic_attack: int = 31
    _magic_defense: int = 18
    _speed: int = 12
    _evade: int = 10
    _magic_evade: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _rare_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = BadMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN

    # misc


class Goby(Enemy):
    """Goby enemy class"""

    _monster_id: int = 9

    # vital status
    _hp: int = 40
    _fp: int = 100
    _attack: int = 22
    _defense: int = 14
    _magic_attack: int = 2
    _magic_defense: int = 10
    _speed: int = 12
    _evade: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _coins: int = 2
    _common_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc


class Bloober(Enemy):
    """Bloober enemy class"""

    _monster_id: int = 10

    # vital status
    _hp: int = 130
    _fp: int = 100
    _attack: int = 80
    _defense: int = 36
    _magic_attack: int = 21
    _magic_defense: int = 16
    _speed: int = 23
    _evade: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.THUNDER]

    # rewards
    _xp: int = 12
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = MaxMushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 20

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PUNCH

    # misc


class BandanaRed(Enemy):
    """BandanaRed enemy class"""

    _monster_id: int = 11

    # vital status
    _hp: int = 120
    _fp: int = 100
    _attack: int = 78
    _defense: int = 60
    _magic_attack: int = 25
    _magic_defense: int = 25
    _speed: int = 20

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 18
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.PIERCE

    # misc



class Lakitu(Enemy):
    """Lakitu enemy class"""

    _monster_id: int = 12

    # vital status
    _hp: int = 124
    _fp: int = 100
    _attack: int = 45
    _defense: int = 43
    _magic_attack: int = 35
    _magic_defense: int = 40
    _speed: int = 28
    _evade: int = 13

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 10
    _coins: int = 3
    _rare_item_drop: "Type[RegularItem]" = MidMushroom
    _common_item_drop: "Type[RegularItem]" = MapleSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK

    # misc


class Birdy(Enemy):
    """Birdy enemy class"""

    _monster_id: int = 13

    # vital status
    _hp: int = 150
    _fp: int = 100
    _attack: int = 110
    _defense: int = 75
    _magic_attack: int = 55
    _magic_defense: int = 13
    _speed: int = 23
    _evade: int = 18

    # effect nullification
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 16
    _coins: int = 3
    _common_item_drop: "Type[RegularItem]" = Energizer
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc


class Pinwheel(Enemy):
    """Pinwheel enemy class"""

    _monster_id: int = 14

    # vital status
    _hp: int = 99
    _fp: int = 100
    _attack: int = 120
    _defense: int = 90
    _magic_attack: int = 70
    _magic_defense: int = 66
    _speed: int = 32
    _evade: int = 35

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 23
    _rare_item_drop: "Type[RegularItem]" = PickMeUp
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 30

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.JAB

    # misc


class Ratfunk(Enemy):
    """Ratfunk enemy class"""

    _monster_id: int = 15

    # vital status
    _hp: int = 32
    _fp: int = 100
    _attack: int = 20
    _defense: int = 14
    _magic_defense: int = 6
    _speed: int = 21
    _evade: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 6
    _common_item_drop: "Type[RegularItem]" = AbleJuice
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0

    # misc


class K9(Enemy):
    """K9 enemy class"""

    _monster_id: int = 16

    # vital status
    _hp: int = 30
    _fp: int = 100
    _attack: int = 13
    _defense: int = 13
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 19

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # other properties
    _morph_chance: float = 0.75

    # misc


class Magmite(Enemy):
    """Magmite enemy class"""

    _monster_id: int = 17

    # vital status
    _hp: int = 26
    _fp: int = 100
    _attack: int = 45
    _defense: int = 70
    _magic_attack: int = 3
    _magic_defense: int = 1
    _speed: int = 2

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 5
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc


class TheBigBoo(Enemy):
    """TheBigBoo enemy class"""

    _monster_id: int = 18

    # vital status
    _hp: int = 43
    _fp: int = 12
    _attack: int = 18
    _magic_attack: int = 18
    _magic_defense: int = 24
    _speed: int = 17
    _evade: int = 40

    # effect nullification
    _status_immunities: List[Status] = [Status.FEAR]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = FrightBomb
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _rare_item_drop: "Type[RegularItem]" = PureWater

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10

    # other properties
    _morph_chance: float = 0.75

    # misc


class DryBones(Enemy):
    """DryBones enemy class"""

    _monster_id: int = 19

    # vital status
    _fp: int = 100
    _attack: int = 74
    _magic_attack: int = 7
    _speed: int = 9

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 12
    _coins: int = 5
    _rare_item_drop: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = MaxMushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES

    # misc


class Greaper(Enemy):
    """Greaper enemy class"""

    _monster_id: int = 20

    # vital status
    _hp: int = 148
    _fp: int = 100
    _attack: int = 72
    _defense: int = 50
    _magic_attack: int = 40
    _magic_defense: int = 20
    _speed: int = 30
    _evade: int = 30
    _magic_evade: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 13
    _rare_item_drop: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 10

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE

    # misc


class Sparky(Enemy):
    """Sparky enemy class"""

    _monster_id: int = 21

    # vital status
    _hp: int = 120
    _fp: int = 12
    _attack: int = 40
    _defense: int = 1
    _magic_attack: int = 38
    _magic_defense: int = 50
    _speed: int = 19
    _evade: int = 6

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # rewards
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 70

    # other properties
    _morph_chance: float = 0.25
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY

    # misc


class Chomp(Enemy):
    """Chomp enemy class"""

    _monster_id: int = 22

    # vital status
    _hp: int = 100
    _fp: int = 100
    _attack: int = 60
    _defense: int = 65
    _magic_attack: int = 5
    _magic_defense: int = 31
    _speed: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _common_item_drop: "Type[RegularItem]" = Mushroom
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc


class Pandorite(Enemy):
    """Pandorite enemy class"""

    _monster_id: int = 23

    # vital status
    _hp: int = 300
    _fp: int = 50
    _attack: int = 30
    _defense: int = 20
    _magic_attack: int = 20
    _magic_defense: int = 20
    _speed: int = 1

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]

    # special status
    _ohko_immune: bool = True

    # rewards
    _xp: int = 20
    _coins: int = 30
    _rare_item_drop: "Type[RegularItem]" = FlowerJar
    _common_item_drop: "Type[RegularItem]" = FlowerJar
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # other properties
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc


class ShyRanger(Enemy):
    """ShyRanger enemy class"""

    _monster_id: int = 24

    # vital status
    _hp: int = 300
    _fp: int = 100
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 4
    _magic_defense: int = 10
    _speed: int = 43
    _evade: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
        Element.JUMP,
    ]

    # rewards
    _xp: int = 60
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = KerokeroCola

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.25

    # special status
    _ohko_immune: bool = True


class Bobomb(Enemy):
    """Bobomb enemy class"""

    _monster_id: int = 111

    # vital status
    _hp: int = 90
    _fp: int = 100
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _speed: int = 1

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _common_item_drop: "Type[RegularItem]" = PickMeUp
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # other properties
    _sound_on_hit: HitSound = HitSound.KNOCK

    # misc



class Spookum(Enemy):
    """Spookum enemy class"""

    _monster_id: int = 26

    # vital status
    _hp: int = 98
    _fp: int = 100
    _attack: int = 50
    _defense: int = 45
    _magic_attack: int = 32
    _magic_defense: int = 5
    _speed: int = 18

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 8
    _coins: int = 4
    _common_item_drop: "Type[RegularItem]" = MidMushroom
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.PUNCH

    # misc


class HammerBro(Enemy):
    """HammerBro enemy class"""

    _monster_id: int = 27

    # vital status
    _hp: int = 50
    _fp: int = 1
    _attack: int = 6
    _defense: int = 13
    _magic_attack: int = 6
    _magic_defense: int = 8
    _speed: int = 10
    _evade: int = 10

    # rewards
    _xp: int = 3
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = FlowerJar
    _common_item_drop: "Type[RegularItem]" = FlowerJar
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # other properties
    _sound_on_hit: HitSound = HitSound.KNOCK
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # special status
    _ohko_immune: bool = True

    # misc

    # boss shuffle attributes


class Buzzer(Enemy):
    """Buzzer enemy class"""

    _monster_id: int = 28

    # vital status
    _hp: int = 43
    _fp: int = 100
    _attack: int = 37
    _defense: int = 15
    _magic_attack: int = 4
    _magic_defense: int = 1
    _speed: int = 25
    _evade: int = 30

    # rewards
    _xp: int = 4
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 70

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc


class Ameboid(Enemy):
    """Ameboid enemy class"""

    _monster_id: int = 29

    # vital status
    _hp: int = 220
    _fp: int = 100
    _attack: int = 130
    _defense: int = 1
    _magic_attack: int = 30
    _magic_defense: int = 120
    _speed: int = 1
    _magic_evade: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 10
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = MaxMushroom

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA

    # misc


class Gecko(Enemy):
    """Gecko enemy class"""

    _monster_id: int = 30

    # vital status
    _hp: int = 92
    _fp: int = 100
    _attack: int = 68
    _defense: int = 46
    _magic_attack: int = 9
    _magic_defense: int = 32
    _speed: int = 22
    _evade: int = 14

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = FroggieDrink

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PUNCH

    # misc


class Wiggler(Enemy):
    """Wiggler enemy class"""

    _monster_id: int = 31

    # vital status
    _hp: int = 120
    _fp: int = 100
    _attack: int = 40
    _defense: int = 25
    _magic_attack: int = 18
    _magic_defense: int = 20
    _speed: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 10
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH

    # misc


class Crusty(Enemy):
    """Crusty enemy class"""

    _monster_id: int = 32

    # vital status
    _hp: int = 80
    _fp: int = 100
    _attack: int = 100
    _defense: int = 100
    _magic_attack: int = 12
    _magic_defense: int = 35
    _speed: int = 6

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 25
    _coins: int = 7
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # other properties
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc


class Kamek(Enemy):
    """Kamek enemy class"""

    _monster_id: int = 33

    # vital status
    _hp: int = 1600
    _fp: int = 250
    _attack: int = 100
    _defense: int = 60
    _magic_attack: int = 120
    _magic_defense: int = 100
    _speed: int = 12

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # other properties
    _sound_on_hit: HitSound = HitSound.PIERCE

    # rewards
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # special status
    _ohko_immune: bool = True

    # misc

    # boss shuffle attributes


class Leuko(Enemy):
    """Leuko enemy class"""

    _monster_id: int = 34

    # vital status
    _hp: int = 220
    _fp: int = 100
    _attack: int = 65
    _defense: int = 50
    _magic_attack: int = 42
    _magic_defense: int = 60
    _speed: int = 3
    _magic_evade: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 20
    _coins: int = 3
    _rare_item_drop: "Type[RegularItem]" = MidMushroom
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _yoshi_cookie_item: "Type[RegularItem]" = Megalixir

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60

    # other properties
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SLAP

    # misc


class Jawful(Enemy):
    """Jawful enemy class"""

    _monster_id: int = 35

    # vital status
    _hp: int = 278
    _fp: int = 100
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 8
    _magic_defense: int = 12
    _speed: int = 200

    # effect nullification
    _status_immunities: List[Status] = [Status.FEAR]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 27
    _yoshi_cookie_item: "Type[RegularItem]" = RockCandy
    _rare_item_drop: "Type[RegularItem]" = SleepyBomb

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # other properties
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW

    # misc


class Enigma(Enemy):
    """Enigma enemy class"""

    _monster_id: int = 36
    _hp: int = 150
    _speed: int = 25
    _attack: int = 55
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _fp: int = 100
    _evade: int = 20
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 5
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _common_item_drop: "Type[RegularItem]" = MapleSyrup


class Blaster(Enemy):
    """Blaster enemy class"""

    _monster_id: int = 37
    _hp: int = 120
    _speed: int = 1
    _attack: int = 70
    _defense: int = 70
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 0.75
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 0

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = FrightBomb
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Guerrilla(Enemy):
    """Guerrilla enemy class"""

    _monster_id: int = 38
    _hp: int = 135
    _speed: int = 7
    _attack: int = 42
    _defense: int = 32
    _magic_attack: int = 1
    _magic_defense: int = 5
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Babayaga(Enemy):
    """Babayaga enemy class"""

    _monster_id: int = 39
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Hobgoblin(Enemy):
    """Hobgoblin enemy class"""

    _monster_id: int = 40
    _hp: int = 50
    _speed: int = 5
    _attack: int = 22
    _defense: int = 22
    _magic_attack: int = 8
    _magic_defense: int = 12
    _fp: int = 8
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = PureWater
    _rare_item_drop: "Type[RegularItem]" = PureWater


class Reacher(Enemy):
    """Reacher enemy class"""

    _monster_id: int = 41
    _hp: int = 184
    _speed: int = 3
    _attack: int = 95
    _defense: int = 75
    _magic_attack: int = 8
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Shogun(Enemy):
    """Shogun enemy class"""

    _monster_id: int = 42
    _hp: int = 150
    _speed: int = 12
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 1
    _magic_defense: int = 32
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.JAB
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = [
        Status.FEAR,
        Status.SLEEP,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 24
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Orbuser(Enemy):
    """Orbuser enemy class"""

    _monster_id: int = 43
    _hp: int = 8
    _speed: int = 15
    _attack: int = 42
    _defense: int = 80
    _magic_attack: int = 28
    _magic_defense: int = 40
    _fp: int = 20
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    # rewards
    _xp: int = 5
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class HeavyTroopa(Enemy):
    """HeavyTroopa enemy class"""

    _monster_id: int = 44
    _hp: int = 250
    _speed: int = 3
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 1
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 2
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 32
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _common_item_drop: "Type[RegularItem]" = Crystalline


class Shadow(Enemy):
    """Shadow enemy class"""

    _monster_id: int = 45
    _hp: int = 85
    _speed: int = 18
    _attack: int = 24
    _defense: int = 5
    _magic_attack: int = 20
    _magic_defense: int = 20
    _fp: int = 14
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class Cluster(Enemy):
    """Cluster enemy class"""

    _monster_id: int = 46
    _hp: int = 60
    _speed: int = 20
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 21
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 8
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Bahamutt(Enemy):
    """Bahamutt enemy class"""

    _monster_id: int = 47
    _hp: int = 500
    _speed: int = 8
    _attack: int = 170
    _defense: int = 100
    _magic_attack: int = 80
    _magic_defense: int = 20
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Octolot(Enemy):
    """Octolot enemy class"""

    _monster_id: int = 48
    _hp: int = 99
    _speed: int = 3
    _attack: int = 38
    _defense: int = 27
    _magic_attack: int = 25
    _magic_defense: int = 30
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = HoneySyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class Frogog(Enemy):
    """Frogog enemy class"""

    _monster_id: int = 49
    _hp: int = 80
    _speed: int = 8
    _attack: int = 15
    _defense: int = 8
    _magic_defense: int = 8
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Clerk(Enemy):
    """Clerk enemy class"""

    _monster_id: int = 50
    _hp: int = 500
    _speed: int = 15
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 47
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 50
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes

    # shuffled overworld sprites
    sprite_width = 60
    sprite_height = 58



class Gunyolk(Enemy):
    """Gunyolk enemy class"""

    _monster_id: int = 51
    _hp: int = 1500
    _speed: int = 25
    _attack: int = 200
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80
    sprite_width = 71
    sprite_height = 63

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE, Element.THUNDER]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 100
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Boomer(Enemy):
    """Boomer enemy class"""

    _monster_id: int = 52
    _hp: int = 2000
    _speed: int = 18
    _attack: int = 200
    _defense: int = 140
    _magic_attack: int = 35
    _magic_defense: int = 26
    _fp: int = 200
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 55
    _coins: int = 9
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes

    # shuffled overworld sprites
    sprite_width = 52
    sprite_width = 49


class Remocon(Enemy):
    """Remocon enemy class"""

    _monster_id: int = 53
    _hp: int = 88
    _speed: int = 5
    _attack: int = 56
    _defense: int = 52
    _magic_attack: int = 25
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.ICE, Element.THUNDER]

    # rewards
    _xp: int = 8
    _coins: int = 7
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _common_item_drop: "Type[RegularItem]" = HoneySyrup


class Snapdragon(Enemy):
    """Snapdragon enemy class"""

    _monster_id: int = 54
    _hp: int = 90
    _speed: int = 4
    _attack: int = 28
    _defense: int = 25
    _magic_attack: int = 31
    _magic_defense: int = 25
    _fp: int = 100
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.SLAP
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Stumpet(Enemy):
    """Stumpet enemy class"""

    _monster_id: int = 55
    _hp: int = 500
    _speed: int = 1
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 6
    _magic_defense: int = 60
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 70
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _common_item_drop: "Type[RegularItem]" = FireBomb
    _rare_item_drop: "Type[RegularItem]" = FrightBomb


class Dodo(Enemy):
    """Dodo enemy class"""

    _monster_id: int = 56
    _hp: int = 1000
    _speed: int = 10
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 9
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 2

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Jester(Enemy):
    """Jester enemy class"""

    _monster_id: int = 57
    _hp: int = 151
    _speed: int = 20
    _attack: int = 48
    _defense: int = 35
    _magic_attack: int = 22
    _magic_defense: int = 35
    _fp: int = 12
    _magic_evade: int = 80
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup


class Artichoker(Enemy):
    """Artichoker enemy class"""

    _monster_id: int = 58
    _hp: int = 200
    _speed: int = 7
    _attack: int = 50
    _defense: int = 54
    _magic_attack: int = 27
    _magic_defense: int = 24
    _fp: int = 100
    _magic_evade: int = 20
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 12
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom
    _rare_item_drop: "Type[RegularItem]" = FrightBomb


class Arachne(Enemy):
    """Arachne enemy class"""

    _monster_id: int = 59
    _hp: int = 82
    _speed: int = 14
    _attack: int = 35
    _defense: int = 35
    _magic_attack: int = 6
    _fp: int = 100
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _common_item_drop: "Type[RegularItem]" = AbleJuice


class Carriboscis(Enemy):
    """Carriboscis enemy class"""

    _monster_id: int = 60
    _hp: int = 90
    _speed: int = 30
    _attack: int = 55
    _defense: int = 44
    _magic_attack: int = 28
    _magic_defense: int = 22
    _fp: int = 100
    _evade: int = 13
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Hippopo(Enemy):
    """Hippopo enemy class"""

    _monster_id: int = 61
    _hp: int = 400
    _speed: int = 6
    _attack: int = 150
    _defense: int = 110
    _magic_attack: int = 85
    _magic_defense: int = 53
    _fp: int = 100
    _magic_evade: int = 15
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 80
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Megalixir
    _common_item_drop: "Type[RegularItem]" = RockCandy


class Mastadoom(Enemy):
    """Mastadoom enemy class"""

    _monster_id: int = 62
    _hp: int = 180
    _speed: int = 3
    _attack: int = 90
    _defense: int = 65
    _magic_attack: int = 30
    _magic_defense: int = 50
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _resistances: List[Element] = [Element.THUNDER]

    # element resistances
    _weaknesses: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _rare_item_drop: "Type[RegularItem]" = MidMushroom


class Corkpedite(Enemy):
    """Corkpedite enemy class"""

    _monster_id: int = 63
    _hp: int = 200
    _speed: int = 5
    _attack: int = 130
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 20
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _rare_item_drop: "Type[RegularItem]" = FrightBomb


class Terracotta(Enemy):
    """Terracotta enemy class"""

    _monster_id: int = 64
    _hp: int = 180
    _speed: int = 23
    _attack: int = 120
    _defense: int = 85
    _magic_attack: int = 36
    _magic_defense: int = 35
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 25
    _yoshi_cookie_item: "Type[RegularItem]" = MidMushroom
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Spikester(Enemy):
    """Spikester enemy class"""

    _monster_id: int = 65
    _hp: int = 50
    _speed: int = 19
    _attack: int = 48
    _defense: int = 60
    _magic_attack: int = 12
    _magic_defense: int = 4
    _fp: int = 100
    _morph_chance: float = 0.75
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 6
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer


class Malakoopa(Enemy):
    """Malakoopa enemy class"""

    _monster_id: int = 66
    _hp: int = 95
    _speed: int = 35
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 47
    _magic_defense: int = 98
    _fp: int = 100
    _evade: int = 20
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 60

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 23
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class Pounder(Enemy):
    """Pounder enemy class"""

    _monster_id: int = 67
    _hp: int = 180
    _speed: int = 25
    _attack: int = 130
    _defense: int = 70
    _magic_attack: int = 45
    _magic_defense: int = 60
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 24
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer



class Poundette(Enemy):
    """Poundette enemy class"""

    _monster_id: int = 68
    _hp: int = 150
    _speed: int = 30
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 28
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer



class Sackit(Enemy):
    """Sackit enemy class"""

    _monster_id: int = 69
    _hp: int = 152
    _speed: int = 26
    _attack: int = 70
    _defense: int = 53
    _magic_attack: int = 13
    _magic_defense: int = 20
    _fp: int = 100
    _evade: int = 20
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = MaxMushroom
    _common_item_drop: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class GuGoomba(Enemy):
    """GuGoomba enemy class"""

    _monster_id: int = 70
    _hp: int = 132
    _speed: int = 14
    _attack: int = 115
    _defense: int = 66
    _magic_attack: int = 13
    _magic_defense: int = 66
    _fp: int = 100
    _magic_evade: int = 50
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 15
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = FroggieDrink
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class Chewy(Enemy):
    """Chewy enemy class"""

    _monster_id: int = 71
    _hp: int = 90
    _speed: int = 6
    _attack: int = 110
    _defense: int = 82
    _magic_attack: int = 70
    _magic_defense: int = 52
    _fp: int = 100
    _magic_evade: int = 50
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 14
    _yoshi_cookie_item: "Type[RegularItem]" = BadMushroom
    _common_item_drop: "Type[RegularItem]" = SleepyBomb


class Fireball(Enemy):
    """Fireball enemy class"""

    _monster_id: int = 72
    _hp: int = 10
    _speed: int = 42
    _attack: int = 55
    _defense: int = 16
    _magic_attack: int = 30
    _magic_defense: int = 16
    _fp: int = 100
    _evade: int = 50
    _magic_evade: int = 30
    _morph_chance: float = 0.25
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class MrKipper(Enemy):
    """MrKipper enemy class"""

    _monster_id: int = 73
    _hp: int = 133
    _speed: int = 23
    _attack: int = 75
    _defense: int = 45
    _magic_attack: int = 14
    _magic_defense: int = 10
    _fp: int = 100
    _evade: int = 13
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 70

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 8
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = AbleJuice


class FactoryChief(Enemy):
    """FactoryChief enemy class"""

    _monster_id: int = 74
    _hp: int = 1000
    _speed: int = 45
    _attack: int = 200
    _defense: int = 120
    _magic_attack: int = 70
    _magic_defense: int = 90
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 80
    _coins: int = 90
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes


class BandanaBlue(Enemy):
    """BandanaBlue enemy class"""

    _monster_id: int = 75
    _hp: int = 150
    _speed: int = 30
    _attack: int = 80
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 30
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Manager(Enemy):
    """Manager enemy class"""

    _monster_id: int = 76
    _hp: int = 800
    _speed: int = 25
    _attack: int = 170
    _defense: int = 110
    _magic_attack: int = 60
    _magic_defense: int = 70
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _coins: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Bluebird(Enemy):
    """Bluebird enemy class"""

    _monster_id: int = 77
    _hp: int = 200
    _speed: int = 29
    _attack: int = 95
    _defense: int = 50
    _magic_attack: int = 80
    _magic_defense: int = 94
    _fp: int = 100
    _evade: int = 8
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 100

    # rewards
    _xp: int = 14
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _common_item_drop: "Type[RegularItem]" = Bracer


class AlleyRat(Enemy):
    """AlleyRat enemy class"""

    _monster_id: int = 79
    _hp: int = 105
    _speed: int = 21
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 13
    _magic_defense: int = 12
    _fp: int = 100
    _evade: int = 15
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # rewards
    _xp: int = 9
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = Mushroom

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []


class Chow(Enemy):
    """Chow enemy class"""

    _monster_id: int = 80
    _hp: int = 80
    _speed: int = 27
    _attack: int = 82
    _defense: int = 77
    _magic_attack: int = 8
    _magic_defense: int = 28
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 15
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = FrightBomb


class Magmus(Enemy):
    """Magmus enemy class"""

    _monster_id: int = 81
    _hp: int = 50
    _speed: int = 6
    _attack: int = 110
    _defense: int = 140
    _magic_attack: int = 3
    _magic_defense: int = 25
    _fp: int = 100
    _magic_evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # rewards
    _xp: int = 18
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _rare_item_drop: "Type[RegularItem]" = Bracer


class LilBoo(Enemy):
    """LilBoo enemy class"""

    _monster_id: int = 82
    _hp: int = 66
    _speed: int = 27
    _attack: int = 120
    _defense: int = 20
    _magic_attack: int = 74
    _magic_defense: int = 120
    _fp: int = 100
    _evade: int = 50
    _magic_evade: int = 20
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 10

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 28
    _yoshi_cookie_item: "Type[RegularItem]" = FreshenUp


class Vomer(Enemy):
    """Vomer enemy class"""

    _monster_id: int = 83
    _speed: int = 10
    _attack: int = 110
    _magic_attack: int = 9
    _fp: int = 100
    _magic_evade: int = 5
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.BONK
    _sound_on_approach: ApproachSound = ApproachSound.DRY_BONES

    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 19
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _rare_item_drop: "Type[RegularItem]" = PureWater


class GlumReaper(Enemy):
    """GlumReaper enemy class"""

    _monster_id: int = 84
    _hp: int = 180
    _speed: int = 35
    _attack: int = 120
    _defense: int = 55
    _magic_attack: int = 60
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 20
    _magic_evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 35
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = PureWater


class Pyrosphere(Enemy):
    """Pyrosphere enemy class"""

    _monster_id: int = 85
    _hp: int = 167
    _speed: int = 24
    _attack: int = 105
    _defense: int = 66
    _magic_attack: int = 100
    _magic_defense: int = 48
    _fp: int = 100
    _evade: int = 7
    _morph_chance: float = 0.25
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.POISON]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 70

    # rewards
    _xp: int = 17
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = FireBomb


class ChompChomp(Enemy):
    """ChompChomp enemy class"""

    _monster_id: int = 86
    _hp: int = 150
    _speed: int = 10
    _attack: int = 100
    _defense: int = 92
    _magic_attack: int = 14
    _magic_defense: int = 30
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 12
    _coins: int = 5
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = Crystalline


class Hidon(Enemy):
    """Hidon enemy class"""

    _monster_id: int = 87
    _hp: int = 600
    _speed: int = 1
    _attack: int = 110
    _defense: int = 90
    _magic_attack: int = 60
    _magic_defense: int = 30
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    # xp = 50
    _xp: int = 42
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class SlingShy(Enemy):
    """SlingShy enemy class"""

    _monster_id: int = 88
    _hp: int = 120
    _speed: int = 16
    _attack: int = 108
    _defense: int = 80
    _magic_attack: int = 42
    _magic_defense: int = 21
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 3
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []


class Robomb(Enemy):
    """Robomb enemy class"""

    _monster_id: int = 89
    _hp: int = 42
    _speed: int = 2
    _attack: int = 54
    _defense: int = 63
    _magic_attack: int = 1
    _magic_defense: int = 20
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 6
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class ShyGuy(Enemy):
    """ShyGuy enemy class"""

    _monster_id: int = 90
    _hp: int = 78
    _speed: int = 14
    _attack: int = 29
    _defense: int = 30
    _magic_attack: int = 20
    _magic_defense: int = 6
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup



class Ninja(Enemy):
    """Ninja enemy class"""

    _monster_id: int = 91
    _hp: int = 235
    _speed: int = 28
    _attack: int = 130
    _defense: int = 76
    _magic_attack: int = 51
    _magic_defense: int = 67
    _fp: int = 100
    _evade: int = 30
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
    ]

    # rewards
    _xp: int = 32
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = PowerBlast
    _common_item_drop: "Type[RegularItem]" = MapleSyrup


class Stinger(Enemy):
    """Stinger enemy class"""

    _monster_id: int = 92
    _hp: int = 65
    _speed: int = 33
    _attack: int = 78
    _defense: int = 80
    _magic_attack: int = 23
    _magic_defense: int = 10
    _fp: int = 100
    _evade: int = 25
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 70

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 13
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = AbleJuice
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Goombette(Enemy):
    """Goombette enemy class"""

    _monster_id: int = 93
    _hp: int = 100
    _speed: int = 16
    _attack: int = 90
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 30
    _fp: int = 100
    _evade: int = 20
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    # made this up
    _xp: int = 2

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes


class Geckit(Enemy):
    """Geckit enemy class"""

    _monster_id: int = 94
    _hp: int = 100
    _speed: int = 25
    _attack: int = 84
    _defense: int = 63
    _magic_attack: int = 20
    _magic_defense: int = 8
    _fp: int = 100
    _evade: int = 14
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PUNCH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 18
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _rare_item_drop: "Type[RegularItem]" = AbleJuice


class Jabit(Enemy):
    """Jabit enemy class"""

    _monster_id: int = 95
    _hp: int = 150
    _speed: int = 13
    _attack: int = 120
    _defense: int = 95
    _magic_attack: int = 27
    _magic_defense: int = 34
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 18
    _yoshi_cookie_item: "Type[RegularItem]" = Bracer
    _common_item_drop: "Type[RegularItem]" = PickMeUp


class Starcruster(Enemy):
    """Starcruster enemy class"""

    _monster_id: int = 96
    _hp: int = 72
    _speed: int = 11
    _attack: int = 135
    _defense: int = 145
    _magic_attack: int = 16
    _magic_defense: int = 53
    _fp: int = 100
    _magic_evade: int = 10
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 36
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _common_item_drop: "Type[RegularItem]" = Crystalline


class Merlin(Enemy):
    """Merlin enemy class"""

    _monster_id: int = 97
    _hp: int = 169
    _speed: int = 20
    _attack: int = 124
    _defense: int = 63
    _magic_attack: int = 90
    _magic_defense: int = 130
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 50
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Muckle(Enemy):
    """Muckle enemy class"""

    _monster_id: int = 98
    _hp: int = 320
    _speed: int = 2
    _attack: int = 90
    _defense: int = 44
    _magic_attack: int = 90
    _magic_defense: int = 44
    _fp: int = 100
    _evade: int = 1
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.SLAP
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 60

    # rewards
    _xp: int = 6
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = IceBomb
    _common_item_drop: "Type[RegularItem]" = IceBomb


class Forkies(Enemy):
    """Forkies enemy class"""

    _monster_id: int = 99
    _hp: int = 350
    _speed: int = 200
    _attack: int = 170
    _defense: int = 120
    _magic_attack: int = 45
    _magic_defense: int = 128
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 32
    _coins: int = 7
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _rare_item_drop: "Type[RegularItem]" = SleepyBomb


class Gorgon(Enemy):
    """Gorgon enemy class"""

    _monster_id: int = 100
    _hp: int = 140
    _speed: int = 16
    _attack: int = 86
    _defense: int = 73
    _magic_attack: int = 24
    _magic_defense: int = 52
    _fp: int = 100
    _evade: int = 11
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 30

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = MidMushroom


class BigBertha(Enemy):
    """BigBertha enemy class"""

    _monster_id: int = 101
    _hp: int = 350
    _speed: int = 1
    _attack: int = 170
    _defense: int = 130
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 35
    _coins: int = 7
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp


class ChainedKong(Enemy):
    """ChainedKong enemy class"""

    _monster_id: int = 102
    _hp: int = 355
    _speed: int = 17
    _attack: int = 150
    _defense: int = 80
    _magic_attack: int = 22
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.GUERRILLA
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 35
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class Fautso(Enemy):
    """Fautso enemy class"""

    _monster_id: int = 103
    _hp: int = 420
    _speed: int = 14
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 60
    _magic_defense: int = 60
    _fp: int = 100
    _evade: int = 10
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.THUNDER, Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.FEAR,
        Status.POISON,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Strawhead(Enemy):
    """Strawhead enemy class"""

    _monster_id: int = 104
    _hp: int = 131
    _speed: int = 9
    _attack: int = 80
    _defense: int = 63
    _magic_attack: int = 18
    _magic_defense: int = 12
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 17
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = PureWater
    _common_item_drop: "Type[RegularItem]" = PureWater
    _rare_item_drop: "Type[RegularItem]" = PureWater


class Juju(Enemy):
    """Juju enemy class"""

    _monster_id: int = 105
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class ArmoredAnt(Enemy):
    """ArmoredAnt enemy class"""

    _monster_id: int = 106
    _hp: int = 230
    _speed: int = 12
    _attack: int = 130
    _defense: int = 120
    _magic_attack: int = 24
    _magic_defense: int = 80
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.JAB
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = [Element.FIRE]

    # rewards
    _xp: int = 30
    _coins: int = 5
    _yoshi_cookie_item: "Type[RegularItem]" = PowerBlast
    _common_item_drop: "Type[RegularItem]" = PowerBlast


class Orbison(Enemy):
    """Orbison enemy class"""

    _monster_id: int = 107
    _hp: int = 30
    _speed: int = 25
    _attack: int = 113
    _defense: int = 140
    _magic_attack: int = 63
    _magic_defense: int = 65
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.JUMP]

    # element resistances
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]

    # rewards
    _xp: int = 18
    _yoshi_cookie_item: "Type[RegularItem]" = RoyalSyrup
    _common_item_drop: "Type[RegularItem]" = PureWater


class TuboTroopa(Enemy):
    """TuboTroopa enemy class"""

    _monster_id: int = 108
    _hp: int = 500
    _speed: int = 5
    _attack: int = 200
    _defense: int = 80
    _magic_attack: int = 7
    _magic_defense: int = 34
    _fp: int = 100
    _evade: int = 1
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 90

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.THUNDER]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 40
    _coins: int = 11
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir
    _common_item_drop: "Type[RegularItem]" = RockCandy


class Doppel(Enemy):
    """Doppel enemy class"""

    _monster_id: int = 109
    _hp: int = 333
    _speed: int = 40
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 44
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 19
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 40
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = PureWater


class Pulsar(Enemy):
    """Pulsar enemy class"""

    _monster_id: int = 110
    _hp: int = 69
    _speed: int = 8
    _attack: int = 75
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 35
    _fp: int = 100
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.PULSAR
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.JUMP]

    # rewards
    _xp: int = 15
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = PickMeUp
    _rare_item_drop: "Type[RegularItem]" = PickMeUp


class Octovader(Enemy):
    """Octovader enemy class"""

    _monster_id: int = 112
    _hp: int = 250
    _speed: int = 5
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 63
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 9
    _magic_evade: int = 8
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.DEEP_KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 30
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = FroggieDrink
    _common_item_drop: "Type[RegularItem]" = PowerBlast


class Ribbite(Enemy):
    """Ribbite enemy class"""

    _monster_id: int = 113
    _hp: int = 250
    _speed: int = 15
    _attack: int = 115
    _defense: int = 20
    _magic_attack: int = 31
    _magic_defense: int = 29
    _fp: int = 100
    _morph_chance: float = 1.0
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.FEAR]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 22
    _coins: int = 8
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir
    _common_item_drop: "Type[RegularItem]" = Elixir


class Director(Enemy):
    """Director enemy class"""

    _monster_id: int = 114
    _hp: int = 1000
    _speed: int = 35
    _attack: int = 190
    _defense: int = 120
    _magic_attack: int = 57
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 70
    _coins: int = 80
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Puppox(Enemy):
    """Puppox enemy class"""

    _monster_id: int = 117
    _hp: int = 300
    _speed: int = 9
    _attack: int = 145
    _defense: int = 110
    _magic_attack: int = 20
    _magic_defense: int = 32
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = [Element.THUNDER]

    # rewards
    _xp: int = 30
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = RockCandy
    _rare_item_drop: "Type[RegularItem]" = FreshenUp


class FinkFlower(Enemy):
    """FinkFlower enemy class"""

    _monster_id: int = 118
    _hp: int = 200
    _speed: int = 4
    _attack: int = 95
    _defense: int = 32
    _magic_attack: int = 63
    _magic_defense: int = 90
    _fp: int = 100
    _magic_evade: int = 12
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SLAP
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = [Element.FIRE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = MaxMushroom
    _rare_item_drop: "Type[RegularItem]" = MidMushroom


class Lumbler(Enemy):
    """Lumbler enemy class"""

    _monster_id: int = 119
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Springer(Enemy):
    """Springer enemy class"""

    _monster_id: int = 120
    _hp: int = 122
    _speed: int = 16
    _attack: int = 155
    _defense: int = 110
    _magic_attack: int = 100
    _magic_defense: int = 79
    _fp: int = 100
    _evade: int = 30
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 29
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Elixir
    _rare_item_drop: "Type[RegularItem]" = Energizer


class Harlequin(Enemy):
    """Harlequin enemy class"""

    _monster_id: int = 121
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Kriffid(Enemy):
    """Kriffid enemy class"""

    _monster_id: int = 122
    _hp: int = 320
    _speed: int = 8
    _attack: int = 95
    _defense: int = 100
    _magic_attack: int = 50
    _magic_defense: int = 40
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.POISON]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 35
    _coins: int = 6
    _yoshi_cookie_item: "Type[RegularItem]" = Crystalline
    _common_item_drop: "Type[RegularItem]" = BadMushroom


class Spinthra(Enemy):
    """Spinthra enemy class"""

    _monster_id: int = 123
    _hp: int = 230
    _speed: int = 19
    _attack: int = 110
    _defense: int = 70
    _magic_attack: int = 4
    _magic_defense: int = 32
    _fp: int = 100
    _morph_chance: float = 0.25
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = [Status.POISON]

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = PowerBlast
    _rare_item_drop: "Type[RegularItem]" = Bracer


class Radish(Enemy):
    """Radish enemy class"""

    _monster_id: int = 124
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.PIERCE
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Crippo(Enemy):
    """Crippo enemy class"""

    _monster_id: int = 125
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class MastaBlasta(Enemy):
    """MastaBlasta enemy class"""

    _monster_id: int = 126
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Piledriver(Enemy):
    """Piledriver enemy class"""

    _monster_id: int = 127
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Apprentice(Enemy):
    """Apprentice enemy class"""

    _monster_id: int = 128
    _hp: int = 120
    _speed: int = 20
    _attack: int = 50
    _defense: int = 50
    _magic_attack: int = 20
    _magic_defense: int = 20
    _fp: int = 32
    _sound_on_hit: HitSound = HitSound.PUNCH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _coins: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb
    _common_item_drop: "Type[RegularItem]" = MidMushroom


class BoxBoy(Enemy):
    """BoxBoy enemy class"""

    _monster_id: int = 134
    _hp: int = 900
    _speed: int = 1
    _attack: int = 180
    _defense: int = 110
    _magic_attack: int = 80
    _magic_defense: int = 40
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 100
    _coins: int = 150
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Shelly(Enemy):
    """Shelly enemy class"""

    _monster_id: int = 135
    _hp: int = 500
    _defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes

    # Specific to Shelly

    _position: int = 1
    _vanilla: bool = True
    _summons: List[int] = [0x28]
    _summon_event: Optional[int] = None

class Superspike(Enemy):
    """Superspike enemy class"""

    _monster_id: int = 136
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class DodoSolo(Enemy):
    """DodoSolo enemy class"""

    _monster_id: int = 137
    _hp: int = 800
    _speed: int = 10
    _attack: int = 140
    _defense: int = 100
    _magic_attack: int = 9
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 70
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Oerlikon(Enemy):
    """Oerlikon enemy class"""

    _monster_id: int = 138
    _hp: int = 85
    _speed: int = 20
    _attack: int = 120
    _defense: int = 125
    _magic_attack: int = 17
    _magic_defense: int = 50
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 22
    _yoshi_cookie_item: "Type[RegularItem]" = Energizer
    _rare_item_drop: "Type[RegularItem]" = Energizer


class Chester(Enemy):
    """Chester enemy class"""

    _monster_id: int = 139
    _hp: int = 1200
    _speed: int = 1
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 120
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.FIRE,
        Element.THUNDER,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 150
    _coins: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class CorkpediteBody(Enemy):
    """CorkpediteBody enemy class"""

    _monster_id: int = 140
    _hp: int = 300
    _speed: int = 5
    _attack: int = 100
    _defense: int = 99
    _magic_attack: int = 6
    _magic_defense: int = 1
    _fp: int = 100
    _morph_chance: float = 1.0
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Torte(Enemy):
    """Torte enemy class"""

    _monster_id: int = 142
    _hp: int = 100
    _speed: int = 99
    _attack: int = 60
    _defense: int = 50
    _magic_attack: int = 8
    _magic_defense: int = 27
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.TORTE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    # made this up
    _xp: int = 3

    # boss shuffle attributes


class Shyaway(Enemy):
    """Shyaway enemy class"""

    _monster_id: int = 143
    _hp: int = 140
    _speed: int = 25
    _attack: int = 90
    _defense: int = 50
    _magic_attack: int = 39
    _magic_defense: int = 73
    _fp: int = 100
    _evade: int = 40
    _morph_chance: float = 1.0
    _sound_on_approach: ApproachSound = ApproachSound.SPARKY_GOOMBA_BIRDY
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 100

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = [Element.ICE]

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = MapleSyrup
    _rare_item_drop: "Type[RegularItem]" = HoneySyrup


class JinxClone(Enemy):
    """JinxClone enemy class"""

    _monster_id: int = 144
    _hp: int = 320
    _speed: int = 22
    _attack: int = 180
    _defense: int = 120
    _magic_defense: int = 35
    _evade: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class MachineMadeShyster(Enemy):
    """MachineMadeShyster enemy class"""

    _monster_id: int = 145
    _hp: int = 100
    _speed: int = 36
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 90
    _magic_defense: int = 65
    _fp: int = 250
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 28
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom



class MachineMadeDrillBit(Enemy):
    """MachineMadeDrillBit enemy class"""

    _monster_id: int = 146
    _hp: int = 180
    _speed: int = 24
    _attack: int = 130
    _defense: int = 82
    _magic_attack: int = 31
    _magic_defense: int = 69
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Formless(Enemy):
    """Formless enemy class"""

    _monster_id: int = 147
    _hp: int = 10
    _speed: int = 2
    _magic_attack: int = 50
    _fp: int = 100
    _evade: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Mokura(Enemy):
    """Mokura enemy class"""

    _monster_id: int = 148
    _hp: int = 620
    _speed: int = 25
    _attack: int = 120
    _defense: int = 75
    _magic_attack: int = 80
    _magic_defense: int = 90
    _fp: int = 100
    _evade: int = 20
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 90
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = KerokeroCola
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class FireCrystal(Enemy):
    """FireCrystal enemy class"""

    _monster_id: int = 149
    _hp: int = 2500
    _speed: int = 10
    _defense: int = 100
    _magic_attack: int = 130
    _magic_defense: int = 60
    _fp: int = 250
    _evade: int = 10
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class WaterCrystal(Enemy):
    """WaterCrystal enemy class"""

    _monster_id: int = 150
    _hp: int = 1800
    _speed: int = 12
    _defense: int = 130
    _magic_attack: int = 120
    _magic_defense: int = 50
    _fp: int = 250
    _evade: int = 20
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class EarthCrystal(Enemy):
    """EarthCrystal enemy class"""

    _monster_id: int = 151
    _hp: int = 3200
    _speed: int = 1
    _defense: int = 70
    _magic_attack: int = 80
    _magic_defense: int = 33
    _fp: int = 250
    _evade: int = 5
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.JUMP]
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class WindCrystal(Enemy):
    """WindCrystal enemy class"""

    _monster_id: int = 152
    _hp: int = 800
    _speed: int = 30
    _defense: int = 200
    _magic_attack: int = 60
    _magic_defense: int = 88
    _fp: int = 250
    _evade: int = 30
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class MarioClone(Enemy):
    """MarioClone enemy class"""

    _monster_id: int = 153
    _hp: int = 200
    _speed: int = 20
    _attack: int = 100
    _defense: int = 90
    _magic_attack: int = 33
    _magic_defense: int = 50
    _fp: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class PeachClone(Enemy):
    """PeachClone enemy class"""

    _monster_id: int = 154
    _hp: int = 120
    _speed: int = 20
    _attack: int = 90
    _defense: int = 60
    _magic_attack: int = 62
    _magic_defense: int = 70
    _fp: int = 180
    _ohko_immune: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class BowserClone(Enemy):
    """BowserClone enemy class"""

    _monster_id: int = 155
    _hp: int = 300
    _speed: int = 12
    _attack: int = 130
    _defense: int = 100
    _magic_attack: int = 12
    _fp: int = 1
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class GenoClone(Enemy):
    """GenoClone enemy class"""

    _monster_id: int = 156
    _hp: int = 250
    _speed: int = 30
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 60
    _magic_defense: int = 30
    _fp: int = 40
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class MallowClone(Enemy):
    """MallowClone enemy class"""

    _monster_id: int = 157
    _hp: int = 150
    _speed: int = 14
    _attack: int = 80
    _defense: int = 65
    _magic_attack: int = 70
    _magic_defense: int = 80
    _fp: int = 80
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.ICE, Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Shyster(Enemy):
    """Shyster enemy class"""

    _monster_id: int = 158
    _hp: int = 30
    _speed: int = 18
    _attack: int = 20
    _defense: int = 26
    _magic_attack: int = 18
    _magic_defense: int = 10
    _fp: int = 2
    _evade: int = 10
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 3
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = HoneySyrup
    _common_item_drop: "Type[RegularItem]" = HoneySyrup


class Kinklink(Enemy):
    """Kinklink enemy class"""

    _monster_id: int = 159
    _hp: int = 60
    _speed: int = 99
    _defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class HanginShy(Enemy):
    """HanginShy enemy class"""

    _monster_id: int = 161
    _hp: int = 10
    _speed: int = 200
    _fp: int = 100
    _ohko_immune: bool = True
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smelter(Enemy):
    """Smelter enemy class"""

    _monster_id: int = 162
    _hp: int = 1500
    _defense: int = 120
    _magic_defense: int = 100
    _fp: int = 100
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class MachineMadeMack(Enemy):
    """MachineMadeMack enemy class"""

    _monster_id: int = 163
    _hp: int = 300
    _speed: int = 10
    _attack: int = 160
    _defense: int = 120
    _magic_attack: int = 95
    _magic_defense: int = 40
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 120
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = FireBomb


class MachineMadeBowyer(Enemy):
    """MachineMadeBowyer enemy class"""

    _monster_id: int = 164
    _hp: int = 1000
    _speed: int = 200
    _attack: int = 150
    _defense: int = 120
    _magic_attack: int = 90
    _magic_defense: int = 80
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 150
    _coins: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = IceBomb


class MachineMadeYaridovich(Enemy):
    """MachineMadeYaridovich enemy class"""

    _monster_id: int = 165
    _hp: int = 800
    _speed: int = 18
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 90
    _magic_defense: int = 50
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 180
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RockCandy


class MachineMadeAxemPink(Enemy):
    """MachineMadeAxemPink enemy class"""

    _monster_id: int = 166
    _hp: int = 100
    _speed: int = 35
    _attack: int = 95
    _defense: int = 90
    _magic_attack: int = 40
    _magic_defense: int = 100
    _fp: int = 200
    _evade: int = 25
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup



class MachineMadeAxemBlack(Enemy):
    """MachineMadeAxemBlack enemy class"""

    _monster_id: int = 167
    _hp: int = 120
    _speed: int = 55
    _attack: int = 120
    _defense: int = 110
    _magic_attack: int = 4
    _magic_defense: int = 40
    _fp: int = 100
    _evade: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom


class MachineMadeAxemRed(Enemy):
    """MachineMadeAxemRed enemy class"""

    _monster_id: int = 168
    _hp: int = 180
    _speed: int = 45
    _attack: int = 135
    _defense: int = 95
    _magic_attack: int = 24
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup


class MachineMadeAxemYellow(Enemy):
    """MachineMadeAxemYellow enemy class"""

    _monster_id: int = 169
    _hp: int = 200
    _speed: int = 20
    _attack: int = 140
    _defense: int = 130
    _magic_attack: int = 16
    _magic_defense: int = 20
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.POISON,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # rewards
    _xp: int = 25
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = MaxMushroom



class MachineMadeAxemGreen(Enemy):
    """MachineMadeAxemGreen enemy class"""

    _monster_id: int = 170
    _hp: int = 80
    _speed: int = 40
    _attack: int = 105
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 120
    _fp: int = 250
    _magic_evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.DEFENSE_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = RoyalSyrup




class Starslap(Enemy):
    """Starslap enemy class"""

    _monster_id: int = 176
    _hp: int = 62
    _speed: int = 9
    _attack: int = 25
    _defense: int = 24
    _magic_attack: int = 4
    _magic_defense: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 2
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Mukumuku(Enemy):
    """Mukumuku enemy class"""

    _monster_id: int = 177
    _hp: int = 108
    _speed: int = 11
    _attack: int = 60
    _defense: int = 47
    _magic_attack: int = 22
    _magic_defense: int = 30
    _fp: int = 100
    _magic_evade: int = 80
    _morph_chance: float = 1.0
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # rewards
    _xp: int = 8
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = MukuCookie
    _rare_item_drop: "Type[RegularItem]" = MapleSyrup


class Zeostar(Enemy):
    """Zeostar enemy class"""

    _monster_id: int = 178
    _hp: int = 90
    _speed: int = 10
    _attack: int = 75
    _defense: int = 60
    _magic_attack: int = 28
    _magic_defense: int = 20
    _fp: int = 4
    _morph_chance: float = 0.75
    _sound_on_hit: HitSound = HitSound.KNOCK
    _sound_on_approach: ApproachSound = ApproachSound.STARSLAP_SPIKEY_ENIGMA
    _weaknesses: List[Element] = [Element.THUNDER, Element.FIRE]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ONCE_AGAIN
    _flower_bonus_chance: int = 50

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 10
    _coins: int = 3
    _yoshi_cookie_item: "Type[RegularItem]" = SleepyBomb
    _rare_item_drop: "Type[RegularItem]" = Mushroom


class Jagger(Enemy):
    """Jagger enemy class"""

    _monster_id: int = 179
    _hp: int = 600
    _speed: int = 30
    _attack: int = 120
    _defense: int = 80
    _magic_defense: int = 50
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.POISON]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class EmptyEnemy(Enemy):
    """EmptyEnemy enemy class"""

    _monster_id: int = 180
    _hp: int = 9999
    _fp: int = 100
    _speed: int = 255

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Specific to Shelly
    _summons: List[int] = [0x28]
    _summon_event: Union[int, None] = None
    _formation_id: Union[int, None] = None


class Smithy2TankHead(Enemy):
    """Smithy2TankHead enemy class"""

    _monster_id: int = 181
    _hp: int = 8000
    _speed: int = 50
    _attack: int = 250
    _defense: int = 130
    _magic_attack: int = 10
    _magic_defense: int = 50
    _fp: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

class Smithy2SafeHead(Enemy):
    """Smithy2SafeHead enemy class"""

    _monster_id: int = 182
    _hp: int = 8000
    _attack: int = 40
    _defense: int = 150
    _magic_attack: int = 70
    _magic_defense: int = 100
    _fp: int = 120
    _ohko_immune: bool = True
    _resistances: List[Element] = [
        Element.THUNDER,
        Element.FIRE,
        Element.JUMP,
    ]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Microbomb(Enemy):
    """Microbomb enemy class"""

    _monster_id: int = 184
    _hp: int = 30
    _speed: int = 15
    _attack: int = 42
    _defense: int = 30
    _magic_attack: int = 6
    _magic_defense: int = 10
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.KNOCK
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes


class Grit(Enemy):
    """Grit enemy class"""

    _monster_id: int = 186
    _hp: int = 10
    _fp: int = 100
    _morph_chance: float = 1.0
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Neosquid(Enemy):
    """Neosquid enemy class"""

    _monster_id: int = 187
    _hp: int = 800
    _speed: int = 20
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 86
    _magic_defense: int = 50
    _fp: int = 200
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class YaridovichMirage(Enemy):
    """YaridovichMirage enemy class"""

    _monster_id: int = 188
    _hp: int = 500
    _speed: int = 16
    _attack: int = 100
    _defense: int = 40
    _magic_attack: int = 60
    _magic_defense: int = 10
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.CLAW
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Helio(Enemy):
    """Helio enemy class"""

    _monster_id: int = 189
    _hp: int = 10
    _attack: int = 140
    _fp: int = 100
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class RightEye(Enemy):
    """RightEye enemy class"""

    _monster_id: int = 190
    _hp: int = 500
    _speed: int = 17
    _attack: int = 128
    _defense: int = 100
    _magic_attack: int = 82
    _magic_defense: int = 36
    _fp: int = 200
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class LeftEye(Enemy):
    """LeftEye enemy class"""

    _monster_id: int = 191
    _hp: int = 300
    _speed: int = 21
    _attack: int = 153
    _defense: int = 130
    _magic_attack: int = 47
    _magic_defense: int = 80
    _fp: int = 200
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class KnifeGuy(Enemy):
    """KnifeGuy enemy class"""

    _monster_id: int = 192
    _hp: int = 700
    _speed: int = 25
    _attack: int = 70
    _defense: int = 55
    _magic_attack: int = 20
    _magic_defense: int = 10
    _fp: int = 35
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 40
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class GrateGuy(Enemy):
    """GrateGuy enemy class"""

    _monster_id: int = 193
    _hp: int = 900
    _speed: int = 14
    _attack: int = 60
    _defense: int = 40
    _magic_attack: int = 25
    _magic_defense: int = 40
    _fp: int = 50
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80

    # rewards
    _xp: int = 50
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = FlowerJar
    _rare_item_drop: "Type[RegularItem]" = FlowerJar

    # boss shuffle attributes



class Bundt(Enemy):
    """Bundt enemy class"""

    _monster_id: int = 194
    _hp: int = 900
    _speed: int = 16
    _attack: int = 65
    _defense: int = 10
    _magic_attack: int = 25
    _magic_defense: int = 50
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    # xp = 25
    _xp: int = 23
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Jinx1(Enemy):
    """Jinx1 enemy class"""

    _monster_id: int = 195
    _hp: int = 600
    _speed: int = 30
    _attack: int = 140
    _defense: int = 100
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 30
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 75
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Jinx2(Enemy):
    """Jinx2 enemy class"""

    _monster_id: int = 196
    _hp: int = 800
    _speed: int = 32
    _attack: int = 160
    _defense: int = 120
    _magic_defense: int = 90
    _fp: int = 100
    _evade: int = 30
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class CountDown(Enemy):
    """CountDown enemy class"""

    _monster_id: int = 197
    _hp: int = 2400
    _speed: int = 5
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 140
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class DingALing(Enemy):
    """DingALing enemy class"""

    _monster_id: int = 198
    _hp: int = 1200
    _speed: int = 10
    _attack: int = 180
    _defense: int = 120
    _magic_attack: int = 20
    _magic_defense: int = 50
    _fp: int = 100
    _ohko_immune: bool = True
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Belome1(Enemy):
    """Belome1 enemy class"""

    _monster_id: int = 199
    _hp: int = 500
    _speed: int = 4
    _attack: int = 30
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _fp: int = 30
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Belome2(Enemy):
    """Belome2 enemy class"""

    _monster_id: int = 200
    _hp: int = 1200
    _speed: int = 4
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 40
    _fp: int = 250
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 80
    _coins: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Smilax(Enemy):
    """Smilax enemy class"""

    _monster_id: int = 202
    _hp: int = 200
    _speed: int = 5
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Thrax(Enemy):
    """Thrax enemy class"""

    _monster_id: int = 203
    _hp: int = 10
    _speed: int = 200
    _fp: int = 100
    _ohko_immune: bool = True
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # effect nullification
    _status_immunities: List[Status] = [Status.SLEEP]

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Megasmilax(Enemy):
    """Megasmilax enemy class"""

    _monster_id: int = 204
    _hp: int = 1000
    _speed: int = 2
    _attack: int = 140
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 120
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes


class Birdetta(Enemy):
    """Birdetta enemy class"""

    _monster_id: int = 205
    _hp: int = 777
    _speed: int = 10
    _attack: int = 160
    _defense: int = 130
    _magic_attack: int = 6
    _magic_defense: int = 100
    _fp: int = 100
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    # xp = 60
    _xp: int = 48
    _coins: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes



class Eggbert(Enemy):
    """Eggbert enemy class"""

    _monster_id: int = 206
    _hp: int = 10
    _attack: int = 210
    _fp: int = 100
    _ohko_immune: bool = True
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    # made this up
    _xp: int = 3

    # boss shuffle attributes


class AxemYellow(Enemy):
    """AxemYellow enemy class"""

    _monster_id: int = 207
    _hp: int = 600
    _speed: int = 3
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 6
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.POISON,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 30
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Punchinello(Enemy):
    """Punchinello enemy class"""

    _monster_id: int = 208
    _hp: int = 1200
    _speed: int = 15
    _attack: int = 60
    _defense: int = 42
    _magic_attack: int = 22
    _magic_defense: int = 40
    _fp: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 80
    battle_sesw_only = True

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 70
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class TentaclesRight(Enemy):
    """TentaclesRight enemy class"""

    _monster_id: int = 209
    _hp: int = 260
    _speed: int = 21
    _attack: int = 82
    _defense: int = 50
    _magic_attack: int = 35
    _magic_defense: int = 40
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.SLAP
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class AxemRed(Enemy):
    """AxemRed enemy class"""

    _monster_id: int = 210
    _hp: int = 800
    _speed: int = 30
    _attack: int = 150
    _defense: int = 100
    _magic_attack: int = 24
    _magic_defense: int = 80
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class AxemGreen(Enemy):
    """AxemGreen enemy class"""

    _monster_id: int = 211
    _hp: int = 450
    _speed: int = 20
    _attack: int = 110
    _defense: int = 60
    _magic_attack: int = 90
    _magic_defense: int = 120
    _fp: int = 200
    _magic_evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 20
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class KingBomb(Enemy):
    """KingBomb enemy class"""

    _monster_id: int = 212
    _hp: int = 500
    _defense: int = 130
    _magic_attack: int = 80
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

class MezzoBomb(Enemy):
    """MezzoBomb enemy class"""

    _monster_id: int = 213
    _hp: int = 150
    _speed: int = 1
    _attack: int = 70
    _defense: int = 40
    _magic_defense: int = 10
    _fp: int = 100
    _sound_on_hit: HitSound = HitSound.SMASH
    _weaknesses: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Raspberry(Enemy):
    """Raspberry enemy class"""

    _monster_id: int = 215
    _hp: int = 600
    _speed: int = 16
    _attack: int = 70
    _defense: int = 20
    _magic_attack: int = 30
    _magic_defense: int = 30
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    # xp = 50
    _xp: int = 46
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class KingCalamari(Enemy):
    """KingCalamari enemy class"""

    _monster_id: int = 216
    _hp: int = 800
    _speed: int = 8
    _attack: int = 100
    _defense: int = 80
    _magic_attack: int = 30
    _magic_defense: int = 40
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.DEEP_JAB
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 100
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes


class TentaclesLeft(Enemy):
    """TentaclesLeft enemy class"""

    _monster_id: int = 217
    _hp: int = 200
    _speed: int = 21
    _attack: int = 87
    _defense: int = 70
    _magic_attack: int = 35
    _magic_defense: int = 23
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SLAP
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Jinx3(Enemy):
    """Jinx3 enemy class"""

    _monster_id: int = 218
    _hp: int = 1000
    _speed: int = 35
    _attack: int = 180
    _defense: int = 140
    _magic_defense: int = 100
    _fp: int = 100
    _evade: int = 30
    _magic_evade: int = 25
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 150
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Zombone(Enemy):
    """Zombone enemy class"""

    _monster_id: int = 219
    _hp: int = 1800
    _speed: int = 6
    _attack: int = 190
    _defense: int = 60
    _magic_attack: int = 80
    _magic_defense: int = 100
    _fp: int = 100
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.ICE, Element.FIRE]
    _weaknesses: List[Element] = [Element.THUNDER, Element.JUMP]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class CzarDragon(Enemy):
    """CzarDragon enemy class"""

    _monster_id: int = 220
    _hp: int = 1400
    _speed: int = 20
    _attack: int = 160
    _defense: int = 100
    _magic_attack: int = 120
    _magic_defense: int = 70
    _fp: int = 100
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE]
    _weaknesses: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes



class Cloaker(Enemy):
    """Cloaker enemy class"""

    _monster_id: int = 221
    _hp: int = 1200
    _speed: int = 20
    _attack: int = 170
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Domino(Enemy):
    """Domino enemy class"""

    _monster_id: int = 222
    _hp: int = 900
    _speed: int = 25
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class MadAdder(Enemy):
    """MadAdder enemy class"""

    _monster_id: int = 223
    _hp: int = 1500
    _speed: int = 10
    _attack: int = 150
    _defense: int = 70
    _magic_attack: int = 90
    _magic_defense: int = 180
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = Crystalline
    _rare_item_drop: "Type[RegularItem]" = Crystalline

    # boss shuffle attributes


class Mack(Enemy):
    """Mack enemy class"""

    _monster_id: int = 224
    _hp: int = 480
    _speed: int = 8
    _attack: int = 22
    _defense: int = 25
    _magic_attack: int = 15
    _magic_defense: int = 20
    _fp: int = 28
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    # xp = 24
    _xp: int = 12
    # coins = 20
    _coins: int = 12
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes



class Bodyguard(Enemy):
    """Bodyguard enemy class"""

    _monster_id: int = 225
    _hp: int = 30
    _speed: int = 15
    _attack: int = 20
    _defense: int = 22
    _magic_attack: int = 19
    _magic_defense: int = 12
    _fp: int = 3
    _evade: int = 10
    _sound_on_hit: HitSound = HitSound.KNOCK
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.HP_MAX

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # Boss shuffle attributes

    # this isn't from the original game
    _xp: int = 3
    _coins: int = 2


class Yaridovich(Enemy):
    """Yaridovich enemy class"""

    _monster_id: int = 226
    _hp: int = 1500
    _speed: int = 20
    _attack: int = 125
    _defense: int = 85
    _magic_attack: int = 70
    _magic_defense: int = 75
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 120
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    # battle_push_length = 78



class DrillBit(Enemy):
    """DrillBit enemy class"""

    _monster_id: int = 227
    _hp: int = 80
    _speed: int = 15
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # rewards
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # boss shuffle attributes


class YaridovichDrillBit(Enemy):
    """YaridovichDrillBit enemy class"""

    _monster_id: int = 244
    _hp: int = 80
    _speed: int = 15
    _attack: int = 85
    _defense: int = 70
    _magic_attack: int = 40
    _magic_defense: int = 56
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 2

    # rewards
    _xp: int = 11
    _coins: int = 1
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes
    # Attuned to ratio of machine made drill bit to machine made yarid.


class AxemPink(Enemy):
    """AxemPink enemy class"""

    _monster_id: int = 228
    _hp: int = 400
    _speed: int = 25
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 100
    _fp: int = 200
    _evade: int = 25
    _magic_evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _resistances: List[Element] = [Element.ICE]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _xp: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class AxemBlack(Enemy):
    """AxemBlack enemy class"""

    _monster_id: int = 229
    _hp: int = 550
    _speed: int = 35
    _attack: int = 140
    _defense: int = 120
    _magic_attack: int = 4
    _magic_defense: int = 40
    _fp: int = 100
    _evade: int = 30
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 40
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Bowyer(Enemy):
    """Bowyer enemy class"""

    _monster_id: int = 230
    _hp: int = 720
    _speed: int = 10
    _attack: int = 50
    _defense: int = 40
    _magic_attack: int = 30
    _magic_defense: int = 35
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = FlowerBox
    _rare_item_drop: "Type[RegularItem]" = FlowerBox



class AeroBowyer(Enemy):
    """AeroBowyer enemy class"""

    # Borrow stats from Bob-omb to be relatively reasonable to match Bowyer
    _monster_id: int = 231
    _hp: int = 90
    _speed: int = 1
    _attack: int = 50
    _defense: int = 38
    _magic_attack: int = 1
    _magic_defense: int = 10
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 4
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class AeroSmithy(Enemy):
    """AeroSmithy enemy class"""

    # Borrow stats from Poundette to be relatively reasonable to match Smithy
    _monster_id: int = 175
    _hp: int = 150
    _speed: int = 30
    _attack: int = 140
    _defense: int = 60
    _magic_attack: int = 66
    _magic_defense: int = 45
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 28
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Exor(Enemy):
    """Exor enemy class"""

    _monster_id: int = 233
    _hp: int = 1800
    _speed: int = 200
    _defense: int = 120
    _magic_defense: int = 80
    _ohko_immune: bool = True
    _resistances: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smithy1(Enemy):
    """Smithy1 enemy class"""

    _monster_id: int = 234
    _hp: int = 2000
    _speed: int = 30
    _attack: int = 230
    _defense: int = 130
    _magic_attack: int = 100
    _magic_defense: int = 100
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom



class Shyper(Enemy):
    """Shyper enemy class"""

    _monster_id: int = 235
    _hp: int = 400
    _speed: int = 42
    _attack: int = 170
    _defense: int = 80
    _magic_attack: int = 70
    _magic_defense: int = 50
    _fp: int = 30
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.KNOCK
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smithy2Body(Enemy):
    """Smithy2Body enemy class"""

    _monster_id: int = 236
    _hp: int = 1000
    _speed: int = 30
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 20
    _magic_defense: int = 60
    _fp: int = 50
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom



class Smithy2Head(Enemy):
    """Smithy2Head enemy class"""

    _monster_id: int = 237
    _hp: int = 8000
    _speed: int = 40
    _attack: int = 180
    _defense: int = 80
    _magic_attack: int = 60
    _magic_defense: int = 50
    _fp: int = 50
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smithy2MageHead(Enemy):
    """Smithy2MageHead enemy class"""

    _monster_id: int = 238
    _hp: int = 8000
    _speed: int = 35
    _attack: int = 135
    _defense: int = 50
    _magic_attack: int = 130
    _magic_defense: int = 150
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [
        Element.ICE,
        Element.THUNDER,
        Element.FIRE,
    ]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Smithy2ChestHead(Enemy):
    """Smithy2ChestHead enemy class"""

    _monster_id: int = 239
    _hp: int = 8000
    _speed: int = 18
    _attack: int = 150
    _defense: int = 120
    _magic_attack: int = 78
    _magic_defense: int = 80
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _resistances: List[Element] = [Element.THUNDER]
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 30

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Croco1(Enemy):
    """Croco1 enemy class"""

    _monster_id: int = 240
    _hp: int = 320
    _speed: int = 16
    _attack: int = 25
    _defense: int = 25
    _magic_attack: int = 30
    _magic_defense: int = 18
    _fp: int = 12
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 16
    _coins: int = 10
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = FlowerTab
    _rare_item_drop: "Type[RegularItem]" = FlowerTab


class Croco2(Enemy):
    """Croco2 enemy class"""

    _monster_id: int = 241
    _hp: int = 750
    _speed: int = 20
    _attack: int = 52
    _defense: int = 50
    _magic_attack: int = 27
    _magic_defense: int = 50
    _fp: int = 12
    _evade: int = 20
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _weaknesses: List[Element] = [Element.FIRE]
    _status_immunities: List[Status] = [
        Status.SLEEP,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 30
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = FlowerBox



class Earthlink(Enemy):
    """Earthlink enemy class"""

    _monster_id: int = 243
    _hp: int = 2500
    _speed: int = 16
    _attack: int = 220
    _defense: int = 120
    _magic_attack: int = 5
    _magic_defense: int = 10
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _common_item_drop: "Type[RegularItem]" = PowerBlast
    _rare_item_drop: "Type[RegularItem]" = PowerBlast

    # boss shuffle attributes


class AxemRangers(Enemy):
    """AxemRangers enemy class"""

    _monster_id: int = 245
    _hp: int = 999
    _speed: int = 200
    _defense: int = 100
    _magic_attack: int = 120
    _magic_defense: int = 100
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _weaknesses: List[Element] = [Element.THUNDER]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Booster(Enemy):
    """Booster enemy class"""

    _monster_id: int = 246
    _hp: int = 800
    _speed: int = 24
    _attack: int = 75
    _defense: int = 55
    _magic_attack: int = 1
    _magic_defense: int = 40
    _fp: int = 2
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _sound_on_approach: ApproachSound = ApproachSound.AMANITA_TERRAPIN
    _weaknesses: List[Element] = [Element.JUMP]
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _coins: int = 100
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = FlowerBox



class Booster2(Enemy):
    """Booster2 enemy class"""

    _monster_id: int = 247
    _hp: int = 10
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.SMASH
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Snifit(Enemy):
    """Snifit enemy class"""

    _monster_id: int = 248
    _hp: int = 200
    _speed: int = 26
    _attack: int = 60
    _defense: int = 60
    _magic_attack: int = 20
    _magic_defense: int = 20
    _fp: int = 32
    _sound_on_hit: HitSound = HitSound.PUNCH
    _weaknesses: List[Element] = [Element.ICE]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.LUCKY
    _flower_bonus_chance: int = 80

    # effect nullification
    _status_immunities: List[Status] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 2
    _coins: int = 15
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom
    _rare_item_drop: "Type[RegularItem]" = Mushroom



class Johnny(Enemy):
    """Johnny enemy class"""

    _monster_id: int = 249
    _hp: int = 820
    _speed: int = 13
    _attack: int = 85
    _defense: int = 80
    _magic_attack: int = 25
    _magic_defense: int = 60
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [Status.SLEEP]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 40

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 90
    _coins: int = 50
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom\


class JohnnySolo(Enemy):
    """JohnnySolo enemy class"""

    _monster_id: int = 250
    _hp: int = 400
    _speed: int = 30
    _attack: int = 90
    _defense: int = 100
    _magic_defense: int = 32
    _fp: int = 100
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.FIRE, Element.JUMP]
    _status_immunities: List[Status] = [Status.POISON]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Valentina(Enemy):
    """Valentina enemy class"""

    _monster_id: int = 251
    _hp: int = 2000
    _speed: int = 200
    _attack: int = 120
    _defense: int = 80
    _magic_attack: int = 80
    _magic_defense: int = 60
    _fp: int = 250
    _evade: int = 10
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _resistances: List[Element] = [Element.ICE]
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # rewards
    _xp: int = 120
    _coins: int = 200
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom


class Cloaker2(Enemy):
    """Cloaker2 enemy class"""

    _monster_id: int = 252
    _hp: int = 1200
    _speed: int = 20
    _attack: int = 180
    _defense: int = 130
    _magic_attack: int = 12
    _magic_defense: int = 20
    _fp: int = 100
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.JAB
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Domino2(Enemy):
    """Domino2 enemy class"""

    _monster_id: int = 253
    _hp: int = 900
    _speed: int = 25
    _attack: int = 65
    _defense: int = 80
    _magic_attack: int = 120
    _magic_defense: int = 150
    _fp: int = 250
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.PIERCE
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 60
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes


class Candle(Enemy):
    """Candle enemy class"""

    _monster_id: int = 254
    _hp: int = 10
    _fp: int = 100
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP

    # rewards
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []


class Culex(Enemy):
    """Culex enemy class"""

    _monster_id: int = 255
    _hp: int = 4096
    _speed: int = 50
    _attack: int = 250
    _defense: int = 100
    _magic_attack: int = 100
    _magic_defense: int = 80
    _fp: int = 200
    _ohko_immune: bool = True
    _sound_on_hit: HitSound = HitSound.CLAW
    _status_immunities: List[Status] = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
    ]
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 10

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 600
    _yoshi_cookie_item: "Type[RegularItem]" = Mushroom

    # boss shuffle attributes

