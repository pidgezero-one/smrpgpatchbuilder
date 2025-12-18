# E1584_TEMPLE_FINAL_ROOM_LOADER

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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 37),
	JmpIfBitClear(TEMP_708C_4, ["EVENT_1584_jmp_if_bit_clear_3"]),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 43),
	JmpIfBitClear(LANDS_END_CHEST_2_REQUESTED, ["EVENT_1584_jmp_if_bit_set_5"], identifier="EVENT_1584_jmp_if_bit_clear_3"),
	SummonObjectToSpecificLevel(NPC_16, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1584_set_bit_8"], identifier="EVENT_1584_jmp_if_bit_set_5"),
	FadeInFromBlack(sync=False),
	Return(),
	SetBit(HAS_A_PRIZE_FORTUNE, identifier="EVENT_1584_set_bit_8"),
	ClearBit(BELOME_FORTUNE_1),
	ClearBit(UNKNOWN_BELOME_FORTUNE),
	ClearBit(UNKNOWN_BELOME_TEMPLE),
	SetVarToConst(TEMP_70AC, 0),
	ClearBit(FLOWER_TOWER_ASCENDED),
	ClearBit(SKIP_MANDATORY_MINECART),
	ClearBit(SKY_BRIDGE_TUTORIAL_BIT),
	SetVarToConst(UNKNOWN_70AD, 0),
	RemoveObjectFromCurrentLevel(NPC_0),
	SetBit(TEMPLE_ELEVATOR_DIRECTION),
	SummonObjectToSpecificLevel(NPC_0, R263_LANDS_END_UNDERGROUND_AREA_01),
	SummonObjectToSpecificLevel(NPC_1, R263_LANDS_END_UNDERGROUND_AREA_01),
	SummonObjectToSpecificLevel(NPC_2, R263_LANDS_END_UNDERGROUND_AREA_01),
	SummonObjectToSpecificLevel(NPC_0, R264_LANDS_END_UNDERGROUND_AREA_02),
	SummonObjectToSpecificLevel(NPC_1, R264_LANDS_END_UNDERGROUND_AREA_02),
	SummonObjectToSpecificLevel(NPC_2, R264_LANDS_END_UNDERGROUND_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R265_LANDS_END_UNDERGROUND_AREA_03),
	SummonObjectToSpecificLevel(NPC_1, R265_LANDS_END_UNDERGROUND_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R265_LANDS_END_UNDERGROUND_AREA_03),
	SummonObjectToSpecificLevel(NPC_0, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_1, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_2, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_3, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_4, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_5, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_6, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_7, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_8, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_9, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_10, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_11, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_12, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_13, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_14, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	SummonObjectToSpecificLevel(NPC_15, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS),
	FadeInFromBlack(sync=True),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	Return()
])
