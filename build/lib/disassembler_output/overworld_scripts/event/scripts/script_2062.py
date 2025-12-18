# E2062_MONSTRO_MIMIC

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
	JmpIfBitSet(BATTLE_DOOR_STAR_PIECE, ["EVENT_2062_copy_var_to_var_3"]),
	RunDialog(dialog_id=DI2634_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(BATTLE_DOOR_STAR_PIECE),
	CopyVarToVar(from_var=HIDDEN_CHEST_COUNTER, to_var=PRIMARY_TEMP_7000, identifier="EVENT_2062_copy_var_to_var_3"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	SetVarToConst(PRIMARY_TEMP_7000, 39),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2062_run_dialog_10"]),
	RunDialog(dialog_id=DI2635_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI2636_MIMICS_HINT, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2062_run_dialog_10"),
	Return()
])
