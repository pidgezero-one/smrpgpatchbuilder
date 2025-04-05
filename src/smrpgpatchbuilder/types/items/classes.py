"""Base classes for item entities"""

from copy import deepcopy
import random
import math
from typing import List, TypeVar


from types.overworld_scripts.arguments.types import (
    PartyCharacter,
)
from types.numbers import UInt8, ByteField, BitMapSet
from types.patch import Patch

# target .enums specifically to prevent cyclic import
from types.spells.enums import Status, Element, TempStatBuff

from .enums import (
    ItemTypeValue,
)
from .constants import (
    ITEMS_BASE_ADDRESS,
    ITEMS_BASE_PRICE_ADDRESS,
)


class Item:
    """Parent class representing an item."""

    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.ITEM
    _item_name: str = ""
    _description: str = ""
    _consumable: bool = False
    _equip_chars: List[PartyCharacter] = []
    _speed: int = 0
    _attack: int = 0
    _defense: int = 0
    _magic_attack: int = 0
    _magic_defense: int = 0
    _variance: UInt8 = UInt8(0)
    _prevent_ko: bool = False
    _elemental_immunities: List[Element] = []
    _elemental_resistances: List[Element] = []
    _status_immunities: List[Status] = []
    _temp_buffs: List[TempStatBuff] = []
    _price: int = 0
    _frog_coin_item: bool = False

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

    def get_patch(self) -> Patch:
        """Get patch for this item."""
        patch = Patch()
        if self.price == 0:
            return patch
        base_addr = ITEMS_BASE_ADDRESS + (self.item_id * 18)

        # Stats and special properties.
        data = bytearray()
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
        patch.add_data(base_addr + 5, data)

        # Price
        price_addr = ITEMS_BASE_PRICE_ADDRESS + (self.item_id * 2)
        patch.add_data(price_addr, ByteField(self.price, num_bytes=2).as_bytes())

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

    def get_patch(self) -> Patch:
        """Get patch for this item."""
        patch = Patch()
        base_addr = ITEMS_BASE_ADDRESS + (self.item_id * 18)

        data = bytearray()

        # Only include initial item type and inflict/protect flags for equipment.

        # Item type and instant KO protection.
        val = self.type_value
        if self.prevent_ko:
            val |= 1 << 7
        data += ByteField(val).as_bytes()

        # Inflict/protect flags for status ailments/buffs.
        val = 0
        if self.status_immunities:
            val += 1 << 0
        if self.temp_buffs:
            val += 1 << 1
        data += ByteField(val).as_bytes()

        # Which characters can equip
        data += BitMapSet(1, self.equip_chars).as_bytes()

        patch.add_data(base_addr, data)

        patch += super().get_patch()

        return patch


class Weapon(Equipment):
    """Base class for all weapons.
    Also provides the weapon ID for unarmed attack animations."""

    _item_id: int = 0
    _type_value: ItemTypeValue = ItemTypeValue.WEAPON

    def set_variance(self, variance: int) -> None:
        """Sets the variance range on this weapon's damage RNG."""
        self._variance = UInt8(variance)


class Armor(Equipment):
    """Base class for all armor."""

    _item_id: int = 1
    _type_value: ItemTypeValue = ItemTypeValue.ARMOR


class Accessory(Equipment):
    """Base class for all accessories."""

    _item_id: int = 2
    _type_value: ItemTypeValue = ItemTypeValue.ACCESSORY