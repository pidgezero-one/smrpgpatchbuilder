import importlib.util
import sys
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        os.makedirs("./src/assembler_output/battle_animations/", exist_ok=True)
        # filepaths = ["./disassembler_output/battle_animation/collection_0x3Axxxx.py", "./disassembler_output/battle_animation/collection_0x35xxxx.py", "./disassembler_output/battle_animation/collection_0x02xxxx.py"]
        filepaths = [
            "disassembler_output.battle_animation.collection_0x3Axxxx",
            "disassembler_output.battle_animation.collection_0x35xxxx",
            "disassembler_output.battle_animation.collection_0x02xxxx",
		]

        for module_path in filepaths:
            module = importlib.import_module(module_path)
            bank = module.collection
            if bank:
                output = bank.render()
                for start, bytes_ in output.items():
                    with open(f'./src/assembler_output/battle_animations/write_to_{start}.img', 'wb') as f:
                        f.write(bytes_)
