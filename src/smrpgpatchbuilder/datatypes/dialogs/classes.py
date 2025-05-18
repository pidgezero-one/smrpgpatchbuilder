"""Base classes related to dialogs and dialog collections"""

from typing import List, Dict
from smrpgpatchbuilder.datatypes.dialogs.ids.misc import (
    DIALOG_BANK_22_BEGINS,
    DIALOG_BANK_22_ENDS,
    DIALOG_BANK_23_BEGINS,
    DIALOG_BANK_23_ENDS,
    DIALOG_BANK_24_BEGINS,
    DIALOG_BANK_24_ENDS,
)
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
)

from .ids.dialog_bank_ids import (
    DIALOG_BANK_22,
)
from .ids.types.classes import DialogBankID
from .utils import compress, COMPRESSION_TABLE, DEFAULT_COMPRESSION_TABLE


class Dialog:
    """An individual dialog in the overworld"""

    _bank: DialogBankID
    _index: int
    _position: int

    @property
    def bank(self) -> DialogBankID:
        """The bank that this dialog belongs to"""
        return self._bank

    @property
    def index(self) -> int:
        """The index of the dialog"""
        return self._index

    @property
    def position(self) -> int:
        """The starting position within the raw text where this dialog begins"""
        return self._position

    def set_position(self, position: int) -> None:
        """Overwrite the starting position within the raw text where this dialog begins"""
        self._position = position

    def __init__(self, bank: DialogBankID, index: int, pos: int) -> None:
        self._bank = bank
        self._index = index
        self.set_position(pos)


class DialogCollection:
    """Houses all dialog banks to allow retrieval and manipulation of any dialog."""

    _dialogs: List[Dialog]
    _raw_data: List[list[str]]
    _dialog_bank_22_begins: int = DIALOG_BANK_22_BEGINS
    _dialog_bank_22_ends: int = DIALOG_BANK_22_ENDS
    _dialog_bank_23_begins: int = DIALOG_BANK_23_BEGINS
    _dialog_bank_23_ends: int = DIALOG_BANK_23_ENDS
    _dialog_bank_24_begins: int = DIALOG_BANK_24_BEGINS
    _dialog_bank_24_ends: int = DIALOG_BANK_24_ENDS

    @property
    def dialogs(self) -> List[Dialog]:
        """The dialogs belonging to this seed."""
        return self._dialogs

    def _set_dialogs(self, dialogs: List[Dialog]) -> None:
        """Overwrite the dialogs belonging to this seed."""
        assert len(dialogs) == 4096
        self._dialogs = dialogs

    @property
    def raw_data(self) -> List[list[str]]:
        """The raw string data comprising dialogs."""
        return self._raw_data

    def _set_raw_data(self, raw_data: List[list[str]]) -> None:
        """Overwrite the raw string data comprising dialogs."""
        assert len(raw_data) == 3
        self._raw_data = raw_data

    def replace_dialog(self, identifier: int, content: str):
        """Replace a whole dialog by its unique ID."""
        dialog = self.dialogs[identifier]
        raw_index = dialog.bank - DIALOG_BANK_22
        self.raw_data[raw_index][dialog.index] = content

    def search_and_replace_in_all_dialogs(self, search: str, replace: str):
        """Replace all instances of the substring across all dialogs."""
        for bank_index, bank in enumerate(self.raw_data):
            for index, string in enumerate(bank):
                self.raw_data[bank_index][index] = string.replace(search, replace)

    def _set_compression_table(
        self, compression_table: List[tuple[str, bytearray]]
    ) -> None:
        """Set the compression table for this dialog collection."""
        self._compression_table = compression_table

    @property
    def compression_table(self) -> List[tuple[str, bytearray]]:
        """Get the compression table for this dialog collection."""
        return self._compression_table

    def __init__(
        self,
        dialogs: List[Dialog],
        raw_data: List[list[str]],
        compression_table: List[tuple[str, bytearray]] = DEFAULT_COMPRESSION_TABLE,
        dialog_bank_22_begins=DIALOG_BANK_22_BEGINS,
        dialog_bank_22_ends=DIALOG_BANK_22_ENDS,
        dialog_bank_23_begins=DIALOG_BANK_23_BEGINS,
        dialog_bank_23_ends=DIALOG_BANK_23_ENDS,
        dialog_bank_24_begins=DIALOG_BANK_24_BEGINS,
        dialog_bank_24_ends=DIALOG_BANK_24_ENDS,
    ) -> None:
        self._set_dialogs(dialogs)
        self._set_raw_data(raw_data)
        self._set_compression_table([*COMPRESSION_TABLE, *compression_table])
        self._dialog_bank_22_begins = dialog_bank_22_begins
        self._dialog_bank_22_ends = dialog_bank_22_ends
        self._dialog_bank_23_begins = dialog_bank_23_begins
        self._dialog_bank_23_ends = dialog_bank_23_ends
        self._dialog_bank_24_begins = dialog_bank_24_begins
        self._dialog_bank_24_ends = dialog_bank_24_ends

    def render(self) -> Dict[int, bytearray]:
        """Get all dialog data in `{0x123456: bytearray([0x00])}` format."""
        if len(self.dialogs) != 4096:
            raise ValueError("must be exactly 4096 dialogs")
        if len(self.raw_data) != 3:
            raise ValueError("must be exactly 3 dialog banks")

        new_pointer_table: List[int] = [-1] * 4096

        compressed_text = [
            [compress(d, self.compression_table) for d in self._raw_data[0]],
            [compress(d, self.compression_table) for d in self._raw_data[1]],
            [compress(d, self.compression_table) for d in self._raw_data[2]],
        ]

        assembled_dialog_data = []
        assembled_pointers = bytearray()

        for bank_index, text_collection in enumerate(compressed_text):
            bank = 0x22 + bank_index
            pointer_position = 0
            assembled_dialog_for_this_bank = bytearray()
            # convert pointer data to offsets
            for dialog_id, dialog_bytes in enumerate(text_collection):
                for index, _ in enumerate(dialog_bytes):
                    indices = [
                        j
                        for j, x in enumerate(self.dialogs)
                        if x.bank == bank
                        and x.index == dialog_id
                        and x.position == index
                    ]
                    for matched_pointer in indices:
                        new_pointer_table[matched_pointer] = pointer_position
                    pointer_position += 1
                assembled_dialog_for_this_bank += dialog_bytes

            # convert to pointers relative to section pointer
            if bank_index == 0:
                table_at_0x200 = new_pointer_table[0x200]
                table_at_0x400 = new_pointer_table[0x400]
                table_at_0x600 = new_pointer_table[0x600]
                assert table_at_0x200 > -1
                assert table_at_0x400 > -1
                assert table_at_0x600 > -1
                offsets = [
                    0,
                    table_at_0x200,
                    table_at_0x400,
                    table_at_0x600,
                ]
                offsets = [o + 8 for o in offsets]
                for index in range(0x3FF, 0x1FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0x200
                for index in range(0x5FF, 0x3FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0x400
                for index in range(0x7FF, 0x5FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0x600
            elif bank_index == 1:
                table_at_0xa00 = new_pointer_table[0xA00]
                assert table_at_0xa00 > -1
                offsets = [0, table_at_0xa00]
                offsets = [o + 4 for o in offsets]
                for index in range(0xBFF, 0x9FF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0xa00
            else:
                table_at_0xe00 = new_pointer_table[0xE00]
                assert table_at_0xe00 > -1
                offsets = [0, table_at_0xe00]
                offsets = [o + 4 for o in offsets]
                for index in range(0xFFF, 0xDFF, -1):
                    assert new_pointer_table[index] > -1
                    new_pointer_table[index] -= table_at_0xe00

            # final output for data bank: section pointers plus dialog data
            assembled_bank_dialog_data = bytearray([])
            for val in offsets:
                assembled_bank_dialog_data.append(val & 0xFF)
                assembled_bank_dialog_data.append(val >> 8)
            assembled_bank_dialog_data += assembled_dialog_for_this_bank

            # make sure it's not overflowing, fill up with empty data if space left
            if bank_index == 0:
                max_length = self._dialog_bank_22_ends - self._dialog_bank_22_begins
                empty_space = max_length - len(assembled_bank_dialog_data)
            elif bank_index == 1:
                max_length = self._dialog_bank_23_ends - self._dialog_bank_23_begins
                empty_space = max_length - len(assembled_bank_dialog_data)
            else:
                max_length = self._dialog_bank_24_ends - self._dialog_bank_24_begins
                empty_space = max_length - len(assembled_bank_dialog_data)
            if empty_space < 0:
                length = len(assembled_bank_dialog_data)
                err_bank = 0x22 + bank_index
                raise ScriptBankTooLongException(
                    (
                        f"Bank 0x{err_bank:02x} dialog data too long: "
                        f"{length} bytes (expected up to {max_length})"
                    )
                )
            if empty_space > 0:
                assembled_bank_dialog_data += bytearray(
                    [0x00 for x in range(empty_space)]
                )

            assembled_dialog_data.append(assembled_bank_dialog_data)

        # pointer bytes
        for val in new_pointer_table:
            assembled_pointers.append(val & 0xFF)
            assembled_pointers.append(val >> 8)

        return {
            0x37E000: assembled_pointers,
            0x220000: assembled_dialog_data[0],
            0x230000: assembled_dialog_data[1],
            0x240000: assembled_dialog_data[2],
        }
        # TODO: add compression table
