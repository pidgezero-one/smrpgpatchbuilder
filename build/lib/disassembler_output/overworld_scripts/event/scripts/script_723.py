# E0723_MUSHROOM_KINGDOM_UNOCCUPIED_EXTERIOR_LOADER

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
	SummonObjectToSpecificLevel(NPC_0, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	SummonObjectToSpecificLevel(NPC_1, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	SummonObjectToSpecificLevel(NPC_2, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_3, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_4, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_5, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_6, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	Set0158Bit7Offset(0x0158),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 10),
	JmpIfBitClear(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_723_jmp_if_bit_set_11"]),
	RemoveObjectFromCurrentLevel(NPC_7),
	JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_723_jmp_if_bit_set_13"], identifier="EVENT_723_jmp_if_bit_set_11"),
	SummonObjectToSpecificLevel(NPC_0, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_723_jmp_if_bit_set_15"], identifier="EVENT_723_jmp_if_bit_set_13"),
	JmpToEvent(E0262_FADE_MUSIC_ROOM_LOADER),
	JmpIfBitSet(UNKNOWN_709C_2, ["EVENT_723_jmp_if_bit_set_18"], identifier="EVENT_723_jmp_if_bit_set_15"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestSteps(2),
		A_WalkNorthwestSteps(1)
	]),
	JmpToEvent(E0262_FADE_MUSIC_ROOM_LOADER),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_262_jmp_if_bit_clear_0"], identifier="EVENT_723_jmp_if_bit_set_18"),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=6, y=84, z=12, direction=EAST),
		A_TransferXYZFPixels(x=16, y=8, z=0, direction=EAST),
		A_SetPriority(2),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetSyncActionScript(NPC_10, A0978_RANDOMLY_FACE_SOUTHWEST),
	JmpToEvent(E0262_FADE_MUSIC_ROOM_LOADER)
])
