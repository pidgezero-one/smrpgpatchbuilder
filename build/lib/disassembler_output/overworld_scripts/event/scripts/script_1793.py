# E1793_LANDS_END_PURCHASABLE_CHEST_1_SUBROUTINE

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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 38),
	JmpIfLoadedMemoryIsNot0(["EVENT_1793_set_bit_6"]),
	SetBit(LANDS_END_CHEST_1_USED),
	ClearBit(LANDS_END_CHEST_1_PAID),
	Jmp(["EVENT_1793_run_event_as_subroutine_8"]),
	SetBit(LANDS_END_CHEST_2_USED, identifier="EVENT_1793_set_bit_6"),
	ClearBit(LANDS_END_CHEST_2_PAID),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER, identifier="EVENT_1793_run_event_as_subroutine_8"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_StartLoopNTimes(2),
		A_VisibilityOn(),
		A_Pause(8),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Return()
])
