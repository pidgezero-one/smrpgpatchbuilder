# E3338_VOLCANO_TRAMPOLINE_TO_2ND_BOSS

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
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_3338_open_location_181"]),
	EnterArea(room_id=R013_BARREL_VOLCANO_FALLING_INTO_VOLCANO, face_direction=SOUTH, x=4, y=48, z=0),
	StopMusicFDA2(),
	RemoveObjectFromCurrentLevel(MARIO),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=4, y=54),
		A_VisibilityOff()
	]),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TEMP_7028, 0),
	SetVarToConst(TEMP_702A, 0),
	SetVarToConst(TEMP_702C, 0),
	SetVarToConst(X_COORD_1, 4),
	SetVarToConst(Y_COORD_1, 44),
	SetVarToConst(Z_COORD_1, 0),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	SetVarToConst(TEMP_70AF, 0),
	CreatePacketAt7010(packet=P046_UNUSED, destinations=["EVENT_3338_pause_17"]),
	Pause(1, identifier="EVENT_3338_pause_17"),
	CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7034),
	Inc(TEMP_70AF),
	CreatePacketAt7010(packet=P046_UNUSED, destinations=["EVENT_3338_pause_22"]),
	Pause(1, identifier="EVENT_3338_pause_22"),
	CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_7036),
	Inc(TEMP_70AF),
	CreatePacketAt7010(packet=P046_UNUSED, destinations=["EVENT_3338_pause_27"]),
	Pause(1, identifier="EVENT_3338_pause_27"),
	CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_7038),
	Inc(TEMP_70AF),
	CreatePacketAt7010(packet=P046_UNUSED, destinations=["EVENT_3338_pause_32"]),
	Pause(1, identifier="EVENT_3338_pause_32"),
	CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	Inc(TEMP_70AF),
	CreatePacketAt7010(packet=P046_UNUSED, destinations=["EVENT_3338_pause_37"]),
	Pause(1, identifier="EVENT_3338_pause_37"),
	CopyVarToVar(from_var=TEMP_70A9, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703C),
	FadeInFromBlack(sync=False),
	Pause(120),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShadowOn(),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(VERY_SLOW),
		A_FloatingOn(),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(height=140, silent=True),
		A_Pause(3),
		A_VisibilityOn(),
		A_Pause(3),
		A_WalkSouthwestPixels(5),
		A_Pause(1),
		A_BPL262728(),
		A_FloatingOff(),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_Pause(2)
	]),
	Pause(50),
	SetVarToConst(TEMP_7028, 1),
	Pause(2),
	CopyVarToVar(from_var=ROSE_WAY_7038, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_StartLoopNTimes(1),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(3),
		A_Pause(2),
		A_WalkSouthPixels(3),
		A_Pause(4),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI1824_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	CopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(4),
		A_Pause(2),
		A_WalkSouthPixels(4)
	]),
	RunDialog(dialog_id=DI1825_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(TEMP_7026, 1),
	Pause(2),
	CopyVarToVar(from_var=UNKNOWN_7036, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_StartLoopNTimes(1),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(3),
		A_Pause(2),
		A_WalkSouthPixels(3),
		A_Pause(4),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI1826_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	CopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(4),
		A_Pause(2),
		A_WalkSouthPixels(4)
	]),
	RunDialog(dialog_id=DI1827_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(TEMP_702A, 1),
	Pause(2),
	CopyVarToVar(from_var=ROSE_WAY_703A, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_StartLoopNTimes(1),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(3),
		A_Pause(2),
		A_WalkSouthPixels(3),
		A_Pause(4),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI1828_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	CopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(4),
		A_Pause(2),
		A_WalkSouthPixels(4)
	]),
	RunDialog(dialog_id=DI1829_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(TEMP_702C, 1),
	Pause(2),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_StartLoopNTimes(1),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(3),
		A_Pause(2),
		A_WalkSouthPixels(3),
		A_Pause(4),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI1830_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	CopyVarToVar(from_var=TEMP_7034, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_WalkNorthPixels(4),
		A_Pause(2),
		A_WalkSouthPixels(4)
	]),
	RunDialog(dialog_id=DI1831_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TEMP_7028, 0),
	SetVarToConst(TEMP_702A, 0),
	SetVarToConst(TEMP_702C, 0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9c[')),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(6)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_StartLoopNTimes(95),
		A_WalkSouthPixels(1),
		A_WalkNorthPixels(1),
		A_EndLoop()
	]),
	SetSyncActionScript(LAYER_2, A0942_HINOPIO_IN_DOORWAY),
	SetSyncActionScript(NPC_1, A0942_HINOPIO_IN_DOORWAY),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	SetVarToConst(TEMP_7026, 1),
	SetVarToConst(TEMP_7028, 1),
	SetVarToConst(TEMP_702A, 1),
	SetVarToConst(TEMP_702C, 1),
	Pause(2),
	RunDialog(dialog_id=DI1832_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(TEMP_70AB, 21),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_StartLoopNTimes(23),
		A_WalkSouthPixels(1),
		A_Pause(1),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_StartLoopNTimes(23),
		A_WalkNorthPixels(1),
		A_Pause(1),
		A_EndLoop()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(47),
		A_WalkSouthPixels(1),
		A_WalkNorthPixels(1),
		A_EndLoop()
	]),
	SetVarToConst(SECONDARY_TEMP_7024, 2),
	Pause(2),
	SetVarToConst(TEMP_7026, 2),
	Pause(4),
	SetVarToConst(TEMP_7028, 2),
	Pause(1),
	SetVarToConst(TEMP_702A, 2),
	Pause(3),
	SetVarToConst(TEMP_702C, 2),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(120),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x03\xe8\xff')),
		A_Pause(30),
		A_BPL262728(),
		A_Pause(8)
	]),
	StartBattleAtBattlefield(PACK182_AXEM_FIGHT_STATIC, BF39_BLADE_AXEM_RANGERS),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	StopMusicFDA2(),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TEMP_7028, 0),
	SetVarToConst(TEMP_702A, 0),
	SetVarToConst(TEMP_702C, 0),
	JmpIfBitSet(GAME_OVER, ["EVENT_3338_reset_and_choose_game_183"]),
	SetBit(VOLCANO_LIBERATED),
	RestoreAllHP(),
	RestoreAllFP(),
	PlaySound(sound=SO091_TUMBLING_BOULDERS, channel=4),
	StopMusicFDA2(),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouth(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthPixels(8),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthPixels(1, identifier="EVENT_3338_action_queue_131_SUBSCRIPT_shift_south_pixels_1"),
		A_WalkNorthPixels(1),
		A_JmpIfBitClear(TEMP_7044_0, ["EVENT_3338_action_queue_131_SUBSCRIPT_shift_south_pixels_1"])
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthSteps(8),
		A_SetBit(TEMP_7044_0)
	]),
	SetVarToRandom(X_COORD_1, 8, identifier="EVENT_3338_set_var_to_random_133"),
	SetVarToRandom(Y_COORD_1, 24),
	AddConstToVar(Y_COORD_1, 32),
	SetVarToConst(Z_COORD_1, 0),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	ScreenFlashesWithColour(WHITE, identifier="EVENT_3338_screen_flashes_with_colour_138"),
	Pause(4),
	CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["EVENT_3338_screen_flashes_with_colour_138"]),
	Pause(4),
	JmpIfRandom1of2(["EVENT_3338_set_var_to_random_133"]),
	SetVarToRandom(X_COORD_1, 8),
	SetVarToRandom(Y_COORD_1, 24),
	AddConstToVar(Y_COORD_1, 32),
	SetVarToConst(Z_COORD_1, 0),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	CreatePacketAt7010(packet=P025_UNUSED, destinations=["EVENT_3338_screen_flashes_with_colour_138"]),
	Pause(4),
	JmpIfRandom1of2(["EVENT_3338_set_var_to_random_133"]),
	ScreenFlashesWithColour(WHITE),
	Pause(4),
	JmpIfBitClear(TEMP_7044_0, ["EVENT_3338_set_var_to_random_133"]),
	FadeOutSoundToVolume(duration=4, volume=0),
	Pause(120),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	Pause(20),
	SetVarToConst(X_COORD_1, 4),
	SetVarToConst(Y_COORD_1, 34),
	SetVarToConst(Z_COORD_1, 0),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	Pause(1, identifier="EVENT_3338_pause_162"),
	CreatePacketAt7010(packet=P048_UNUSED, destinations=["EVENT_3338_pause_162"]),
	Pause(1, identifier="EVENT_3338_pause_164"),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3338_pause_164"]),
	Pause(48),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	Pause(60),
	Pause(1, identifier="EVENT_3338_pause_169"),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_3338_pause_169"]),
	Pause(1),
	RunStarPieceSequence(6),
	Pause(1),
	EnterArea(room_id=R391_VOLCANO_POSTCD_AREA_04, face_direction=SOUTH, x=4, y=16, z=0),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI1839_DUPLICATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(6),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(30),
		A_PlaySound(sound=SO013_COIN, channel=6),
		A_Pause(30)
	]),
	Pause(2),
	ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True),
	Return(),
	ExitToWorldMap(area=OW50_BARREL_VOLCANO, bit_6=True, bit_7=True, identifier="EVENT_3338_open_location_181"),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3338_reset_and_choose_game_183")
])
