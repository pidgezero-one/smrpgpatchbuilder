# E0697_MARRYMORE_ENTRANCE_TOAD

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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_697_run_dialog_17"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_697_run_dialog_8"]),
	RunDialog(dialog_id=DI2158_MARRYMORE_FIELD_NPC, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2159_MARRYMORE_FIELD_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C()
	]),
	Return(),
	RunDialog(dialog_id=DI2160_MARRYMORE_FIELD_NPC, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_697_run_dialog_8"),
	Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2161_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2162_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C()
	]),
	Return(),
	RunDialog(dialog_id=DI2179_CHAPEL_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_697_run_dialog_17"),
	Return()
])
