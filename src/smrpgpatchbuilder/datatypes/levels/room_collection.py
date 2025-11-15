"""RoomCollection class for managing and rendering all 512 rooms in the game."""
from typing import Optional, Union
from smrpgpatchbuilder.datatypes.levels.classes import (
    Room, NPC, Partition, BaseRoomObject, RoomObject, Clone,
    BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone,
    RoomExit, MapExit
)


class RoomCollection:
    """Manages all 512 rooms and handles rendering them to ROM format."""

    _rooms: list[Optional[Room]]
    _large_partition_table: bool

    def __init__(self, rooms: list[Optional[Room]], large_partition_table: bool = False):
        """Initialize the room collection.

        Args:
            rooms: List of 512 rooms (some can be None)
            large_partition_table: If True, use extended partition table at 0x1DEBE0
        """
        assert len(rooms) == 512, f"Expected 512 rooms, got {len(rooms)}"
        # Ensure last room (511) is None
        assert rooms[511] is None, "Room 511 must be None"

        self._rooms = rooms
        self._large_partition_table = large_partition_table

    def _get_npc_signature(self, npc: NPC, room_obj: Optional[BaseRoomObject] = None) -> tuple:
        """Get a unique signature for an NPC that includes all properties.

        If room_obj is provided, include any BaseRoomObject-level overrides.
        """
        sig = [
            npc.sprite_id,
            npc.shadow_size,
            npc.acute_axis,
            npc.obtuse_axis,
            npc.height,
            npc.y_shift,
            npc.show_shadow,
            npc.directions,
            npc.min_vram_size,
            npc.priority_0,
            npc.priority_1,
            npc.priority_2,
            npc.cannot_clone,
            npc.byte2_bit0,
            npc.byte2_bit1,
            npc.byte2_bit2,
            npc.byte2_bit3,
            npc.byte2_bit4,
            npc.byte5_bit6,
            npc.byte5_bit7,
            npc.byte6_bit2,
        ]

        # Add BaseRoomObject overrides if present
        if room_obj:
            sig.extend([
                room_obj.show_shadow if room_obj.show_shadow is not None else None,
                room_obj.shadow_size if room_obj.shadow_size is not None else None,
                room_obj.y_shift if room_obj.y_shift is not None else None,
                room_obj.acute_axis if room_obj.acute_axis is not None else None,
                room_obj.obtuse_axis if room_obj.obtuse_axis is not None else None,
                room_obj.height if room_obj.height is not None else None,
                room_obj.directions if room_obj.directions is not None else None,
                room_obj.min_vram_size if room_obj.min_vram_size is not None else None,
                room_obj.priority_0 if room_obj.priority_0 is not None else None,
                room_obj.priority_1 if room_obj.priority_1 is not None else None,
                room_obj.priority_2 if room_obj.priority_2 is not None else None,
                room_obj.cannot_clone if room_obj.cannot_clone is not None else None,
                room_obj.byte2_bit0 if room_obj.byte2_bit0 is not None else None,
                room_obj.byte2_bit1 if room_obj.byte2_bit1 is not None else None,
                room_obj.byte2_bit2 if room_obj.byte2_bit2 is not None else None,
                room_obj.byte2_bit3 if room_obj.byte2_bit3 is not None else None,
                room_obj.byte2_bit4 if room_obj.byte2_bit4 is not None else None,
                room_obj.byte5_bit6 if room_obj.byte5_bit6 is not None else None,
                room_obj.byte5_bit7 if room_obj.byte5_bit7 is not None else None,
                room_obj.byte6_bit2 if room_obj.byte6_bit2 is not None else None,
            ])

        return tuple(sig)

    def _build_npc_table(self) -> tuple[list[NPC], dict[tuple, int]]:
        """Build unique NPC table and mapping.

        Returns:
            Tuple of (unique_npcs, npc_signature_to_index)

        Raises:
            ValueError: If more than allowed NPCs (0x1DDE00 - 0x1DB800 bytes / 7 bytes per NPC)
        """
        max_npcs = (0x1DDE00 - 0x1DB800) // 7  # ~1143 NPCs max

        unique_npcs: list[NPC] = []
        npc_signature_to_index: dict[tuple, int] = {}

        for room_idx, room in enumerate(self._rooms):
            if room is None:
                continue

            for obj in room.objects:
                if isinstance(obj, Clone):
                    continue  # Clones don't need unique NPC entries

                # Get signature including any room-level overrides
                sig = self._get_npc_signature(obj._npc, obj)

                if sig not in npc_signature_to_index:
                    if len(unique_npcs) >= max_npcs:
                        raise ValueError(
                            f"Too many unique NPCs: {len(unique_npcs)} exceeds maximum of {max_npcs}"
                        )
                    npc_signature_to_index[sig] = len(unique_npcs)
                    # Create new NPC with room-level overrides applied
                    unique_npcs.append(self._create_merged_npc(obj._npc, obj))

        return unique_npcs, npc_signature_to_index

    def _create_merged_npc(self, base_npc: NPC, room_obj: BaseRoomObject) -> NPC:
        """Create a new NPC with room-level overrides merged in."""
        # Start with base NPC properties
        merged = NPC(
            sprite_id=base_npc.sprite_id,
            shadow_size=room_obj.shadow_size if room_obj.shadow_size is not None else base_npc.shadow_size,
            acute_axis=room_obj.acute_axis if room_obj.acute_axis is not None else base_npc.acute_axis,
            obtuse_axis=room_obj.obtuse_axis if room_obj.obtuse_axis is not None else base_npc.obtuse_axis,
            height=room_obj.height if room_obj.height is not None else base_npc.height,
            y_shift=room_obj.y_shift if room_obj.y_shift is not None else base_npc.y_shift,
            show_shadow=room_obj.show_shadow if room_obj.show_shadow is not None else base_npc.show_shadow,
            directions=room_obj.directions if room_obj.directions is not None else base_npc.directions,
            min_vram_size=room_obj.min_vram_size if room_obj.min_vram_size is not None else base_npc.min_vram_size,
            priority_0=room_obj.priority_0 if room_obj.priority_0 is not None else base_npc.priority_0,
            priority_1=room_obj.priority_1 if room_obj.priority_1 is not None else base_npc.priority_1,
            priority_2=room_obj.priority_2 if room_obj.priority_2 is not None else base_npc.priority_2,
            cannot_clone=room_obj.cannot_clone if room_obj.cannot_clone is not None else base_npc.cannot_clone,
            byte2_bit0=room_obj.byte2_bit0 if room_obj.byte2_bit0 is not None else base_npc.byte2_bit0,
            byte2_bit1=room_obj.byte2_bit1 if room_obj.byte2_bit1 is not None else base_npc.byte2_bit1,
            byte2_bit2=room_obj.byte2_bit2 if room_obj.byte2_bit2 is not None else base_npc.byte2_bit2,
            byte2_bit3=room_obj.byte2_bit3 if room_obj.byte2_bit3 is not None else base_npc.byte2_bit3,
            byte2_bit4=room_obj.byte2_bit4 if room_obj.byte2_bit4 is not None else base_npc.byte2_bit4,
            byte5_bit6=room_obj.byte5_bit6 if room_obj.byte5_bit6 is not None else base_npc.byte5_bit6,
            byte5_bit7=room_obj.byte5_bit7 if room_obj.byte5_bit7 is not None else base_npc.byte5_bit7,
            byte6_bit2=room_obj.byte6_bit2 if room_obj.byte6_bit2 is not None else base_npc.byte6_bit2,
        )
        return merged

    def _validate_and_fix_clones(self, unique_npcs: list[NPC], npc_signature_to_index: dict[tuple, int]):
        """Validate clone constraints and insert intermediate NPCs if needed.

        Modifies unique_npcs and npc_signature_to_index in place.

        Raises:
            ValueError: If clones violate constraints that can't be auto-fixed
        """
        for room_idx, room in enumerate(self._rooms):
            if room is None:
                continue

            last_non_clone = None
            clone_group = []  # Track consecutive clones

            for obj_idx, obj in enumerate(room.objects):
                if isinstance(obj, Clone):
                    if last_non_clone is None:
                        raise ValueError(
                            f"Room {room_idx}: Clone at index {obj_idx} has no preceding non-clone object"
                        )

                    # Validate clone type matches parent type
                    if isinstance(obj, RegularClone) and not isinstance(last_non_clone, RegularNPC):
                        raise ValueError(
                            f"Room {room_idx}: RegularClone at index {obj_idx} must follow a RegularNPC, "
                            f"but follows {type(last_non_clone).__name__}"
                        )
                    elif isinstance(obj, ChestClone) and not isinstance(last_non_clone, ChestNPC):
                        raise ValueError(
                            f"Room {room_idx}: ChestClone at index {obj_idx} must follow a ChestNPC, "
                            f"but follows {type(last_non_clone).__name__}"
                        )
                    elif isinstance(obj, BattlePackClone) and not isinstance(last_non_clone, BattlePackNPC):
                        raise ValueError(
                            f"Room {room_idx}: BattlePackClone at index {obj_idx} must follow a BattlePackNPC, "
                            f"but follows {type(last_non_clone).__name__}"
                        )

                    clone_group.append(obj)

                    # Validate action script difference
                    action_diff = abs(obj.action_script - last_non_clone.action_script)
                    if action_diff > 15:
                        raise ValueError(
                            f"Room {room_idx}: Clone at {obj_idx} has action_script {obj.action_script} "
                            f"which is {action_diff} away from parent's {last_non_clone.action_script} (max 15)"
                        )

                    # Validate type-specific constraints
                    if isinstance(obj, RegularClone) and isinstance(last_non_clone, RegularNPC):
                        event_diff = abs(obj.event_script - last_non_clone.event_script)
                        if event_diff > 7:
                            raise ValueError(
                                f"Room {room_idx}: RegularClone at {obj_idx} has event_script {obj.event_script} "
                                f"which is {event_diff} away from parent's {last_non_clone.event_script} (max 7)"
                            )

                    elif isinstance(obj, BattlePackClone) and isinstance(last_non_clone, BattlePackNPC):
                        pack_diff = abs(obj.battle_pack - last_non_clone.battle_pack)
                        if pack_diff > 15:
                            raise ValueError(
                                f"Room {room_idx}: BattlePackClone at {obj_idx} has battle_pack {obj.battle_pack} "
                                f"which is {pack_diff} away from parent's {last_non_clone.battle_pack} (max 15)"
                            )

                else:
                    # Process accumulated clone group
                    if clone_group and last_non_clone:
                        self._process_clone_group(last_non_clone, clone_group, unique_npcs, npc_signature_to_index, room_idx)

                    # Reset for next group
                    last_non_clone = obj
                    clone_group = []

            # Process final clone group if any
            if clone_group and last_non_clone:
                self._process_clone_group(last_non_clone, clone_group, unique_npcs, npc_signature_to_index, room_idx)

    def _process_clone_group(self, parent: RoomObject, clones: list[Clone], unique_npcs: list[NPC],
                            npc_signature_to_index: dict[tuple, int], room_idx: int):
        """Process a group of consecutive clones, inserting intermediate NPCs if needed."""
        # Collect all unique NPCs needed (parent + all clones with different NPCs)
        needed_npc_indices = []

        parent_sig = self._get_npc_signature(parent._npc, parent)
        parent_npc_idx = npc_signature_to_index[parent_sig]
        needed_npc_indices.append(parent_npc_idx)

        for clone in clones:
            clone_sig = self._get_npc_signature(clone._npc, clone)
            clone_npc_idx = npc_signature_to_index.get(clone_sig, parent_npc_idx)
            if clone_npc_idx not in needed_npc_indices:
                needed_npc_indices.append(clone_npc_idx)

        # Check if all NPCs fit within a 7-index range
        if len(needed_npc_indices) > 8:  # Parent + 7 different clones
            raise ValueError(
                f"Room {room_idx}: Clone group has {len(needed_npc_indices)} different NPCs (max 8)"
            )

        # Check if they're already sequential
        needed_npc_indices.sort()
        if needed_npc_indices[-1] - needed_npc_indices[0] <= 7:
            return  # Already fits, no need for intermediate NPCs

        # Need to create sequential copies at end of NPC table
        new_base_idx = len(unique_npcs)

        for i, old_idx in enumerate(needed_npc_indices):
            # Copy the NPC
            npc_copy = unique_npcs[old_idx]
            unique_npcs.append(npc_copy)

            # Update the signature mapping for objects using this NPC
            # We need to update references for the parent and clones
            if old_idx == parent_npc_idx:
                new_parent_sig = self._get_npc_signature(npc_copy, parent)
                npc_signature_to_index[new_parent_sig] = new_base_idx + i

            for clone in clones:
                clone_sig = self._get_npc_signature(clone._npc, clone)
                if npc_signature_to_index.get(clone_sig, parent_npc_idx) == old_idx:
                    npc_signature_to_index[clone_sig] = new_base_idx + i

    def _build_partition_table(self) -> tuple[list[Partition], dict]:
        """Build partition table.

        Returns:
            Tuple of (unique_partitions, room_to_partition_index)

        Raises:
            ValueError: If more than 128 unique partitions when large_partition_table is False
        """
        if self._large_partition_table:
            # Each room gets its own partition
            partitions = []
            room_to_partition_index = {}

            for room_idx, room in enumerate(self._rooms):
                if room is None or room.partition is None:
                    partitions.append(None)
                    room_to_partition_index[room_idx] = room_idx
                else:
                    partitions.append(room.partition)
                    room_to_partition_index[room_idx] = room_idx

            return partitions, room_to_partition_index
        else:
            # Collect unique partitions (max 128)
            unique_partitions: list[Partition] = []
            partition_to_index: dict[int, int] = {}  # id(partition) -> index
            room_to_partition_index: dict[int, int] = {}

            for room_idx, room in enumerate(self._rooms):
                if room is None or room.partition is None:
                    room_to_partition_index[room_idx] = 0  # Default partition
                    if 0 not in partition_to_index:
                        # Add default partition
                        unique_partitions.append(Partition())
                        partition_to_index[0] = 0
                    continue

                # Check if we already have this partition
                partition_id = None
                for existing_idx, existing_partition in enumerate(unique_partitions):
                    if existing_partition.is_same(room.partition):
                        partition_id = existing_idx
                        break

                if partition_id is None:
                    # New unique partition
                    if len(unique_partitions) >= 128:
                        raise ValueError(
                            f"Too many unique partitions: {len(unique_partitions)} exceeds maximum of 128. "
                            f"Consider using --large-partition-table flag."
                        )
                    partition_id = len(unique_partitions)
                    unique_partitions.append(room.partition)
                    partition_to_index[id(room.partition)] = partition_id

                room_to_partition_index[room_idx] = partition_id

            return unique_partitions, room_to_partition_index

    def render(self) -> dict[int, bytearray]:
        """Render all rooms to ROM patches.

        Returns:
            Dictionary mapping ROM addresses to byte data to write at those addresses

        Raises:
            ValueError: If constraints are violated
        """
        patches = {}

        # Build NPC table
        unique_npcs, npc_signature_to_index = self._build_npc_table()

        # Validate and fix clones
        self._validate_and_fix_clones(unique_npcs, npc_signature_to_index)

        # Build partition table
        partitions, room_to_partition_index = self._build_partition_table()

        # Write partition table bank pointer
        if self._large_partition_table:
            # Write [0xE0 0xEB] to 0x008BB0 and 0x008B9D
            patches[0x008BB0] = bytearray([0xE0, 0xEB])
            patches[0x008B9D] = bytearray([0xE0, 0xEB])

            # Write partitions to 0x1DEBE0-0x1DF3DF (512 partitions * 4 bytes)
            partition_start = 0x1DEBE0
            for idx in range(512):
                offset = partition_start + (idx * 4)
                if idx < len(partitions) and partitions[idx] is not None:
                    patches[offset] = self._render_partition(partitions[idx])
                else:
                    # Default partition
                    patches[offset] = bytearray([0x00, 0x00, 0x00, 0x00])
        else:
            # Write [0x00 0xDE] to 0x008BB0 and 0x008B9D
            patches[0x008BB0] = bytearray([0x00, 0xDE])
            patches[0x008B9D] = bytearray([0x00, 0xDE])

            # Write partitions to 0x1DDE00-0x1DDFFF (128 partitions * 4 bytes)
            partition_start = 0x1DDE00
            for idx, partition in enumerate(partitions):
                offset = partition_start + (idx * 4)
                patches[offset] = self._render_partition(partition)

        # Write NPC table to 0x1DB800-0x1DDDFF
        npc_start = 0x1DB800
        for idx, npc in enumerate(unique_npcs):
            offset = npc_start + (idx * 7)
            patches[offset] = self._render_npc(npc)

        # Fill remaining NPC slots with 0xFF
        for idx in range(len(unique_npcs), (0x1DDE00 - 0x1DB800) // 7):
            offset = npc_start + (idx * 7)
            patches[offset] = bytearray([0xFF] * 7)

        # Render room object data (NPCs)
        room_object_patches = self._render_room_objects(npc_signature_to_index, room_to_partition_index)
        patches.update(room_object_patches)

        # Render event data
        event_patches = self._render_events()
        patches.update(event_patches)

        # Render exit data
        exit_patches = self._render_exits()
        patches.update(exit_patches)

        return patches

    def _render_partition(self, partition: Partition) -> bytearray:
        """Render a partition to 4 bytes."""
        data = bytearray(4)

        # Byte 0
        data[0] = (partition.ally_sprite_buffer_size << 5) | (0x10 if partition.allow_extra_sprite_buffer else 0) | partition.extra_sprite_buffer_size | (0x80 if partition.full_palette_buffer else 0)

        # Bytes 1-3: buffers
        for buf_idx in range(3):
            buf = partition.buffers[buf_idx]
            byte_val = buf.buffer_type | (buf.main_buffer_space << 4) | (0x80 if buf.index_in_main_buffer else 0)
            data[buf_idx + 1] = byte_val

        return data

    def _render_npc(self, npc: NPC) -> bytearray:
        """Render an NPC to 7 bytes."""
        data = bytearray(7)

        # Bytes 0-1: sprite_id (10 bits) + vram_store (3 bits) + vram_size (3 bits)
        data[0] = npc.sprite_id & 0xFF
        data[1] = ((npc.sprite_id >> 8) & 0x03) | ((npc.directions & 0x07) << 2) | ((npc.min_vram_size & 0x07) << 5)

        # Byte 2: priority and misc bits
        data[2] = (
            (1 if npc.byte2_bit0 else 0) |
            ((1 if npc.byte2_bit1 else 0) << 1) |
            ((1 if npc.byte2_bit2 else 0) << 2) |
            ((1 if npc.byte2_bit3 else 0) << 3) |
            ((1 if npc.byte2_bit4 else 0) << 4) |
            ((1 if npc.priority_0 else 0) << 5) |
            ((1 if npc.priority_1 else 0) << 6) |
            ((1 if npc.priority_2 else 0) << 7)
        )

        # Byte 3: y_shift (4 bits) + shift_16_px_down (1 bit) + shadow_size (2 bits) + cannot_clone (1 bit)
        y_shift_val = npc.y_shift if npc.y_shift >= 0 else npc.y_shift + 16
        shift_16_down = 1 if npc.y_shift < 0 else 0
        data[3] = (y_shift_val & 0x0F) | ((shift_16_down) << 4) | ((npc.shadow_size & 0x03) << 5) | ((1 if npc.cannot_clone else 0) << 7)

        # Byte 4: acute_axis (4 bits) + obtuse_axis (4 bits)
        data[4] = (npc.acute_axis & 0x0F) | ((npc.obtuse_axis & 0x0F) << 4)

        # Byte 5: height (5 bits) + show_shadow (1 bit) + byte5_bit6 (1 bit) + byte5_bit7 (1 bit)
        data[5] = (npc.height & 0x1F) | ((1 if npc.show_shadow else 0) << 5) | ((1 if npc.byte5_bit6 else 0) << 6) | ((1 if npc.byte5_bit7 else 0) << 7)

        # Byte 6: byte6_bit2 and reserved bits
        data[6] = ((1 if npc.byte6_bit2 else 0) << 2)

        return data

    def _render_room_objects(self, npc_signature_to_index: dict[tuple, int],
                            room_to_partition_index: dict[int, int]) -> dict[int, bytearray]:
        """Render room object (NPC) data.

        Pointer table: 0x148000-0x1483FF (512 rooms * 2 bytes)
        Data section: 0x148400-0x14FFFF

        Returns:
            Dictionary of patches
        """
        patches = {}
        pointer_table_start = 0x148000
        data_section_start = 0x148400
        data_offset = data_section_start

        # Build all room data first
        all_room_data = bytearray()

        for room_idx in range(512):
            room = self._rooms[room_idx]

            # Write pointer (little-endian offset from start of data section)
            pointer_value = data_offset - data_section_start
            patches[pointer_table_start + (room_idx * 2)] = bytearray([
                pointer_value & 0xFF,
                (pointer_value >> 8) & 0xFF
            ])

            if room is None or len(room.objects) == 0:
                # Empty room - next room will have same pointer (zero delta)
                continue

            # First byte: partition ID
            partition_id = room_to_partition_index.get(room_idx, 0)
            all_room_data.append(partition_id)
            data_offset += 1

            # Render each object (track parent for clones and count extra_length)
            last_parent = None
            obj_idx = 0
            while obj_idx < len(room.objects):
                obj = room.objects[obj_idx]

                if isinstance(obj, Clone):
                    # This is a clone, render it
                    obj_data = self._render_room_object(obj, npc_signature_to_index, last_parent)
                    all_room_data.extend(obj_data)
                    data_offset += len(obj_data)
                    obj_idx += 1
                else:
                    # This is a parent object - count consecutive clones
                    clone_count = 0
                    check_idx = obj_idx + 1
                    while check_idx < len(room.objects) and isinstance(room.objects[check_idx], Clone):
                        clone_count += 1
                        check_idx += 1

                    # Render parent with correct extra_length
                    obj_data = self._render_room_object(obj, npc_signature_to_index, None)
                    # Update byte 0 with clone count
                    obj_data[0] = (obj.object_type << 4) | (clone_count & 0x0F)
                    all_room_data.extend(obj_data)
                    data_offset += len(obj_data)

                    last_parent = obj
                    obj_idx += 1

        # Write all room data as a single patch
        if len(all_room_data) > 0:
            patches[data_section_start] = all_room_data

        return patches

    def _render_room_object(self, obj: BaseRoomObject, npc_signature_to_index: dict[tuple, int],
                           parent: Optional[RoomObject] = None) -> bytearray:
        """Render a single room object to bytes.

        Args:
            obj: The room object to render
            npc_signature_to_index: Mapping from NPC signatures to indices
            parent: The parent object (required for clones)
        """
        # Get NPC index
        obj_sig = self._get_npc_signature(obj._npc, obj)
        npc_index = npc_signature_to_index[obj_sig]

        if isinstance(obj, Clone):
            # Clone: 4 bytes
            # Follows disassembler lines 744-784
            if parent is None:
                raise ValueError("Clone object requires parent object")

            data = bytearray(4)

            # Get parent NPC index for calculating offsets
            parent_sig = self._get_npc_signature(parent._npc, parent)
            parent_npc_index = npc_signature_to_index[parent_sig]

            # Byte 0: Offsets (type-specific encoding)
            if isinstance(obj, RegularClone):
                assert isinstance(parent, RegularNPC), "Parent must be RegularNPC for RegularClone"
                # (event_offset << 5) + (action_offset << 3) + npc_offset
                npc_offset = npc_index - parent_npc_index
                action_offset = obj.action_script - parent.action_script
                event_offset = obj.event_script - parent.event_script
                data[0] = (event_offset << 5) | (action_offset << 3) | (npc_offset & 0x07)
            elif isinstance(obj, ChestClone):
                assert isinstance(parent, ChestNPC), "Parent must be ChestNPC for ChestClone"
                # (upper_70a7 << 4) + lower_70a7
                data[0] = (obj.upper_70a7 << 4) | (obj.lower_70a7 & 0x0F)
            elif isinstance(obj, BattlePackClone):
                assert isinstance(parent, BattlePackNPC), "Parent must be BattlePackNPC for BattlePackClone"
                # (pack_offset << 4) + action_offset
                action_offset = obj.action_script - parent.action_script
                pack_offset = obj.battle_pack - parent.battle_pack
                data[0] = (pack_offset << 4) | (action_offset & 0x0F)
            else:
                data[0] = 0

            # Byte 1: (visible << 7) | x
            data[1] = (1 if obj.visible else 0) << 7 | (obj.x & 0x7F)

            # Byte 2: (z_half << 7) | y
            data[2] = (1 if obj.z_half else 0) << 7 | (obj.y & 0x7F)

            # Byte 3: (direction << 5) | z
            data[3] = (obj.direction << 5) | (obj.z & 0x1F)

            return data

        else:
            assert isinstance(obj, RoomObject), "Parent object must be RoomObject"
            # Parent object: 12 bytes + (extra_length * 4)
            # Follows disassembler lines 625-738

            # Calculate extra_length (number of clones)
            extra_length = 0
            # This will be set by _render_room_objects based on consecutive clones

            data = bytearray(12)

            # Byte 0: (object_type << 4) | extra_length
            # Note: extra_length will be updated by caller
            data[0] = (obj.object_type << 4) | 0  # Placeholder for extra_length

            # Byte 1: Movement flags byte 1
            # speed (bits 0-2), face_on_trigger (bit 3), cant_enter_doors (bit 4),
            # byte2_bit5 (bit 5), set_sequence_playback (bit 6), cant_float (bit 7)
            data[1] = (
                (obj.speed & 0x07) |
                ((1 if obj.face_on_trigger else 0) << 3) |
                ((1 if obj.cant_enter_doors else 0) << 4) |
                ((1 if obj.byte2_bit5 else 0) << 5) |
                ((1 if obj.set_sequence_playback else 0) << 6) |
                ((1 if obj.cant_float else 0) << 7)
            )

            # Byte 2: Movement flags byte 2
            data[2] = (
                (1 if obj.cant_walk_up_stairs else 0) |
                ((1 if obj.cant_walk_under else 0) << 1) |
                ((1 if obj.cant_pass_walls else 0) << 2) |
                ((1 if obj.cant_jump_through else 0) << 3) |
                ((1 if obj.cant_pass_npcs else 0) << 4) |
                ((1 if obj.byte3_bit5 else 0) << 5) |
                ((1 if obj.cant_walk_through else 0) << 6) |
                ((1 if obj.byte3_bit7 else 0) << 7)
            )

            # Bytes 3-5: NPC ID and action script (packed)
            # base_assigned_npc = ((d[offset + 4] & 0x0F) << 6) + (d[offset + 3] >> 2)
            # base_action_script = ((d[offset + 5] & 0x3F) << 4) + ((d[offset + 4] & 0xFF) >> 4)

            # Byte 3: (base_npc_id << 2) low 8 bits + slidable_along_walls (bit 0) + cant_move_if_in_air (bit 1)
            data[3] = ((npc_index << 2) & 0xFF) | (1 if obj.slidable_along_walls else 0) | ((1 if obj.cant_move_if_in_air else 0) << 1)

            # Byte 4: (action_script low 4 bits << 4) + (base_npc_id >> 6)
            data[4] = ((obj.action_script & 0x0F) << 4) | ((npc_index >> 6) & 0x0F)

            # Byte 5: byte7_upper2 (bits 6-7) + (action_script >> 4 in low 6 bits)
            data[5] = ((obj.byte7_upper2 & 0x03) << 6) | ((obj.action_script >> 4) & 0x3F)

            # Bytes 6-7: Event ID or battle pack + initiator
            if isinstance(obj, BattlePackNPC):
                # Byte 6: battle_pack
                data[6] = obj.battle_pack & 0xFF
                # Byte 7: (initiator << 4) + after_battle
                data[7] = (obj.initiator << 4) | (obj.after_battle & 0x0F)
            else:
                assert isinstance(obj, (RegularNPC, ChestNPC)), "Parent object must be RegularNPC, ChestNPC, or BattlePackNPC"
                # Regular or Chest NPC
                # Byte 6: event_id low 8 bits
                data[6] = obj.event_script & 0xFF
                # Byte 7: (initiator << 4) + event_id high 4 bits
                data[7] = (obj.initiator << 4) | ((obj.event_script >> 8) & 0x0F)

            # Byte 8: Offsets (type-specific, all zeros for parent)
            if isinstance(obj, RegularNPC):
                # (event_offset << 5) + (action_offset << 3) + npc_offset
                # For parent, all offsets are 0
                data[8] = 0
            elif isinstance(obj, ChestNPC):
                # (upper_70a7 << 4) + lower_70a7
                data[8] = (obj.upper_70a7 << 4) | (obj.lower_70a7 & 0x0F)
            elif isinstance(obj, BattlePackNPC):
                # (pack_offset << 4) + action_offset
                # For parent, all offsets are 0
                data[8] = 0
            else:
                data[8] = 0

            # Byte 9: (visible << 7) | x
            data[9] = (1 if obj.visible else 0) << 7 | (obj.x & 0x7F)

            # Byte 10: (z_half << 7) | y
            data[10] = (1 if obj.z_half else 0) << 7 | (obj.y & 0x7F)

            # Byte 11: (direction << 5) | z
            data[11] = (obj.direction << 5) | (obj.z & 0x1F)

            return data

    def _render_events(self) -> dict[int, bytearray]:
        """Render event data.

        Pointer table: 0x20E000-0x20E3FF (512 rooms * 2 bytes)
        Data section: 0x20E400-0x20FFFF

        Returns:
            Dictionary of patches
        """
        patches = {}
        pointer_table_start = 0x20E000
        data_section_start = 0x20E400
        data_offset = data_section_start

        # Build all event data first
        all_event_data = bytearray()

        for room_idx in range(512):
            room = self._rooms[room_idx]

            # Write pointer (little-endian offset from start of data section)
            pointer_value = data_offset - data_section_start
            patches[pointer_table_start + (room_idx * 2)] = bytearray([
                pointer_value & 0xFF,
                (pointer_value >> 8) & 0xFF
            ])

            # Always write 3-byte header (music + entrance_event)
            if room is None:
                # Default header
                all_event_data.extend(bytearray([0x00, 0x00, 0x00]))
                data_offset += 3
            else:
                assert isinstance(room, Room), "Expected Room instance"
                # Write music (byte 0) and entrance_event (bytes 1-2, little-endian)
                all_event_data.append(room.music)
                all_event_data.append(room.entrance_event & 0xFF)
                all_event_data.append((room.entrance_event >> 8) & 0xFF)
                data_offset += 3

                # Write event tiles if any
                if room.event_tiles:
                    for event in room.event_tiles:
                        event_data = self._render_event(event)
                        all_event_data.extend(event_data)
                        data_offset += len(event_data)

        # Write all event data as a single patch
        if len(all_event_data) > 0:
            patches[data_section_start] = all_event_data

        return patches

    def _render_event(self, event) -> bytearray:
        """Render a single event tile to bytes.

        Follows disassembler lines 424-454.
        """
        from smrpgpatchbuilder.datatypes.levels.classes import Event

        if isinstance(event, Event):
            # Event: 5 or 6 bytes depending on length
            # Disassembler reads:
            # trigger_data[0-1]: event value (12 bits, little-endian)
            # trigger_data[2]: x + (nw_se_edge_active << 7)
            # trigger_data[3]: y + (ne_sw_edge_active << 7)
            # trigger_data[4]: z + (height << 5)
            # trigger_data[5] (optional): (length-1) + (byte_8_bit_4 << 4) + (f << 7)

            # Byte 0-1: event value (12 bits little-endian)
            data = bytearray()
            data.append(event.event & 0xFF)
            data.append((event.event >> 8) & 0x0F)

            # Check if we need the length byte
            if event.length > 1:
                data[1] |= 0x80  # Set bit 7 to indicate length byte present

            # Byte 2: x + (nw_se_edge_active << 7)
            data.append((event.x & 0x7F) | ((1 if event.nw_se_edge_active else 0) << 7))

            # Byte 3: y + (ne_sw_edge_active << 7)
            data.append((event.y & 0x7F) | ((1 if event.ne_sw_edge_active else 0) << 7))

            # Byte 4: z + (height << 5)
            data.append((event.z & 0x1F) | ((event.height & 0x07) << 5))

            # Byte 5 (optional): length and flags
            if event.length > 1:
                data.append(
                    ((event.length - 1) & 0x0F) |
                    ((1 if event.byte_8_bit_4 else 0) << 4) |
                    ((event.f & 0x01) << 7)
                )

            return data
        else:
            # Unknown event type
            return bytearray()

    def _render_exits(self) -> dict[int, bytearray]:
        """Render exit data.

        Pointer table: 0x1D2D64-0x1D3165 (512 rooms * 2 bytes)
        Data section: 0x1D3166-0x1D4904

        Returns:
            Dictionary of patches
        """
        patches = {}
        pointer_table_start = 0x1D2D64
        data_section_start = 0x1D3166
        data_offset = data_section_start

        # Build all exit data first
        all_exit_data = bytearray()

        for room_idx in range(512):
            room = self._rooms[room_idx]

            # Write pointer (little-endian offset from start of data section)
            pointer_value = data_offset - data_section_start
            patches[pointer_table_start + (room_idx * 2)] = bytearray([
                pointer_value & 0xFF,
                (pointer_value >> 8) & 0xFF
            ])

            if room is None or not room.exit_fields:
                # Empty room - next room will have same pointer (zero delta)
                continue

            # Render exits
            for exit_obj in room.exit_fields:
                exit_data = self._render_exit(exit_obj)
                all_exit_data.extend(exit_data)
                data_offset += len(exit_data)

        # Write all exit data as a single patch
        if len(all_exit_data) > 0:
            patches[data_section_start] = all_exit_data

        return patches

    def _render_exit(self, exit_obj: Union[RoomExit, MapExit]) -> bytearray:
        """Render a single exit to bytes.

        Follows disassembler lines 488-551.
        """
        if isinstance(exit_obj, RoomExit):
            # RoomExit: 8 or 9 bytes (+ optional length byte)
            # Disassembler reads:
            # field_data[0-1]: destination (9 bits) + flags
            # field_data[2]: x + (nw_se_edge_active << 7)
            # field_data[3]: y + (ne_sw_edge_active << 7)
            # field_data[4]: z + (height << 5)
            # field_data[5-7]: destination coords (for room exits)
            # field_data[offset] (optional): length byte

            data = bytearray()

            # Byte 0: destination low 8 bits
            data.append(exit_obj.destination & 0xFF)

            # Byte 1: Complex flags byte
            # exit_type = (field_data[1] & 0x60) >> 6
            # dst = ((field_data[1] << 8) + field_data[0]) & 0x1FF
            # length_determinant = field_data[1] & 0x80 == 0x80
            byte1 = (exit_obj.destination >> 8) & 0x01  # Bit 0 of destination
            byte1 |= (0 << 5)  # Exit type 0 for ROOM (bits 5-6)
            if exit_obj.show_message:
                byte1 |= 0x08
            if exit_obj.byte_2_bit_2:
                byte1 |= 0x04
            # Length flag will be set later if needed
            data.append(byte1)

            # Byte 2: x + (nw_se_edge_active << 7)
            data.append((exit_obj.x & 0x7F) | ((1 if exit_obj.nw_se_edge_active else 0) << 7))

            # Byte 3: y + (ne_sw_edge_active << 7)
            data.append((exit_obj.y & 0x7F) | ((1 if exit_obj.ne_sw_edge_active else 0) << 7))

            # Byte 4: z + (height << 5)
            data.append((exit_obj.z & 0x1F) | ((exit_obj.height & 0x07) << 5))

            # Bytes 5-7: Destination properties (for ROOM exits)
            # Byte 5: dst_x + (x_bit_7 << 7)
            data.append((exit_obj.destination_props.x & 0x7F) | ((1 if exit_obj.destination_props.x_bit_7 else 0) << 7))

            # Byte 6: dst_y + (dst_z_half << 7)
            data.append((exit_obj.destination_props.y & 0x7F) | ((1 if exit_obj.destination_props.z_half else 0) << 7))

            # Byte 7: dst_z + (dst_f << 5)
            data.append((exit_obj.destination_props.z & 0x1F) | ((exit_obj.destination_props.f & 0x07) << 5))

            # Optional length byte
            if exit_obj.length > 1 or exit_obj.f != 0:
                data[1] |= 0x80  # Set length flag in byte 1
                data.append(((exit_obj.length - 1) & 0x0F) | ((exit_obj.f & 0x01) << 7))

            return data

        elif isinstance(exit_obj, MapExit):
            # MapExit: 5 or 6 bytes (+ optional length byte)
            data = bytearray()

            # Byte 0: destination low 8 bits
            data.append(exit_obj.destination & 0xFF)

            # Byte 1: Complex flags byte
            byte1 = 0
            byte1 |= (1 << 6)  # Exit type 1 for MAP (bits 5-6 = 01)
            if exit_obj.show_message:
                byte1 |= 0x08
            if exit_obj.byte_2_bit_2:
                byte1 |= 0x04
            if exit_obj.byte_2_bit_1:
                byte1 |= 0x02
            if exit_obj.byte_2_bit_0:
                byte1 |= 0x01
            # Length flag will be set later if needed
            data.append(byte1)

            # Byte 2: x + (nw_se_edge_active << 7)
            data.append((exit_obj.x & 0x7F) | ((1 if exit_obj.nw_se_edge_active else 0) << 7))

            # Byte 3: y + (ne_sw_edge_active << 7)
            data.append((exit_obj.y & 0x7F) | ((1 if exit_obj.ne_sw_edge_active else 0) << 7))

            # Byte 4: z + (height << 5)
            data.append((exit_obj.z & 0x1F) | ((exit_obj.height & 0x07) << 5))

            # Optional length byte
            if exit_obj.length > 1 or exit_obj.f != 0:
                data[1] |= 0x80  # Set length flag in byte 1
                data.append(((exit_obj.length - 1) & 0x0F) | ((exit_obj.f & 0x01) << 7))

            return data

        else:
            # Unknown exit type
            return bytearray()
