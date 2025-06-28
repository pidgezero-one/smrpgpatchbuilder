"""Base classes for item entities"""

from copy import deepcopy
import random
import math
from typing import List, TypeVar, Optional, Dict


from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.party_character import (
    PartyCharacter,
)
from smrpgpatchbuilder.datatypes.numbers.classes import UInt8, ByteField, BitMapSet


# target .enums specifically to prevent cyclic import
from smrpgpatchbuilder.datatypes.spells.enums import Status, Element, TempStatBuff

from .enums import ItemTypeValue, EffectType, InflictFunction, OverworldMenuBehaviour
from .constants import (
    ITEMS_BASE_ADDRESS,
    ITEMS_BASE_PRICE_ADDRESS,
    ITEMS_BASE_TIMING_ADDRESS,
)


class Item:
    """Parent class representing an item."""

    _item_id: int = 0

    _item_name: str = ""
    _description: str = ""

    _price: int = 0

    _speed: int = 0
    _variance: UInt8 = UInt8(0)
    _inflict: int = 0
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0

    _type_value: ItemTypeValue = ItemTypeValue.ITEM
    _effect_type: Optional[EffectType]
    _inflict_type: Optional[InflictFunction]
    _inflict_element: Optional[Element]

    _equip_chars: List[PartyCharacter] = []
    _elemental_immunities: List[Element] = []
    _elemental_resistances: List[Element] = []
    _status_immunities: List[Status] = []
    _temp_buffs: List[TempStatBuff] = []

    _prevent_ko: bool = False
    _hide_damage: bool = False
    _usable_battle: bool = False
    _usable_overworld: bool = False
    _reusable: bool = False

    _overworld_menu_behaviour: OverworldMenuBehaviour = (
        OverworldMenuBehaviour.LEAD_TO_HP
    )
    _overworld_menu_fill_fp: bool = False
    _overworld_menu_fill_hp: bool = False

    _can_target_others: bool = False
    _can_target_self: bool = True
    _one_side_only: bool = False
    _koed_target_only: bool = False
    _target_enemies: bool = False
    _target_all: bool = False

    _frog_coin_item: bool = False

    @property
    def index(self) -> int:
        return self._item_id

    @property
    def item_id(self) -> int:
        """Unique identifier for this item"""
        return self._item_id

    @property
    def type_value(self) -> ItemTypeValue:
        """Armor, accessory, weapon, or other"""
        return self._type_value

    @property
    def description(self) -> str:
        """The description as it appears in the in-game menu"""
        return self._description

    def set_description(self, description: str) -> None:
        """Update the description as it appears in the in-game menu"""
        self._description = description

    @property
    def consumable(self) -> bool:
        """Consumable items are single-use, like mushrooms and syrups."""
        return self._consumable

    @property
    def equip_chars(self) -> List[PartyCharacter]:
        """A list of which characters can equip this item"""
        return self._equip_chars

    def set_equip_chars(self, equip_chars: List[PartyCharacter]) -> None:
        """Overwrites the list of which characters can equip this item"""
        self._equip_chars = equip_chars

    def append_equip_char(self, char: PartyCharacter) -> None:
        """Add a character who should be able to equip this item"""
        assert char < 5
        if char not in self._equip_chars:
            self._equip_chars.append(char)

    def remove_equip_char(self, char: PartyCharacter) -> None:
        """Remove a character from the list of characters who can equip this item"""
        assert char < 5
        if char in self._equip_chars:
            self._equip_chars.remove(char)

    @property
    def speed(self) -> int:
        """Base speed increase for this item."""
        return self._speed

    @property
    def attack(self) -> int:
        """Base physical attack increase for this item."""
        return self._attack

    @property
    def defense(self) -> int:
        """Base physical defense increase for this item."""
        return self._defense

    @property
    def magic_attack(self) -> int:
        """Base magic attack increase for this item."""
        return self._magic_attack

    @property
    def magic_defense(self) -> int:
        """Base magic defense increase for this item."""
        return self._magic_defense

    @property
    def variance(self) -> UInt8:
        """The range of randomness applied to weapon output."""
        return self._variance

    @property
    def prevent_ko(self) -> bool:
        """If true, OHKO moves like Shaker and Magnum have no effect on the wearer."""
        return self._prevent_ko

    @property
    def elemental_immunities(self) -> List[Element]:
        """The wearer takes 0 damage from spells infused with these elements."""
        return deepcopy(self._elemental_immunities)

    @property
    def elemental_resistances(self) -> List[Element]:
        """The wearer takes half damage from spells infused with these elements."""
        return deepcopy(self._elemental_resistances)

    @property
    def status_immunities(self) -> List[Status]:
        """The wearer is immune to these status effects."""
        return deepcopy(self._status_immunities)

    def set_status_immunities(self, status_immunities: List[Status]) -> None:
        """Overwrites the status effect immunities for this item."""
        self._status_immunities = deepcopy(status_immunities)

    def append_status_immunity(self, immunity: Status) -> None:
        """Adds a status effect to the immunities for this item."""
        if immunity not in self._status_immunities:
            self._status_immunities.append(immunity)

    def remove_status_immunity(self, immunity: Status) -> None:
        """Removes a status effect from the immunities for this item."""
        if immunity in self._status_immunities:
            self._status_immunities.remove(immunity)

    @property
    def temp_buffs(self) -> List[TempStatBuff]:
        """Boost multiplier effects applied to the wearer at the start of battle."""
        return deepcopy(self._temp_buffs)

    @property
    def price(self) -> int:
        """Purchase cost of the item, regardless of currency type."""
        return self._price

    def set_price(self, price: int) -> None:
        """Set item cost, regardless of currency type."""
        maximum: int = 999 if self.frog_coin_item else 9999
        self._price = min(maximum, price)

    @property
    def inflict(self) -> int:
        """The inflict value used in effect resolution"""
        return self._inflict

    def set_inflict(self, inflict: int) -> None:
        """Update the inflict value used in effect resolution"""
        self._inflict = inflict

    @property
    def effect_type(self) -> Optional[EffectType]:
        """The type of effect this represents"""
        return self._effect_type

    def set_effect_type(self, effect_type: Optional[EffectType]) -> None:
        """Update the effect type"""
        self._effect_type = effect_type

    @property
    def inflict_type(self) -> Optional[InflictFunction]:
        """The function that determines infliction logic"""
        return self._inflict_type

    def set_inflict_type(self, inflict_type: Optional[InflictFunction]) -> None:
        """Update the inflict type function"""
        self._inflict_type = inflict_type

    @property
    def inflict_element(self) -> Optional[Element]:
        """The elemental type associated with this effect"""
        return self._inflict_element

    def set_inflict_element(self, inflict_element: Optional[Element]) -> None:
        """Update the infliction element"""
        self._inflict_element = inflict_element

    @property
    def prevent_ko(self) -> bool:
        """Whether this prevents KO"""
        return self._prevent_ko

    def set_prevent_ko(self, prevent_ko: bool) -> None:
        """Set whether this prevents KO"""
        self._prevent_ko = prevent_ko

    @property
    def hide_damage(self) -> bool:
        """Whether to hide damage display"""
        return self._hide_damage

    def set_hide_damage(self, hide_damage: bool) -> None:
        """Set whether to hide damage display"""
        self._hide_damage = hide_damage

    @property
    def usable_battle(self) -> bool:
        """Whether this can be used in battle"""
        return self._usable_battle

    def set_usable_battle(self, usable_battle: bool) -> None:
        """Set battle usability"""
        self._usable_battle = usable_battle

    @property
    def usable_overworld(self) -> bool:
        """Whether this can be used in the overworld"""
        return self._usable_overworld

    def set_usable_overworld(self, usable_overworld: bool) -> None:
        """Set overworld usability"""
        self._usable_overworld = usable_overworld

    @property
    def overworld_menu_behaviour(self) -> OverworldMenuBehaviour:
        """The menu behavior when used in the overworld"""
        return self._overworld_menu_behaviour

    def set_overworld_menu_behaviour(self, behaviour: OverworldMenuBehaviour) -> None:
        """Set overworld menu behavior"""
        self._overworld_menu_behaviour = behaviour

    @property
    def overworld_menu_fill_fp(self) -> bool:
        """Whether this fills FP in the overworld"""
        return self._overworld_menu_fill_fp

    def set_overworld_menu_fill_fp(self, fill_fp: bool) -> None:
        """Set whether this fills FP in the overworld"""
        self._overworld_menu_fill_fp = fill_fp

    @property
    def overworld_menu_fill_hp(self) -> bool:
        """Whether this fills HP in the overworld"""
        return self._overworld_menu_fill_hp

    def set_overworld_menu_fill_hp(self, fill_hp: bool) -> None:
        """Set whether this fills HP in the overworld"""
        self._overworld_menu_fill_hp = fill_hp

    @property
    def can_target_others(self) -> bool:
        """Whether this can target others"""
        return self._can_target_others

    def set_can_target_others(self, can_target_others: bool) -> None:
        """Set whether this can target others"""
        self._can_target_others = can_target_others

    @property
    def can_target_self(self) -> bool:
        """Whether this can target self"""
        return self._can_target_self

    def set_can_target_self(self, can_target_self: bool) -> None:
        """Set whether this can target self"""
        self._can_target_self = can_target_self

    @property
    def one_side_only(self) -> bool:
        """Whether this can only target one character"""
        return self._one_side_only

    def set_one_side_only(self, one_side_only: bool) -> None:
        """Set single target only restriction"""
        self._one_side_only = one_side_only

    @property
    def koed_target_only(self) -> bool:
        """Whether this can only target KOed characters"""
        return self._koed_target_only

    def set_koed_target_only(self, koed_target_only: bool) -> None:
        """Set KOed target only restriction"""
        self._koed_target_only = koed_target_only

    @property
    def target_enemies(self) -> bool:
        """Whether this can target enemies"""
        return self._target_enemies

    def set_target_enemies(self, target_enemies: bool) -> None:
        """Set enemy targeting"""
        self._target_enemies = target_enemies

    @property
    def target_all(self) -> bool:
        """Whether this can target party members"""
        return self._target_all

    def set_target_all(self, target_all: bool) -> None:
        """Set party targeting"""
        self._target_all = target_all

    @property
    def frog_coin_item(self) -> bool:
        """If true, item should only be purchasable in frog coin shops."""
        return self._frog_coin_item

    def _set_frog_coin_item(self, frog_coin_item: bool) -> None:
        self._frog_coin_item = frog_coin_item

    def __init__(self):
        if len(self.equip_chars) == 0:
            self.set_equip_chars([])
        if len(self.elemental_immunities) == 0:
            self._elemental_immunities = []
        if len(self.elemental_resistances) == 0:
            self._elemental_resistances = []
        if len(self.status_immunities) == 0:
            self._status_immunities = []
        if len(self.temp_buffs) == 0:
            self._temp_buffs = []

    @property
    def name(self) -> str:
        """Human readable item name"""
        if self._item_name != "":
            return self._item_name
        return self.__class__.__name__

    def __str__(self):
        return f"<{self.name}: price {self.price}>"

    def __repr__(self):
        return str(self)

    def become_frog_coin_item(self) -> None:
        """Makes it so that item is only purchasable in frog coin shops,
        and sets price accordingly."""
        if self.frog_coin_item:
            return

        price: int = max(math.ceil(self.rank_value / 5), 1)

        self.set_price(price)
        self._set_frog_coin_item(True)

    def unbecome_frog_coin_item(self) -> None:
        """Makes it so that item is only purchasable in regular coin shops,
        and sets price accordingly."""
        if not self.frog_coin_item:
            return

        factor = float(random.randint(50, random.randint(50, 100)))
        price = int(round(self.price * factor))

        self.set_price(min(price, 9999))
        self._set_frog_coin_item(False)

    def render(self) -> Dict[int, bytearray]:
        """Get data for this item in `{0x123456: bytearray([0x00])}` format"""
        patch: Dict[int, bytearray] = {}
        if self.price == 0:
            return patch
        base_addr = ITEMS_BASE_ADDRESS + (self.item_id * 18)

        # Stats and special properties.
        data = bytearray()
        val = self.type_value
        if self.usable_battle:
            val |= 1 << 3
        if self.usable_overworld:
            val |= 1 << 4
        if self._reusable:
            val |= 1 << 5
        if self.prevent_ko:
            val |= 1 << 7
        data += ByteField(val).as_bytes()

        val = 0
        if self.effect_type is not None:
            val = self.effect_type
        if self.overworld_menu_behaviour == OverworldMenuBehaviour.LEAD_TO_FP:
            val |= 1 << 5
        if self.overworld_menu_fill_hp:
            val |= 1 << 6
        if self.overworld_menu_fill_fp:
            val |= 1 << 7
        data += ByteField(val).as_bytes()

        val = 0
        for c in self.equip_chars:
            val += 1 << int(c)
        data += ByteField(val).as_bytes()

        target = (
            (self.can_target_others << 1)
            + (self.target_enemies << 2)
            + (self.target_all << 4)
            + (self.koed_target_only << 5)
            + (self.one_side_only << 6)
            + (not (self.can_target_self) << 7)
        )
        data += ByteField(target).as_bytes()

        if self.inflict_element is not None:
            data += ByteField(self.inflict_element[2]).as_bytes()
        else:
            data += ByteField(0).as_bytes()

        data += BitMapSet(
            1, [i.stat_value for i in self.elemental_immunities]
        ).as_bytes()

        data += BitMapSet(
            1, [r.stat_value for r in self.elemental_resistances]
        ).as_bytes()

        data += BitMapSet(1, [i.stat_value for i in self.status_immunities]).as_bytes()

        data += BitMapSet(1, self.temp_buffs).as_bytes()

        data += ByteField(self.speed).as_bytes()
        data += ByteField(self.attack).as_bytes()
        data += ByteField(self.defense).as_bytes()
        data += ByteField(self.magic_attack).as_bytes()
        data += ByteField(self.magic_defense).as_bytes()
        data += ByteField(self.variance).as_bytes()
        data += ByteField(self.inflict).as_bytes()

        if self.inflict_type is None:
            data += ByteField(0xDD).as_bytes()
        else:
            val = self.inflict_type
            if self.hide_damage:
                val |= 1 << 2
            data += ByteField(val).as_bytes()

        patch[base_addr] = data

        # Price
        price_addr = ITEMS_BASE_PRICE_ADDRESS + (self.item_id * 2)
        patch[price_addr] = ByteField(self.price, num_bytes=2).as_bytes()

        return patch


ItemT = TypeVar("ItemT", bound=Item)


class Equipment(Item):
    """Base class for weapons, armor, and accessories."""

    def set_speed(self, speed: int) -> None:
        """Modify the base speed increase for this equip."""
        assert -128 <= speed <= 127
        self._speed = speed

    def set_attack(self, attack: int) -> None:
        """Modify the base attack increase for this equip."""
        assert -128 <= attack <= 127
        self._attack = attack

    def set_defense(self, defense: int) -> None:
        """Modify the base defense increase for this equip."""
        assert -128 <= defense <= 127
        self._defense = defense

    def set_magic_attack(self, magic_attack: int) -> None:
        """Modify the base magic attack increase for this equip."""
        assert -128 <= magic_attack <= 127
        self._magic_attack = magic_attack

    def set_magic_defense(self, magic_defense: int) -> None:
        """Modify the base magic defense increase for this equip."""
        assert -128 <= magic_defense <= 127
        self._magic_defense = magic_defense

    def set_prevent_ko(self, prevent_ko: bool) -> None:
        """Modify the OHKO protection flag for this equip."""
        self._prevent_ko = prevent_ko

    def set_elemental_immunities(self, elemental_immunities: List[Element]) -> None:
        """Overwrite the elemental immunities for this equip."""
        self._elemental_immunities = deepcopy(elemental_immunities)

    def append_elemental_immunity(self, element: Element) -> None:
        """Add an elemental immunity to this equip."""
        if element not in self._elemental_immunities:
            self._elemental_immunities.append(element)

    def remove_elemental_immunity(self, element: Element) -> None:
        """Remove an elemental immunity from this equip."""
        if element in self._elemental_immunities:
            self._elemental_immunities.remove(element)

    def set_elemental_resistances(self, elemental_resistances: List[Element]) -> None:
        """Overwrite the elemental resistances for this equip."""
        self._elemental_resistances = deepcopy(elemental_resistances)

    def append_elemental_resistance(self, element: Element) -> None:
        """Add an elemental resistance to this equip."""
        if element not in self._elemental_resistances:
            self._elemental_resistances.append(element)

    def remove_elemental_resistance(self, element: Element) -> None:
        """Remove an elemental resistance from this equip."""
        if element in self._elemental_resistances:
            self._elemental_resistances.remove(element)

    def set_temp_buffs(self, temp_buffs: List[TempStatBuff]) -> None:
        """Overwrite the buff multipliers for this equip."""
        self._temp_buffs = deepcopy(temp_buffs)

    def append_temp_buff(self, buff: TempStatBuff) -> None:
        """Add a buff multiplier to this equip."""
        if buff not in self._temp_buffs:
            self._temp_buffs.append(buff)

    def remove_temp_buff(self, buff: TempStatBuff) -> None:
        """Remove a buff multiplier from this equip."""
        if buff in self._temp_buffs:
            self._temp_buffs.remove(buff)


class Weapon(Equipment):
    """Base class for all weapons.
    Also provides the weapon ID for unarmed attack animations."""

    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.WEAPON

    _half_time_window_begins: UInt8 = 0
    _perfect_window_begins: UInt8 = 0
    _perfect_window_ends: UInt8 = 0
    _half_time_window_ends: UInt8 = 0

    def set_variance(self, variance: int) -> None:
        """Sets the variance range on this weapon's damage RNG."""
        self._variance = UInt8(variance)

    @property
    def half_time_window_begins(self) -> UInt8:
        """Frame where half timing window starts"""
        return self._half_time_window_begins

    def set_half_time_window_begins(self, value: int) -> None:
        """Set frame for half timing window start"""
        self._half_time_window_begins = UInt8(value)

    @property
    def perfect_window_begins(self) -> UInt8:
        """Frame where perfect timing window starts"""
        return self._perfect_window_begins

    def set_perfect_window_begins(self, value: int) -> None:
        """Set frame for perfect timing window start"""
        self._perfect_window_begins = UInt8(value)

    @property
    def perfect_window_ends(self) -> UInt8:
        """Frame where perfect timing window ends"""
        return self._perfect_window_ends

    def set_perfect_window_ends(self, value: int) -> None:
        """Set frame for perfect timing window end"""
        self._perfect_window_ends = UInt8(value)

    @property
    def half_time_window_ends(self) -> UInt8:
        """Frame where half timing window ends"""
        return self._half_time_window_ends

    def set_half_time_window_ends(self, value: int) -> None:
        """Set frame for half timing window end"""
        self._half_time_window_ends = UInt8(value)

    def render(self) -> Dict[int, bytearray]:
        """Get data for this item in `{0x123456: bytearray([0x00])}` format"""
        if self.item_id > 40:
            raise TypeError("weapon IDs can only be 0-40")
        patch = super().render()
        if self.price == 0:
            return patch
        base_addr = ITEMS_BASE_TIMING_ADDRESS + (self.item_id * 4)

        data += ByteField(self.half_time_window_begins).as_bytes()
        data += ByteField(self.perfect_window_begins).as_bytes()
        data += ByteField(self.perfect_window_ends).as_bytes()
        data += ByteField(self.half_time_window_ends).as_bytes()

        patch[base_addr] = data

        return patch


class Armor(Equipment):
    """Base class for all armor."""

    _item_id: int = 1
    _type_value: ItemTypeValue = ItemTypeValue.ARMOR


class Accessory(Equipment):
    """Base class for all accessories."""

    _item_id: int = 2
    _type_value: ItemTypeValue = ItemTypeValue.ACCESSORY


class RegularItem(Item):
    """Base class for most obtainable, non-equippable items."""

    _type_value: ItemTypeValue = ItemTypeValue.ITEM

    @property
    def consumable(self) -> bool:
        return self._reusable == False
