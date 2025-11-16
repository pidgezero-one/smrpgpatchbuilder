# SMRPG Patch Builder

Freeform editing of various things in Super Mario RPG.

This is not a decomp.

## How this works

Convert some contents of your ROM into Python code so you can freely edit it, then create a patch to get your changes into your ROM. You can do this for:
- ✅ [event scripts](#event-and-action-scripts)
- [battle animation scripts](#battle-animation-scripts)
- [monsters](#monsters)
- [monster AI scripts](#monster-ai-scripts)
- ✅ [monster attacks](#monster-attacks)
- ✅ [monster and ally spells](#monster-and-ally-spells)
- ✅ [allies](#allies)
- ✅ [items](#items)
- [sprites](#sprites)
- ✅ [shops](#shops)
- ✅ [overworld dialogs](#overworld-dialogs)
- ✅ [battle dialogs and battle messages](#battle-dialogs-and-messages)
- [battle packs and formations](#battle-packs-and-formations)
- ✅ [packet NPCs](#packet-npcs)
- ✅ [rooms and NPCs](#rooms-and-npcs)
- ✅ [overworld location data](#overworld-location-data)

(✅ = roundtrip tested and working)

You can also take the contents of your disassembler_output folder and stick it in whatever Python project you want, as long as that project imports this package. (example: SMRPG randomizer)

## Getting started

These instructions are for bash terminals (no powershell). On Windows, you can use WSL (note that your ROM will be in `/mnt/some_drive_letter/path/to/your/smrpg/rom`) but setup for WSL is beyond the scope of this guide.

### Step 0

- Install the Python runtime for your operating system. All further steps assume that your PATH variable will execute python 3 when you use `python` in the command line (and that you don't have that pointing to a separate python 2 install for example)
- Create a virtual environment: `python -m venv MyVirtualEnvironmentNameWhateverIWant`
- Activate the virtual environment: `source ~/.venvs/MyVirtualEnvironmentNameWhateverIWant/bin/activate` (might differ depending on your setup, use google if that's the case)
- Install required packages: `pip install -r requirements.txt`

Everything you do beyond this point must be in your venv. You'll know you're in your venv when your terminal prompts have your venv name in them, like this if you use vscode:

```
(MyVirtualEnvironmentNameWhateverIWant) stef@Stefs-MBP smrpgpatchbuilder %
```

### Step 1

This patch builder helps you remember the context of the things you're building. The first thing you should do is copy the contents of the config.example folder into the config folder. 

Then inside the config folder, you'll see a bunch of plaintext files. They are:
- `action_script_names.input`: Describe your 1024 action scripts.
- `animationdata_write.input`: If you want to move animation pack data for sprites to anywhere else in the ROM beyond where SMRPG keeps it by default (which you could do if you want to free up space for sprite tile data in 0x280000-0x370000), indicate your desired ranges here. Be sure to break them up by upper byte so that they work correctly.
- `animationpack_read.input`: If you have moved the pointer table for sprite animation pack data to anywhere else in the ROM besides where SMRPG keeps it by default, indicate the range here.
- `battle_effect_names.input`: These are the things you edit in the `Effects` editor in Lazy Shell (128 total).
- `battle_event_names.input`: There are 103 battle events in the game, you can describe them here if you have modified them.
- `battle_sfx_names.input`: If you have changed any of the 211 sound effects accessible during battle, you can name them here.
- `battle_variable_names.input`: If you've modified monster AI scripts in a way that reserves certain $7EE00x variables for certain purposes, you can describe them here.
- `battlefield_names.input`: If you've changed any of the 64 battlefields, rename them here.
- `dialog_names.input`: If you want to remember what certain overworld dialogs are being used for, you can give them names here. There's 4096 of them, so it can be handy.
- `event_script_names.input`: Describe your 4096 event scripts.
- `imagepack_read.input`: If you have moved image pack data for sprites to anywhere else in the ROM besides where SMRPG keeps it by default, indicate the range here.
- `item_prefixes.input`: Items and ally spells can begin with a special symbol or a blank space. If you've changed what any of those symbols look like in your ROM's alphabet, indicate them here. (i.e. if you've replaced the fan symbol, normally 0x26, wholesale with some other symbol, rename it here)
- `music_names.input`: Rename the game's music tracks if you've changed them.
- `overworld_area_names`: Rename the 56 world map destinations here if you need to.
- `overworld_sfx_names`: If you have changed any of the 163 sound effects accessible in the overworld, you can name them here. (There are actually 256 rows because there is one instance in the original game of a SFX command trying to use ID 255, so ID 255 acts as a placeholder)
- `pack_names.input`: Describe any of the 256 battle pack definitions here (these are referenced by overworld scripts when loading a specific battle)
- `packet_names.input`: A packet is a NPC created on the fly by an event script or action script (as opposed to a NPC that exists in the room definition), such as the mushrooms/flowers/etc that appear temporarily when you open a treasure chest. You can disassemble and edit those. In this file, put descriptive names for them.
- `room_names.input`: You can name the 510 levels in the game. By default most of these are derived from the level descriptions in Lazy Shell.
- `screen_effect_names.input`: If you've changed any of the 21 screen effects used in battle, you can describe them here.
- `shop_names.input`: If you've changed any of the 33 shops, rename them here.
- `sprite_names.input`: Give names to the 1024 NPC sprites in your ROM.
- `tiles_read.input`: The list of ranges where uncompressed NPC tiles are in the ROM
- `tiles_write.input`: The list of ranges where uncompressed NPC tiles in the ROM should be written to (if you've moved animation packs somewhere else, for instance, you could expand this to accommodate more tiles). Be sure to break them up by upper byte so that pointers work correctly, see example file. This should be the same as tiles_read.input if you want to read and write tile data to the same place.
- `toplevelsprite_read.input`: The addresses where sprite containers live (which hold image pack data and animation pack data to make a whole sprite). This should only be one line. You can change it if you've moved that data in your ROM to somewhere else.
- `variable_names.input`: Every $7000 var and $7000 var bit that can be used by Lazy Shell's event script editor is in this file. Rename the variables according to what you're using them for in your ROM.

Make sure that even if you don't rename any variables, **do not delete any lines**, it will mess up your code that uses it. 

<sup>Note: There are no files here to name your items, enemies, attacks, or spells. This is on purpose! Those will be retrieved from your ROM in a different way.</sup>

### Step 2

Run 
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py variableparser
```
in the root folder of this repo. It will create files in `./src/disassembler_output/variables` that define Python variables according to the names you gave in Step 1. Everything else you disassemble will be using these.

### Step 3

Disassemble items, spells, monster attacks, and packets by running:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py itemdisassembler --rom "/path/to/your/smrpg/rom"
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py enemyattackdisassembler --rom "/path/to/your/smrpg/rom"
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py spelldisassembler --rom "/path/to/your/smrpg/rom"
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packetdisassembler --rom "/path/to/your/smrpg/rom"
```

These will produce: 
- `./src/disassembler_output/items.items.py`
- `./src/disassembler_output/enemy_attacks/attacks.py`
- `./src/disassembler_output/spells/spells.py`
- `./src/disassembler_output/packets/packets.py`

It is important to do these next because other things will use these. Event scripts and monster definitions (ie loot drops) will need to reference items, monster AI scripts use attacks and spells, allies use spells, and event/action scripts use packets.

### Step 4

Disassemble monsters and battle animations (warning: this takes several hours)
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py combined_disassembler --rom "/path/to/your/smrpg/rom"
```

These will produce `./src/disassembler_output/battle_animation/scripts.py` and `./src/disassembler_output/enemies/enemies.py`. It is important to do these together at first because they depend on each other (battle animations need to use enemy classes but enemy classes need a battle animation pointer label for Sprite Behaviour). (On subsequent runs you can disassemble them separately.)

### Step 5

Now you can disassemble whatever else you want. There are no more dependencies.

## Details on the things you can disassemble and patch

### Event and action scripts

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py eventconverter --rom "path/to/your/smrpg/rom" # be warned, this will probably take a few hours
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py eventassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/overworld_scripts/event
./src/disassembler_output/overworld_scripts/animation
```

For an example of an overworld script, if your ROM has this:
![alt text](image-6.png)
you would get this:
```python
# E0313_MUSHROOM_KINGDOM_OCCUPIED_GRANDMA

script = EventScript([
	RunDialog(dialog_id=DI0676_GRANDMA_DURING_MK_INVASION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
```

You can then edit that however you like. For example you could set a variable:
```python
# E0313_MUSHROOM_KINGDOM_OCCUPIED_GRANDMA

script = EventScript([
	RunDialog(dialog_id=DI0676_GRANDMA_DURING_MK_INVASION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddConstToVar(COIN_COUNTER_1, 1),
	Return()
])
```

You can also use `Jump to address` commands without having to worry about pointer addresses at all*. In this example, `JmpIfBitClear` is looking for a name instead of a $xxxx pointer, and the `SetBit` command further below has the name it's looking for:
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

This disassembler/assembler always processes event scripts and action scripts together. Action scripts look like this:
![alt text](image-3.png)
```python
#A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES

script = ActionScript([
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_JmpIfBitClear(TEMP_707C_1, ["ACTION_2_start_loop_n_times_3"]),
	A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
	A_StartLoopNTimes(15, identifier="ACTION_2_start_loop_n_times_3"),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_EndLoop(),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue()
])
```
<sup>(All action script commands are prefixed with `A_` to distinguish them from event script commands.)</sup>

Embedded action queues within event scripts are also supported. They use the same contents as action scripts:
![alt text](image-2.png)
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
	CreatePacketAtObjectCoords(packet=P031_LEVELUP_TEXT, target_npc=MARIO, destinations=["EVENT_255_set_bit_5"]),
	PlaySound(sound=SO095_LEVEL_UP_WITH_STAR, channel=6),
	SetVarToConst(TIMER_701E, 64),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0254_EXP_STAR_HIT_SUBROUTINE, timer_var=TIMER_701E),
	Return(identifier="EVENT_255_ret_13")
])
```

When it comes time to build your scripts into ROM patches, the builder code will convert names into pointers for you.

<sup>*caveat: you still need to be conscious about the script ID because two-byte pointers are still a thing. Jump commands in scripts 0-1535 can only jump to other scripts in 0-1535 (0x1Exxxx), same with 1536-3071 (0x1Fxxxx), same with 3072-4095 (0x20xxxx).</sup>

The `__init__.py` in each of the two output folders will export either a `ActionScriptBank` or three `EventScriptBank`s. If you want to use these in another Python project, it should import these. For both types, `bank.render()` returns a bytearray that when building your ROM should be patched at `bank.pointer_table_start`.

Notes:
- You can Ctrl+F the name of a command in Lazy Shell in src/smrpgpatchbuilder/datatypes/overworld_scripts to find the documentation for how to use that command in Python.
- The disassembler will produce scripts that add up to exactly the amount of bytes each bank can contain. To free up space, go to the final script (event 4095, action 1023) and delete all of the trailing `EndAll` class instantiators.
- Yo'ster Isle (events 470, 1837, 1839, 3329, 3729) has some weird implementation of this called "non-embedded action queues." That's event script code that's supposed to be read as NPC animation script code, despite having no header to indicate that. Non-embedded action queues are expected to begin at a certain offset relative to the start of the event. These are the five events that editing is disabled for in Lazy Shell. With disassembled scripts, you can edit these scripts if you like, but if you add too much code such that the NEAQ is pushed to a greater offset than it's expected to be, you'll get an error when building your patch. (Removing code before the NEAQ is fine, the assembler will fill in space to adjust it.)
- There's a couple of overrides that are technically legal but that you should probably never do. Normally, when you're using commands that jump to other commands, you specify another command's `identifier` property as the destination, so that this code will take care of filling these in with ROM addresses for you. However, event 580 in the original game issues a jump to an address that isn't associated to an event. I've flagged this with `ILLEGAL_JUMP` in the identifier, which means you're allowed in general to use a destination of `ILLEGAL_JUMP_XXXX` where `XXXX` is a four-digit hex int indicating the offset you want to jump to and is unassociated with any other command. I *strongly* recommend against ever doing this.
- Similarly, queue 53 and queue 137 use sound ID 255. I have no idea what that is, but it's accommodated for. This is another thing that's technically legal but that you shouldn't do.

<sub>([back to top](#how-this-works))</sub>

### Battle animation scripts

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py animationdisassembler --rom "path/to/your/smrpg/rom" # be warned, this will probably take a few hours
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py animationassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/battle_animation/scripts.py
```
which exports three folders, each with its own `AnimationScriptBank` class (one for $02xxxx, one for $35xxxx, one for $3Axxxx) - if you want to use your disassembled scripts in another Python project, these are what your project should import. `bank.render()` return type is `list[tuple[int, bytearray]]`, when building your ROM patch, each bytearray should be patched at its corresponding int (address).

For an example of a battle animation script, if your ROM has:
![alt text](image.png)
you would get this:
```python
# BE0022_YARIDOVICH_MIRAGE_ATTACK

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
<sup>(note you can see how your custom battle event names and sprite names are used here!)</sup>

Battle animations are typically the most restrictive type of script to edit because of how sensitive pointers to things like object queues and sprite queues are, but those restrictions are accounted for to give you more freedom. This is accomplished by the disassembler reading all of the scripts it can find in your ROM and recursively tracing through them to find subroutines, object queues, sprites queues, etc to build a profile of how much code it can find and where it lives. Like with event and action scripts, pointers (including object/sprite queue pointers) are replaced with name strings. 

This allows you to freely edit your battle animation scripts however you like, just as if they were event scripts or animation scripts. For example, there's no longer any need to worry about whether a command you're trying to replace will be the same size or not. The assembler will warn you if your code is too long and will go out of bounds, and if it's not, it'll proceed to build your patch and calculate pointers on its own.*

Battle animations however are NOT like event scripts and action scripts in that script files are not separated by pointer. When the disassembler recursively traces your code, it builds a profile of which ranges within the ROM it can verify are being used, and then create one script file per contiguous range. That means in the above Yaridovich script, you can see the code that comes after what would be the final "Jump to $3A7550" command in Lazy Shell.

<sup>*caveat: you still need to be conscious about where in the ROM your script is going. Commands in 0x35xxxx can't jump to 0x02xxxx or 0x3Axxxx or vice versa.</sup>

This is still easily the most volatile part of the game that this repo lets you edit, so here are some considerations to be aware of:

- You can Ctrl+F the name of a command in Lazy Shell in src/smrpgpatchbuilder/datatypes/battle_animation_scripts to find the documentation for how to use that command in Python.
- This is still very, very much in alpha. You'll find that disassembly takes an extremely long time to complete, to the order of several hours, because the recursive tracer goes as far as trying to find object queue branches based on all possible AMEM $60 values there can be when trying to reach it. This is still an imperfect approximation and not completely comprehensive, because of things like `SetAMEMToRandomByte` or setting AMEM to non-AMEM $7E:xxxx vars. 
- Every script file you get will include an address that it intends to patch to and an expected size that it shouldn't exceed. **Do not change these.** This is determined by what parts of the ROM the disassembler was able to access when reading your code. Changing this value means you might be overwriting something that wasn't hit by the recursive trace, aka something the assembler doesn't know exists and might be bad to overwrite.
- If your changed script is shorter than the script's expected size, that's okay! It just can't be longer than the expected size.
- I've done my best to make sure that pointers referenced outside of battle animations (such as monster definitions including pointers to where their sprite behaviours live) will stay intact, however it's possible that there are some I missed, which means those external pointers will no longer work if your code changes shape too much. Let me know if you come across anything like that and I can add it to the disassembler.
- Pointer tables for things like weapons, battle events, etc are treated as object queues, because that's basically what they are. For reasons above, don't try to add or remove pointers from these unless you really know what you're doing.
- If you've changed the start or end of any top-level pointer tables in your ROM, then this will not work correctly and you will need to fork this repo and modify the `banks` dict of animationdisassembler.py. (If you're doing this, note the `end` address of a bank dict entry is **inclusive**, not exclusive. Don't ask me why I did it that way because I don't remember).
- Object queues always assume that their pointers point only toward code that comes AFTER it. For example if you define an object queue at $3A1234 and the first pointer is `0x23 0x01`, it might compile correctly, but it will never decompile correctly after that. Be careful to avoid doing this.
- The "Ally tries to run" animation in the original game does something weird, as in it jumps to a byte that is actually an argument of another command and not a command on its own. The disassembler forcibly changes this so that it points instead to a real command. This required some educated guesses about what opcodes 0x02 and 0x47 do, so you'll see those command classes named with the word "EXPERIMENTAL" in them. No other scripts in the original game do this as far as I could find.
- `UnknownCommand`s produced by the disassembler are raw bytes whose opcode we don't know what it does. It's possible that some of these undocumented commands might be pointers, which means the code will break if the destination these raw bytes were meant to point to changes. If this happens, let me know and I'll see if you might have discovered an opcode that uses a pointer, and will integrate it into this code (for example I had to do this for 0x47).

<sub>([back to top](#how-this-works))</sub>

### Monsters

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py enemydisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py enemyassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/enemies/enemies.py
```

Using Mokura as an example:
![alt text](image-7.png)
The disassembler produces this Python class:
```python
class MOKURA(Enemy):
    """MOKURA enemy class"""
    _monster_id: int = 148
    _name: str = "MOKURA"

    _hp: int = 620
    _fp: int = 100
    _attack: int = 120
    _defense: int = 75
    _magic_attack: int = 80
    _magic_defense: int = 90
    _speed: int = 25
    _evade: int = 20
    _magic_evade: int = 10
    _status_immunities: List[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    _resistances: List[Element] = [Element.THUNDER, Element.JUMP]
    _xp: int = 90
    _coins: int = 0
    _yoshi_cookie_item = MushroomItem
    _rare_item_drop = RoyalSyrupItem
    _common_item_drop = KerokeroColaItem
    _flower_bonus_type: FlowerBonusType = FlowerBonusType.ATTACK_UP
    _flower_bonus_chance: int = 20
    _sound_on_hit: HitSound = HitSound.CLAW
    _sound_on_approach: ApproachSound = ApproachSound.NONE
    _coin_sprite: CoinSprite = CoinSprite.NONE
    _entrance_style: EntranceStyle = EntranceStyle.NONE
    _monster_behaviour: str = "unknown_0x350ADF"
    _elevate: int = 2
    _ohko_immune: bool = True
    _psychopath_message: str = " Mwa ha ha...[await]"
	# TODO cursor positions
```

The disassembler creates an `EnemyCollection` containing all 256 enemies:

```python
ALL_ENEMIES = EnemyCollection([
    Goomba(),
    Spikey(),
    ...
])
```

Other things like battle packs will import these classes.

If you want to use these in another Python project, you'll need to import the `EnemyCollection`. To build a patch for it, you will _also_ need an `AnimationScriptBank` (so that it can figure out what pointers to use for your monsters' sprite behaviours). `enemycollection.render(animationscriptbank.build_command_address_mapping())` produces a `dict[int, bytearray]` where each `int` is a ROM address where its corresponding `bytearray` should be patched.

<sub>([back to top](#how-this-works))</sub>

### Monster AI scripts

This was based off of the battle disassembler that patcdr made in smrpg randomizer that enabled spell randomization!

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battledisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battleassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/monster_ai/monster_scripts.py
```
which exports a `MonsterScriptBank` - if you want to use your disassembled scripts in another Python project, this is what your project should import. `bank.render()` returns `tuple[bytearray, bytearray]` - when building your ROM patch, the first `bytearray` should go to `bank.range_1_start` and the second to `bank.range_2_start`.

For individual scripts, if you have this in your ROM:
![alt text](image-1.png)
the disassembler will give you:
```python
# 204 - Megasmilax

script = MonsterScript([
	IfVarBitsClear(BV7EE00A, [0]),
	SetVarBits(BV7EE00A, [0]),
	CastSpell(PetalBlastSpell),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(4),
	CastSpell(PetalBlastSpell),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	ClearVar(BV7EE005_DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(BV7EE005_DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, Attack0, ScrowDustAttack),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(DrainSpell, FlameWallSpell, FlameWallSpell),
	StartCounterCommands(),
	IfHPBelow(0),
	RunObjectSequence(3),
	IncreaseVarBy1(BV7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(BV7EE00F, [0]),
	Attack(Attack0, DoNothing, DoNothing),
	ClearVarBits(BV7EE00F, [0]),
	Wait1TurnandRestartScript()
])
```

You can Ctrl+F the name of a command in Lazy Shell in src/smrpgpatchbuilder/datatypes/monster_scripts to find the documentation for how to use that command in Python.

<sub>([back to top](#how-this-works))</sub>

### Monster attacks

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py enemyattackdisassembler --rom "path/to/your/smrpg/rom"
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py enemyattackassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/enemy_attacks/attacks.py
```

The disassembler creates an `EnemyAttackCollection` (in the same file) that instantiates all of your EnemyAttack classes. If you want to use these attacks in another Python project, you'll need to import the `EnemyAttackCollection`. To prepare the patch data, run `collection.render()` to get a `dict[int, bytearray]` where each `int` is a ROM address to which the `bytearray` should be patched.

<sub>([back to top](#how-this-works))</sub>

### Monster and ally spells

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py spelldisassembler --rom "path/to/your/smrpg/rom"
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py spellassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/spells/spells.py
```

The disassembler creates a `SpellCollection` (in the same file) that instantiates all of your Spell classes. If you want to use these spells in another Python project, you'll need to import the `SpellCollection`. To prepare the patch data, run `collection.render()` to get a `dict[int, bytearray]` where each `int` is a ROM address to which the `bytearray` should be patched.

<sub>([back to top](#how-this-works))</sub>

### Allies

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py spelldisassembler --rom "path/to/your/smrpg/rom"
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py spellassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/allies/allies.py
```

The disassembler creates an `AllyCollection` that instantiates all five of your allies. If you want to use these characters in another Python project, you'll need to import the `AllyCollection`. To prepare the patch data, run `collection.render()` to get a `dict[int, bytearray]` where each `int` is a ROM address to which the `bytearray` should be patched.

Allies look like this:
![alt text](image-15.png)

```python
MARIO_Ally = Ally(
    index=0,
    name="Mario",
    starting_level=1,
    starting_current_hp=20,
    starting_max_hp=20,
    starting_speed=20,
    starting_attack=20,
    starting_defense=0,
    starting_mg_attack=10,
    starting_mg_defense=2,
    starting_experience=0,
    starting_weapon=None,
    starting_armor=None,
    starting_accessory=None,
    starting_magic=[
        JumpSpell,
    ],
    levels=[
        LevelUp(
            level=2,
            exp_needed=16,
            spell_learned=None,
            hp_plus=5,
            attack_plus=3,
            defense_plus=2,
            mg_attack_plus=2,
            mg_defense_plus=2,
            hp_plus_bonus=3,
            attack_plus_bonus=1,
            defense_plus_bonus=1,
            mg_attack_plus_bonus=3,
            mg_defense_plus_bonus=1,
        ),
        ...
    ],
    coordinates=AllyCoordinate(
        cursor_x=1,
        cursor_y=3,
        sprite_abxy_y=191,
        cursor_x_scarecrow=1,
        cursor_y_scarecrow=3,
        sprite_abxy_y_scarecrow=192,
    )
)
```

where `coordinates` controls where the cursor and ABXY buttons will appear relative to their sprites in battle (the rest of the properties should be self explanatory).

The assembler can rename your characters, but be aware that it will not change the point at which their names get cut off in the shop menu (such as when looking at who can equip an item). The renaming will also apply to the levelup screen, but their names will be written to 0x2F9B0 instead of 0x2D3AF (to be more forgiving with space for longer names). This assumes that you haven't added anything to the ROM at 0x2F9B0.

<sub>([back to top](#how-this-works))</sub>

### Items

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py itemdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py itemassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/items.items.py
```

Examples - NokNokShell, Muku Cookie, and Fire Bomb:
![alt text](image-8.png) ![alt text](image-9.png) ![alt text](image-10.png)

```python
class NokNokShellItem(Weapon):
    """NokNok Shell item class"""
    _item_name: str = "NokNok Shell"
    _prefix = ItemPrefix.SHELL

    _item_id: int = 7
    _description: str = " Kick to attack"
    _equip_chars: List[PartyCharacter] = [MARIO]
    _attack: int = 20
    _variance: int = 2
    _price: int = 20
    _hide_damage: bool = True
    _half_time_window_begins = UInt8(20)
    _perfect_window_begins = UInt8(25)
    _perfect_window_ends = UInt8(31)
    _half_time_window_ends = UInt8(36)


class MukuCookieItem(RegularItem):
    """Muku Cookie item class"""
    _item_name: str = "Muku Cookie"
    _prefix = ItemPrefix.DOT

    _item_id: int = 120
    _description: str = " Muku! Muku-\n muku! Muka?"
    _inflict: int = 69
    _price: int = 69
    _effect_type = EffectType.NULLIFICATION
    _hide_damage: bool = True
    _usable_battle: bool = True
    _overworld_menu_fill_fp: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
    _status_immunities: List[Status] = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR, Status.BERSERK, Status.MUSHROOM, Status.SCARECROW]


class FireBombItem(RegularItem):
    """Fire Bomb item class"""
    _item_name: str = "Fire Bomb"
    _prefix = ItemPrefix.BOMB

    _item_id: int = 113
    _description: str = " Hit all\n enemies w/fire"
    _inflict: int = 120
    _price: int = 200
    _inflict_element = Element.FIRE
    _hide_damage: bool = True
    _usable_battle: bool = True
    _target_enemies: bool = True
    _target_all: bool = True
    _one_side_only: bool = True
```

It is assumed (for now) that the item subclass ranges are as follows:
- 0-36: weapons
- 37-73: armor
- 74-95: accessory
- 96-255: regular items

Almost everything that can be disassembled will need access to your item classes, so it's important for this to be one of the first things you do.

The disassembler creates an `ItemCollection` (in the same file) that instantiates all of your Item classes (this is necessary to create a ROM patch). If you want to use these items in another Python project, you'll need to import the `ItemCollection`. To prepare the patch data, run `itemcollection.render()` to get a `dict[int, bytearray]` where each `int` is a ROM address to which the `bytearray` should be patched.

<sub>([back to top](#how-this-works))</sub>

### Sprites

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py graphicsdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py graphicsassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/sprites/sprites.py
```

NPC sprites use uncompressed tiles, an image pack, an animation pack, and a container that references all three of those things. These all exist in different parts of the ROM. The sprite disassembler combines all of these things into a single object (which is why you won't see animation or image pack IDs) so that the assembler can create and write that info to the rom in an optimized manner that prioritizes clearing up empty space for more tiles.

Palettes are not covered by the disassembler, you still need to use IDs for those.

Here is an example of a disassembled sprite:

```python
# SPR0524_EMPTY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xff\xf0\xff\xc0\xff\x80\xff\x80\xff\x00\xff\x00\xff\x00\xff\x00\x0f\xff?\xff\x7f\xff~\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xe0\xe0'),
                            bytearray(b'\xff\x0f\xff\x03\xff\x01\xff\x01\xff\x00\xff\x00\xff\x00\xff\x00\xf0\xff\xfc\xff\xfe\xff~\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x07\x07'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\xff\x80\xff\xc0\xff\xf0\xe0\xe0\xfe\xfe\xfe\xfe\xfe\xfe~\xfe\x7f\xff?\xff\x0f\xff'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\xff\x00\xff\x01\xff\x01\xff\x03\xff\x0f\x07\x07\x7f\x7f\x7f\x7f\x7f\x7f~\x7f\xfe\xff\xfc\xff\xf0\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=0,
    palette_offset=0,
    unknown_num=8
)
```

Disassembly will produce a `SpriteCollection`. If you want to import your sprites into another Python project, this is what you should import. `collection.render()` produces a `list[tuple[int, bytearray]]` where each tuple is a ROM address and the bytes to patch to that address.

<sub>([back to top](#how-this-works))</sub>

### Shops

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py shopdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py shopassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/shops/shops.py
```
which produces a `ShopCollection` of 33 shops. If you want to use your disassembled shops in another project, this is what your project should import. `ShopCollection.render()` produces a `dict[int, bytearray]` where each `int` is a ROM address where the corresponding `bytearray` is supposed to be patched.

Example shop:

```python
shops[SH06_FROG_COIN_EMPORIUM] = Shop(
    index=6,
    items=[
        SleepyBombItem,
        BracerItem,
        EnergizerItem,
        CrystallineItem,
        PowerBlastItem,
    ],
    buy_frog_coin=True,
)
```


<sub>([back to top](#how-this-works))</sub>

### Overworld dialogs

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py dialogdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py dialogassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/dialogs/dialogs.py
```
which produces a `DialogCollection`. If you want to use your disassembled dialogs in another project, this is what your project should import. `DialogCollection.render()` produces a `dict[int, bytearray]` where each `int` is a ROM address where the corresponding `bytearray` is supposed to be patched.

Dialogs in SMRPG are split into banks 0x22xxxx, 0x23xxxx, 0x24xxxx. You can disassemble dialog info into files that you can more or less edit as text.

Disassembled dialog data is split up into two parts. You'll see three files full of actual dialog data that look like this:
```python
dialog_data[300] = ''' Mario! How are we feeling?[await]
 [select]  (Like a new man!)
 [select]  (Need coffee. Keep away.)[await]'''
dialog_data[301] = ''' Well, that's good to hear.
 Thank you so much for spending
 time with Gaz.[await]
 He just loved it![await]'''
dialog_data[302] = ''' Yes, you look awful!
 Why don't you rest some more?[await]'''
```

The data files contain the actual dialog text. They're broken up into individual strings based on where text-terminating characters were in the original game. You can add or delete dialogs in these tables as you like (I think), as long as the whole file doesn't have too much text to fit into the ROM.

And then to make use of this raw text, you get one pointer file that looks like this (using the contextual names you gave for your dialogs):
```python
...
pointers[DI0776_ROSE_TOWN_NEXT_MORNING] = Dialog(bank=0x22, index=300, pos=0)
pointers[DI0777_ROSE_TOWN_NEXT_MORNING_CONFIRM] = Dialog(bank=0x22, index=301, pos=0)
pointers[DI0778_ROSE_TOWN_NEXT_MORNING_DECLINE] = Dialog(bank=0x22, index=302, pos=0)
...
```
Here, the `index` property corresponds to which raw text string in the data file you want. So in the above example, dialog 776 references raw text string 300 (in the 0x22 file, as indicated by the `bank` property), which is the "Mario! How are we feeling?" dialog. To use this in your romhack, you'd use dialog ID 793 in your event scripts to get a NPC to say that.
The `pos` property determines where the dialog should actually start. If you want the dialog to start reading partway through a raw text string, set `pos` to how many characters you want it to skip. 

Be aware that you might need to do some mental math if you're using a `pos` that isn't 0. Dialog use **compression**, some of which is built-in in the game and some of which I added to the codebase to explain what certain text bytes are supposed to do. `[await]` followed by a line break for example is actually just one byte, `0x02` (waits for a button press and then starts writing text on a new line), not eight bytes. You can find these definitions in src/smrpgpatchbuilder/datatypes/dialogs/utils.py. 

Your ROM also uses a customizable compression table which gets written to `disassembler_output/dialogs/contents/compression_table`, which shows you whole text strings that the game is going to treat a single byte every time it appears. The word "Booster" is shortened into a single byte, `0x18`, and whenever the game comes across this byte, it knows to spell it out as "Booster". You are free to change this table as you like if there are other character sequences your romhack uses more than the ones the game uses by default. You will also need to consider this when using a nonzero `pos`.

<sub>([back to top](#how-this-works))</sub>

### Battle dialogs and messages

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battledialogdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py battledialogassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/battle_dialogs/battle_dialogs.py
```

This is like overworld dialogs but less complicated.  Most of the compression table in src/smrpgpatchbuilder/datatypes/dialogs/utils.py is also used here for readability purposes. This handles dialogs classified both as battle dialogs AND battle messages (but not Psychopath messages, the monster classes handle those).

The disassembler creates a `BattleDialogCollection` (in the same file). If you want to use these dialogs in another Python project,this is what the project should import. `collection.render()` produces a `dict[int, bytearray]` where each `int` is a ROM address at which the `bytearray` should be patched.

<sub>([back to top](#how-this-works))</sub>

### Battle packs and formations

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/packs/pack_collection.py
```

There are 255 battle packs. When you disassemble them, you will see formations established inside the Pack class. When you assemble your packs, the assembler will identify which formations are identical, and warn you if you have more than 512 unique ones.

Here is what this pack looks like disassembled:
![alt text](image-11.png)
```python
packs[PACK098_SHAMAN_WITH_ORBISON_JAWFUL] = FormationPack(
    Formation(
        members=[
            FormationMember(SHAMAN, 151, 111),
            FormationMember(SHAMAN, 199, 151),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHAMAN, 135, 119),
            FormationMember(ORBISON, 199, 151),
            FormationMember(JAWFUL, 199, 119),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
    ,
    Formation(
        members=[
            FormationMember(SHAMAN, 167, 103),
            FormationMember(SHAMAN, 231, 135),
            FormationMember(JAWFUL, 167, 135),
        ],
        music=NormalBattleMusic(),
        unknown_bit=True,
    )
)
```

The assembler produces a `PackCollection`. If you want to use your packs in another Python project, this is what your project should import. When building a patch, the `collection.render()` method produces a `dict[int, bytearray]` where each int is the address at which to patch the bytearray.

<sub>([back to top](#how-this-works))</sub>

### Rooms and NPCs

The room disassembler handles loading events, loading music, event tiles, exit fields, NPCs and clones, partitions, and standalone NPCs (indicated by NPC IDs in the room data).

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py roomdisassembler --rom "path/to/your/smrpg/rom"  --large-partition-table
# The --large-partition-table argument can be included or omitted. 
# If included, it will try to read partitions from 0x1DEBE0 instead of 0x1DDE00. 
# You should only use this if you've already assembled your rooms before such that the partitions have moved here.
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py roomassembler -r path/to/your/smrpg/rom -t -b --large-partition-table
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
# The --large-partition-table argument can be included or omitted. 
# If included, it will write partitions from 0x1DEBE0 instead of 0x1DDE00. 
# 0x1DEBE0 is normally a big block of empty space. Assumes you haven't made any custom changes to your ROM that have put other data here. 
# 0x1DEBE0 is big enough to hold one partition per room.
```
Writes to:
```
./src/disassembler_output/rooms/npcs.py
./src/disassembler_output/rooms/rooms.py
```

If you want to use these in another project, you'll need to import the `RoomCollection` in rooms.py. Optionally, you can also import the NPCs in npcs.py. The `render` method of the `RoomCollection` will render everything on its own as a `dict[int, bytearray]` where each int is the address at which to patch the bytearray.

![alt text](image-16.png) ![alt text](image-17.png) ![alt text](image-18.png)

Example room:
```python
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0011_BOWSER_SCASTLE_1STTIME,
    entrance_event=E2498_EMPTY,
    events=[
        Event(
            event=E2497_ADDITIONAL_GATING_LOGIC_START_PLAYING,
            x=14,
            y=70,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=7,
            length=8,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False,
        ),
    ],
    exits=[
        RoomExit(
            x=17,
            y=67,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
            show_message=False,
            dst_x=4,
            dst_y=66,
            dst_z=5,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False,
        ),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.TERRAPIN_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E2304_BANK_1F_RETURN_EVENT_2,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=True,
            x=16,
            y=68,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
        ),
        RegularClone( # 1
            npc=npcs.TERRAPIN_NPC_2,
            event_script=E2304_BANK_1F_RETURN_EVENT_2,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=16,
            y=69,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 2
            npc=npcs.TERRAPIN_NPC_2,
            event_script=E2304_BANK_1F_RETURN_EVENT_2,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=True,
            x=17,
            y=71,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        RegularClone( # 3
            npc=npcs.TERRAPIN_NPC_2,
            event_script=E2304_BANK_1F_RETURN_EVENT_2,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=False,
            x=17,
            y=70,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
        ),
        BattlePackNPC( # 4
            npc=npcs.TERRAPIN_NPC_2,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_UNTIL_RELOAD,
            battle_pack=0,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=True,
            x=10,
            y=80,
            z=0,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3,
        ),
        BattlePackClone( # 5
            npc=npcs.TERRAPIN_NPC_2,
            battle_pack=0,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=True,
            x=14,
            y=80,
            z=0,
            z_half=False,
            direction=NORTHWEST,
        ),
        BattlePackClone( # 6
            npc=npcs.TERRAPIN_NPC_2,
            battle_pack=0,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=True,
            x=10,
            y=88,
            z=0,
            z_half=False,
            direction=NORTHWEST,
        ),
        BattlePackClone( # 7
            npc=npcs.TERRAPIN_NPC_2,
            battle_pack=0,
            action_script=A0400_SEQUENCE_LOOPING_ON,
            visible=True,
            x=6,
            y=88,
            z=0,
            z_half=False,
            direction=SOUTHEAST,
        ),
    ]
)
```

And here is TERRAPIN_NPC_2:
 ![alt text](image-19.png)
```python
TERRAPIN_NPC_2 = NPC(
    sprite_id=256,
    shadow_size=ShadowSize.OVAL_MED,
    acute_axis=4,
    obtuse_axis=4,
    height=11,
    y_shift=1,
    show_shadow=True,
    directions=VramStore.DIR0_SWSE_NWNE,
    min_vram_size=0,
    priority_0=False,
    priority_1=False,
    priority_2=True,
    cannot_clone=False,
    byte2_bit0=False,
    byte2_bit1=False,
    byte2_bit2=False,
    byte2_bit3=False,
    byte2_bit4=False,
    byte5_bit6=False,
    byte5_bit7=False,
    byte6_bit2=False,
)
```

Here are some things to be aware of:
- Partitions are disassembled as part of the room definition, not as a separate list you select an ID from. If you set `large_partition_table` in your RoomCollection, then every room can have its own partition, so you won't have to worry at all about picking partition IDs, you can just choose what will be the best for the room you're working on.
- I don't have it doing anything like automatically selecting a partition for a room because nobody fully understands how they work, but someday I'd like to figure out how to make that happen.
- NPCs work a little differently than in Lazy Shell. 
  - Within a room, your NPC has an ID, and the ID points to a "standalone" NPC object that specifies its sprite ID, shadow size, height/acute/obtuse collision sizes, how many directions they should be able to face and how much vram they should be allowed to use, etc.
  - In the disassembler, you'll see all these properties disassembled as part of your NPC list, but they can also be overridden at the room NPC level, which will _only_ change those properties in that room. 
  - When assembled, having these overrides creates a separate NPC for that room. This is designed such that you don't need to worry about NPC IDs, the assembler will take care of that (you can actually have over 1300, not just 512, so the assembler takes advantage of that extra space to give you freedom to make the objects in your room as detached as possible from other rooms).
  - Because you can have more than 511 NPCs, Lazy Shell will not load some of them correctly. (todo: add a pull request to LS that offers this flexibility)

<sub>([back to top](#how-this-works))</sub>

### Packet NPCs

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packetdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packetassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/packets/packets.py
```
Packet NPCs are the objects generated by "Create NPC at coords ..." commands, aka NPCs that are not loaded into memory when the level opens because they aren't in the room definition. You can modify these however you like.

```python
P000_FLASHING_POOF_FLOWER = Packet(
    packet_id=0,
    sprite_id=SPR0195_FLOWER,
    shadow=False,
    action_script_id=A0910_FLOWER_FLASH_THEN_POOF,
    unknown_bits=[False, False, False],
    unknown_bytes=bytearray([0x00, 0x00, 0x03, 0x03, 0x01, 0x00, 0x00]),
)
```

The disassembler produces a list of 255 packet definitions and a PacketCollection. If you want to use your packets in another Python project, your project should import the PacketCollection. The `collection.render()` method produces a `dict[int, bytearray]` where each int is the address at which to patch the bytearray.

<sub>([back to top](#how-this-works))</sub>

### Overworld location data

Disassemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py worldmaplocationdisassembler --rom "path/to/your/smrpg/rom" 
```
Assemble:
```bash
PYTHONPATH=src python src/smrpgpatchbuilder/manage.py worldmaplocationassembler -r path/to/your/smrpg/rom -t -b
# -r generates a ROM patch, -t generates a text file, -b generates a FlexHEX .bin
```
Writes to:
```
./src/disassembler_output/world_map_locations/world_map_locations.py
```
These are the level entry points on the overworld map.

![alt text](image-13.png)

```python
world_map_locations[OW10_MUSHROOM_KINGDOM] = WorldMapLocation(
    index=10,
    name="Mushroom Kingdom",
    x=144,
    y=108,
    show_check_flag=MAP_MUSHROOM_KINGDOM,
    go_location=False,
    run_event=E3843_WORLD_MAP_MUSHROOM_KINGDOM,
    enabled_to_east=True,
    check_flag_to_east=MAP_DIRECTIONAL_MUSHROOM_KINGDOM_KERO_SEWERS,
    location_to_east=OW12_KERO_SEWERS,
    enabled_to_south=True,
    check_flag_to_south=MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY,
    location_to_south=OW11_BANDITS_WAY,
    enabled_to_west=True,
    check_flag_to_west=MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY,
    location_to_west=OW11_BANDITS_WAY,
    enabled_to_north=True,
    check_flag_to_north=MAP_DIRECTIONAL_MUSHROOM_WAY_MUSHROOM_KINGDOM,
    location_to_north=OW09_MUSHROOM_WAY,
)
```

The disassembler produces a list of 56 world map locations and a WorldMapLocationCollection. If you want to use your packets in another Python project, your project should import the WorldMapLocationCollection. The `collection.render()` method produces a `dict[int, bytearray]` where each int is the address at which to patch the bytearray.

<sub>([back to top](#how-this-works))</sub>

## How to run tests

In your venv:
`PYTHONPATH=src pytest src/tests`