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

If you want to use any `Jump to address` commands, you can do it by putting labels on your commands. You don't need to worry about ROM addresses at all! (However, just like in Lazy Shell, commads in 0x1Exxxx can only jump to other commands in 0x1Exxxx and not in 0x1Fxxxx, etc. These are called **banks** and you can jump to any command in any script as long as it's in the same bank.)
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

Most of this was designed to be used with smrpg randomizer. A lot of it can be reused, but there'll be a lot of stuff in here that doesn't match up to the original game, like the const names I've given to variables like event IDs, dialog IDs, etc. But you can extend this code's base classes for your purposes however you like.

This repo allows you to parse, modify, and rebuild:
- Battle animations ([disassemble](#disassembling-battle-animations) | [assemble](#assembling-battle-animations))
- Monster AI ([disassemble](#disassembling-monster-ai) | [assemble](#assembling-monster-ai))
- Event scripts and overworld NPC animations  ([disassemble](#disassembling-overworld-scripts) | [assemble](assembling-overworld-scripts))
- Overworld dialogs ([disassemble](#disassembling-dialogs) | [assemble](assembling-dialogs))
- Battle dialogs (soon)
- Overworld sprites (soon)

## Developing and changing your scripts

This repo's tools will output the scripts that are in your ROM. You can then browse them in an editor like VSCode. You can hover over each command to see hints about how to use it as well as what it's based on in Lazy Shell.
![alt text](image-4.png)

There are some commands included that are not in Lazy Shell yet that you can still use here.

If you're looking for a certain Lazy Shell command but don't know what class it is, search the src/smrpgpatchbuilder folder for the Lazy Shell command as it appears in the script editor's command dropdown. That will bring you to the class definition for the command you're looking for.

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

## How to run tests

In your venv:
`PYTHONPATH=src pytest src/tests`

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

You might notice that this outputs much more code sometimes than you will see in Lazy Shell. This is because this script outputs files for contiguous code blocks regardless of how they are pointed at. So if it finds a subroutine at `0x3a7531` that ends at `0x3a7543` (inclusive) but also finds a subroutine that begins at `0x3a7544`, it will just write one file for as much continuous relevant code as it can find.

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
- Try your best not to move commands around in a way that makes 0x35053C refer to something different than in the original ROM (this is part of the ally run away animation). There's a very annoying jump that targets partway through another command that I don't have a lenient way of dealing with yet.
- This is very, very much in alpha. You'll find that this takes an extremely long time to complete, to the order of several days. That's because this script does its best to recursively trace as much code as the game touches (in an attempt to help you find potentially unused code), which includes tracking all possible AMEM values when GOTOing different addresses based on what AMEM is (i.e. jump if amem = some number, object queue with index at amem $60, etc). Even though the script will attempt to do this accurately, it can't be done perfectly because of things like `SetAMEMToRandomByte`. For this reason I recommend never changing the start address and max size of any script file as it is generated for you.
- If you've changed the start or end of any top-level pointer tables in your ROM, then this will not work correctly and you will need to modify the `banks` dict of animationdisassembler.py. (If you're doing this, note the `end` address of a bank dict entry is **inclusive**, not exclusive. Don't ask me why I did it that way because I don't remember).
- Object queues always assume that their pointers point only toward code that comes AFTER it. For example if you define an object queue at $3A1234 and the first pointer is `0x23 0x01`, it might compile correctly, but it will never decompile correctly after that. Be careful to avoid doing this.

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
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, AttackDoNothing, AttackDoNothing),
	ClearVarBits(0x7EE00F, [0]),
	Wait1TurnandRestartScript()
])
```

I didn't bother matching Lazy Shell UI indents to the disassembled output because, well... python.

You will also get a folder in the root of the monster_ai folder, monster_scripts.py, which imports all 256 battle scripts into a `MonsterScriptBank`. If you're using these scripts in your own code, you can import the `MonsterScriptBank` and run its `.render()` method, which will retur a tuple of **two bytearrays**. The first is meant to be patched at `0x3930AA` (where monster AI goes in the original game) and the second is meant to be patched to `0x39F400` (in case your scripts are very long and need some overflow room, the block at `0x39F400` is empty in the original game).

Standalone, this will produce a series of files that represent all of the monster AI code your ROM currently uses that the script could find. The output folders will be inside `src`.

### Assembling monster AI

After you've changed the files produced by the disassembler to do whatever you want, you can use this:

```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battleassembler -r /path/to/rom/you/want/to/patch -t -b
```

- `-r`, `-t`, and `-b` are individually optional, but at least one needs to be used. 
- If you include `-r /path/to/rom/you/want/to/patch`, it will output a bps patch file with the contents of your battle animation files.
- If you include `-t`, it will output plain text files (split up according to the address the byte string starts at) with your assembled bytes. You can use this for debugging, such as if you want to side-by-side compare your results against the Lazy Shell editor's hex. It's all on one line though so it might be hard to use.
- If you include `-b`, it will output binary files (split up according to the address the byte string starts at) that you can paste over sections of your rom using FlexHEX.

The assembler script is really just a glorified wrapper that imports the disassembler output and then calls the script bank's `.render()` method and writes the raw output to a file. If you're using the `.render()` method on a `MonsterScriptBank` in your own project, it will return 2 bytearrays that you can do whatever you want with (see previous section)

### Disassembling overworld scripts

You can convert all 4096 overworld scripts and 1024 standalone NPC animations into Python code as well. One command will do both at the same time:

```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py eventconverter --rom "path/to/your/smrpg/rom/or/modified/smrpg/rom" 
```

This runs really, really slowly and takes several hours. I originally wrote disassembled events as dicts rather than command classes, and then wrote another script to convert them, so it does one and then the other. Possibly an issue to fix in a future revision, but I couldn't be bothered with how annoying it is to deal with embedded NPC animations.

Here is event 255 as it appears in Lazy Shell:
![alt text](image-2.png)

And here's how it looks when converted to Python:
```python
# E0255_EXP_STAR_HIT

script = EventScript([
	DisableObjectTrigger(MEM_70A8),
	StartSyncEmbeddedActionScript(target=MEM_70A8, prefix=0xF1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_Db(bytearray(b'\xfd\xf2'))
	]),
	SetSyncActionScript(MEM_70A8, A1022_HIT_BY_EXP_STAR),
	IncEXPByPacket(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_255_ret_13"]),
	SetBit(UNKNOWN_MIMIC_BIT, identifier="EVENT_255_set_bit_5"),
	SetBit(EXP_STAR_BIT_6),
	UnfreezeAllNPCs(),
	Pause(3),
	CreatePacketAtObjectCoords(packet=P031_LEVELUP_TEXT, object=MARIO, destinations=["EVENT_255_set_bit_5"]),
	PlaySound(sound=SO095_LEVEL_UP_WITH_STAR, channel=6),
	SetVarToConst(TIMER_701E, 64),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0254_EXP_STAR_HIT_SUBROUTINE, timer_var=TIMER_701E),
	Return(identifier="EVENT_255_ret_13")
])
```

Similarly, here's action script 2:
![alt text](image-3.png)

And here's how it looks in Python:
```python
#A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES

script = ActionScript([
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_JmpIfBitClear(TEMP_707C_1, ["ACTION_2_start_loop_n_times_3"]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(15),
	A_Pause(2),
	A_VisibilityOff(),
	Pause(2),
	A_VisibilityOn(),
	A_EndLoop(),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Return()
])
```

All action script commands are prefixed with `A_`. This is to distinguish them from event script commands.

Things to be aware of:
- This will produce scripts that add up to exactly the amount of bytes each bank can contain. To free up space, go to the final script (event 4095, action 1023) and delete all of the trailing `EndAll` class instantiators.
- Yo'ster Isle (events 470, 1837, 1839, 3329, 3729) has some weird implementation of this called "non-embedded action queues." That's event script code that's supposed to be read as NPC animation script code, despite having no header to indicate that. Non-embedded action queues are expected to begin at a certain offset relative to the start of the event. You can edit these events if you like, and the assembler will just insert dummy commands to fill space to keep the NEAQ where the game expects it. However, if you have too much code before the NEAQ that pushes it to a greater offset than it needs to be, you'll get an error when building your patch.
- There's a couple of overrides that are technically legal but that you should probably never do. Normally, when you're using commands that jump to other commands, you specify another command's `identifier` property as the destination, so that this code will take care of filling these in with ROM addresses for you. However, event 580 in the original game issues a jump to an address that isn't associated to an event. I've flagged this with `ILLEGAL_JUMP` in the identifier, which means you're allowed in general to use a destination of `ILLEGAL_JUMP_XXXX` where `XXXX` is a four-digit hex int indicating the offset you want to jump to and is unassociated with any other command. I *strongly* recommend against ever doing this.
- Similarly, queue 53 and queue 137 in the original game use sound ID 255. I have no idea what that is, sounds are only supposed to go up to 163 or something like that. This is another thing that's technically legal but that you shouldn't do.

### Assembling overworld scripts

The disassembler produces individual script files as well as two files (events.py and actionqueues.py) that contain them. events.py includes an `EventScriptController` that contains all of the event scripts in 0x1Exxxx, 0x1Fxxxx, and 0x20xxxx, each in their own `EventScriptBank`. Calling the `EventScriptController`'s `render()` method will produce three bytearrays that include a pointer table and script data, one per high byte. Standalone action scripts on the other hand are all contained in 0x21xxxx, so actionqueues.py only contains one `ActionScriptBank` and its `render()` method produces a single bytearray that contains the pointer table and script data in a contiguous block.

After you've edited the script files to do whatever you want, you can assemble event scripts and NPC action scripts back into ROM data in one command, since the assembler is just a glorified wrapper for `render()`:

```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py eventassembler -r /path/to/rom/you/want/to/patch -t -b
```

- `-r`, `-t`, and `-b` are individually optional, but at least one needs to be used. 
- If you include `-r /path/to/rom/you/want/to/patch`, it will output a bps patch file with the contents of your battle animation files.
- If you include `-t`, it will output plain text files (split up according to the address the byte string starts at) with your assembled bytes. You can use this for debugging, such as if you want to side-by-side compare your results against the Lazy Shell editor's hex. It's all on one line though so it might be hard to use.
- If you include `-b`, it will output binary files (split up according to the address the byte string starts at) that you can paste over sections of your rom using FlexHEX.

This will assemble event scripts **and** standalone NPC action scripts.

### Disassembling dialogs

Dialogs in SMRPG are split into banks 0x22xxxx, 0x23xxxx, 0x24xxxx. You can disassemble dialog info into files that you can more or less edit as text.

Run this **in the root directory of this project** against an SMRPG rom file (vanilla or not). It will read all overworld dialogs and convert them into Python code. For example:

```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py dialogdisassembler --rom "path/to/your/smrpg/rom/or/modified/smrpg/rom" 
```

This will output to a subfolder, `./src/disassembler_output/dialogs`. This one's a bit slower, I could have written the code a lot better, oh well.

You'll see a file called dialogs.py:

```python
from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection
from .contents.dialog_pointers import pointers
from .contents.dialog_table_0x22 import dialog_data as data_0
from .contents.dialog_table_0x23 import dialog_data as data_1
from .contents.dialog_table_0x24 import dialog_data as data_2

data = DialogCollection(pointers, [data_0, data_1, data_2], ...)
```

A `DialogCollection` represents all of the dialog in the game. If you're importing this in your own project, `.render()` will produce a `Dict[int, bytearray]` where the int is the address to patch the bytearray at.

Disassembled dialog data is split up into two parts. You'll see three files full of actual dialog data that look like this:
```python
dialog_data[315] = ''' Thanks a million, Mario!
 Say[delay][delay],...[delay][delay]were my treasures OK?[await]
 [select]  (They sure were)
 [select]  (I wouldn't say so)[await]'''
dialog_data[316] = ''' Oh! That’s great news!
 What a relief![await]'''
```

And one pointer file that looks like this:
```python
...
pointers[793] = Dialog(bank=0x22, index=315, pos=22)
pointers[794] = Dialog(bank=0x22, index=316, pos=0)
...
```

The data files contain the actual dialog text. They're broken up into individual strings based on where text-terminating characters were in the original game. You can add or delete dialogs in these tables as you like (I think), as long as the whole file doesn't have too much text to fit into the ROM.

The pointer table is what you'll need to make your dialogs work. Don't change the length of this table or any of the `bank` properties.
The `index` property corresponds to which entry in the data file you want. So in the above example, dialog 793 references data entry 315 (in the 0x22 file, as indicated by the `bank` property), which is the "Thanks a million, Mario!" dialog. To use this in your romhack, you'd run dialog ID 793 in your event scripts to get a NPC to say that.
The `pos` property determines where the dialog should actually start. In the first example, `pos=22` means that the dialog will actually start after 22 characters. So if you run dialog 793 in your event script, the NPC will actually start talking at "Say... were my treasures OK?"

"But wait, there's more than 22 characters before that!" Yes - this script accommodates **compression tables**. The string "in" is actually represented by a single byte, 0x10. By default, SMRPG has space for twelve of these compressions and they use bytes 0x0E to 0x19 inclusive. The disassembler will parse the compression table in your rom and include it in the output dialogs.py file.

You'll also see that some special characters I've represented with directives like `[await]` and `[pause]` etc, just so that it's easier for you to understand what's actually happening in the dialog. These are single bytes in the game as well and they will be assembled as such.


### Assembling dialogs

After you've changed the dialog data files output by the disassembler, including changing your compression table in dialogs.py if you like, you can run:

```
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py dialogassembler -r /path/to/rom/you/want/to/patch -t -b
```

- `-r`, `-t`, and `-b` are individually optional, but at least one needs to be used. 
- If you include `-r /path/to/rom/you/want/to/patch`, it will output a bps patch file with the contents of your battle animation files.
- If you include `-t`, it will output plain text files (split up according to the address the byte string starts at) with your assembled bytes. You can use this for debugging, such as if you want to side-by-side compare your results against the Lazy Shell editor's hex. It's all on one line though so it might be hard to use.
- If you include `-b`, it will output binary files (split up according to the address the byte string starts at) that you can paste over sections of your rom using FlexHEX.

The assembler script is really just a glorified wrapper that looks for files in the disassembler output directory and then calls the dialog collection's `.render()` method and writes the raw output to a file. If you're using the `.render()` method on a `DialogCollection` in your own project, it will return 2 bytearrays that you can do whatever you want with (see previous section)
