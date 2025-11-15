"""Disassembler for ROM's PackCollection (formation packs).

This disassembler reads the formation pack data from a Super Mario RPG ROM
and outputs a Python file containing the PackCollection with all 255 packs
and their associated formations.

Usage:
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packdisassembler --rom "/path/to/your/smrpg/rom"

This will produce:
    ./src/disassembler_output/packs/pack_collection.py

Prerequisites:
    - Enemy classes must be disassembled first (enemydisassembler)
    - Variable names should be parsed (variableparser)

The output file will contain:
    - Formation definitions for all formations used by packs
    - FormationPack definitions for all 255 packs
    - A PackCollection instance containing all packs

Note:
    - Music is output as Music class instances (NormalBattleMusic(), MidbossMusic(), etc.)
      rather than BattleMusic enum values
    - Both Music instances and BattleMusic enum values are accepted by Formation
"""

import os
import shutil
from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import shortify, writeline
from .input_file_parser import load_arrays_from_input_files, load_class_names_from_config
from smrpgpatchbuilder.datatypes.battles.ids.misc import (
    PACK_BASE_ADDRESS,
    BASE_FORMATION_ADDRESS,
    BASE_FORMATION_META_ADDRESS,
    TOTAL_PACKS,
    TOTAL_FORMATIONS,
)


class Command(BaseCommand):
    help = "Disassembles formation packs from a ROM file"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom", required=True)

    def handle(self, *args, **options):
        # Load variable names and class names from disassembler output
        varnames = load_arrays_from_input_files()
        classnames = load_class_names_from_config()

        # Get enemy class names
        ENEMIES = classnames["enemies"]

        # Get pack names from variable output
        PACK_NAMES = varnames.get("packs", [])

        # Load ROM
        rom = bytearray(open(options["rom"], "rb").read())

        # Create output directory
        output_path = "./src/disassembler_output/packs"
        shutil.rmtree(output_path, ignore_errors=True)
        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w").close()

        # First, disassemble all formations
        formations_data = []
        for formation_id in range(TOTAL_FORMATIONS):
            formation_data = self.read_formation(rom, formation_id, ENEMIES)
            formations_data.append(formation_data)

        # Then, disassemble all packs
        packs_data = []
        for pack_id in range(255):  # Only 255 packs (0-254)
            pack_data = self.read_pack(rom, pack_id)
            packs_data.append(pack_data)

        # Generate the output file
        self.generate_output_file(output_path, packs_data, formations_data, PACK_NAMES)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully disassembled {len(packs_data)} packs and {len(formations_data)} formations to {output_path}/"
            )
        )

    def read_formation(self, rom, formation_id, enemies):
        """Read a single formation from ROM."""
        # Read formation data (26 bytes)
        base_addr = BASE_FORMATION_ADDRESS + (formation_id * 26)
        data = rom[base_addr:base_addr + 26]

        # Read formation metadata (3 bytes)
        meta_addr = BASE_FORMATION_META_ADDRESS + (formation_id * 3)
        meta_data = rom[meta_addr:meta_addr + 3]

        # Parse monsters present bitmap (1 byte)
        monsters_present = data[0]

        # Parse monsters hidden bitmap (1 byte)
        monsters_hidden = data[1]

        # Parse member data (8 members * 3 bytes each = 24 bytes)
        members = []
        for i in range(8):
            offset = 2 + (i * 3)
            enemy_index = data[offset]
            x_pos = data[offset + 1]
            y_pos = data[offset + 2]

            # Check if this member is present
            is_present = (monsters_present & (1 << (7 - i))) != 0
            is_hidden = (monsters_hidden & (1 << (7 - i))) != 0

            if is_present:
                members.append({
                    'enemy': enemies[enemy_index] if enemy_index < len(enemies) else f"ENEMY_{enemy_index}",
                    'x_pos': x_pos,
                    'y_pos': y_pos,
                    'hidden_at_start': is_hidden,
                })
            else:
                members.append(None)

        # Parse metadata
        unknown_byte = meta_data[0]
        run_event = meta_data[1]
        music_byte = meta_data[2]

        # Parse music_byte
        # Bit 0: music bit 0
        # Bit 1: cannot run away
        # Bit 2-7: music bits 1-6 and unknown bit
        music_value = 8 if (music_byte & 0xC0 == 0xC0) else (music_byte >> 2)
        can_run_away = (music_byte & 0x02) == 0
        unknown_bit: bool = (music_byte & 0x01) == 0x01

        # Map music value to Music class instances
        music_map = {
            0: "NormalBattleMusic()",
            1: "MidbossMusic()",
            2: "BossMusic()",
            3: "Smithy1Music()",
            4: "CorndillyMusic()",
            5: "BoosterHillMusic()",
            6: "VolcanoMusic()",
            7: "CulexMusic()",
        }
        music_str = music_map.get(music_value, "None")

        return {
            'id': formation_id,
            'members': members,
            'run_event': run_event if run_event != 0xFF else None,
            'music': music_str,
            'can_run_away': can_run_away,
            'unknown_byte': unknown_byte,
            'unknown_bit': unknown_bit,
        }

    def read_pack(self, rom, pack_id):
        """Read a single pack from ROM."""
        base_addr = PACK_BASE_ADDRESS + (pack_id * 4)
        data = rom[base_addr:base_addr + 4]

        formation_1 = data[0]
        formation_2 = data[1]
        formation_3 = data[2]
        hi_bank = data[3]

        # Check if high bank is used
        if hi_bank == 7:
            formation_1 += 256
            formation_2 += 256
            formation_3 += 256

        return {
            'id': pack_id,
            'formations': [formation_1, formation_2, formation_3]
        }

    def generate_output_file(self, output_path, packs_data, formations_data, pack_names):
        """Generate the Python file with PackCollection."""
        file_path = f"{output_path}/pack_collection.py"

        with open(file_path, "w") as f:
            # Write imports
            writeline(f, "\"\"\"ROM's PackCollection disassembled from the original game.\"\"\"")
            writeline(f, "")
            writeline(f, "from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (")
            writeline(f, "    Formation,")
            writeline(f, "    FormationMember,")
            writeline(f, "    FormationPack,")
            writeline(f, "    PackCollection,")
            writeline(f, ")")
            writeline(f, "from smrpgpatchbuilder.datatypes.battles.music import (")
            writeline(f, "    NormalBattleMusic,")
            writeline(f, "    MidbossMusic,")
            writeline(f, "    BossMusic,")
            writeline(f, "    Smithy1Music,")
            writeline(f, "    CorndillyMusic,")
            writeline(f, "    BoosterHillMusic,")
            writeline(f, "    VolcanoMusic,")
            writeline(f, "    CulexMusic,")
            writeline(f, ")")
            writeline(f, "from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield")
            writeline(f, "from ..enemies.enemies import *")
            writeline(f, "from ..variables.pack_names import *")
            writeline(f, "")
            writeline(f, "")

            writeline(f, "# Initialize packs array with None values")
            writeline(f, "packs: list[FormationPack] = [None] * 256 # type: ignore")
            writeline(f, "")
            writeline(f, "")

            # Generate pack definitions with inline formations
            for pack in packs_data:
                self.write_pack_inline(f, pack, formations_data, pack_names)

            writeline(f, "")
            writeline(f, "# Pack Collection")
            writeline(f, "pack_collection = PackCollection(packs[:255])")

    def write_formation_inline(self, f, formation, indent="    "):
        """Write a formation definition inline."""
        writeline(f, f"{indent}Formation(")
        writeline(f, f"{indent}    members=[")

        # Find the last non-None member
        last_member_index = -1
        for i in range(len(formation['members']) - 1, -1, -1):
            if formation['members'][i] is not None:
                last_member_index = i
                break

        # Only write members up to the last non-None member
        for i, member in enumerate(formation['members']):
            if i > last_member_index:
                break

            if member is None:
                writeline(f, f"{indent}        None,")
            else:
                enemy = member['enemy']
                x = member['x_pos']
                y = member['y_pos']
                hidden = member['hidden_at_start']

                if hidden:
                    writeline(f, f"{indent}        FormationMember({enemy}, {x}, {y}, hidden_at_start=True),")
                else:
                    writeline(f, f"{indent}        FormationMember({enemy}, {x}, {y}),")

        writeline(f, f"{indent}    ],")

        if formation['run_event'] is not None:
            writeline(f, f"{indent}    run_event_at_load={formation['run_event']},")

        writeline(f, f"{indent}    music={formation['music']},")

        if not formation['can_run_away']:
            writeline(f, f"{indent}    can_run_away=False,")

        if formation['unknown_byte'] != 0:
            writeline(f, f"{indent}    unknown_byte={formation['unknown_byte']},")

        if formation['unknown_bit'] != 0:
            writeline(f, f"{indent}    unknown_bit={formation['unknown_bit']},")

        writeline(f, f"{indent})")

    def write_pack_inline(self, f, pack, formations_data, pack_names):
        """Write a pack definition with inline formations to the file."""
        pack_id = pack['id']
        formation_ids = pack['formations']

        # Get pack name from pack_names array, or use generic name
        pack_name = pack_names[pack_id] if pack_id < len(pack_names) and pack_names[pack_id] else f"PACK_{pack_id}"

        # Check if all three formations are the same
        if formation_ids[0] == formation_ids[1] == formation_ids[2]:
            writeline(f, f"packs[{pack_name}] = FormationPack(")
            self.write_formation_inline(f, formations_data[formation_ids[0]], indent="    ")
            writeline(f, ")")
        else:
            writeline(f, f"packs[{pack_name}] = FormationPack(")
            self.write_formation_inline(f, formations_data[formation_ids[0]], indent="    ")
            writeline(f, "    ,")
            self.write_formation_inline(f, formations_data[formation_ids[1]], indent="    ")
            writeline(f, "    ,")
            self.write_formation_inline(f, formations_data[formation_ids[2]], indent="    ")
            writeline(f, ")")
