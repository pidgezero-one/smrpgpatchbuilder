# E3013_CLONE_RESERVED

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
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_3013_run_dialog_11"]),
	JmpIfBitClear(UNKNOWN_709D_6, ["EVENT_3013_run_dialog_13"]),
	JmpIfBitClear(UNKNOWN_709E_0, ["EVENT_3013_run_dialog_15"]),
	JmpIfBitClear(UNKNOWN_709E_1, ["EVENT_3013_run_dialog_17"]),
	JmpIfBitClear(UNKNOWN_709E_4, ["EVENT_3013_run_dialog_19"]),
	JmpIfBitClear(UNKNOWN_709E_5, ["EVENT_3013_run_dialog_21"]),
	JmpIfBitClear(UNKNOWN_709D_4, ["EVENT_3013_run_dialog_23"]),
	JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_3013_run_dialog_25"]),
	JmpIfBitClear(UNKNOWN_709E_6, ["EVENT_3013_run_dialog_27"]),
	RunDialog(dialog_id=DI1027_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1028_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_11"),
	Return(),
	RunDialog(dialog_id=DI3680_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_13"),
	Return(),
	RunDialog(dialog_id=DI3921_VICTORY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_15"),
	Return(),
	RunDialog(dialog_id=DI3936_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_17"),
	Return(),
	RunDialog(dialog_id=DI3954_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_19"),
	Return(),
	RunDialog(dialog_id=DI1320_2_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_21"),
	Return(),
	RunDialog(dialog_id=DI1337_20_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_23"),
	Return(),
	RunDialog(dialog_id=DI1029_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_25"),
	Return(),
	RunDialog(dialog_id=DI1030_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3013_run_dialog_27"),
	Return()
])
