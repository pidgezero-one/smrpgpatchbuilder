"""Base classes for playable characters."""

from copy import deepcopy
from typing import Dict, List


from smrpgpatchbuilder.datatypes.numbers.classes import (
    UInt4,
    UInt8,
    UInt16,
    ByteField,
    BitMapSet,
)

from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell

from .constants import (
    CHARACTER_BASE_ADDRESS,
    CHARACTER_BASE_LEARNED_SPELLS_ADDRESS,
    CHARACTER_BASE_STAT_BONUS_ADDRESS,
    CHARACTER_BASE_STAT_GROWTH_ADDRESS,
    LEVEL_CURVE,
    LEVELUP_BASE_ADDRESS,
)


class StatGrowth:
    """A container class for stat growth/bonus values for a certain level + character.

    Attributes:
        max_hp (UInt8): The max HP growth/bonus value.
        attack (UInt4): The attack growth/bonus value.
        defense (UInt4): The defense growth/bonus value.
        magic_attack (UInt4): The magic attack growth/bonus value.
        magic_defense (UInt4): The magic defense growth/bonus value.
    """

    _max_hp: UInt8 = UInt8(0)
    _attack: UInt4 = UInt4(0)
    _defense: UInt4 = UInt4(0)
    _magic_attack: UInt4 = UInt4(0)
    _magic_defense: UInt4 = UInt4(0)

    @property
    def max_hp(self) -> UInt8:
        """The max HP growth/bonus value."""
        return self._max_hp

    def set_max_hp(self, max_hp: int) -> None:
        """Sets the max HP growth/bonus value.

        Args:
            max_hp (int): The max HP growth/bonus value.
        """
        self._max_hp = UInt8(max_hp)

    @property
    def attack(self) -> UInt4:
        """The attack growth/bonus value."""
        return self._attack

    def set_attack(self, attack: int) -> None:
        """Sets the attack growth/bonus value.

        Args:
            attack (int): The attack growth/bonus value.
        """
        self._attack = UInt4(attack)

    @property
    def defense(self) -> UInt4:
        """The defense growth/bonus value."""
        return self._defense

    def set_defense(self, defense: int) -> None:
        """Sets the defense growth/bonus value.

        Args:
            defense (int): The defense growth/bonus value.
        """
        self._defense = UInt4(defense)

    @property
    def magic_attack(self) -> UInt4:
        """The magic attack growth/bonus value."""
        return self._magic_attack

    def set_magic_attack(self, magic_attack: int) -> None:
        """Sets the magic attack growth/bonus value.

        Args:
            magic_attack (int): The magic attack growth/bonus value.
        """
        self._magic_attack = UInt4(magic_attack)

    @property
    def magic_defense(self) -> UInt4:
        """The magic defense growth/bonus value."""
        return self._magic_defense

    def set_magic_defense(self, magic_defense: int) -> None:
        """Sets the magic defense growth/bonus value.

        Args:
            magic_defense (int): The magic defense growth/bonus value.
        """
        self._magic_defense = UInt4(magic_defense)

    def __init__(
        self,
        max_hp: int,
        attack: int,
        defense: int,
        magic_attack: int,
        magic_defense: int,
    ):
        self.set_max_hp(max_hp)
        self.set_attack(attack)
        self.set_defense(defense)
        self.set_magic_attack(magic_attack)
        self.set_magic_defense(magic_defense)

    @property
    def best_choices(self) -> "tuple[str]":
        """Best choice of attributes for a levelup bonus based on the numbers
        For HP, it must be twice the total of the attack + defense options
        to be considered "better". This is arbitrary, but HP is less useful."""
        options = [
            (self.max_hp / 2, ("max_hp",)),
            (self.attack + self.defense, ("attack", "defense")),
            (self.magic_attack + self.magic_defense, ("magic_attack", "magic_defense")),
        ]
        option_a, option_b = max(options)
        options = [(c, d) for (c, d) in options if c == option_a]
        option_a, option_b = options[0]
        return option_b

    def as_bytes(self) -> bytearray:
        """Return byte representation of this stat growth object for the patch."""
        data = bytearray()

        # HP is one byte on its own.
        # Attack/defense stats are 4 bits each combined into a single byte together.
        data += ByteField(self.max_hp).as_bytes()

        physical = self.attack << 4
        physical |= self.defense
        data += ByteField(physical).as_bytes()

        magical = self.magic_attack << 4
        magical |= self.magic_defense
        data += ByteField(magical).as_bytes()

        return data


class LevelUpExps:
    """Class for amounts of exp required for each levelup."""

    _levels: List[int] = []

    @property
    def levels(self) -> List[UInt16]:
        """Each value in this list is the amount of EXP needed to achieve
        the level corresponding to its index."""
        return [UInt16(l) for l in self._levels]

    def _set_levels(self, levels: List[int]) -> None:
        """Overwrite the list of EXP needed to achieve the level denoted
        by the value's index in the list (relative to the previous level)."""
        self._levels = levels

    def set_exp_for_level(self, exp: int, level: int):
        """Set the EXP needed to achieve the specific given level
        (relative to the previous level)."""
        assert 1 <= level <= 30
        self._levels[level] = UInt16(exp)

    def __init__(self):
        self._set_levels(deepcopy(LEVEL_CURVE))

    def get_xp_for_level(self, level: int) -> int:
        """
        The XP required to reach this level.
        """
        assert 1 <= level <= 30
        return self.levels[level - 1]

    def render(self) -> Dict[int, bytearray]:
        """Get data for exp required for each level up in `{0x123456: bytearray([0x00])}` format"""
        # Data is 29 blocks (starting at level 2), 2 bytes each block.
        data = bytearray()
        for level in range(2, 31):
            data += ByteField(self.get_xp_for_level(level)).as_bytes()

        patch: Dict[int, bytearray] = {}
        patch[LEVELUP_BASE_ADDRESS] = data
        return patch


class Character:
    """Base class for a playable character."""

    # Base stats.
    _character_id: int = 0
    _starting_level: int = 1
    _max_hp: UInt16 = UInt16(1)
    _speed: UInt8 = UInt8(1)
    _attack: UInt8 = UInt8(1)
    _defense: UInt8 = UInt8(1)
    _magic_attack: UInt8 = UInt8(1)
    _magic_defense: UInt8 = UInt8(1)
    _xp: UInt16 = UInt16(0)
    _learned_spells: Dict[int, CharacterSpell] = {}

    _starting_growths: List[StatGrowth] = []
    _levelup_bonuses: List[StatGrowth] = []

    @property
    def character_id(self) -> int:
        """A static ID number for this character."""
        return self._character_id

    @property
    def starting_level(self) -> int:
        """The level that this character should be when recruited."""
        return self._starting_level

    @property
    def max_hp(self) -> UInt16:
        """The max HP that this character has when recruited."""
        return self._max_hp

    @property
    def speed(self) -> UInt8:
        """The speed that this character has."""
        return self._speed

    @property
    def attack(self) -> UInt8:
        """The attack power that this character has when recruited."""
        return self._attack

    @property
    def defense(self) -> UInt8:
        """The defense that this character has when recruited."""
        return self._defense

    @property
    def magic_attack(self) -> UInt8:
        """The magic attack power that this character has when recruited."""
        return self._magic_attack

    @property
    def magic_defense(self) -> UInt8:
        """The magic defense that this character has when recruited."""
        return self._magic_defense

    @property
    def xp(self) -> UInt16:
        """The amount of XP the character has when recruited."""
        return self._xp

    @property
    def learned_spells(self) -> Dict[int, CharacterSpell]:
        """The list of spells the character will learn, and at which levels."""
        return self._learned_spells

    @property
    def starting_growths(self) -> List[StatGrowth]:
        """The base stat increases that are guaranteed at each level."""
        return self._starting_growths

    @property
    def levelup_bonuses(self) -> List[StatGrowth]:
        """The bonus stat increases that the player can choose from at each level."""
        return self._levelup_bonuses

    def __str__(self):
        """String representation of current state"""
        return f"<{self.name}>"

    def __repr__(self):
        """String representation of current state"""
        return str(self)

    @property
    def name(self):
        """String representation of class name"""
        return self.__class__.__name__

    def render(self) -> Dict[int, bytearray]:
        """Get data for this character in `{0x123456: bytearray([0x00])}` format"""
        patch: Dict[int, bytearray] = {}

        # Build character patch data.
        char_data = bytearray()
        char_data += ByteField(self.starting_level).as_bytes()
        char_data += ByteField(self.max_hp).as_bytes()  # Current HP
        char_data += ByteField(self.max_hp).as_bytes()  # Max HP
        char_data += ByteField(self.speed).as_bytes()
        char_data += ByteField(self.attack).as_bytes()
        char_data += ByteField(self.defense).as_bytes()
        char_data += ByteField(self.magic_attack).as_bytes()
        char_data += ByteField(self.magic_defense).as_bytes()
        char_data += ByteField(self.xp).as_bytes()
        # Set starting weapon/armor/accessory as blank for all characters.
        char_data += ByteField(0xFF).as_bytes()
        char_data += ByteField(0xFF).as_bytes()
        char_data += ByteField(0xFF).as_bytes()
        char_data.append(0x00)  # Unused byte

        starting_spells: List[CharacterSpell] = [
            spell
            for level, spell in self.learned_spells.items()
            if level < self.starting_level
        ]
        # TODO Ensure that less than 4 assigned spells are below the starting level

        assert len(starting_spells) <= 4
        char_data += BitMapSet(
            4,
            [int(spell.index) for spell in starting_spells],
        ).as_bytes()

        # Base address plus offset based on character index.
        addr = CHARACTER_BASE_ADDRESS + (self.character_id * 20)
        patch[addr] = char_data

        # Add levelup stat growth and bonuses to the patch data for this character.
        # Offset is 15 bytes for each stat object, 3 bytes per character.
        for growth_index, stat in enumerate(self.starting_growths):
            addr = (
                CHARACTER_BASE_STAT_GROWTH_ADDRESS
                + (growth_index * 15)
                + (self.character_id * 3)
            )
            patch[addr] = stat.as_bytes()

        for growth_index, stat in enumerate(self.levelup_bonuses):
            addr = (
                CHARACTER_BASE_STAT_BONUS_ADDRESS
                + (growth_index * 15)
                + (self.character_id * 3)
            )
            patch[addr] = stat.as_bytes()

        # Add learned spells data.
        # Data is 29 blocks (starting at level 2), 5 bytes each block
        # (1 byte per character in order)
        base_addr = CHARACTER_BASE_LEARNED_SPELLS_ADDRESS + self.character_id
        for level in range(2, 31):
            level_addr = base_addr + ((level - 2) * 5)
            # If we have a spell for this level, add the index.
            # Otherwise it should be 0xff for no spell learned.
            if self.learned_spells.get(level):
                patch[level_addr] = ByteField(
                    self.learned_spells[level].index
                ).as_bytes()
            else:
                patch[level_addr] = ByteField(0xFF).as_bytes()

        return patch
