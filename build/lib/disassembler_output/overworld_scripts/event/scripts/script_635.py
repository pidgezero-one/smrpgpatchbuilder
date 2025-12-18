# E0635_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUNROUTINE_3

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
	JmpIfBitSet(MARRYMORE_UNKNOWN_7063_2, ["EVENT_256_ret_0"]),
	SetBit(MARRYMORE_UNKNOWN_7063_2),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2064_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_BounceToXYWithHeight(x=7, y=34, height=4),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_BounceToXYWithHeight(x=2, y=16, height=0)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2065_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
	CloseDialog(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_635_action_queue_10_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_635_action_queue_10_SUBSCRIPT_pause_1"])
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI2066_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceWest()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(3),
		A_WalkToXYCoords(x=4, y=32),
		A_FaceNortheast()
	]),
	SetBit(TEMP_7044_7),
	SetSyncActionScript(NPC_10, A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceNorthwest(),
		A_Pause(90),
		A_FaceWest()
	]),
	UnsyncActionScript(NPC_10),
	ClearBit(TEMP_7044_7),
	Pause(40),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2067_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI2068_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkWestSteps(2),
		A_Walk1StepNorthwest()
	]),
	RunDialog(dialog_id=DI2201_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceNortheast()
	]),
	Pause(30),
	SetSyncActionScript(NPC_10, A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH),
	ApplySolidityModToLevel(permanent=True, room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER, mod_id=0),
	RemoveObjectFromSpecificLevel(NPC_12, R005_MARRYMORE_OUTSIDE_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_13, R005_MARRYMORE_OUTSIDE_DURING_BOOSTER),
	Return()
])
