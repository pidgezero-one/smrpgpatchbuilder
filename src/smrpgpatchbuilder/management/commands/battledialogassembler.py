import os
import shutil
from django.core.management.base import BaseCommand
from copy import deepcopy
import importlib.util
from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress
from datetime import datetime


# Battle dialog addresses
BATTLE_DIALOG_POINTER_ADDRESS = 0x396554
BATTLE_DIALOG_DATA_START = 0x396755
BATTLE_DIALOG_DATA_END = 0x3992D0

# Battle message addresses
BATTLE_MESSAGE_POINTER_ADDRESS = 0x3A26F1
BATTLE_MESSAGE_DATA_START = 0x3A274D
BATTLE_MESSAGE_DATA_END = 0x3A29FF


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-t", "--text", action='store_true', dest="text", help="use -t if you want to output your assembled bytes as plain text files.")
        parser.add_argument("-b", "--bin", action='store_true', dest="bin", help="use -b if you want to output your assembled bytes as flexhex-compatible img files.")
        parser.add_argument("-r", "--rom", dest="rom", help="specify a path to a mario rpg rom if you want to output your assembled bytes as a bps patch.")

    def handle(self, *args, **options):
        module_path = "disassembler_output.battle_dialogs.battle_dialogs"

        outputToText = options["text"] or False
        outputToBin = options["bin"] or False
        romPath = options["rom"]
        outputToPatch = romPath is not None

        if not (outputToText or outputToBin or outputToPatch):
            print("you need to specify at least one output format. options are --text, --bin, --rom")
            exit(1)

        if outputToText:
            shutil.rmtree("./src/assembler_output/battle_dialogs/txt", ignore_errors=True)
            os.makedirs("./src/assembler_output/battle_dialogs/txt", exist_ok=True)
        if outputToBin:
            shutil.rmtree("./src/assembler_output/battle_dialogs/bin", ignore_errors=True)
            os.makedirs("./src/assembler_output/battle_dialogs/bin", exist_ok=True)
        if outputToPatch:
            os.makedirs("./src/assembler_output/battle_dialogs/bps", exist_ok=True)

        rom = bytearray()
        if outputToPatch:
            original_rom = bytearray(open(romPath, "rb").read())
            rom = deepcopy(original_rom)

        # Import the battle dialogs and messages
        module = importlib.import_module(module_path)
        battle_dialogs = module.battle_dialogs
        battle_messages = module.battle_messages

        if len(battle_dialogs) != 256:
            raise ValueError(f"Expected 256 battle dialogs, got {len(battle_dialogs)}")

        if len(battle_messages) != 46:
            raise ValueError(f"Expected 46 battle messages, got {len(battle_messages)}")

        # Import compression utilities
        from smrpgpatchbuilder.datatypes.dialogs.utils import compress, COMPRESSION_TABLE

        # Use same compression table as psychopath messages with battle-specific additions
        battle_compression_table = [
            ("\n", b"\x01"),
            ("[await]", b"\x02"),
            ("[pause]", b"\x03"),
            ("[delay]", b"\x0C")
        ] + COMPRESSION_TABLE[17:]

        # Compress all battle dialogs
        compressed_dialogs = []
        for message in battle_dialogs:
            if message:
                compressed_dialogs.append(compress(message, battle_compression_table))
            else:
                compressed_dialogs.append(bytearray([0x00]))

        # Build the battle dialog data section
        assembled_dialog_data = bytearray()
        dialog_pointer_table = bytearray()
        current_offset = BATTLE_DIALOG_DATA_START & 0xFFFF  # Relative to bank 0x39

        for message_bytes in compressed_dialogs:
            # Add pointer (little-endian 16-bit)
            dialog_pointer_table.append(current_offset & 0xFF)
            dialog_pointer_table.append((current_offset >> 8) & 0xFF)

            # Add message data
            assembled_dialog_data += message_bytes

            # Update offset
            current_offset += len(message_bytes)

        # Check size constraints for battle dialogs
        max_dialog_size = BATTLE_DIALOG_DATA_END - BATTLE_DIALOG_DATA_START + 1
        if len(assembled_dialog_data) > max_dialog_size:
            raise ValueError(
                f"Battle dialog data too long: {len(assembled_dialog_data)} bytes (expected up to {max_dialog_size})"
            )

        # Pad data to fill the space
        if len(assembled_dialog_data) < max_dialog_size:
            assembled_dialog_data += bytearray(max_dialog_size - len(assembled_dialog_data))

        # Compress all battle messages
        compressed_messages = []
        for message in battle_messages:
            if message:
                compressed_messages.append(compress(message, battle_compression_table))
            else:
                compressed_messages.append(bytearray([0x00]))

        # Build the battle message data section
        assembled_message_data = bytearray()
        message_pointer_table = bytearray()
        current_offset = BATTLE_MESSAGE_DATA_START & 0xFFFF  # Relative to bank 0x3A

        for message_bytes in compressed_messages:
            # Add pointer (little-endian 16-bit)
            message_pointer_table.append(current_offset & 0xFF)
            message_pointer_table.append((current_offset >> 8) & 0xFF)

            # Add message data
            assembled_message_data += message_bytes

            # Update offset
            current_offset += len(message_bytes)

        # Check size constraints for battle messages
        max_message_size = BATTLE_MESSAGE_DATA_END - BATTLE_MESSAGE_DATA_START + 1
        if len(assembled_message_data) > max_message_size:
            raise ValueError(
                f"Battle message data too long: {len(assembled_message_data)} bytes (expected up to {max_message_size})"
            )

        # Pad data to fill the space
        if len(assembled_message_data) < max_message_size:
            assembled_message_data += bytearray(max_message_size - len(assembled_message_data))

        # Create patch dictionary
        collection = {
            BATTLE_DIALOG_POINTER_ADDRESS: dialog_pointer_table,
            BATTLE_DIALOG_DATA_START: assembled_dialog_data,
            BATTLE_MESSAGE_POINTER_ADDRESS: message_pointer_table,
            BATTLE_MESSAGE_DATA_START: assembled_message_data,
        }

        if collection:
            for start, bytes_ in collection.items():
                if outputToBin:
                    with open(f'./src/assembler_output/battle_dialogs/bin/write_to_0x{start:06X}.img', 'wb') as f:
                        f.write(bytes_)
                if outputToText:
                    with open(f'./src/assembler_output/battle_dialogs/txt/write_to_0x{start:06X}.txt', 'w') as f:
                        f.write(" ".join([f'{b:02X}' for b in bytes_]))
                if outputToPatch:
                    end = start + len(bytes_)
                    if end > len(rom):
                        raise ValueError(f"change at {start:#X} exceeds file size (end = {end:#X})")
                    rom[start:end] = bytes_

            if outputToPatch:
                blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
                iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
                with open(f'./src/assembler_output/battle_dialogs/bps/smrpg-battledialogs-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps', 'wb') as f:
                    write_bps(bps_progress(iterable), f)

        self.stdout.write(self.style.SUCCESS("successfully assembled battle dialog data"))
