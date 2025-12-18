# E2603_FACTORY_4TH_BOSS_FIGHT

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
	JmpIfBitSet(INNER_FACTORY_ROOM_4_COMPLETED, ["EVENT_2603_ret_70"]),
	SetBit(INNER_FACTORY_ROOM_4_COMPLETED),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=5, y=75)
	]),
	Pause(16),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(16),
		A_FaceSoutheast(),
		A_Pause(16),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(2)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3231_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3232_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(10),
		A_WalkNorthwestSteps(2),
		A_FaceSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3233_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartBattleAtBattlefield(PACK149_GUNYOLK_STATIC, BF48_FACTORY_GROUNDS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2603_restore_all_hp_17"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2603_restore_all_hp_17"),
	RestoreAllFP(),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_13),
	SummonObjectToCurrentLevel(NPC_15),
	RemoveObjectFromSpecificLevel(NPC_0, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_1, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_2, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_3, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_4, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_5, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_6, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_13, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	SummonObjectToSpecificLevel(NPC_15, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=10, y=91),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(8),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=False),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_12),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(3)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3261_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3266_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_12, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=0, y=57),
		A_Pause(160),
		A_WalkToXYCoords(x=5, y=75)
	]),
	Pause(32),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3262_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	SetAsyncActionScript(NPC_12, A0854_EMPTY),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_FaceSoutheast(),
		A_Pause(16),
		A_ResetProperties()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3263_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(TEMP_70AE, 32),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(48),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3264_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(64),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3265_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(80),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_ResetProperties()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3212_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(3),
		A_VisibilityOff()
	]),
	Return(identifier="EVENT_2603_ret_70")
])
