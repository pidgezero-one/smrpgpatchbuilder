# E2074_ENTER_MONSTRO_SEALED_ROOM

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
	EnterArea(room_id=R351_CULEXS_ROOM, face_direction=NORTH, x=29, y=45, z=0),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkEastPixels(12)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2074_set_action_script_9"]),
	SummonObjectToCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOn()
	]),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_3),
	SummonObjectToCurrentLevel(NPC_4),
	SetSyncActionScript(LAYER_1, A0575_MONSTRO_LAIR_TRANSPARENCY_LAYER, identifier="EVENT_2074_set_action_script_9"),
	FadeInFromBlack(sync=False, duration=70),
	Pause(60),
	JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2074_action_queue_14"]),
	JmpToEvent(E3012_CLONE_RESERVED),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30)
	], identifier="EVENT_2074_action_queue_14"),
	JmpIfBitSet(BELOME_HEAD_3, ["EVENT_2074_run_dialog_24"]),
	RunDialog(dialog_id=DI3056_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3057_MONSTRO_SUPERBOSS_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(BELOME_HEAD_3),
	JmpIfDialogOptionBSelected(["EVENT_2074_run_dialog_27"]),
	RunDialog(dialog_id=DI3061_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2074_run_dialog_20"),
	StartBattleAtBattlefield(PACK216_CULEX_BOSS_STATIC, BF47_CULEX),
	JmpIfBitClear(GAME_OVER, ["EVENT_2074_fade_in_from_black_async_37"]),
	ResetAndChooseGame(),
	RunDialog(dialog_id=DI3059_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2074_run_dialog_24"),
	JmpIfDialogOptionBSelected(["EVENT_2074_run_dialog_27"]),
	Jmp(["EVENT_2074_run_dialog_20"]),
	RunDialog(dialog_id=DI3058_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2074_run_dialog_27"),
	Jmp(["EVENT_2074_action_queue_29"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30)
	], identifier="EVENT_2074_action_queue_29"),
	JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2074_apply_solidity_mod_33"]),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4),
	Jmp(["EVENT_2048_remove_from_current_level_0"]),
	ApplySolidityModToLevel(permanent=False, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_2074_apply_solidity_mod_33"),
	ApplyTileModToLevel(use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=33),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4),
	Jmp(["EVENT_2048_remove_from_current_level_0"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2074_fade_in_from_black_async_37"),
	Pause(5),
	PlayMusicAtDefaultVolume(M0058_CONVERSATIONWITHCULEX),
	Pause(60),
	RunDialog(dialog_id=DI3060_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	SetVarToConst(ITEM_ID, QuartzCharmItem),
	SetVarToConst(PRIMARY_TEMP_7000, 3355),
	RunEventAsSubroutine(E3829_EMPTY),
	Pause(15),
	RunDialog(dialog_id=DI3354_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(MONSTRO_MIDDLE_DOOR_COMPLETED),
	RestoreAllHP(),
	RestoreAllFP(),
	Jmp(["EVENT_2074_action_queue_29"])
])
