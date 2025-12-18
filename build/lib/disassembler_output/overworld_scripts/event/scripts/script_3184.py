# E3184_MINES_FIRST_ROOM_LOADER

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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 54),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3184_set_bit_3"]),
	JmpToSubroutine(["EVENT_3183_jmp_if_bit_set_4"]),
	SetBit(TEMP_7042_0, identifier="EVENT_3184_set_bit_3"),
	JmpIfBitSet(PROGRESSIVE_BOSS_EXP_ENABLED, ["EVENT_3184_jmp_if_bit_set_57"]),
	PlayMusicAtDefaultVolume(M0027_DUNGEONISFULLOFMONSTERS),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(4)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	RunDialog(dialog_id=DI1616_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest7D(arg=0x14),
		A_JumpToHeight(64)
	]),
	RunDialog(dialog_id=DI1617_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_FaceSouthwest7D(arg=0x15),
		A_SequenceLoopingOff(),
		A_Pause(70),
		A_FaceNortheast(),
		A_Pause(12),
		A_FaceSouthwest7D(arg=0x15),
		A_WalkToXYCoords(x=18, y=30),
		A_FaceNortheast(),
		A_Pause(16),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_Pause(24),
		A_Walk1StepSouthwest(),
		A_Pause(48),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_ReturnAll()
	]),
	SetBit(PROGRESSIVE_BOSS_EXP_ENABLED),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_FaceNortheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_FaceNortheast()
	]),
	Pause(32),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_WalkToXYCoords(x=19, y=29)
	]),
	RunDialog(dialog_id=DI1618_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartAsyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_WalkToXYCoords(x=18, y=26)
	]),
	RunDialog(dialog_id=DI1619_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(29)
	]),
	StartSyncEmbeddedActionScript(target=SCREEN_FOCUS, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNorth(),
		A_Walk1StepNortheast()
	]),
	RunDialog(dialog_id=DI1620_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(29),
		A_Pause(20),
		A_FaceNortheast(),
		A_Pause(20),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI1621_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(29)
	]),
	RunDialog(dialog_id=DI1622_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_FaceNortheast(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_Pause(1, identifier="EVENT_3184_start_embedded_action_script_27_SUBSCRIPT_pause_3"),
		A_JmpIfBitClear(TEMP_7043_2, ["EVENT_3184_start_embedded_action_script_27_SUBSCRIPT_pause_3"]),
		A_FaceSouthwest(),
		A_JumpToHeight(72),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI1623_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartAsyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_Pause(24),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceNorthwest(),
		A_Pause(24),
		A_SetBit(TEMP_7043_3),
		A_JumpToHeight(29),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(12),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_JumpToHeight(72),
		A_SetWalkingSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_Pause(8),
		A_SetBit(TEMP_7043_2)
	]),
	Pause(1, identifier="EVENT_3184_pause_30"),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3184_pause_30"]),
	RunDialog(dialog_id=DI1624_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(TEMP_70AE, 21),
	SetTempSyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1625_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3184_set_var_to_const_48"]),
	SetVarToConst(TEMP_70AE, 21),
	SetTempSyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1628_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3184_run_dialog_39"),
	JmpIfDialogOptionBSelected(["EVENT_3184_set_var_to_const_53"]),
	SetVarToConst(TEMP_70AE, 21),
	SetTempSyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1630_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOff(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_WalkToXYCoords(x=19, y=27),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOff(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_WalkToXYCoords(x=19, y=26),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI1631_MOUNTAIN_ENTRANCE_GUYS, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	SetVarToConst(TEMP_70AE, 21, identifier="EVENT_3184_set_var_to_const_48"),
	SetTempSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1626_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI1627_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3184_run_dialog_39"]),
	SetVarToConst(TEMP_70AE, 21, identifier="EVENT_3184_set_var_to_const_53"),
	SetTempSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1629_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3184_run_dialog_39"]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_3184_remove_from_current_level_62"], identifier="EVENT_3184_jmp_if_bit_set_57"),
	PlayMusicAtDefaultVolume(M0027_DUNGEONISFULLOFMONSTERS),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_WalkToXYCoords(x=19, y=27),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_WalkToXYCoords(x=19, y=26),
		A_FaceNortheast()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_3184_remove_from_current_level_62"),
	RemoveObjectFromCurrentLevel(NPC_2),
	DisableObjectTrigger(NPC_1),
	DisableObjectTrigger(NPC_2),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
