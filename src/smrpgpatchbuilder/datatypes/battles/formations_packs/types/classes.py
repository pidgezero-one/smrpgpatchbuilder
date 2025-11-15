"""Base class for formations, and battle packs, consisting of 3 formations."""

from random import choices
import statistics
from typing import List, Tuple, Type, Optional, Dict, Union


from smrpgpatchbuilder.datatypes.battles.enums import BattleMusic, Battlefields
from smrpgpatchbuilder.datatypes.battles.types.classes import Music
from smrpgpatchbuilder.datatypes.enemies.classes import Enemy
from smrpgpatchbuilder.datatypes.numbers.classes import (
    ByteField,
    BitMapSet,
    UInt16,
    UInt8,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield

from smrpgpatchbuilder.datatypes.battles.ids.misc import (
    BASE_FORMATION_ADDRESS,
    BASE_FORMATION_META_ADDRESS,
    TOTAL_FORMATIONS,
    PACK_BASE_ADDRESS,
)


class FormationMember:
    """Class representing a single enemy in a formation with metadata."""

    _hidden_at_start: bool
    _enemy: Type[Enemy]
    _x_pos: UInt8
    _y_pos: UInt8
    _anchor: bool
    _include_in_stat_totaling: bool

    @property
    def hidden_at_start(self) -> bool:
        """If true, this enemy will be hidden when the battle begins."""
        return self._hidden_at_start

    def set_hidden_at_start(self, hidden_at_start: bool) -> None:
        """If true, this enemy will be hidden when the battle begins."""
        self._hidden_at_start = hidden_at_start

    @property
    def enemy(self) -> Type[Enemy]:
        """The class of the enemy being included in the formation."""
        return self._enemy

    def set_enemy(self, enemy: Type[Enemy]) -> None:
        """Set the class of the enemy being included in the formation."""
        self._enemy = enemy

    @property
    def x_pos(self) -> UInt8:
        """The X coordinate that the enemy will be stationed at."""
        return self._x_pos

    def set_x_pos(self, x_pos: int) -> None:
        """Set the X coordinate that the enemy will be stationed at."""
        self._x_pos = UInt8(x_pos)

    @property
    def y_pos(self) -> UInt8:
        """The Y coordinate that the enemy will be stationed at."""
        return self._y_pos

    def set_y_pos(self, y_pos: int) -> None:
        """Set the Y coordinate that the enemy will be stationed at."""
        self._y_pos = UInt8(y_pos)

    @property
    def anchor(self) -> bool:
        """(deprecated)"""
        return self._anchor

    def set_anchor(self, anchor: bool) -> None:
        """(deprecated)"""
        self._anchor = anchor

    @property
    def include_in_stat_totaling(self) -> bool:
        """true by default. if false, this enemy's stats will not be considered
        when calculating the total stats for a boss location to distribute to
        the boss fight that is shuffled into it."""
        return self._include_in_stat_totaling

    def set_include_in_stat_totaling(self, include_in_stat_totaling: bool) -> None:
        """if false, this enemy's stats will not be considered
        when calculating the total stats for a boss location to distribute to
        the boss fight that is shuffled into it."""
        self._include_in_stat_totaling = include_in_stat_totaling

    def __init__(
        self,
        enemy: Type[Enemy],
        x_pos: int,
        y_pos: int,
        hidden_at_start: bool = False,
        anchor: bool = False,
        include_in_stat_totaling: bool = True,
    ) -> None:
        self.set_enemy(enemy)
        self.set_x_pos(x_pos)
        self.set_y_pos(y_pos)
        self.set_hidden_at_start(hidden_at_start)
        self.set_anchor(anchor)
        self.set_include_in_stat_totaling(include_in_stat_totaling)


class Formation:
    """A subclass that defines an arrangement of enemies in a battle."""

    _members: List[Optional[FormationMember]]
    _run_event_at_load: Optional[UInt8]
    _music: Optional[Music]
    _can_run_away: bool
    _unknown_byte: UInt8
    _unknown_bit: bool
    _battlefield: Battlefield

    @property
    def members(self) -> List[Optional[FormationMember]]:
        """A list of containers including info about enemies and their positioning."""
        return self._members

    def set_members(self, members: List[Optional[FormationMember]]) -> None:
        """Overwrite the list of containers including info about enemies and their positioning."""
        self._members = members
        self._members.extend([None] * (8 - len(self._members)))

    @property
    def run_event_at_load(self) -> Optional[UInt8]:
        """the event that should run at the start of the battle when this formation is used.
        If not set, no event will run."""
        return self._run_event_at_load

    def set_run_event_at_load(self, run_event_at_load: Optional[int]) -> None:
        """set the event that should run at the start of the battle when this formation is used.
        If not set, no event will run."""
        if run_event_at_load is None:
            self._run_event_at_load = run_event_at_load
        else:
            self._run_event_at_load = UInt8(run_event_at_load)

    @property
    def music(self) -> Optional[Music]:
        """The battle music that should accompany this formation."""
        return self._music

    def set_music(self, music: Optional[Music]) -> None:
        """Set the battle music that should accompany this formation."""
        self._music = music

    @property
    def can_run_away(self) -> bool:
        """If false, running away from this formation is impossible."""
        return self._can_run_away

    def set_can_run_away(self, can_run_away: bool) -> None:
        """If false, running away from this formation is impossible."""
        self._can_run_away = can_run_away

    @property
    def unknown_byte(self) -> UInt8:
        """(unknown)"""
        return self._unknown_byte

    def set_unknown_byte(self, unknown_byte: int) -> None:
        """(unknown)"""
        self._unknown_byte = UInt8(unknown_byte)

    @property
    def unknown_bit(self) -> bool:
        """(unknown)"""
        return self._unknown_bit

    def set_unknown_bit(self, unknown_bit: bool) -> None:
        """(unknown)"""
        self._unknown_bit = unknown_bit

    @property
    def battlefield(self) -> Battlefield:
        """Battlefield to use for this formation"""
        return self._battlefield

    def set_battlefield(
        self, battlefield: Battlefield
    ) -> None:
        """Battlefield to use for this formation"""
        self._battlefield = battlefield
        
    def __init__(
        self,
        members: List[Optional[FormationMember]],
        run_event_at_load: Optional[int] = None,
        music: Optional[Music] = None,
        can_run_away: bool = True,
        unknown_byte: int = 0,
        unknown_bit: bool = False,
    ) -> None:
        self.set_members(members)
        self.set_run_event_at_load(run_event_at_load)
        self.set_music(music)
        self.set_can_run_away(can_run_away)
        self.set_unknown_byte(unknown_byte)
        self.set_unknown_bit(unknown_bit)

    def render(self, formation_index: int) -> Dict[int, bytearray]:
        """Get formation data in `{0x123456: bytearray([0x00])}` format."""
        assert 0 <= formation_index < TOTAL_FORMATIONS
        patch: Dict[int, bytearray] = {}
        data = bytearray()

        # monsters present bitmap.
        monsters_present = [
            7 - index for (index, enemy) in enumerate(self.members) if enemy is not None
        ]
        data += BitMapSet(1, monsters_present).as_bytes()

        # monsters hidden bitmap.
        monsters_hidden = [
            7 - index
            for (index, enemy) in enumerate(self.members)
            if enemy is not None and enemy.hidden_at_start
        ]
        data += BitMapSet(1, monsters_hidden).as_bytes()

        # monster data.
        for index, member in enumerate(self.members):
            if member is not None:
                data += ByteField(index).as_bytes()
                data += ByteField(member.x_pos).as_bytes()
                data += ByteField(member.y_pos).as_bytes()
            else:
                data += ByteField(0).as_bytes()
                data += ByteField(0).as_bytes()
                data += ByteField(0).as_bytes()

        base_addr = BASE_FORMATION_ADDRESS + (formation_index * 26)
        patch[base_addr] = data

        # add formation metadata.
        data = bytearray([self.unknown_byte])
        data += ByteField(
            self.run_event_at_load if self.run_event_at_load is not None else 0xFF
        ).as_bytes()
        music_byte = (
            ((self.music.value if self.music else 0x30) << 2) + ((not self.can_run_away) * 0x02) + self.unknown_bit
        )
        data += ByteField(music_byte).as_bytes()

        base_addr = BASE_FORMATION_META_ADDRESS + formation_index * 3
        patch[base_addr] = data

        return patch


class FormationPack:
    """A pack containing either 1 or 3 Formation instances for battle."""

    _formations: List[Formation]

    @property
    def formations(self) -> List[Formation]:
        """The list of formations in this pack (either 1 or 3 formations)."""
        return self._formations

    def __init__(self, *formations: Formation) -> None:
        """Initialize a FormationPack with either 1 or 3 Formation instances.

        Args:
            *formations: Either 1 Formation (will be used for all 3 slots)
                        or 3 Formations (one for each slot)

        Raises:
            AssertionError: If not exactly 1 or 3 formations are provided
        """
        assert len(formations) in (1, 3), \
            f"FormationPack requires exactly 1 or 3 formations, got {len(formations)}"

        if len(formations) == 1:
            # Store 3 references to the same formation
            self._formations = [formations[0], formations[0], formations[0]]
        else:
            # Store the 3 different formations
            self._formations = list(formations)


class PackCollection:
    """Collection of 255 FormationPacks that manages formation deduplication and rendering."""

    _packs: List[FormationPack]

    @property
    def packs(self) -> List[FormationPack]:
        """The list of 255 FormationPacks in this collection."""
        return self._packs

    def __init__(self, packs: List[FormationPack]) -> None:
        """Initialize a PackCollection with exactly 255 FormationPacks.

        Args:
            packs: A list of exactly 255 FormationPack instances

        Raises:
            AssertionError: If not exactly 255 packs are provided
        """
        assert len(packs) == 255, \
            f"PackCollection requires exactly 255 packs, got {len(packs)}"
        self._packs = packs

    def _formations_equal(self, f1: Formation, f2: Formation) -> bool:
        """Check if two formations are identical by comparing their rendered output."""
        # Render both formations at index 0 to compare their data
        render1 = f1.render(0)
        render2 = f2.render(0)
        return render1 == render2

    def render(self) -> Dict[int, bytearray]:
        """Render all packs and formations, deduplicating identical formations.

        This method:
        1. Collects all unique formations from all packs
        2. Assigns IDs to each unique formation
        3. Renders all unique formations
        4. Renders all packs using the assigned formation IDs

        Returns:
            A dictionary mapping ROM addresses to bytearrays for patching
        """
        patch: Dict[int, bytearray] = {}

        # Collect all formations from all packs
        all_formations: List[Formation] = []
        for pack in self._packs:
            all_formations.extend(pack.formations)

        # Deduplicate formations and assign IDs
        unique_formations: List[Formation] = []
        formation_to_id: Dict[int, int] = {}  # Maps id(formation) to formation_id

        for formation in all_formations:
            # Check if this formation is identical to any existing unique formation
            found_id = None
            for idx, unique_formation in enumerate(unique_formations):
                if self._formations_equal(formation, unique_formation):
                    found_id = idx
                    break

            if found_id is not None:
                # Use existing formation ID
                formation_to_id[id(formation)] = found_id
            else:
                # Add as new unique formation
                formation_id = len(unique_formations)
                if formation_id >= TOTAL_FORMATIONS:
                    raise ValueError(
                        f"Too many unique formations: {formation_id + 1} unique formations found, "
                        f"but maximum is {TOTAL_FORMATIONS}. Please reduce the number of unique formations "
                        f"or reuse existing formations."
                    )
                unique_formations.append(formation)
                formation_to_id[id(formation)] = formation_id

        # Render all unique formations
        for formation_id, formation in enumerate(unique_formations):
            formation_patch = formation.render(formation_id)
            patch.update(formation_patch)

        # Render all packs using the assigned formation IDs
        for pack_index, pack in enumerate(self._packs):
            # Get the formation IDs for this pack
            formation_ids = [formation_to_id[id(f)] for f in pack.formations]

            # Render pack data
            data = bytearray()
            hi_num = False

            for formation_id in formation_ids:
                val = formation_id
                if val > 255:
                    hi_num = True
                    val -= 256
                data += ByteField(val).as_bytes()

            # high bank indicator
            val = 7 if hi_num else 0
            data += ByteField(val).as_bytes()

            base_addr = PACK_BASE_ADDRESS + (pack_index * 4)
            patch[base_addr] = data

        return patch
