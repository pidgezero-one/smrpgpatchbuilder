# E3348_KEEP_DOOR_REWARD_CHEST

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
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(2),
		A_Pause(8),
		A_ShiftZDownSteps(2),
		A_SetWalkingSpeed(NORMAL)
	]),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x0007),
	AddConstToVar(PRIMARY_TEMP_7000, 512),
	Dec(PRIMARY_TEMP_7000),
	SetMem704XAt7000Bit(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 513, ["EVENT_3348_set_var_to_const_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 514, ["EVENT_3348_set_var_to_const_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 515, ["EVENT_3348_set_var_to_const_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 516, ["EVENT_3348_set_var_to_const_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 517, ["EVENT_3348_set_var_to_const_21"]),
	SetVarToConst(ITEM_ID, SonicCymbalItem),
	Jmp(["EVENT_3348_run_event_as_subroutine_22"]),
	SetVarToConst(ITEM_ID, SuperSlapItem, identifier="EVENT_3348_set_var_to_const_13"),
	Jmp(["EVENT_3348_run_event_as_subroutine_22"]),
	SetVarToConst(ITEM_ID, DrillClawItem, identifier="EVENT_3348_set_var_to_const_15"),
	Jmp(["EVENT_3348_run_event_as_subroutine_22"]),
	SetVarToConst(ITEM_ID, StarGunItem, identifier="EVENT_3348_set_var_to_const_17"),
	Jmp(["EVENT_3348_run_event_as_subroutine_22"]),
	SetVarToConst(ITEM_ID, RockCandyItem, identifier="EVENT_3348_set_var_to_const_19"),
	Jmp(["EVENT_3348_run_event_as_subroutine_22"]),
	SetVarToConst(ITEM_ID, RockCandyItem, identifier="EVENT_3348_set_var_to_const_21"),
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED, identifier="EVENT_3348_run_event_as_subroutine_22"),
	SetVarToConst(PRIMARY_TEMP_7000, 1586),
	RunEventAsSubroutine(E3829_EMPTY),
	Return()
])
