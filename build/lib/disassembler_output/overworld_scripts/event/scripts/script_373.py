# E0373_MUSHROOM_KINGDOM_BOSS_FIGHT

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *

script = EventScript([
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_375_play_music_default_volume_0"]),
	Pause(1, identifier="EVENT_373_pause_1"),
	JmpIfMarioInAir(["EVENT_373_pause_1"]),
	Set7016701BToObjectXYZ(target=MARIO, bit_7=True),
	JmpIfVarNotEqualsConst(Z_COORD_2, 4, ["EVENT_256_ret_0"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_BounceToXYWithHeight(x=16, y=29, height=4),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True)
	], identifier="EVENT_373_action_queue_5"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=12, y=9)
	]),
	SetBit(TEMP_7043_5),
	Pause(30),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO086_BIG_BOUNCE, channel=6),
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\n\xe0\xff')),
		A_Walk1StepSouthwest(),
		A_BPL262728(),
		A_TransferToXYZF(x=18, y=26, z=20, direction=EAST),
		A_Pause(120),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkSouthwestPixels(3),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(13)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(150),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True)
	]),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(180),
	SetBit(TEMP_7043_5),
	PauseActionScript(NPC_13),
	SetSyncActionScript(NPC_13, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_4, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_5, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_6, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_7, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	JmpIfBitClear(UNUSED_7082_4, ["EVENT_373_action_queue_32"]),
	SetSyncActionScript(NPC_8, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	SetSyncActionScript(NPC_9, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
	Jmp(["EVENT_373_play_sound_34"]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_FloatingOn(),
		A_WalkNorthwestPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(8),
		A_FixedFCoordOff()
	], identifier="EVENT_373_action_queue_32"),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_FloatingOn(),
		A_WalkSoutheastPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(8),
		A_FixedFCoordOff()
	]),
	PlaySound(sound=SO021_RUMBLING, channel=6, identifier="EVENT_373_play_sound_34"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_Walk1StepNorth(),
		A_WalkSouthPixels(12),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(6),
		A_WalkNorthPixels(4),
		A_StopSound(),
		A_WalkSouthPixels(3),
		A_WalkNorthPixels(1)
	]),
	Pause(60),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_13, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	SetAsyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
	PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
	RunDialog(dialog_id=DI0625_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(40),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(40),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	ClearBit(TEMP_7043_5),
	RunEventAsSubroutine(E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(80),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(80),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(80),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(80),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(80),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(80),
		A_FaceNorthwest()
	]),
	UnsyncDialog(),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_JumpToHeight(height=72, silent=True),
		A_Walk1StepSoutheast()
	]),
	SetVarToConst(TEMP_70A9, 24),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI0626_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceSoutheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(4)
	]),
	SetVarToConst(TEMP_70A9, 25),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI0627_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceNorthwest(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(4)
	]),
	SetVarToConst(TEMP_70A9, 26),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI0628_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_JumpToHeight(height=72, silent=True),
		A_Walk1StepNorthwest()
	]),
	SetVarToConst(TEMP_70A9, 26),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI0629_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNortheast(),
		A_Pause(10),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
	ReturnFD(),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_SetPriority(3),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(20),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_Pause(20),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%@\x08\x84\xff')),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_BPL262728()
	]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	RememberLastObject(),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	FadeOutMusicToVolume(duration=0, volume=1),
	StartBattleAtBattlefield(PACK179_MACK_FIGHT_STATIC, BF15_MUSHROOM_KINGDOM_CASTLE),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	ReturnFD(),
	SetBit(MUSHROOM_KINGDOM_LIBERATED),
	RestoreAllHP(),
	RestoreAllFP(),
	PlayMusicAtCurrentVolume(M0023_GOTASTARPIECE_PART1),
	Pause(1),
	StopMusicFDA2(),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6])
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	FadeInFromBlack(sync=False),
	Pause(30),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(4)
	]),
	Store02To0248(),
	UnknownCommand(bytearray(b'\xfd\x8e\x99\x07\x0f')),
	Pause(60),
	Store00To0248(),
	PauseActionScript(NPC_1),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShadowOn(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(1),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(16),
		A_VisibilityOff()
	]),
	Pause(30),
	RememberLastObject(),
	Pause(90),
	StartAsyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Pause(69),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	Pause(51),
	SetSyncActionScript(NPC_0, A0634_EMPTY),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(12),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(20),
		A_SetWalkingSpeed(FAST),
		A_WalkWestPixels(16),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepWest(),
		A_WalkWestPixels(8)
	]),
	UnsyncActionScript(NPC_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_BPL262728(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(16)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	SetSyncActionScript(NPC_1, A0120_EMBEDDED_ROUTINE),
	Pause(120),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(2),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(10),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(6),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(1),
		A_Pause(100),
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_SetSequenceSpeed(FASTEST),
		A_Pause(90)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=16, y=29, z=13, direction=EAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(6),
		A_VisibilityOff()
	]),
	Pause(232),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	RememberLastObject(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthSteps(2)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownSteps(4),
		A_ShiftZDownPixels(10),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(14),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	Pause(240),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpSteps(2)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=16, y=29, z=9, direction=EAST),
		A_Pause(42),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(3),
		A_ShiftZUpPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(6),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(34),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpSteps(6),
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step()
	]),
	RememberLastObject(),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\n\x06')),
	SetBit(STAR_PIECE_MENU_UNLOCKED),
	SetSyncActionScript(NPC_1, A0120_EMBEDDED_ROUTINE),
	Pause(60),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(8)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(8)
	]),
	RememberLastObject(),
	RunStarPieceSequence(1),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth()
	]),
	UnknownCommand(bytearray(b'\xfd\x8er\x00\x06')),
	FadeOutMusicToVolume(duration=0, volume=1),
	PlayMusicAtCurrentVolume(M0002_MUSHROOMKINGDOM),
	Pause(1),
	StopMusicFDA2(),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	FadeInFromBlack(sync=False),
	Pause(30),
	SetSyncActionScript(NPC_8, A0135_HENCHMAN_IMPRESSING_JUMP_LADY),
	Pause(30),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_BounceToXYWithHeight(x=11, y=15, height=0)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceWest()
	]),
	RunDialog(dialog_id=DI0708_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_9, A0135_HENCHMAN_IMPRESSING_JUMP_LADY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI0708_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_8, A0135_HENCHMAN_IMPRESSING_JUMP_LADY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceWest()
	]),
	RunDialog(dialog_id=DI0709_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_9, A0135_HENCHMAN_IMPRESSING_JUMP_LADY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI0710_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_8, A0135_HENCHMAN_IMPRESSING_JUMP_LADY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceWest()
	]),
	RunDialog(dialog_id=DI0711_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_9, A0135_HENCHMAN_IMPRESSING_JUMP_LADY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI0712_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_UnknownCommand(bytearray(b' \x04')),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_UnknownCommand(bytearray(b'%\x00\x08\x00\xff')),
		A_WalkSouthwestSteps(2),
		A_FaceSoutheast(),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_UnknownCommand(bytearray(b'%\x00\x08\x00\xff')),
		A_WalkSoutheastSteps(2),
		A_FaceSouthwest(),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
		A_UnknownCommand(bytearray(b'%\x00\x08\x00\xff')),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(12),
		A_BPL262728(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\x00\xff')),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest(),
		A_UnknownCommand(bytearray(b'%\x00\x08\x00\xff')),
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest(),
		A_UnknownCommand(bytearray(b'%\x00\x08\x00\xff')),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(12),
		A_BPL262728(),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_8, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM),
	RemoveObjectFromSpecificLevel(NPC_9, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM),
	Pause(30),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
