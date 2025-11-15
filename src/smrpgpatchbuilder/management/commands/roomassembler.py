"""Django management command to assemble rooms into a ROM file."""
from django.core.management.base import BaseCommand
import importlib.util
import sys


class Command(BaseCommand):
    help = "Assemble rooms from Python files into a ROM"

    def add_arguments(self, parser):
        parser.add_argument(
            "-r", "--rom",
            dest="rom",
            required=True,
            help="Path to the Mario RPG ROM file to modify"
        )

        parser.add_argument(
            "-i", "--input",
            dest="input",
            required=True,
            help="Path to the rooms.py file containing the RoomCollection"
        )

        parser.add_argument(
            "-o", "--output",
            dest="output",
            required=True,
            help="Path to write the modified ROM"
        )

        parser.add_argument(
            "--large-partition-table",
            dest="large_partition_table",
            action="store_true",
            help="Use larger partition table (512 partitions at 0x1DEBE0 instead of 128 at 0x1DDE00)"
        )

    def handle(self, *args, **options):
        rom_path = options["rom"]
        input_path = options["input"]
        output_path = options["output"]
        large_partition_table = options["large_partition_table"]

        # Load the ROM
        self.stdout.write(f"Loading ROM from {rom_path}...")
        with open(rom_path, "rb") as f:
            rom = bytearray(f.read())

        # Load the rooms module
        self.stdout.write(f"Loading rooms from {input_path}...")
        spec = importlib.util.spec_from_file_location("rooms_module", input_path)
        if spec is None or spec.loader is None:
            raise ValueError(f"Could not load module from {input_path}")

        rooms_module = importlib.util.module_from_spec(spec)
        sys.modules["rooms_module"] = rooms_module
        spec.loader.exec_module(rooms_module)

        # Get the RoomCollection
        if not hasattr(rooms_module, "room_collection"):
            raise ValueError(
                f"Module {input_path} must define a 'room_collection' variable of type RoomCollection"
            )

        room_collection = rooms_module.room_collection

        # Override large_partition_table if specified
        if large_partition_table:
            room_collection._large_partition_table = True
            self.stdout.write(self.style.WARNING("Using large partition table (--large-partition-table flag)"))

        # Render to patches
        self.stdout.write("Rendering rooms to patches...")
        patches = room_collection.render()

        # Apply patches to ROM
        self.stdout.write(f"Applying {len(patches)} patches to ROM...")
        for address, data in patches.items():
            rom[address:address + len(data)] = data

        # Write output
        self.stdout.write(f"Writing modified ROM to {output_path}...")
        with open(output_path, "wb") as f:
            f.write(rom)

        self.stdout.write(self.style.SUCCESS(
            f"Successfully assembled rooms into {output_path}"
        ))