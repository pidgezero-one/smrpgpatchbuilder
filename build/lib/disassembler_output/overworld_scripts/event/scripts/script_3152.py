# E3152_ROSE_WAY_FIVE_CHESTS

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
	JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3152_set_bit_8"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3152_set_bit_12"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3152_set_bit_16"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3152_set_bit_20"]),
	SetBit(TEMP_7043_0),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	EnableObjectTriggerInSpecificLevel(NPC_0, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_3152_set_bit_8"),
	RunEventAsSubroutine(E0034_COIN_CHEST_CONTAINER),
	EnableObjectTriggerInSpecificLevel(NPC_1, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	Return(),
	SetBit(TEMP_7043_2, identifier="EVENT_3152_set_bit_12"),
	RunEventAsSubroutine(E0034_COIN_CHEST_CONTAINER),
	EnableObjectTriggerInSpecificLevel(NPC_2, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	Return(),
	SetBit(TEMP_7043_3, identifier="EVENT_3152_set_bit_16"),
	RunEventAsSubroutine(E0034_COIN_CHEST_CONTAINER),
	EnableObjectTriggerInSpecificLevel(NPC_3, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	Return(),
	SetBit(TEMP_7043_4, identifier="EVENT_3152_set_bit_20"),
	RunEventAsSubroutine(E0034_COIN_CHEST_CONTAINER),
	EnableObjectTriggerInSpecificLevel(NPC_4, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
	Return()
])
