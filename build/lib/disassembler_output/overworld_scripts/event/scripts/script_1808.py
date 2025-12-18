# E1808_BELOME_FORTUNE_PRIZE_CHEST_1_SUBROUTINE

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
	JmpIfVarEqualsConst(ACTIVE_NPC, 27, ["EVENT_1808_run_event_as_subroutine_9"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 29, ["EVENT_1808_run_event_as_subroutine_4"]),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	JmpToEvent(E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS),
	RunEventAsSubroutine(E0034_COIN_CHEST_CONTAINER, identifier="EVENT_1808_run_event_as_subroutine_4"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1808_ret_8"]),
	SetBit(TEMP_7043_3),
	JmpToEvent(E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS),
	Return(identifier="EVENT_1808_ret_8"),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER, identifier="EVENT_1808_run_event_as_subroutine_9"),
	SetVarToConst(ITEM_ID, YoshiCookieItem),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RunDialog(dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddToInventory(ITEM_ID),
	JmpToEvent(E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS)
])
