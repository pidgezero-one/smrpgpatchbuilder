# E0291_MUSHROOM_KINGDOM_OUTER_CASTLE_GUARDS

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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 20, ["EVENT_291_action_queue_4"]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_Pause(16),
		A_FaceNorthwest(),
		A_Pause(32),
		A_FaceSouthwest()
	]),
	Jmp(["EVENT_291_jmp_if_bit_set_5"]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_Pause(16),
		A_FaceSoutheast(),
		A_Pause(32),
		A_FaceSouthwest()
	], identifier="EVENT_291_action_queue_4"),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_291_run_dialog_12"], identifier="EVENT_291_jmp_if_bit_set_5"),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_291_run_dialog_10"]),
	RunDialog(dialog_id=DI0528_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	Return(),
	RunDialog(dialog_id=DI0603_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_291_run_dialog_10"),
	Return(),
	RunDialog(dialog_id=DI2230_TOAD_GUARD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_291_run_dialog_12"),
	Return()
])
