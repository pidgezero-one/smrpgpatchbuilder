# SMRPG Patch Builder

Freeform editing of various kinds of SMRPG scripts and sprites. You can disassemble the contents of your ROM, edit the output, reassemble, and then patch to your ROM. Some basic coding knowledge is ideal for using this, but scripts overall are made to resemble how they're written in Lazy Shell.

Most of this was designed to be used with smrpg randomizer. A lot of it can be reused, but there'll be a lot of stuff in here that doesn't match up to the original game, like descriptions of what event script variables are used for, unused enemy classes being missing, certain item implementations being missing (there's no alto card item class in here for example), etc. You can extend this code for your purposes however you like.

## How to use scripts

These instructions are for bash terminals, aka mac/linux only (no powershell). If you want to do this on windows you'll need to figure out on your own what the equivalent steps are here (but you can probably use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) and these steps will likely still work after some finagling).

- Install the Python runtime for your operating system. All further steps assume that your PATH variable will execute python 3 when you use `python` in the command line (and that you don't have that pointing to a separate python 2 install for example)
- Create a virtual environment: `python -m venv MyVirtualEnvironmentNameWhateverIWant`
- Activate the virtual environment: `source ~/.venvs/MyVirtualEnvironmentNameWhateverIWant/bin/activate`
- Install required packages: `pip install -r requirements.txt`

Everything beyond this point must be in your venv. You'll know you're doing that correctly when your terminal prompts have your venv name in them, like this if you use vscode:
```
(MyVirtualEnvironmentNameWhateverIWant) stefkischak@Stefs-MBP smrpgpatchbuilder %
```

### Battle animation disassembler

Run this script **in the root directory of this project** against an SMRPG rom file (vanilla or not). It will read all battle animations and convert them into Python code. For example:

```bash
PTHONPATH=src python src/smrpgpatchbuilder/manage.py animationdisassembler --rom "path/to/your/smrpg/rom/or/modified/smrpg/rom" 
```

This will output to a subfolder, `./src/disassembler_output/battle_animation`. 

For example, here is part of the Yaridovich mirage attack as seen in Lazy Shell:

![alt text](image.png)

Here is the code that the script creates from reading that (battle_events/contents/script_22.py):

```python
# BE0022_YARIDOVICH_MIRAGE_ATTACK

from smrpgpatchbuilder.datatypes.battle_animation_scripts import *

script = BattleAnimationScript(header=["command_0x3a647c"], script = [
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac3b2"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a7729"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=90),
	ClearAMEM8Bit(0x68),
	SetAMEMToRandom(amem=0x68, upper_bound=7),
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

You might have noticed that this has much more code than the first subroutine in the Lazy Shell screenshot. This is because this script outputs files for contiguous code blocks, not necessarily contiguous cutscenes. So if it finds a subroutine at `0x3a7531` that ends at `0x3a7543` (inclusive) but also finds a subroutine that begins at `0x3a7544`, it will just write one file for as much continuous relevant code as it can find.

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

You can then import `collection` in your own Python files/projects which will give you the ability to modify your scripts and then convert them back to patchable bytes.

This will produce a series of files that represents all of the battle animation code your ROM currently uses that the script could find. You can then copy and paste these files into your own Python project where you have this library imported, and edit them however you like. Then when you call `.render()` on your `AnimationScriptBank`, it will turn your edited battle animation code into bytes. From there you can write your own code to patch it to your ROM or whatever.

Things to be careful about:
- This script will try to recursively find every subroutine and sprite queue that gets used by your pointer-indexed battle animation types (item animations, ally spells, etc, any animation type that uses a pointer table). For un-indexed animation types (battle behaviours) I hardcoded some of the ranges it'll need to look for in the original game. That means if you've changed the start or end of any monster behaviours then this will not work correctly and you will need to supply those ranges yourself in the `banks` dict. (If you're doing this, note the `end` address of a bank dict entry is **inclusive**, not exclusive. Don't ask me why I did it that way because I don't remember).

Now if you've worked with Lazy Shell's battle animation editor in any great capacity you know that there are commands like object queues whose offsets depend on the value of AMEM $60. I did my best to have the script keep an estimate of what your $AMEM 60 value is as it steps through your ROM's code so that it can disassemble and include the correct object queues.

### Battle animation assembler

Takes the files created by the battle animation disassembler and converts them back into bytes that could be patched into a rom. That means you can edit the files produced by the disassembler to whatever you want, and this would be how you get your changes back into bytes.

You can use it like this:

```
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py animationassembler -r /path/to/rom/you/want/to/patch -t -b
```

-r, -t, and -b are optional individually, but there needs to be at least one present. 
- If you include `-r /path/to/rom/you/want/to/patch`, it will output a bps patch file with the contents of your battle animation files.
- If you include `-t`, it will output plain text files (split up according to the address the byte string starts at) with your assembled bytes. You can use this for debugging, such as if you want to side-by-side compare your results against the Lazy Shell editor's hex. It's all on one line though so it might be hard to use.
- If you include `-b`, it will output binary files (split up according to the address the byte string starts at) that you can paste over sections of your rom using FlexHEX.

The assembler script is really just a glorified wrapper that looks for files in the disassembler output directory ansd then calls each script bank's `.render()` method and writes the raw output to a file. If you're using the `.render()` method on `AnimationScriptBank`s in your own project, it will return bytearrays that you can do whatever you want with.

Things to be careful about:
- Battle animations are extremely finnicky, they aren't like event scripts or action scripts which are entirely indexed with a pointer table. There's not a whole lot of accountability I can add to this program to make sure that sprite queues begin where they are supposed to begin. Therefore some commands in your script files will have identifiers like "queuestart_0xsomeaddress". When it's assembling your script bank, if it determines that an animation queue's starting address does not match what's in its `queuestart` identifier, it will throw an error.
- Similarly, the disassembler identifies how long a subroutine is supposed to be. I do not recommend changing the subroutine lengths because that can throw off where sprite queues end up. If you want to change subroutines or break a subroutine block into multiple subroutines or delete some commands, you are more than free to do that, just make sure that the `SubroutineOrBanklessScript` still comes to a length that matches its `expected_size`.
- If you change subroutines or anything that might change where a sprite queue starts, you can fill space with useless bytes to make sure that the expected starts/lengths are still respected. There are a few ways you can do this. 
  - At the end of your subroutine, if you have 3 or more bytes left, you can give your return statement an identifier and put a `Jmp` before it that jumps to your return statement. Then you can fill all the remaining space between `Jmp` and your return statement with useless bytes. Useless bytes could be things like repeating a bunch of  `StopShakingObject()` commands when no object is shaking or `StopCurrentSoundEffect()` when there are no sound effects (both of these are single-byte commands and you can use them repeatedly to fill any space) or use `AddCoins(0)` for three filler bytes, etc.