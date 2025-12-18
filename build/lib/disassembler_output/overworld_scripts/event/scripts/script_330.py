# E0330_CHANCELLOR

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
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_330_jmp_if_var_equals_const_10"]),
	JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["EVENT_330_jmp_to_event_20"]),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 3, ["EVENT_330_action_queue_6"]),
	RunDialog(dialog_id=DI0568_CHANCELLOR, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_330_run_dialog_4"),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties()
	], identifier="EVENT_330_action_queue_6"),
	RunDialog(dialog_id=DI0569_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(TEMP_70AE, 0),
	Return(),
	JmpIfVarEqualsConst(TEMP_70AE, 1, ["EVENT_330_run_dialog_4"], identifier="EVENT_330_jmp_if_var_equals_const_10"),
	JmpIfVarEqualsConst(TEMP_70AE, 2, ["EVENT_330_run_dialog_4"]),
	JmpIfVarEqualsConst(TEMP_70AE, 3, ["EVENT_330_action_queue_6"]),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ResetProperties(),
		A_FaceMario()
	]),
	Inc(TEMP_70AE),
	RunDialog(dialog_id=DI0568_CHANCELLOR, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C()
	]),
	Return(),
	JmpToEvent(E3598_EMPTY, identifier="EVENT_330_jmp_to_event_20")
])
