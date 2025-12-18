# E3355_KEEP_BARREL_COUNT_LOADER_CONTD

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
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	SetVarToRandom(PRIMARY_TEMP_7000, 256),
	RunDialog(dialog_id=DI1888_BARREL_COUNT_1_START, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToRandom(PRIMARY_TEMP_7000, 256),
	RunDialog(dialog_id=DI1889_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\x02\x07')),
	Pause(8),
	SetVarToConst(SECONDARY_TEMP_7024, 12),
	SetVarToConst(TEMP_7026, 22),
	SetVarToConst(TEMP_7028, 4),
	JmpToSubroutine(["EVENT_3355_copy_var_to_var_84"]),
	RunDialog(dialog_id=DI1890_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8e2\x02\x07')),
	SetVarToConst(PRIMARY_TEMP_7000, 9),
	JmpToSubroutine(["EVENT_3355_play_music_default_volume_93"]),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\x02\x07')),
	JmpToSubroutine(["EVENT_3355_clear_bit_111"]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3355_play_sound_28"]),
	JmpIfVarEqualsConst(ROSE_WAY_703E, 2, ["EVENT_3355_jmp_if_dialog_option_b_or_c_24"]),
	JmpIfVarEqualsConst(ROSE_WAY_703E, 3, ["EVENT_3355_jmp_if_dialog_option_b_or_c_26"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3355_play_sound_28', 'EVENT_3355_play_sound_28']),
	Jmp(["EVENT_3355_pause_38"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3355_pause_38', 'EVENT_3355_play_sound_28'], identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_24"),
	Jmp(["EVENT_3355_play_sound_28"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3355_play_sound_28', 'EVENT_3355_pause_38'], identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_26"),
	Jmp(["EVENT_3355_play_sound_28"]),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_3355_play_sound_28"),
	SlowDownMusic(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=DI1887_QUIZ_FAILED, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	Pause(240),
	FadeOutToBlack(sync=False),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
	Pause(4, identifier="EVENT_3355_pause_38"),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=DI1895_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\x02\x07')),
	SetBit(TEMP_7044_7),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(40),
		A_WalkNortheastPixels(4),
		A_Walk1StepNortheast(),
		A_Pause(20),
		A_FloatingOff(),
		A_ShiftZUpSteps(8),
		A_WalkToXYCoords(x=11, y=42)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(40),
		A_JumpToHeight(56),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_VisibilityOff(),
		A_Pause(120),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=13, y=39, z=16, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_StartLoopNTimes(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff(),
		A_Pause(4),
		A_EndLoop(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(2)
	]),
	Pause(8),
	SetVarToConst(SECONDARY_TEMP_7024, 43),
	SetVarToConst(TEMP_7026, 26),
	SetVarToConst(TEMP_7028, 4),
	JmpToSubroutine(["EVENT_3355_copy_var_to_var_84"]),
	RunDialog(dialog_id=DI1896_BARREL_COUNT_2_START, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8e2\x02\x07')),
	SetVarToConst(PRIMARY_TEMP_7000, 19),
	JmpToSubroutine(["EVENT_3355_play_music_default_volume_93"]),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\x02\x07')),
	JmpToSubroutine(["EVENT_3355_clear_bit_111"]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3355_play_sound_28"]),
	JmpIfVarEqualsConst(ROSE_WAY_703E, 2, ["EVENT_3355_jmp_if_dialog_option_b_or_c_65"]),
	JmpIfVarEqualsConst(ROSE_WAY_703E, 3, ["EVENT_3355_jmp_if_dialog_option_b_or_c_67"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3355_play_sound_28', 'EVENT_3355_play_sound_28']),
	Jmp(["EVENT_3355_pause_69"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3355_pause_69', 'EVENT_3355_play_sound_28'], identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_65"),
	Jmp(["EVENT_3355_play_sound_28"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3355_play_sound_28', 'EVENT_3355_pause_69'], identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_67"),
	Jmp(["EVENT_3355_play_sound_28"]),
	Pause(4, identifier="EVENT_3355_pause_69"),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	Pause(8),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	PlayMusicAtDefaultVolume(M0009_VICTORY),
	RunDialog(dialog_id=DI1897_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(7),
		A_Walk1StepSoutheast()
	]),
	PlaySound(sound=SO016_OPEN_DOOR, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING, mod_id=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(48),
		A_Walk1StepNortheast()
	]),
	EnterArea(room_id=R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM, face_direction=NORTHEAST, x=12, y=97, z=0, run_entrance_event=True),
	Return(),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3355_copy_var_to_var_84"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	SetObjectMemoryToVar(TEMP_7028),
	JmpIfRandom1of2(["EVENT_3355_end_loop_91"]),
	SetSyncActionScript(MEM_70A9, A0279_KEEP_BARREL_COUNTING_OPTIONAL_BARREL),
	Inc(SECONDARY_TEMP_7024),
	Inc(TEMP_70A9),
	EndLoop(identifier="EVENT_3355_end_loop_91"),
	Return(),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION, identifier="EVENT_3355_play_music_default_volume_93"),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	Pause(30),
	SetObjectMemoryToVar(PRIMARY_TEMP_7000),
	Pause(30),
	PlaySound(sound=SO144_CLICK, channel=4),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=DI1891_X_SECONDS_LEFT, above_object=NPC_14, closable=False, sync=True, multiline=False, use_background=False),
	Pause(30),
	SetBit(TEMP_7044_7),
	Dec(PRIMARY_TEMP_7000),
	EndLoop(),
	Pause(30),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=4),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(1)
	]),
	PlayMusicAtDefaultVolume(M0066_BOWSER_SCASTLE_2NDTIME),
	Return(),
	ClearBit(TEMP_7044_7, identifier="EVENT_3355_clear_bit_111"),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=DI1892_PROMPT_FOR_BARREL_ANSWER, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	SetBit(TEMP_7044_7),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	SetVarToConst(ROSE_WAY_703E, 0),
	JmpIfRandom2of3(['EVENT_3355_inc_121', 'EVENT_3355_inc_123']),
	Inc(ROSE_WAY_703E),
	Dec(PRIMARY_TEMP_7000),
	Inc(ROSE_WAY_703E, identifier="EVENT_3355_inc_121"),
	Dec(PRIMARY_TEMP_7000),
	Inc(ROSE_WAY_703E, identifier="EVENT_3355_inc_123"),
	RunDialog(dialog_id=DI1893_DUPLICATE, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Inc(PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1893_DUPLICATE, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Inc(PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1893_DUPLICATE, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI1894_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ClearBit(TEMP_7044_6),
	SetVarToConst(TEMP_7028, 30),
	StartLoopNFrames(299),
	Pause(1),
	SetVarToRandom(PRIMARY_TEMP_7000, 256),
	Inc(TEMP_7028),
	JmpIfVarNotEqualsConst(TEMP_7028, 60, ["EVENT_3355_if_0210_bits_012_clear_do_not_jump_139"]),
	PlaySound(sound=SO144_CLICK, channel=4),
	SetVarToConst(TEMP_7028, 0),
	If0210Bits012ClearDoNotJump(["EVENT_3355_end_loop_141"], identifier="EVENT_3355_if_0210_bits_012_clear_do_not_jump_139"),
	Jmp(["EVENT_3355_close_dialog_143"]),
	EndLoop(identifier="EVENT_3355_end_loop_141"),
	SetBit(TEMP_7044_6),
	CloseDialog(identifier="EVENT_3355_close_dialog_143"),
	UnknownCommand(bytearray(b'\xfd\x8e2\x02\x07')),
	Return()
])
