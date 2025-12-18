# E0515_EMPTY

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
	JmpIfBitSet(UNUSED_7085_0, ["EVENT_256_ret_0"]),
	SetBit(MAP_FOREST_MAZE),
	SetBit(MAP_DIRECTIONAL_ROSE_TOWN_FOREST_MAZE),
	SetBit(UNKNOWN_ROSE_TOWN_7060_7),
	MoveScriptToBackgroundThread2(),
	SetBit(UNUSED_7085_0),
	SetBit(TEMP_7044_6),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1])
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_FaceWest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	SetBit(TEMP_7043_7),
	RunDialog(dialog_id=DI0769_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Pause(10),
	SetAsyncActionScript(NPC_1, A0624_EMPTY),
	SetAsyncActionScript(NPC_0, A0625_EMPTY),
	Pause(30),
	RunDialog(dialog_id=DI0770_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	SetAsyncActionScript(NPC_0, A0626_EMPTY),
	RunDialog(dialog_id=DI0771_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	SetAsyncActionScript(NPC_1, A0625_EMPTY),
	RunDialog(dialog_id=DI0772_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	SetAsyncActionScript(NPC_1, A0627_EMPTY),
	SetSyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0773_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_1),
	SetSyncActionScript(NPC_0, A0629_EMPTY),
	Pause(20),
	SetSyncActionScript(NPC_1, A0628_EMPTY),
	RunDialog(dialog_id=DI0774_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	SetSyncActionScript(NPC_0, A0630_EMPTY),
	SetSyncActionScript(NPC_1, A0631_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI0775_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	MoveScriptToMainThread(),
	Return()
])
