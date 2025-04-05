"""Base classes for enemies encountered in battle and their overworld representations."""

from copy import deepcopy
from typing import List, Optional

from types.numbers import BitMapSet, ByteField, UInt16, UInt8
from types.patch import Patch
from types.spells import Status, Element

from .constants import (
    BASE_ENEMY_ADDRESS,
    BASE_REWARD_ADDRESS,
    FLOWER_BONUS_BASE_ADDRESS,
)
from .enums import ApproachSound, HitSound, FlowerBonusType


class Enemy:
    """Class representing an enemy in the game."""

    # properties in lazy shell

    _monster_id: int = 0

    # vital status
    _hp: int = 0
    _fp: int = 0
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _speed: int = 0
    _evade: int = 0
    _magic_evade: int = 0

    # effect nullification
    _status_immunities: List[Status] = []

    # element weaknesses
    _weaknesses: List[Element] = []

    # element resistances
    _resistances: List[Element] = []

    # rewards
    _xp: int = 0
    _coins: int = 0
    _rare_item_drop_id: Optional[int] = None
    _common_item_drop_id: Optional[int] = None
    _yoshi_cookie_item_id: int = 96

    # flower bonus
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.NONE
    _flower_bonus_chance: int = 0

    # other properties
    _morph_chance: float = 0
    _sound_on_hit: HitSound = HitSound.BITE
    _sound_on_approach: ApproachSound = ApproachSound.NONE

    # special status
    _invincible: bool = False
    _ohko_immune: bool = False

    @property
    def monster_id(self) -> UInt8:
        """Enemy's unique index."""
        return UInt8(self._monster_id)

    @property
    def hp(self) -> UInt16:
        """The enemy's HP at the start of the fight."""
        return UInt16(self._hp)

    def set_hp(self, hp: int) -> None:
        """Set how much HP the enemy will have at the start of the fight."""
        assert UInt16(hp)
        self._hp = hp

    @property
    def fp(self) -> UInt8:
        """The enemy's FP at the start of the fight."""
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        """Set how much FP the enemy will have at the start of the fight."""
        assert UInt8(fp)
        self._fp = fp

    @property
    def attack(self) -> UInt8:
        """The enemy's base physical attack power."""
        return UInt8(self._attack)

    def set_attack(self, attack: int) -> None:
        """Set the enemy's base physical attack power."""
        assert UInt8(attack)
        self._attack = attack

    @property
    def defense(self) -> UInt8:
        """The enemy's base physical defense power."""
        return UInt8(self._defense)

    def set_defense(self, defense: int) -> None:
        """Set the enemy's base physical defense power."""
        assert UInt8(defense)
        self._defense = defense

    @property
    def magic_attack(self) -> UInt8:
        """The enemy's base magic attack power."""
        return UInt8(self._magic_attack)

    def set_magic_attack(self, magic_attack: int) -> None:
        """Set the enemy's base magic attack power."""
        assert UInt8(magic_attack)
        self._magic_attack = magic_attack

    @property
    def magic_defense(self) -> UInt8:
        """The enemy's base magic defense power."""
        return UInt8(self._magic_defense)

    def set_magic_defense(self, magic_defense: int) -> None:
        """Set the enemy's base magic defense power."""
        assert UInt8(magic_defense)
        self._magic_defense = magic_defense

    @property
    def speed(self) -> UInt8:
        """The enemy's speed."""
        return UInt8(self._speed)

    def set_speed(self, speed: int) -> None:
        """Set the enemy's speed."""
        assert UInt8(speed)
        self._speed = speed

    @property
    def evade(self) -> UInt8:
        """The enemy's percent likelihood of evading a physical attack."""
        return UInt8(self._evade)

    def set_evade(self, evade: int) -> None:
        """Set the enemy's percent likelihood of evading a physical attack."""
        assert 0 <= evade <= 100
        self._evade = evade

    @property
    def magic_evade(self) -> UInt8:
        """The enemy's percent likelihood of evading a magic attack."""
        return UInt8(self._magic_evade)

    def set_magic_evade(self, magic_evade: int) -> None:
        """Set the enemy's percent likelihood of evading a magic attack."""
        assert 0 <= magic_evade <= 100
        self._magic_evade = magic_evade

    @property
    def status_immunities(self) -> List[Status]:
        """The list of status effects that the enemy is unaffected by."""
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: List[Status]) -> None:
        """Overwrite the list of status effects that the enemy is unaffected by."""
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: Status) -> None:
        """Add a status effect that the enemy should be unaffected by."""
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: Status) -> None:
        """Remove a status effect from the list that the enemy should be unaffected by."""
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def weaknesses(self) -> List[Element]:
        """The list of elements that cause double damage to the enemy."""
        return deepcopy(self._weaknesses)

    def set_weaknesses(self, weaknesses: List[Element]) -> None:
        """Overwrite the list of elements that cause double damage to the enemy."""
        self._weaknesses = deepcopy(weaknesses)

    def append_weakness(self, element: Element) -> None:
        """Add an element that should cause double damage to the enemy."""
        if element not in self._weaknesses:
            self._weaknesses.append(element)

    def remove_weakness(self, element: Element) -> None:
        """Remove an element from the list that should cause double damage to the enemy."""
        if element in self._weaknesses:
            self._weaknesses.remove(element)

    @property
    def resistances(self) -> List[Element]:
        """The list of elements which will have their damage to the enemy reduced by 50%."""
        return deepcopy(self._resistances)

    def set_resistances(self, resistances: List[Element]) -> None:
        """Overwrite the list of elements which will have their damage to the enemy reduced
        by 50%."""
        self._resistances = deepcopy(resistances)

    def append_resistance(self, element: Element) -> None:
        """Add an element which will have their damage to the enemy reduced by 50%."""
        if element not in self._resistances:
            self._resistances.append(element)

    def remove_resistance(self, element: Element) -> None:
        """Remove an element from the list that will have their damage to the enemy
        reduced by 50%."""
        if element in self._resistances:
            self._resistances.remove(element)

    @property
    def xp(self) -> UInt16:
        """The amount of EXP awarded by the enemy. This number is divided by the number of
        active party members you have at the start of the battle."""
        return UInt16(self._xp)

    def set_xp(self, xp: int) -> None:
        """Set the amount of EXP awarded by the enemy. This number is divided by the number of
        active party members you have at the start of the battle."""
        assert 0 <= xp <= 9999
        self._xp = xp

    @property
    def coins(self) -> UInt8:
        """The amount of coins rewarded by the enemy."""
        return UInt8(self._coins)

    def set_coins(self, coins: int) -> None:
        """Set the amount of coins rewarded by the enemy."""
        assert UInt8(coins)
        self._coins = coins

    @property
    def rare_item_drop_id(self) -> Optional[int]:
        """A single item that the enemy has a very small chance of dropping."""
        return self._rare_item_drop_id

    def set_rare_item_drop_id(self, rare_item_drop_id: Optional[int]) -> None:
        """Set the single item that the enemy has a very small chance of dropping."""
        self._rare_item_drop_id = rare_item_drop_id

    @property
    def common_item_drop_id(self) -> Optional[int]:
        """A single item that the enemy has a high chance of dropping."""
        return self._common_item_drop_id

    def set_common_item_drop_id(self, common_item_drop_id: int) -> None:
        """Set the single item that the enemy has a high chance of dropping."""
        self._common_item_drop_id = common_item_drop_id

    @property
    def yoshi_cookie_item_id(self) -> int:
        """The item to be granted if a Yoshi Cookie on this enemy is successful."""
        return self._yoshi_cookie_item_id

    def set_yoshi_cookie_item_id(self, yoshi_cookie_item_id: int) -> None:
        """Set the item to be granted if a Yoshi Cookie on this enemy is successful."""
        self._yoshi_cookie_item_id = yoshi_cookie_item_id

    @property
    def flower_bonus_type(self) -> FlowerBonusType:
        """The bonus flower that is granted by defeating this enemy."""
        return self._flower_bonus_type

    def set_flower_bonus_type(self, flower_bonus_type: FlowerBonusType) -> None:
        """Set the bonus flower that is granted by defeating this enemy."""
        self._flower_bonus_type = flower_bonus_type

    @property
    def flower_bonus_chance(self) -> UInt8:
        """The percent likelihood of this enemy granting a bonus flower."""
        return UInt8(self._flower_bonus_chance)

    def set_flower_bonus_chance(self, flower_bonus_chance: int) -> None:
        """Set the percent likelihood of this enemy granting a bonus flower."""
        assert 0 <= flower_bonus_chance <= 100 and flower_bonus_chance % 10 == 0
        self._flower_bonus_chance = flower_bonus_chance

    @property
    def morph_chance(self) -> float:
        """The percent success rate that the enemy is affected by a Yoshi Cookie, Lamb's Lure,
        or Sheep Attack. Valid values are 0, 25, 75, or 100."""
        return self._morph_chance

    def set_morph_chance(self, morph_chance: float) -> None:
        """Set the percent success rate that the enemy is affected by a Yoshi Cookie, Lamb's Lure,
        or Sheep Attack. Valid values are 0, 25, 75, or 100."""
        assert morph_chance in [0, 25, 75, 100]
        self._morph_chance = morph_chance

    @property
    def sound_on_hit(self) -> HitSound:
        """The sound the enemy should make when it attacks you."""
        return self._sound_on_hit

    def set_sound_on_hit(self, sound_on_hit: HitSound) -> None:
        """Set the sound the enemy should make when it attacks you."""
        self._sound_on_hit = sound_on_hit

    @property
    def sound_on_approach(self) -> ApproachSound:
        """The sound the enemy should make when it approaches you."""
        return self._sound_on_approach

    def set_sound_on_approach(self, sound_on_approach: ApproachSound) -> None:
        """Set the sound the enemy should make when it approaches you."""
        self._sound_on_approach = sound_on_approach

    @property
    def invincible(self) -> bool:
        """If true, damage taken will not reduce the enemy's HP."""
        return self._invincible

    def set_invincible(self, invincible: bool) -> None:
        """If true, damage taken will not reduce the enemy's HP."""
        self._invincible = invincible

    @property
    def ohko_immune(self) -> bool:
        """If true, the enemy is immune to a timed Geno Whirl."""
        return self._ohko_immune

    def set_ohko_immune(self, ohko_immune: bool) -> None:
        """If true, the enemy is immune to a timed Geno Whirl."""
        self._ohko_immune = ohko_immune

    @property
    def address(self):
        """The ROM address at which to begin writing properties to for this enemy."""
        return BASE_ENEMY_ADDRESS + self.monster_id * 16

    @property
    def reward_address(self):
        """The ROM address at which to begin writing reward/drop properties to for this enemy."""
        return BASE_REWARD_ADDRESS + self.monster_id * 6
    
    def __str__(self) -> str:
        return f"""<{self.name}
         hp: {self.hp} 
         attack: {self.attack}
         defense: {self.defense} 
         m.attack: {self.magic_attack} 
         m.defense: {self.magic_defense}>"""

    def __repr__(self) -> str:
        return str(self)

    @property
    def name(self) -> str:
        """Enemy's default name"""
        return self.__class__.__name__
    
    def get_patch(self) -> Patch:
        """Get patch for this enemy."""
        patch = Patch()

        # Main stats.
        data = bytearray()
        data += ByteField(self.hp).as_bytes()
        data += ByteField(self.speed).as_bytes()
        data += ByteField(self.attack).as_bytes()
        data += ByteField(self.defense).as_bytes()
        data += ByteField(self.magic_attack).as_bytes()
        data += ByteField(self.magic_defense).as_bytes()
        data += ByteField(self.fp).as_bytes()
        data += ByteField(self.evade).as_bytes()
        data += ByteField(self.magic_evade).as_bytes()
        patch.add_data(self.address, data)

        # Special defense bits, sound on hit is top half.
        data = bytearray()
        hit_special_defense = 1 if self.invincible else 0
        hit_special_defense |= (1 if self.ohko_immune else 0) << 1
        morph_chance: int = 0
        if self.morph_chance == 0.25:
            morph_chance = 1
        elif self.morph_chance == 0.75:
            morph_chance = 2
        if self.morph_chance == 1.0:
            morph_chance = 3
        hit_special_defense |= morph_chance << 2
        hit_special_defense |= self.sound_on_hit << 4
        data.append(hit_special_defense)

        # Elemental resistances.
        data += BitMapSet(
            1, [resistance.stat_value for resistance in self.resistances]
        ).as_bytes()

        # Elemental weaknesses byte (top half), sound on approach is bottom half.
        weaknesses_approach = self.sound_on_approach
        for weakness in self.weaknesses:
            weaknesses_approach |= 1 << weakness.stat_value
        data.append(weaknesses_approach)

        # Status immunities.
        data += BitMapSet(
            1, [immunity.stat_value for immunity in self.status_immunities]
        ).as_bytes()

        patch.add_data(self.address + 11, data)

        # Flower bonus.
        bonus_addr = FLOWER_BONUS_BASE_ADDRESS + self.monster_id
        bonus = (self.flower_bonus_chance // 10) << 4
        bonus |= self.flower_bonus_type
        patch.add_data(bonus_addr, ByteField(bonus).as_bytes())

        yoshi_cookie_item_id = self.yoshi_cookie_item_id
        common_item = 0xFF
        if self.common_item_drop_id is not None:
            common_item = self.common_item_drop_id
        rare_item = 0xFF
        if self.rare_item_drop_id is not None:
            rare_item = self.rare_item_drop_id

        # Build reward data patch.
        data = bytearray()
        data += ByteField(self.xp).as_bytes()
        data += ByteField(self.coins).as_bytes()
        data += ByteField(yoshi_cookie_item_id).as_bytes()
        data += ByteField(common_item).as_bytes()
        data += ByteField(rare_item).as_bytes()
        patch.add_data(self.reward_address, data)

        return patch