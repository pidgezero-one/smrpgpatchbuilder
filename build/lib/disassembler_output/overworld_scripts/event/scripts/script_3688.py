# E3688_MARRYMORE_SERVICE_BELL

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
	Set70107015ToObjectXYZ(target=MARIO, bit_7=True),
	CompareVarToConst(Z_COORD_1, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3584_ret_0"]),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	Pause(20),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	Pause(20),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(BELLHOP_CALLED, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(BELLHOP_UNKNOWN, ["EVENT_3584_ret_0"]),
	SetBit(BELLHOP_CALLED),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=6, y=22),
		A_Pause(60),
		A_FaceNorthwest()
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FaceNortheast(),
		A_TransferToXYZF(x=3, y=23, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(1),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3846_LINK, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3688_close_dialog_34"]),
	RunDialog(dialog_id=DI3847_ROOM_SERVICE_MENU, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBOrCSelected(['EVENT_3688_set_var_to_const_41', 'EVENT_3688_close_dialog_34']),
	SetVarToConst(SECONDARY_TEMP_7024, 10),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3688_run_dialog_52"]),
	RunDialog(dialog_id=DI3849_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_Pause(90),
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(1),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(30),
	RunDialog(dialog_id=DI3850_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(ITEM_ID, PickMeUpItem),
	SetVarToConst(PRIMARY_TEMP_7000, 10),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	SetVarToConst(PRIMARY_TEMP_7000, 3852, identifier="EVENT_3688_set_var_to_const_30"),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	CopyVarToVar(from_var=ROSE_WAY_703A, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	CloseDialog(identifier="EVENT_3688_close_dialog_34"),
	Pause(10),
	RunDialog(dialog_id=DI3851_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	SetSyncActionScript(NPC_0, A0978_RANDOMLY_FACE_SOUTHWEST),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	SetVarToConst(SECONDARY_TEMP_7024, 150, identifier="EVENT_3688_set_var_to_const_41"),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3688_run_dialog_52"]),
	RunDialog(dialog_id=DI3849_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_Pause(90),
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(1),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(30),
	RunDialog(dialog_id=DI3850_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(ITEM_ID, KerokeroColaItem),
	SetVarToConst(PRIMARY_TEMP_7000, 150),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	Jmp(["EVENT_3688_set_var_to_const_30"]),
	RunDialog(dialog_id=DI3853_ROOM_SERVICE_INSUFFICIENT_COINS, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3688_run_dialog_52"),
	Jmp(["EVENT_3688_close_dialog_34"])
])
