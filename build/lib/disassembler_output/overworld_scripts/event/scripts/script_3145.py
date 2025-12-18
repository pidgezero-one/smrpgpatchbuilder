# E3145_SEWERS_FLIPPABLE_CHEST

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
	JmpIfVarEqualsConst(ACTIVE_NPC, 20, ["EVENT_3145_jmp_to_event_3"]),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_3145_set_var_to_const_4"]),
	JmpToEvent(E0032_NON_COIN_CHEST_CONTAINER),
	JmpToEvent(E0032_NON_COIN_CHEST_CONTAINER, identifier="EVENT_3145_jmp_to_event_3"),
	SetVarToConst(ITEM_ID, CricketJamItem, identifier="EVENT_3145_set_var_to_const_4"),
	RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
	SetVarToConst(PRIMARY_TEMP_7000, 1586),
	SetVarToConst(ITEM_ID, CricketJamItem),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	SetBit(SEWERS_FLIPPED_CHEST_OPENED),
	Return()
])
