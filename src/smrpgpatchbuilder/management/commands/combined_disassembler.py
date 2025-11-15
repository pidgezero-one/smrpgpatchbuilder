"""
Combined Django management command to disassemble enemies and animations together.

This command resolves the circular dependency between enemies and animations:
1. Enemies need AnimationScriptBank.build_command_address_mapping() for _monster_behaviour
2. Animations need Enemy classes for SummonMonster commands

The solution:
1. Disassemble enemies first WITHOUT monster_behaviour set
2. Load enemy classes into memory and build enemy_id -> class_name mapping
3. Disassemble animations using the enemy class names for SummonMonster commands
4. Load AnimationScriptBank and run build_command_address_mapping()
5. Update enemy classes with correct _monster_behaviour values
6. Write final output files for both enemies and animations
"""

from django.core.management.base import BaseCommand
from pathlib import Path
import importlib
import sys
import tempfile
import shutil
from typing import Set, Dict, List


class Command(BaseCommand):
    help = "Combined disassemble of enemies and animations to resolve circular dependencies"

    def add_arguments(self, parser):
        parser.add_argument(
            "-r",
            "--rom",
            dest="rom",
            required=True,
            help="Path to a Mario RPG ROM file",
        )
        parser.add_argument(
            "--enemy-output",
            dest="enemy_output",
            default="src/disassembler_output/enemies/enemies.py",
            help="Output file path for enemies",
        )
        parser.add_argument(
            "--animation-output",
            dest="animation_output",
            default="src/disassembler_output/battle_animation",
            help="Output directory path for animations",
        )

    def handle(self, *args, **options):
        rom_path = options["rom"]
        enemy_output_path = options["enemy_output"]
        animation_output_path = options["animation_output"]

        self.stdout.write(self.style.WARNING("Starting combined disassembly..."))

        # ========== STAGE 1: Disassemble enemies without monster_behaviour ==========
        self.stdout.write(self.style.WARNING("\n[Stage 1/6] Disassembling enemies (without behaviour)..."))

        temp_enemy_dir = Path(tempfile.mkdtemp(prefix="enemy_temp_"))
        temp_enemy_file = temp_enemy_dir / "enemies.py"

        try:
            self._disassemble_enemies_stage1(
                rom_path,
                str(temp_enemy_file),
                None  # No animation bank yet
            )

            # ========== STAGE 2: Load enemy classes into memory ==========
            self.stdout.write(self.style.WARNING("\n[Stage 2/6] Loading enemy classes into memory..."))

            enemy_id_to_class = self._load_enemy_classes(temp_enemy_dir)
            self.stdout.write(self.style.SUCCESS(f"Loaded {len(enemy_id_to_class)} enemy classes"))

            # ========== STAGE 3: Disassemble animations with enemy references ==========
            self.stdout.write(self.style.WARNING("\n[Stage 3/6] Disassembling animations..."))

            # Import and run the animation disassembler with enemy class names
            from .animationdisassembler import Command as AnimationCommand
            anim_cmd = AnimationCommand()

            # Monkey-patch the loaded_class_names to include our enemies
            import smrpgpatchbuilder.management.commands.input_file_parser as parser_module
            original_load_func = parser_module.load_class_names_from_config

            def patched_load_class_names():
                result = original_load_func()
                result["enemies"] = enemy_id_to_class
                return result

            parser_module.load_class_names_from_config = patched_load_class_names

            try:
                # Run animation disassembler
                anim_cmd.handle(rom=rom_path)
            finally:
                # Restore original function
                parser_module.load_class_names_from_config = original_load_func

            # ========== STAGE 4: Load AnimationScriptBank and get command mappings ==========
            self.stdout.write(self.style.WARNING("\n[Stage 4/6] Building animation command address mapping..."))

            animation_bank_path = f"{animation_output_path}/35/export.py"
            address_to_identifier = self._load_animation_bank(animation_bank_path)
            self.stdout.write(self.style.SUCCESS(f"Built address mapping with {len(address_to_identifier)} entries"))

            # ========== STAGE 5: Re-disassemble enemies WITH monster_behaviour ==========
            self.stdout.write(self.style.WARNING("\n[Stage 5/6] Re-disassembling enemies (with behaviour)..."))

            self._disassemble_enemies_stage1(
                rom_path,
                enemy_output_path,
                animation_bank_path
            )

            # ========== STAGE 6: Validate monster behaviours ==========
            self.stdout.write(self.style.WARNING("\n[Stage 6/6] Validating monster behaviours..."))

            validation_errors = self._validate_monster_behaviours(enemy_output_path, address_to_identifier)

            if validation_errors:
                self.stdout.write(self.style.ERROR("\nERROR: Failed to populate monster behaviours for the following enemies:"))
                for error in validation_errors:
                    self.stdout.write(self.style.ERROR(f"  - {error}"))
                self.stdout.write(self.style.ERROR(
                    "\nThis likely means the animation disassembler did not generate identifiers for "
                    "all monster behaviour addresses. Check monster_behaviour_oq_offsets."
                ))
                raise ValueError(f"Failed to populate {len(validation_errors)} monster behaviours")

            # ========== Done ==========
            self.stdout.write(self.style.SUCCESS(
                f"\nSuccessfully completed combined disassembly!"
            ))
            self.stdout.write(self.style.SUCCESS(f"  - Enemies written to: {enemy_output_path}"))
            self.stdout.write(self.style.SUCCESS(f"  - Animations written to: {animation_output_path}"))

        finally:
            # Clean up temporary directory
            if temp_enemy_dir.exists():
                shutil.rmtree(temp_enemy_dir)

    def _disassemble_enemies_stage1(self, rom_path, output_path, animation_bank_path):
        """
        Run the enemy disassembler.

        Args:
            rom_path: Path to ROM file
            output_path: Where to write enemies.py
            animation_bank_path: Path to animation bank (or None for stage 1)
        """
        from .enemydisassembler import Command as EnemyCommand

        enemy_cmd = EnemyCommand()

        # Build arguments
        args = {"rom": rom_path, "output": output_path}

        if animation_bank_path:
            args["animation_bank"] = animation_bank_path
        else:
            # For stage 1, pass a dummy path that won't be used
            # We'll need to modify enemydisassembler to handle this gracefully
            args["animation_bank"] = "dummy"

        # Call the enemy disassembler
        # Note: We may need to modify enemydisassembler.py to handle missing animation bank gracefully
        enemy_cmd.handle(**args)

    def _load_enemy_classes(self, temp_enemy_dir: Path) -> Dict[int, str]:
        """
        Load enemy classes from temporary directory.

        Args:
            temp_enemy_dir: Path to temporary directory containing enemies.py

        Returns:
            Dictionary mapping enemy ID to class name
        """
        # Read the generated file and parse enemy class names directly
        # This avoids import issues with relative imports in the temporary file
        enemy_file = temp_enemy_dir / "enemies.py"
        content = enemy_file.read_text()

        enemy_id_to_class = {}

        # Parse the file to extract class names and their IDs
        import re

        # Find all class definitions with their monster_id
        # Pattern: class <ClassName>(Enemy): ... _monster_id: int = <id>
        class_pattern = re.compile(
            r'class\s+(\w+)\(Enemy\):'  # Class name
            r'.*?'  # Any content
            r'_monster_id:\s*int\s*=\s*(\d+)',  # Monster ID
            re.DOTALL
        )

        for match in class_pattern.finditer(content):
            class_name = match.group(1)
            enemy_id = int(match.group(2))
            enemy_id_to_class[enemy_id] = class_name

        return enemy_id_to_class

    def _validate_monster_behaviours(self, enemy_output_path: str, address_to_identifier: Dict[int, str]) -> List[str]:
        """
        Validate that all enemies have their monster_behaviour properly set.

        Args:
            enemy_output_path: Path to the enemies.py file
            address_to_identifier: Address to identifier mapping from animation bank

        Returns:
            List of error messages for enemies with missing/empty monster_behaviour
        """
        import re

        enemy_file = Path(enemy_output_path)
        content = enemy_file.read_text()

        errors = []

        # Find all enemy classes with their names and monster_behaviour values
        # Pattern: class <ClassName>(Enemy): ... _monster_behaviour: str = "<value>"
        class_pattern = re.compile(
            r'class\s+(\w+)\(Enemy\):.*?'  # Class name
            r'_monster_id:\s*int\s*=\s*(\d+).*?'  # Monster ID
            r'_name:\s*str\s*=\s*"([^"]*)".*?'  # Enemy name
            r'_monster_behaviour:\s*str\s*=\s*"([^"]*)"',  # Monster behaviour
            re.DOTALL
        )

        for match in class_pattern.finditer(content):
            class_name = match.group(1)
            monster_id = int(match.group(2))
            enemy_name = match.group(3)
            monster_behaviour = match.group(4)

            # Check if monster_behaviour is empty or still has the placeholder comment
            if not monster_behaviour or "To be filled by combined_disassembler" in content[match.start():match.end()]:
                errors.append(
                    f"Enemy #{monster_id} ({enemy_name}, class {class_name}): "
                    f"monster_behaviour is empty or not populated"
                )
            # Check if the behaviour value is "None" (string)
            elif monster_behaviour == "None":
                errors.append(
                    f"Enemy #{monster_id} ({enemy_name}, class {class_name}): "
                    f"monster_behaviour is 'None' - address not found in animation mappings"
                )

        return errors

    def _load_animation_bank(self, animation_bank_path):
        """
        Load animation bank and build address to identifier mapping.

        Args:
            animation_bank_path: Path to export.py file

        Returns:
            Dictionary mapping addresses to command identifiers
        """
        import os

        # Convert file path to module path
        normalized_path = animation_bank_path.replace(os.sep, '/')
        if normalized_path.endswith('.py'):
            normalized_path = normalized_path[:-3]

        if normalized_path.startswith('src/'):
            normalized_path = normalized_path[4:]

        module_path = normalized_path.replace('/', '.')

        # Import the module
        try:
            module = importlib.import_module(module_path)
        except ImportError as e:
            raise ValueError(f"Could not load animation bank from {animation_bank_path}: {e}")

        # Get the bank instance
        bank = getattr(module, 'bank', None)

        if bank is None:
            # Search for an instance with the method
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (hasattr(attr, 'build_command_address_mapping') and
                    not isinstance(attr, type) and
                    callable(getattr(attr, 'build_command_address_mapping', None))):
                    bank = attr
                    break

        if bank is None:
            raise ValueError(f"Could not find AnimationScriptBank instance in {animation_bank_path}")

        # Build the mapping
        identifier_to_address = bank.build_command_address_mapping()

        # Reverse the mapping (address -> identifier)
        address_to_identifier = {v: k for k, v in identifier_to_address.items()}

        return address_to_identifier
