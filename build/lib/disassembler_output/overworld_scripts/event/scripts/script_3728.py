# E3728_EMPTY

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
	RunDialog(dialog_id=DI3599_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	JmpIfBitSet(UNKNOWN_7090_0, ["EVENT_3584_ret_0"]),
	SetBit(UNKNOWN_7090_0),
	Pause(10),
	RunDialog(dialog_id=DI2188_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=25, y=18),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceNortheast(),
		A_VisibilityOff(),
		A_TransferToXYZF(x=25, y=18, z=0, direction=EAST),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(12),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3605_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=21, y=2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Walk1StepSouthwest(),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3606_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True)
	]),
	SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3607_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3727_action_queue_15"])
])
