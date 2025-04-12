# SMRPG Patch Builder

Freeform editing of various kinds of SMRPG scripts and sprites. 

This is not a decomp.

# How this works: converting your ROM's scripts into Python code

You can disassemble the contents of your ROM, which turns your ROM into Python code like this:

```python
# This is event 32, which is for treasure chests that don't contain coins
script = EventScript([
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
])
```

You can edit that however you like. For example you could make a dialog run every time you open a chest (not sure why you'd want to, but you could do it):
```python
script = EventScript([
	RunDialog(
		dialog_id=DI0520_LITTLE_SHORT_ON_COINS,
		above_object=MEM_70A8,
		closable=True,
		sync=False,
		multiline=True,
		use_background=True,
	),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
])
```

If you want to use any `Jump to address` commands, you can do it by putting labels on your commands. You don't need to worry about ROM addresses at all!
```python
script = EventScript([
	JmpIfBitClear(UNKNOWN_7049_4, ["LabelGoesHere"]), # This will skip the RunDialog command by jumping to the SetBit command
	RunDialog(
		dialog_id=DI0520_LITTLE_SHORT_ON_COINS,
		above_object=MEM_70A8,
		closable=True,
		sync=False,
		multiline=True,
		use_background=True,
	),
	SetBit(INSUFFICIENT_COINS, identifier="LabelGoesHere"),
	JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
])
```

You have total freedom to put commands anywhere you want, just like in Lazy Shell. And then you can convert that Python code back into a patch for your ROM. The names of each command in a script, and the arguments that they take, are meant to resemble how they're written in Lazy Shell.

You don't need a whole lot of coding knowledge if you just want to use these scripts to read, modify, and output a patch for your SMRPG code. But you can import this repo and use its classes in your own Python projects if you like, if for example you're working on something complicated and non-static like SMRPG Randomizer. You can assemble a whole collection of scripts into bytes like this example of the 1Exxxx event script bank:
```python
bank = EventScriptBank(
    pointer_table_start=0x1E0000,
    start=0x1E0C00,
    end=0x1F0000,
    scripts=[
		# This is where you would put all of your EventScript instances, in order
	])
patchbytes = bank.render() # This outputs a bytearray
```

Most of this was designed to be used with smrpg randomizer. A lot of it can be reused, but there'll be a lot of stuff in here that doesn't match up to the original game, like descriptions of what event script variables are used for, unused enemy classes being missing, certain item implementations being missing (there's no alto card item class in here for example), etc. But you can extend this code's base classes for your purposes however you like.

This repo allows you to parse, modify, and rebuild:
- Battle animations ([disassemble](#disassembling-battle-animations) | [assemble](#assembling-battle-animations))
- Monster AI ([disassemble](#disassembling-monster-ai) | [assemble](#assembling-monster-ai))
- Event scripts (soon)
- NPC animations (soon)

TODO: Command class reference

## How to use this repo's standalone tools

These instructions are for bash terminals, aka mac/linux only (no powershell). If you want to do this on windows you'll need to figure out on your own what the equivalent steps are here (but you can probably use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and these steps will likely still work after some finagling).

- Install the Python runtime for your operating system. All further steps assume that your PATH variable will execute python 3 when you use `python` in the command line (and that you don't have that pointing to a separate python 2 install for example)
- Create a virtual environment: `python -m venv MyVirtualEnvironmentNameWhateverIWant`
- Activate the virtual environment: `source ~/.venvs/MyVirtualEnvironmentNameWhateverIWant/bin/activate` (might differ depending on your setup, use google if that's the case)
- Install required packages: `pip install -r requirements.txt`

Everything you do beyond this point must be in your venv. You'll know you're in your venv when your terminal prompts have your venv name in them, like this if you use vscode:
```
(MyVirtualEnvironmentNameWhateverIWant) stefkischak@Stefs-MBP smrpgpatchbuilder %
```

### Disassembling battle animations

Run this **in the root directory of this project** against an SMRPG rom file (vanilla or not). It will read all battle animations and convert them into Python code. For example:

```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py animationdisassembler --rom "path/to/your/smrpg/rom/or/modified/smrpg/rom" 
```

This will output to a subfolder, `./src/disassembler_output/battle_animation`. 

For example, here is part of the Yaridovich mirage attack as seen in Lazy Shell:

![alt text](image.png)

Here is the code that the script creates from reading that (battle_events/contents/script_22.py):

```python
# BE0022_YARIDOVICH_MIRAGE_ATTACK

from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from smrpgpatchbuilder.datatypes.enemies.implementations import *
from smrpgpatchbuilder.datatypes.items.implementations import *

script = BattleAnimationScript(header=["command_0x3a647c"], script = [
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac3b2"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a7729"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=90),
	ClearAMEM8Bit(0x68),
	SetAMEMToRandomByte(amem=0x68, upper_bound=7),
	JmpIfAMEM8BitLessThanConst(0x68, 3, ["command_0x3a646c"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac345"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac35f"], bit_2=True, bit_4=True),
	Jmp(["command_0x3a6476"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac345"], bit_2=True, bit_4=True, identifier="command_0x3a646c"),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac35f"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"], identifier="command_0x3a6476"),
	Jmp(["command_0x3a7550"]),
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=183, y=127, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x3a647c"),
	NewSpriteAtCoords(sprite_id=SPR0482_YARIDOVICH, sequence=0, priority=2, vram_address=0x7800, palette_row=12, overwrite_vram=True, looping=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	RunSubroutine(["command_0x3a756c"]),
	SummonMonster(monster=Yaridovich, position=1, bit_6=True, bit_7=True)
])
```

Subroutines go in their own files. Here's the first one, it will have annotations telling you which events use it:
```python
"""referenced by battle_events BE0067_AXEM_RANGERS_GROUP_FORMATION, battle_events BE0088_SMITHY_TRANSFORMS_INTO_MAGIC_HEAD, ..."""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=33,
    script=[
        ClearAMEM8Bit(0x68, identifier="command_0x3a7531"),
        Set7E1xToAMEM8Bit(0x7EE01C, 0x68),
        Set7E1xToAMEM8Bit(0x7EE01D, 0x68),
        Set7E1xToAMEM8Bit(0x7EE01E, 0x68),
        Set7E1xToAMEM8Bit(0x7EE01F, 0x68),
        ReturnSubroutine(),
        SetAMEM8BitToAMEM(amem=0x60, source_amem=0xB0),
        ClearAMEMBits(0x60, [6]),
        SetAMEMToAMEM8Bit(dest_amem=0xB0, amem=0x60),
        ReturnSubroutine(),
        Db(bytearray(b"\xa0"), identifier="command_0x3a7550"),
        ReturnObjectQueue(),
    ],
)
```

You might have noticed that this has much more code than the first subroutine in the Lazy Shell screenshot. This is because this script outputs files for contiguous code blocks and not individual subroutines. So if it finds a subroutine at `0x3a7531` that ends at `0x3a7543` (inclusive) but also finds a subroutine that begins at `0x3a7544`, it will just write one file for as much continuous relevant code as it can find.

Finally, the script outputs python files that import all of these disassembled SMRPG scripts. Here's a short one that contains flower bonus messages, Toad tutorials, and their associated subroutines, aka everything in the 0x02xxxx range:
```
from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import AnimationScriptBankCollection
from .flower_bonus.export import bank as flower_bonus
from .toad_tutorial.export import bank as toad_tutorial
from .subroutines.export_0x02F50E import bank as subroutine_0x02F50E

collection = AnimationScriptBankCollection([
	flower_bonus,
	toad_tutorial,
	subroutine_0x02F50E,
])
```

(If you are importing this into your own python project, you can use `collection.render()` to get a `Dict[int,bytearray]` where the bytearray is your re-assembled bytes and the int is the ROM address you should begin patching them to.)

Standalone, this will produce a series of files that represent all of the battle animation code your ROM currently uses that the script could find. The output folders will be inside `src`.

Things to be careful about:
- I had to hardcode a lot of the ROM ranges that this will check. This is because pointers in battle animations aren't static, an object queue for example can start in a different place depending on what the value of AMEM $60 is. Even though the script will attempt to recursively trace all of you subroutines and queues and track AMEM $60 as best as it can to do this accurately, this can't be done perfectly because of things like `SetAMEMToRandomByte`, so a bunch more ranges are included because I determined that they were accessible via Lazy Shell animation types in one way or another. If you've changed the start or end of unindexed animations like monster behaviours in your ROM, then this will not work correctly and you will need to modify the `banks` dict of animationdisassembler.py. (If you're doing this, note the `end` address of a bank dict entry is **inclusive**, not exclusive. Don't ask me why I did it that way because I don't remember).

### Assembling battle animations

After you've changed the files produced by the disassembler to do whatever you want, you can use this:

```
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py animationassembler -r /path/to/rom/you/want/to/patch -t -b
```

- `-r`, `-t`, and `-b` are individually optional, but at least one needs to be used. 
- If you include `-r /path/to/rom/you/want/to/patch`, it will output a bps patch file with the contents of your battle animation files.
- If you include `-t`, it will output plain text files (split up according to the address the byte string starts at) with your assembled bytes. You can use this for debugging, such as if you want to side-by-side compare your results against the Lazy Shell editor's hex. It's all on one line though so it might be hard to use.
- If you include `-b`, it will output binary files (split up according to the address the byte string starts at) that you can paste over sections of your rom using FlexHEX.

The assembler script is really just a glorified wrapper that looks for files in the disassembler output directory and then calls each script bank's `.render()` method and writes the raw output to a file. If you're using the `.render()` method on `AnimationScriptBank`s in your own project, it will return bytearrays that you can do whatever you want with.

Things to be careful about:
- Battle animations are finnicky and largely unindexed, and worse yet, GOTO targets can be changed depending on the value of AMEM $60. To keep everything stable, some commands in your script files will have labels like `queuestart_0xsomeaddress`. **Do not change these particular labels.** When your scripts are being assembled, if it determines that a queue doesn't start where its `queuestart` label indicates, the task will fail.
- Similarly, the disassembler identifies how long a subroutine is supposed to be, so you'll see an `expected_size` argument in those scripts. **Don't change these lengths.** It can throw off where sprite queues end up. 
  - If you want to change subroutines or break a subroutine block into multiple subroutines or delete some commands, you are more than free to do that, just make sure that the `SubroutineOrBanklessScript` still comes to a length that matches its `expected_size`. You can fill space with useless bytes to make sure that the expected starts/lengths are still respected. There are a few ways you can do this. 
  - Example: At the end of your subroutine, if you have 3 or more bytes left, you can give your return statement an identifier and put a `Jmp` before it that jumps to your return statement. Then you can fill all the remaining space between `Jmp` and your return statement with useless bytes. Useless bytes could be things like repeating a bunch of  `StopShakingObject()` commands when no object is shaking or `StopCurrentSoundEffect()` when there are no sound effects (both of these are single-byte commands and you can use them repeatedly to fill any space) or use `AddCoins(0)` for three filler bytes, etc.

### Disassembling monster AI

This was based off of the battle disassembler that patcdr made in smrpg randomizer that enabled spell randomization!


Run this **in the root directory of this project** against an SMRPG rom file (vanilla or not). It will read all monster AI scripts and convert them into Python code. For example:

```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battledisassembler --rom "path/to/your/smrpg/rom/or/modified/smrpg/rom" 
```

This will output to a subfolder, `./src/disassembler_output/monster_ai`. 

For example, here is Megasmilax's AI as seen in Lazy Shell:

![alt text](image-1.png)

Here is the code that the script creates from reading that (scripts/script_204.py):

```python
# 204 - Megasmilax

from smrpgpatchbuilder.datatypes.enemies.implementations import *
from smrpgpatchbuilder.datatypes.items.implementations import *
from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.ids.battle_events import *

script = MonsterScript([
	IfVarBitsClear(0x7EE00A, [0]),
	SetVarBits(0x7EE00A, [0]),
	CastSpell(PetalBlast),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(4),
	CastSpell(PetalBlast),
	ClearVar(ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, PhysicalAttack0, ScrowDust),
	ClearVarBits(0x7EE00F, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(Drain, FlameWall, FlameWall),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	IncreaseVarBy1(0x7EE00E),
	RemoveTarget(MARIO),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, AttackDoNothing, AttackDoNothing),
	ClearVarBits(0x7EE00F, [0]),
	Wait1TurnandRestartScript()
])
```

I didn't bother adding indents to the disassembled output because, well... python.

You will also get a folder in the root of the monster_ai folder, monster_scripts.py, which imports all 256 battle scripts into a `MonsterScriptBank`. If you're using these scripts in your own code, you can import the `MonsterScriptBank` and run its `.render()` method, which will retur a tuple of **two bytearrays**. The first is meant to be patched at `0x3930AA` (where monster AI goes in the original game) and the second is meant to be patched to `0x39F400` (in case your scripts are very long and need some overflow room, the block at `0x39F400` is empty in the original game).

Standalone, this will produce a series of files that represent all of the monster AI code your ROM currently uses that the script could find. The output folders will be inside `src`.

### Assembling monster AI

After you've changed the files produced by the disassembler to do whatever you want, you can use this:

```
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battleassembler -r /path/to/rom/you/want/to/patch -t -b
```

- `-r`, `-t`, and `-b` are individually optional, but at least one needs to be used. 
- If you include `-r /path/to/rom/you/want/to/patch`, it will output a bps patch file with the contents of your battle animation files.
- If you include `-t`, it will output plain text files (split up according to the address the byte string starts at) with your assembled bytes. You can use this for debugging, such as if you want to side-by-side compare your results against the Lazy Shell editor's hex. It's all on one line though so it might be hard to use.
- If you include `-b`, it will output binary files (split up according to the address the byte string starts at) that you can paste over sections of your rom using FlexHEX.

The assembler script is really just a glorified wrapper that looks for files in the disassembler output directory and then calls each script bank's `.render()` method and writes the raw output to a file. If you're using the `.render()` method on a `MonsterScriptBank` in your own project, it will return 2 bytearrays that you can do whatever you want with (see previous section)
