"""Base classes for enemy attack data."""

from typing import List, Dict

from smrpgpatchbuilder.datatypes.numbers.classes import (
    BitMapSet,
    ByteField,
    UInt4,
    UInt8,
)

from smrpgpatchbuilder.datatypes.spells.enums import TempStatBuff, Status

from .constants import ENEMY_ATTACK_BASE_ADDRESS


class EnemyAttack:
    """Class representing an enemy attack."""

    # Default instance attributes.
    _index: int = 0
    _attack_level: int = 0
    _ohko: bool = False
    _damageless_flag_1: bool = False
    _hide_numbers: bool = False
    _damageless_flag_2: bool = False
    _hit_rate: int = 0
    _status_effects: List[Status] = []
    _buffs: List[TempStatBuff] = []

    @property
    def index(self) -> UInt8:
        """The enemy attack's unique index."""
        assert 0 <= self._index <= 128 or self._index == 251
        return UInt8(self._index)

    @property
    def attack_level(self) -> UInt4:
        """The relative damage output of this attack."""
        return UInt4(self._attack_level)

    def set_attack_level(self, attack_level: int) -> None:
        """Set the relative damage output of this attack."""
        assert 0 <= attack_level <= 7
        self._attack_level = attack_level

    @property
    def ohko(self) -> bool:
        """If true, the attack will OHKO when not blocked."""
        return self._ohko

    def set_ohko(self, ohko: bool) -> None:
        """If true, the attack will OHKO when not blocked."""
        self._ohko = ohko

    @property
    def damageless_flag_1(self) -> bool:
        """(unknown)"""
        return self._damageless_flag_1

    def set_damageless_flag_1(self, damageless_flag_1: bool) -> None:
        """(unknown)"""
        self._damageless_flag_1 = damageless_flag_1

    @property
    def hide_numbers(self) -> bool:
        """If true, the damage output will not be displayed on contact."""
        return self._hide_numbers

    def set_hide_numbers(self, hide_numbers: bool) -> None:
        """If true, the damage output will not be displayed on contact."""
        self._hide_numbers = hide_numbers

    @property
    def damageless_flag_2(self) -> bool:
        """(unknown)"""
        return self._damageless_flag_2

    def set_damageless_flag_2(self, damageless_flag_2: bool) -> None:
        """(unknown)"""
        self._damageless_flag_2 = damageless_flag_2

    @property
    def hit_rate(self) -> UInt8:
        """The success rate of this attack (max is 255)."""
        return UInt8(self._hit_rate)

    def set_hit_rate(self, hit_rate: int) -> None:
        """Set the success rate of this attack (max is 255)."""
        assert UInt8(hit_rate)
        self._hit_rate = hit_rate

    @property
    def status_effects(self) -> List[Status]:
        """The list of status effects that are induced by this attack.
        Since a party member can only have one status at a time, effectively only the
        status occupying the highest bit (referenced by stat_value) will be applied."""
        return self._status_effects

    def set_status_effects(self, status_effects: List[Status]) -> None:
        """Overwrite the list of status effects that are induced by this attack.
        Since a party member can only have one status at a time, effectively only the
        status occupying the highest bit (referenced by stat_value) will be applied."""
        self._status_effects = status_effects

    @property
    def buffs(self) -> List[TempStatBuff]:
        """The list of temporary buffs to be applied by this attack."""
        return self._buffs

    def set_buffs(self, buffs: List[TempStatBuff]) -> None:
        """Overwrite the list of temporary buffs to be applied by this attack."""
        self._buffs = buffs

    def __str__(self) -> str:
        return f"<{self.name}>"

    def __repr__(self) -> str:
        return str(self)

    @property
    def name(self) -> str:
        """Attack's default name"""
        return self.__class__.__name__

    def render(self) -> Dict[int, bytearray]:
        """Get data for this attack in `{0x123456: bytearray([0x00])}` format"""
        patch: Dict[int, bytearray] = {}
        base_addr = ENEMY_ATTACK_BASE_ADDRESS + (self.index * 4)

        data = bytearray()

        # First byte is attack level + damage type flags in a bitmap.
        attack_flags = [i for i in range(3) if self.attack_level & (1 << i)]
        if self.ohko:
            attack_flags.append(3)
        if self.damageless_flag_1:
            attack_flags.append(4)
        if self.hide_numbers:
            attack_flags.append(5)
        if self.damageless_flag_2:
            attack_flags.append(6)
        data += BitMapSet(1, attack_flags).as_bytes()

        # Other bytes are hit rate, status effects, and buffs.
        data += ByteField(self.hit_rate).as_bytes()
        data += BitMapSet(1, self.status_effects).as_bytes()
        data += BitMapSet(1, self.buffs).as_bytes()

        patch[base_addr] = data
        return patch
