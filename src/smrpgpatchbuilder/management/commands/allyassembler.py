"""Django management command to assemble allies into a ROM file."""

from django.core.management.base import BaseCommand
import importlib.util
import sys


class Command(BaseCommand):
    help = "Assemble allies from Python file into a ROM"

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
            help="Path to the allies.py file containing the AllyCollection"
        )

        parser.add_argument(
            "-o", "--output",
            dest="output",
            required=True,
            help="Path to write the modified ROM"
        )

    def handle(self, *args, **options):
        rom_path = options["rom"]
        input_path = options["input"]
        output_path = options["output"]

        # Load the ROM
        self.stdout.write(f"Loading ROM from {rom_path}...")
        with open(rom_path, "rb") as f:
            rom = bytearray(f.read())

        # Load the allies module
        self.stdout.write(f"Loading allies from {input_path}...")
        spec = importlib.util.spec_from_file_location("allies_module", input_path)
        if spec is None or spec.loader is None:
            raise ValueError(f"Could not load module from {input_path}")

        allies_module = importlib.util.module_from_spec(spec)
        sys.modules["allies_module"] = allies_module
        spec.loader.exec_module(allies_module)

        # Get the AllyCollection
        if not hasattr(allies_module, "ally_collection"):
            raise ValueError(
                f"Module {input_path} must define an 'ally_collection' variable of type AllyCollection"
            )

        ally_collection = allies_module.ally_collection

        # Render to patches
        self.stdout.write("Rendering allies to patches...")
        patches = ally_collection.render()

        # Apply patches to ROM
        self.stdout.write(f"Applying {len(patches)} patches to ROM...")
        for address, data in patches.items():
            rom[address:address + len(data)] = data

        # Write output
        self.stdout.write(f"Writing modified ROM to {output_path}...")
        with open(output_path, "wb") as f:
            f.write(rom)

        self.stdout.write(self.style.SUCCESS(
            f"Successfully assembled allies into {output_path}"
        ))
