from typing import Dict, List, Optional

from smrpgpatchbuilder.datatypes.numbers.classes import UInt8, UInt16

# Constants to avoid circular imports
TOTAL_SPRITES = 0x400
TOTAL_SCRIPTS = 0x400

class Packet:
    """An object to be spawned on the field that does not exist in the room's
    list of NPCs.\n
    Packets are fairly limited in what they can do, they are not as complex
    as NPCs.\n
    They are usually meant to be temporary, such as collectable items or
    treasure chest contents.\n
    It is recommended to use packet ID, sprite ID, and action script ID constant names.
    """

    _packet_id: UInt8 = UInt8(8)
    _sprite_id: UInt16 = UInt16(0)
    _shadow: bool = False
    _action_script_id: UInt16 = UInt16(0)
    _unknown_bits: List[bool] = [False] * 3
    _unknown_bytes: bytearray = bytearray()

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet."""
        return self._packet_id

    @property
    def sprite_id(self) -> UInt16:
        """The sprite ID for the packet to use."""
        return self._sprite_id

    def _set_sprite_id(self, sprite_id: int) -> None:
        """Set the sprite ID for the packet to use.\n
        It is recommended to use sprite ID constant names for this."""
        assert sprite_id < TOTAL_SPRITES
        self._sprite_id = UInt16(sprite_id)

    @property
    def shadow(self) -> bool:
        """If true, the packet casts a shadow when above ground."""
        return self._shadow

    def _set_shadow(self, shadow: bool) -> None:
        """If true, the packet casts a shadow when above ground."""
        self._shadow = shadow

    @property
    def action_script_id(self) -> UInt16:
        """The action script for this packet to run when spawned."""
        return self._action_script_id

    def _set_action_script_id(self, action_script_id: int) -> None:
        """Set the action script for this packet to run when spawned.\n
        It is recommended to use action script ID constant names for this."""
        assert action_script_id < TOTAL_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    @property
    def unknown_bits(self) -> List[bool]:
        """(unknown)"""
        return self._unknown_bits

    def _set_unknown_bits(self, unknown_bits: List[bool]) -> None:
        """(unknown)"""
        for bit in unknown_bits:
            assert 0 <= bit <= 7
        self._unknown_bits = unknown_bits

    @property
    def unknown_bytes(self) -> bytearray:
        """(unknown)"""
        return self._unknown_bytes

    def _set_unknown_bytes(self, unknown_bytes: bytearray) -> None:
        """(unknown)"""
        self._unknown_bytes = unknown_bytes

    def __init__(
        self,
        packet_id: int,
        sprite_id: int = 524,
        shadow: bool = False,
        action_script_id: int = 15,
        unknown_bits: Optional[List[bool]] = None,
        unknown_bytes: Optional[bytearray] = None,
    ) -> None:
        if unknown_bits is None:
            unknown_bits = [False, False, False]
        if unknown_bytes is None:
            unknown_bytes = bytearray([0, 0, 0, 0, 0, 0, 0])
        self._packet_id = UInt8(packet_id)
        self._set_sprite_id(sprite_id)
        self._set_shadow(shadow)
        self._set_action_script_id(action_script_id)
        self._set_unknown_bits(unknown_bits)
        self._set_unknown_bytes(unknown_bytes)

    def render(self) -> bytearray:
        output = bytearray()
        output.append(((self.sprite_id - 0xC0) & 0x3F) + (self.unknown_bytes[0] << 6))
        output.append(self.unknown_bytes[1] + (self.unknown_bytes[2] << 3) + (self.unknown_bytes[3] << 5))
        output.append(self.unknown_bytes[4] + (self.unknown_bits[0] << 2) + (self.unknown_bits[1] << 3) + (self.unknown_bits[2] << 4) + (self.shadow << 5) + (self.unknown_bytes[5] << 6))
        output.append(self.action_script_id & 0xFF)
        output.append(((self.action_script_id >> 8) & 0x03) + (self.unknown_bytes[6] << 4))
        return output


class PacketCollection:
    """Collection of up to 256 packets with rendering support.

    Each packet occupies 5 bytes in the ROM. When a packet slot is None,
    it is represented by 5 0xFF bytes.
    """

    def __init__(self, packets: List[Optional[Packet]]):
        """Initialize the collection with a list of up to 256 optional packets.

        Args:
            packets: list of optional Packet objects (up to 256 entries)

        Raises:
            ValueError: if more than 256 packets are provided
        """
        if len(packets) > 256:
            raise ValueError(
                f"PacketCollection can contain at most 256 packets, "
                f"but {len(packets)} were provided."
            )

        # Pad with None to ensure exactly 256 entries
        self.packets = packets + [None] * (256 - len(packets))

    def render(self) -> Dict[int, bytearray]:
        """Render all packets to ROM format.

        Returns:
            dictionary mapping ROM address (0x1DB000) to bytearray of all packet data
        """
        data = bytearray()

        for packet in self.packets:
            if packet is None:
                # Empty packet slot: 5 bytes of 0xFF
                data.extend([0xFF] * 5)
            else:
                # Render the packet
                data.extend(packet.render())

        return {0x1DB000: data}
