# E0379_MUSHROOM_KINGDOM_OCCUPIED_GUEST_ROOM_GRANT

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
	JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED, ["EVENT_379_run_dialog_16"]),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED),
	PauseActionScript(NPC_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(VERY_FAST)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=27, y=49),
		A_FaceNortheast(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	RunDialog(dialog_id=DI2559_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI0654_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, WakeUpPinItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(WakeUpPinItem),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequenceLoopingOn()
	]),
	Return(),
	RunDialog(dialog_id=DI0655_VAULT_HINT, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_379_run_dialog_16"),
	Return()
])
