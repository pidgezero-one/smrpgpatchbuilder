# E2419_EMPTY

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
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_2419_jmp_if_present_in_current_level_10"]),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_2419_pause_action_script_31"]),
	JmpIfObjectInSpecificLevel(NPC_5, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, ["EVENT_2419_action_queue_7"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_2419_jmp_if_present_in_current_level_10"]),
	SetSyncActionScript(NPC_1, A0388_EMPTY),
	SetSyncActionScript(NPC_5, A0388_EMPTY),
	Jmp(["EVENT_2419_jmp_if_present_in_current_level_10"]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=14, y=90, z=16, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(3),
		A_VisibilityOn()
	], identifier="EVENT_2419_action_queue_7"),
	SetSyncActionScript(NPC_1, A0388_EMPTY),
	SetSyncActionScript(NPC_5, A0388_EMPTY),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2419_jmp_if_present_in_current_level_20"], identifier="EVENT_2419_jmp_if_present_in_current_level_10"),
	JmpIfBitClear(TEMP_7044_0, ["EVENT_2419_pause_action_script_37"]),
	JmpIfObjectInSpecificLevel(NPC_7, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, ["EVENT_2419_action_queue_17"]),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_2419_jmp_if_present_in_current_level_20"]),
	SetSyncActionScript(NPC_3, A0388_EMPTY),
	SetSyncActionScript(NPC_7, A0388_EMPTY),
	Jmp(["EVENT_2419_jmp_if_present_in_current_level_20"]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=11, y=82, z=16, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(8),
		A_WalkWestPixels(3),
		A_VisibilityOn()
	], identifier="EVENT_2419_action_queue_17"),
	SetSyncActionScript(NPC_3, A0388_EMPTY),
	SetSyncActionScript(NPC_7, A0388_EMPTY),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_2419_ret_30"], identifier="EVENT_2419_jmp_if_present_in_current_level_20"),
	JmpIfBitClear(TEMP_7044_1, ["EVENT_2419_pause_action_script_34"]),
	JmpIfObjectInSpecificLevel(NPC_6, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, ["EVENT_2419_action_queue_27"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_2419_ret_30"]),
	SetSyncActionScript(NPC_2, A0388_EMPTY),
	SetSyncActionScript(NPC_6, A0388_EMPTY),
	Jmp(["EVENT_2419_ret_30"]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=13, y=85, z=18, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(3),
		A_VisibilityOn()
	], identifier="EVENT_2419_action_queue_27"),
	SetSyncActionScript(NPC_2, A0388_EMPTY),
	SetSyncActionScript(NPC_6, A0388_EMPTY),
	Return(identifier="EVENT_2419_ret_30"),
	PauseActionScript(NPC_1, identifier="EVENT_2419_pause_action_script_31"),
	RemoveObjectFromCurrentLevel(NPC_1),
	Return(),
	PauseActionScript(NPC_2, identifier="EVENT_2419_pause_action_script_34"),
	RemoveObjectFromCurrentLevel(NPC_2),
	Return(),
	PauseActionScript(NPC_3, identifier="EVENT_2419_pause_action_script_37"),
	RemoveObjectFromCurrentLevel(NPC_3),
	Return()
])
