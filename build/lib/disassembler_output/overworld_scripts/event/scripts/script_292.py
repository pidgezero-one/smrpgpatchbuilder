# E0292_MUSHROOM_KINGDOM_WEST_BLUE_TOAD

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
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_292_run_dialog_13"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_292_jmp_if_bit_set_5"]),
	JmpIfBitSet(TOWER_BOSS_1_STAR_PIECE, ["EVENT_292_jmp_if_bit_set_5"]),
	RunDialog(dialog_id=DI0530_MUSHROOM_KINGDOM_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_292_jmp_if_bit_set_8"], identifier="EVENT_292_jmp_if_bit_set_5"),
	RunDialog(dialog_id=DI0605_BERSERK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_292_run_dialog_11"], identifier="EVENT_292_jmp_if_bit_set_8"),
	RunDialog(dialog_id=DI0724_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0605_BERSERK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_292_run_dialog_11"),
	Return(),
	RunDialog(dialog_id=DI2232_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_292_run_dialog_13"),
	Pause(10),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	Pause(40),
	RunDialog(dialog_id=DI2233_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
