# E2808_MUSHROOM_WAY_BOSS_FIGHT

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
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_2808_ret_84"], identifier="EVENT_2808_jmp_if_bit_set_0"),
	FreezeAllNPCsUntilReturn(),
	ActionQueueSync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=27, y=94),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3168_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(MARIO),
	StartBattleAtBattlefield(PACK183_HAMMERBRO_FIGHT_STATIC, BF09_GRASSLANDS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2808_restore_all_hp_8"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2808_restore_all_hp_8"),
	RestoreAllFP(),
	SetBit(TOAD_IN_MUSHROOM_WAY_3),
	SetBit(MAP_DIRECTIONAL_MUSHROOM_WAY_MUSHROOM_KINGDOM),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_7),
	SummonObjectToCurrentLevel(NPC_8),
	FreezeAllNPCsUntilReturn(),
	RemoveObjectFromSpecificLevel(NPC_7, R205_MUSHROOM_WAY_AREA_03),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=24, y=79),
		A_SetWalkingSpeed(NORMAL)
	]),
	JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_2, ["EVENT_2808_action_queue_62"]),
	SetAsyncActionScript(NPC_5, A0401_SEQUENCE_LOOPING_OFF),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=27, y=92),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ShiftToXYCoords(x=28, y=94),
		A_FaceNorthwest()
	]),
	FadeInFromBlack(sync=False),
	Pause(16),
	RunDialog(dialog_id=DI3177_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(64, identifier="EVENT_2808_action_queue_27_SUBSCRIPT_jump_to_height_1"),
		A_Pause(1, identifier="EVENT_2808_action_queue_27_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_27_SUBSCRIPT_pause_2"]),
		A_JmpIfBitSet(TEMP_7044_0, ["EVENT_2808_run_dialog_28"]),
		A_Jmp(["EVENT_2808_action_queue_27_SUBSCRIPT_jump_to_height_1"])
	]),
	RunDialog(dialog_id=DI3178_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2808_run_dialog_28"),
	SetBit(TEMP_7044_0),
	StopEmbeddedActionScript(NPC_5),
	Pause(32),
	ActionQueueSync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_Pause(32),
		A_FaceEast()
	]),
	RunDialog(dialog_id=DI3179_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkNortheastPixels(48),
		A_FaceNorthwest(),
		A_WalkNorthwestPixels(8)
	]),
	UnsyncDialog(),
	RunDialog(dialog_id=DI3180_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_StartLoopNTimes(1),
		A_JumpToHeight(64),
		A_Pause(1, identifier="EVENT_2808_action_queue_37_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_37_SUBSCRIPT_pause_2"]),
		A_Pause(16),
		A_EndLoop(),
		A_WalkSouthwestPixels(16),
		A_WalkNorthwestPixels(16),
		A_FaceNortheast(),
		A_StartLoopNTimes(1),
		A_JumpToHeight(64),
		A_Pause(1, identifier="EVENT_2808_action_queue_37_SUBSCRIPT_pause_11"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_37_SUBSCRIPT_pause_11"]),
		A_Pause(16),
		A_EndLoop(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkNorthwestPixels(16),
		A_WalkNortheastPixels(16),
		A_FaceSoutheast(),
		A_StartLoopNTimes(1),
		A_JumpToHeight(64),
		A_Pause(1, identifier="EVENT_2808_action_queue_37_SUBSCRIPT_pause_21"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_37_SUBSCRIPT_pause_21"]),
		A_Pause(16),
		A_EndLoop(),
		A_Pause(24),
		A_FaceSouthwest()
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkSoutheastPixels(12),
		A_Pause(16),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_WalkEastPixels(12),
		A_WalkSouthPixels(11),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(29)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(8),
		A_WalkSouthwestPixels(26)
	]),
	RunDialog(dialog_id=DI3181_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	FreezeCamera(),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(176),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(128),
		A_VisibilityOff(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_TransferToXYZF(x=28, y=92, z=1, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(2)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(24),
		A_WalkNortheastPixels(24),
		A_FaceNorthwest(),
		A_Pause(32),
		A_SetSpriteSequence(index=26, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI3173_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	RemoveObjectFromCurrentLevel(NPC_8),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	AddToInventory(HammerItem),
	SetAsyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	RunDialog(dialog_id=DI3174_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI3182_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(32),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_JumpToHeight(108),
		A_Pause(32),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastSteps(4),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_5, R205_MUSHROOM_WAY_AREA_03),
	UnfreezeCamera(),
	UnfreezeAllNPCs(),
	Jmp(["EVENT_2808_ret_84"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_ShiftToXYCoords(x=27, y=93),
		A_FaceNortheast()
	], identifier="EVENT_2808_action_queue_62"),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	Pause(32),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(24),
		A_Pause(32),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_2808_action_queue_66_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_66_SUBSCRIPT_pause_6"]),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_2808_action_queue_66_SUBSCRIPT_pause_10"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_66_SUBSCRIPT_pause_10"]),
		A_Pause(32),
		A_WalkEastPixels(37),
		A_FaceNorthwest(),
		A_Pause(32)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_2808_action_queue_67_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_67_SUBSCRIPT_pause_2"]),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_2808_action_queue_67_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_2808_action_queue_67_SUBSCRIPT_pause_6"])
	]),
	RunDialog(dialog_id=DI3171_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(MARIO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3172_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestPixels(12),
		A_SetSpriteSequence(index=26, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Pause(32),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(8),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	RunDialog(dialog_id=DI3173_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	RemoveObjectFromCurrentLevel(NPC_8),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	AddToInventory(HammerItem),
	SetAsyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	RunDialog(dialog_id=DI3174_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	UnfreezeAllNPCs(),
	Return(identifier="EVENT_2808_ret_84")
])
