# E3134_RESUMMON_ENEMIES_IN_SEWER

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
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	MoveScriptToBackgroundThread2(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 256, ["EVENT_3134_set_var_to_const_11"]),
	RunDialog(dialog_id=DI1583_EMPTY, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=True),
	SetVarToConst(SECONDARY_TEMP_7024, 300),
	Pause(1, identifier="EVENT_3134_pause_5"),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(bits=[0, 1, 2, 3, 4, 7], destinations=["EVENT_3134_close_dialog_10"]),
	Dec(SECONDARY_TEMP_7024),
	JmpIfLoadedMemoryIsNot0(["EVENT_3134_pause_5"]),
	CloseDialog(identifier="EVENT_3134_close_dialog_10"),
	SetVarToConst(TIMER_701C, 300, identifier="EVENT_3134_set_var_to_const_11"),
	StopBackgroundEvent(TIMER_701C),
	MoveScriptToMainThread(),
	Return(),
	SummonObjectToSpecificLevel(NPC_0, R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, identifier="EVENT_3134_summon_to_level_15"),
	SummonObjectToSpecificLevel(NPC_1, R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES),
	RemoveObjectFromSpecificLevel(NPC_2, R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES),
	SummonObjectToSpecificLevel(NPC_0, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER),
	SummonObjectToSpecificLevel(NPC_1, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER),
	SummonObjectToSpecificLevel(NPC_2, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER),
	SummonObjectToSpecificLevel(NPC_3, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER),
	SummonObjectToSpecificLevel(NPC_4, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER),
	SummonObjectToSpecificLevel(NPC_5, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER),
	SummonObjectToSpecificLevel(NPC_0, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE),
	SummonObjectToSpecificLevel(NPC_1, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE),
	SummonObjectToSpecificLevel(NPC_2, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE),
	SummonObjectToSpecificLevel(NPC_3, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE),
	SummonObjectToSpecificLevel(NPC_1, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_2, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_3, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_4, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_5, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_6, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_2, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_3, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_4, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_5, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_6, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS),
	SummonObjectToSpecificLevel(NPC_3, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS),
	SummonObjectToSpecificLevel(NPC_4, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS),
	SummonObjectToSpecificLevel(NPC_5, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS),
	ClearBit(SEWER_WATER_LEVEL),
	ApplySolidityModToLevel(permanent=False, room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, mod_id=0),
	ApplySolidityModToLevel(permanent=False, room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, mod_id=1),
	ApplySolidityModToLevel(permanent=False, room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, mod_id=0),
	ApplySolidityModToLevel(permanent=False, room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, mod_id=1),
	ApplySolidityModToLevel(permanent=False, room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, mod_id=0),
	ApplySolidityModToLevel(permanent=False, room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, mod_id=1),
	SetBit(TEMP_7042_0),
	Return()
])
