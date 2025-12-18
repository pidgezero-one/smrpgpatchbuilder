# E0298_MUSHROOM_KINGDOM_PINK_TOAD

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
	Pause(1, identifier="EVENT_298_pause_0"),
	JmpIfMarioInAir(["EVENT_298_pause_0"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_3, ["EVENT_298_action_queue_18"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_298_run_dialog_16"]),
	FreezeCamera(identifier="EVENT_298_freeze_camera_4"),
	RunDialog(dialog_id=DI0535_EMPTY, above_object=NPC_4, closable=False, sync=True, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_298_action_queue_8_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_298_action_queue_8_SUBSCRIPT_pause_1"])
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(NORMAL)
	]),
	Pause(10),
	RunDialog(dialog_id=DI0536_EMPTY, above_object=NPC_4, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	UnfreezeCamera(),
	Return(),
	RunDialog(dialog_id=DI0580_SUPER_JUMP_TIMING_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_298_run_dialog_16"),
	Return(),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Set700CToObjectCoord(target_npc=NPC_4, coord=COORD_F),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
		A_FixedFCoordOn(),
		A_AddConstToVar(PRIMARY_TEMP_700C, 4),
		A_Mem700CAndConst(0x0007),
		A_FixedFCoordOff(),
		A_FaceEast7C()
	], identifier="EVENT_298_action_queue_18"),
	RunDialog(dialog_id=DI0588_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C()
	]),
	Return()
])
