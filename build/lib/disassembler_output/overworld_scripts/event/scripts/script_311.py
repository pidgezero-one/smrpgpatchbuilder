# E0311_MUSHROOM_KINGDOM_EAST_GUARD

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
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_311_run_dialog_13"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_256_ret_0"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_311_run_dialog_7"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_4, ["EVENT_311_run_dialog_11"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_311_set_bit_9"]),
	RunDialog(dialog_id=DI0590_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0591_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_311_run_dialog_7"),
	Return(),
	SetBit(TEMP_7043_3, identifier="EVENT_311_set_bit_9"),
	JmpToEvent(E0332_EMPTY),
	RunDialog(dialog_id=DI0604_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_311_run_dialog_11"),
	Return(),
	RunDialog(dialog_id=DI2224_TOAD_GUARD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_311_run_dialog_13"),
	Return()
])
