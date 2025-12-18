# E3126_MIMIC_2_CHEST

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
	JmpIfBitSet(MIMIC_2_CLEARED, ["EVENT_3126_jmp_to_event_10"]),
	SetVarToConst(BATTLE_PACK_ID, 157),
	RunEventAsSubroutine(E0035_MIMIC_OR_SLOT_CHEST_CONTAINER),
	JmpIfBitClear(UNKNOWN_MIMIC_BIT, ["EVENT_3126_ret_9"]),
	SetBit(MIMIC_2_CLEARED),
	SetSyncActionScript(MEM_70A8, A0015_DO_NOTHING),
	SetVarToConst(ITEM_ID, SafetyBadgeItem),
	SetVarToConst(PRIMARY_TEMP_7000, 1586),
	RunEventAsSubroutine(E3829_EMPTY),
	Return(identifier="EVENT_3126_ret_9"),
	JmpToEvent(E0034_COIN_CHEST_CONTAINER, identifier="EVENT_3126_jmp_to_event_10")
])
