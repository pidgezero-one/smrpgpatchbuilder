import os
import shutil
from django.core.management.base import BaseCommand
from copy import deepcopy
import importlib.util
from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress
from datetime import datetime



class Command(BaseCommand):
	def add_arguments(self, parser):
		parser.add_argument("-t", "--text", action='store_true', dest="text", help="Use -t if you want to output your assembled bytes as plain text files.")
		parser.add_argument("-b", "--bin", action='store_true', dest="bin", help="Use -b if you want to output your assembled bytes as FlexHEX-compatible IMG files.")
		parser.add_argument("-r", "--rom", dest="rom", help="Specify a path to a Mario RPG rom if you want to output your assembled bytes as a bps patch.")

	def handle(self, *args, **options):
		filepaths = [
			"disassembler_output.battle_animation.collection_0x3Axxxx",
			"disassembler_output.battle_animation.collection_0x35xxxx",
			"disassembler_output.battle_animation.collection_0x02xxxx",
		]
		
		outputToText = options["text"] or False
		outputToBin = options["bin"] or False
		romPath = options["rom"]
		outputToPatch = romPath is not None 
		
		if not (outputToText or outputToBin or outputToPatch):
			print("You need to specify at least one output format. Options are --text, --bin, --rom")
			exit(1)

		if outputToText:
			shutil.rmtree("./src/assembler_output/battle_animations/txt", ignore_errors=True)
			os.makedirs("./src/assembler_output/battle_animations/txt", exist_ok=True)
		if outputToBin:
			shutil.rmtree("./src/assembler_output/battle_animations/bin", ignore_errors=True)
			os.makedirs("./src/assembler_output/battle_animations/bin", exist_ok=True)
		if outputToPatch:
			os.makedirs("./src/assembler_output/battle_animations/bps", exist_ok=True)
		
		rom = bytearray()
		if outputToPatch:
			original_rom = bytearray(open(romPath, "rb").read())
			rom = deepcopy(original_rom)

		for module_path in filepaths:
			module = importlib.import_module(module_path)
			bank = module.collection
			if bank:
				output = bank.render()
				for start, bytes_ in output.items():
					if outputToBin:
						with open(f'./src/assembler_output/battle_animations/bin/write_to_0x{start:06X}.img', 'wb') as f:
							f.write(bytes_)
					if outputToText:
						with open(f'./src/assembler_output/battle_animations/txt/write_to_0x{start:06X}.txt', 'w') as f:
							f.write(" ".join([f'{b:02X}' for b in bytes_]))
					if outputToPatch:
						end = start + len(bytes_)
						if end > len(rom):
							raise ValueError(f"Change at {start:#X} exceeds file size (end = {end:#X})")
						rom[start:end] = bytes_

		if outputToPatch:
			blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
			iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
			with open(f'./src/assembler_output/battle_animations/bps/smrpg-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps', 'wb') as f:
				write_bps(bps_progress(iterable), f)
