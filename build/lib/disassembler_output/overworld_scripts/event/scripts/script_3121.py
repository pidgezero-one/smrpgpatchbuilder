# E3121_SEWER_BOSS_FIGHT

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
	SummonObjectToCurrentLevelAtMariosCoords(NPC_2),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SequenceLoopingOff(),
		A_VisibilityOn(),
		A_ResetProperties(),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(1),
		A_FixedFCoordOn(),
		A_WalkToXYCoords(x=7, y=38),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_Pause(32),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(2),
		A_FaceNorthwest(),
		A_Pause(16),
		A_WalkNorthSteps(2),
		A_FaceSouthwest(),
		A_Pause(32),
		A_WalkWestSteps(2),
		A_FaceSoutheast(),
		A_Pause(24),
		A_WalkSouthSteps(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_SetWalkingSpeed(NORMAL),
		A_SetBit(TEMP_7043_2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOn(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=6, y=37),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeOutMusicToVolume(duration=16, volume=0),
	RunDialog(dialog_id=DI1588_EMPTY, above_object=NPC_2, closable=False, sync=False, multiline=True, use_background=True),
	Pause(1, identifier="EVENT_3121_pause_5"),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_3121_pause_5"]),
	CloseDialog(),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SequenceLoopingOn()
	]),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_Pause(32),
		A_JumpToHeight(108),
		A_Pause(32)
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_Pause(32),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(108),
		A_Pause(32),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI1589_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK168_BELOME1_FIGHT_STATIC, BF21_KERO_SEWERS),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	EnterArea(room_id=R303_KERO_SEWERS_AREA_08_BELOMES_ROOM_AFTER_DEFEAT, face_direction=NORTHEAST, x=6, y=37, z=1),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=7, y=38, z=2, direction=EAST),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(1)
	]),
	FadeInFromBlack(sync=False),
	SetBit(SEWER_BOSS_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(120),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	SetSyncActionScript(NPC_3, A0056_SEWER_WATER_DRAIN),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(64),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_PlaySound(sound=SO017_OPEN_FRONT_GATE, channel=6),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(1),
		A_Pause(2),
		A_WalkSouthPixels(2),
		A_Pause(2),
		A_WalkSouthPixels(4),
		A_Pause(1),
		A_WalkSouthPixels(9),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(4),
		A_Pause(1, identifier="EVENT_3121_action_queue_27_SUBSCRIPT_pause_11"),
		A_JmpIfBitClear(TEMP_7043_1, ["EVENT_3121_action_queue_27_SUBSCRIPT_pause_11"]),
		A_WalkNorthPixels(1, identifier="EVENT_3121_action_queue_27_SUBSCRIPT_shift_north_pixels_13"),
		A_Pause(2),
		A_JmpIfBitClear(TEMP_7043_2, ["EVENT_3121_action_queue_27_SUBSCRIPT_shift_north_pixels_13"]),
		A_WalkSouthSteps(2),
		A_SetBit(TEMP_7043_3)
	]),
	RunDialog(dialog_id=DI1592_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_6),
	PlaySound(sound=SO007_GUSHING_WATER, channel=4),
	RunDialog(dialog_id=DI1593_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_5),
	PauseActionScript(NPC_2),
	Pause(48),
	RunDialog(dialog_id=DI1594_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	FreezeCamera(),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_JumpToHeight(108),
		A_Pause(48),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(2),
		A_WalkSoutheastSteps(2),
		A_WalkNorthwestSteps(2),
		A_WalkSoutheastSteps(2),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_JumpToHeight(108),
		A_WalkNortheastSteps(2),
		A_JumpToHeight(108),
		A_WalkNortheastSteps(2),
		A_JumpToHeight(108),
		A_WalkNortheastSteps(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(108, identifier="EVENT_3121_start_embedded_action_script_37_SUBSCRIPT_jump_to_height_18"),
		A_Pause(16),
		A_JmpIfBitClear(TEMP_7043_3, ["EVENT_3121_start_embedded_action_script_37_SUBSCRIPT_jump_to_height_18"]),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_Pause(1),
		A_SetAllSpeeds(NORMAL)
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_JumpToHeight(108),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48),
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(16),
		A_ResetProperties(),
		A_WalkNortheastSteps(2),
		A_JumpToHeight(72),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_Walk1StepNortheast(),
		A_SetBit(TEMP_7043_1),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ShiftZDownPixels(8),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(120),
		A_SetBit(TEMP_7043_2),
		A_ResetProperties(),
		A_JumpToHeight(108),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True),
		A_SetAllSpeeds(NORMAL)
	]),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(1, identifier="EVENT_3121_start_embedded_action_script_39_SUBSCRIPT_pause_1"),
		A_JmpIfBitClear(TEMP_7043_1, ["EVENT_3121_start_embedded_action_script_39_SUBSCRIPT_pause_1"]),
		A_PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(1, identifier="EVENT_3121_start_embedded_action_script_39_SUBSCRIPT_pause_5"),
		A_JmpIfBitClear(TEMP_7043_2, ["EVENT_3121_start_embedded_action_script_39_SUBSCRIPT_pause_5"]),
		A_PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(1)
	]),
	Pause(1, identifier="EVENT_3121_pause_40"),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3121_pause_40"]),
	CloseDialog(),
	PlaySound(sound=SO007_GUSHING_WATER, channel=6),
	StartSyncEmbeddedActionScript(target=LAYER_3, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(5),
		A_SetBit(TEMP_7043_4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(4),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(10)
	]),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_Pause(8),
		A_SetSequenceSpeed(VERY_FAST),
		A_ResetProperties(),
		A_FaceSouth(),
		A_SequenceLoopingOn(),
		A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
		A_Pause(1, identifier="EVENT_3121_start_embedded_action_script_45_SUBSCRIPT_pause_6"),
		A_JmpIfBitClear(TEMP_7043_4, ["EVENT_3121_start_embedded_action_script_45_SUBSCRIPT_pause_6"]),
		A_Pause(4),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_SetBit(TEMP_7043_5),
		A_WalkSouthwestSteps(3),
		A_SetBit(TEMP_7043_7),
		A_WalkSouthwestSteps(5),
		A_SetBit(TEMP_7043_6),
		A_Walk1StepSouthwest(),
		A_SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
		A_SetWalkingSpeed(NORMAL),
		A_SequenceLoopingOff(),
		A_ResetProperties()
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_Pause(1, identifier="EVENT_3121_start_embedded_action_script_46_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_5, ["EVENT_3121_start_embedded_action_script_46_SUBSCRIPT_pause_0"]),
		A_Pause(9),
		A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	]),
	StartSyncEmbeddedActionScript(target=SCREEN_FOCUS, prefix=0xF1, subscript=[
		A_Pause(1, identifier="EVENT_3121_start_embedded_action_script_47_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_5, ["EVENT_3121_start_embedded_action_script_47_SUBSCRIPT_pause_0"]),
		A_WalkSouthwestSteps(3)
	]),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_Pause(1, identifier="EVENT_3121_start_embedded_action_script_48_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_6, ["EVENT_3121_start_embedded_action_script_48_SUBSCRIPT_pause_0"]),
		A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_SequencePlaybackOff(),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_SequencePlaybackOn()
	]),
	Pause(1, identifier="EVENT_3121_pause_49"),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_3121_pause_49"]),
	FadeOutSoundToVolume(duration=2, volume=0),
	FadeOutToBlack(sync=False, duration=16),
	UnfreezeCamera(),
	RemoveObjectFromCurrentLevel(MARIO),
	SetBit(UNKNOWN_MIDAS_RIVER_704D_6),
	ClearBit(BUCKET_WARP_BIT),
	EnterArea(room_id=R069_MIDAS_RIVER_WATERFALL, face_direction=SOUTH, x=9, y=108, z=0, run_entrance_event=True),
	Return()
])
