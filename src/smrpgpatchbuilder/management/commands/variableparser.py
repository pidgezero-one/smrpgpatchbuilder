from pathlib import Path
import re
from django.core.management.base import BaseCommand
import shutil
from .input_file_parser import parse_input_files

class Command(BaseCommand):
    help = "Parse *_names.input files in .config and write python mappings to disassembler_output/variables/"

    def handle(self, *args, **options):
        out_base = Path.cwd() / "src" / "disassembler_output" / "variables"
        if out_base.exists():
            try:
                shutil.rmtree(out_base)
            except Exception as e:
                self.stderr.write(f"failed to clear output directory: {e}")
                return

        try:
            parsed = parse_input_files()
        except ValueError as e:
            self.stderr.write(str(e))
            return

        # write outputs
        out_base = Path.cwd() / "src" / "disassembler_output" / "variables"
        out_base.mkdir(parents=True, exist_ok=True)

        for key, tuples in parsed.items():
            out_file = out_base / f"{key}.py"
            lines = []
            if key == "variable_names" or key == "variable_names.input":
                lines.append("from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.byte_var import ByteVar")
                lines.append("from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.short_var import ShortVar")
                lines.append("from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag")
                lines.append("")

            for name, value in tuples:
                if re.match(r"^(ShortVar|ByteVar|Flag)\(", value) or value.startswith("0x"):
                    lines.append(f"{name} = {value}")
                else:
                    escaped = value.replace('"', '\\"')
                    lines.append(f"{name} = {escaped}")
            out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")

        self.stdout.write(f"Wrote {len(parsed)} variable files to {out_base}")