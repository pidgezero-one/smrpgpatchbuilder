# E2627_FACTORY_3RD_BOSS_FIGHT

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
	JmpIfObjectNotInSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["EVENT_2627_ret_47"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=7, y=88)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_2627_action_queue_2_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_2627_action_queue_2_SUBSCRIPT_pause_0"]),
		A_WalkToXYCoords(x=11, y=113),
		A_FaceNorthwest()
	]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_11),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNorth(),
		A_WalkNorthwestSteps(2),
		A_SetSequenceSpeed(NORMAL)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3270_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=1, looping=False, mirror_sprite=True)
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3271_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3272_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_WalkSoutheastPixels(10),
		A_WalkSouthwestPixels(12),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=11, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3273_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(7)
	]),
	Pause(32),
	StartBattleAtBattlefield(PACK148_DIRECTOR_STATIC, BF48_FACTORY_GROUNDS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2627_restore_all_hp_31"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2627_restore_all_hp_31"),
	RestoreAllFP(),
	StopEmbeddedActionScript(NPC_10),
	RemoveObjectFromSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03),
	RemoveObjectFromCurrentLevel(NPC_10),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(32),
		A_ResetProperties(),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
		A_Pause(48),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_WalkNorthwestSteps(3),
		A_Pause(24),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3274_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	SetVarToConst(TEMP_70AE, 31),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(16),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_ResetProperties(),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkToXYCoords(x=11, y=113),
		A_VisibilityOff()
	]),
	Return(identifier="EVENT_2627_ret_47")
])
