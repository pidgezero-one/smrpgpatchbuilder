# E0556_ROSE_TOWN_LIBERATED_LOADER

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
	FadeOutMusicToVolume(duration=1, volume=127),
	JmpIfBitClear(UNUSED_705D_1, ["EVENT_556_action_queue_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=4),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3)
	], identifier="EVENT_556_action_queue_4"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetPriority(3)
	]),
	RememberLastObject(),
	SummonObjectToSpecificLevel(NPC_2, R087_ROSE_TOWN_ITEM_SHOP),
	SummonObjectToSpecificLevel(NPC_3, R087_ROSE_TOWN_ITEM_SHOP),
	SummonObjectToSpecificLevel(NPC_1, R091_ROSE_TOWN_COUPLES_HOUSE),
	JmpIfObjectNotInSpecificLevel(NPC_10, R084_ROSE_TOWN_OUTSIDE, ["EVENT_556_run_background_event_23"]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetPriority(3)
	]),
	JmpIfObjectNotInSpecificLevel(NPC_1, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, ["EVENT_556_apply_tile_mod_29"]),
	JmpIfBitSet(UNUSED_7060_4, ["EVENT_556_set_var_to_const_41"]),
	RunBackgroundEvent(event_id=E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND, return_on_level_exit=True),
	SetBit(TEMP_709F_5),
	FadeInFromBlack(sync=False),
	Return(),
	RunBackgroundEvent(event_id=E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND, return_on_level_exit=True, identifier="EVENT_556_run_background_event_23"),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(UNUSED_7060_4, ["EVENT_256_ret_0"]),
	Pause(60),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(3),
		A_WalkNorthPixels(1)
	]),
	Pause(8),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_556_apply_tile_mod_29"),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0),
	JmpIfBitClear(TEMP_709F_5, ["EVENT_556_set_bit_33"]),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetBit(TEMP_709F_5, identifier="EVENT_556_set_bit_33"),
	SetBit(UNUSED_7060_4),
	JmpIfObjectNotInSpecificLevel(NPC_10, R084_ROSE_TOWN_OUTSIDE, ["EVENT_256_ret_0"]),
	RemoveObjectFromSpecificLevel(NPC_10, R084_ROSE_TOWN_OUTSIDE),
	RemoveObjectFromCurrentLevel(NPC_10),
	RunBackgroundEvent(event_id=E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	SetVarToConst(TEMP_70A9, 30, identifier="EVENT_556_set_var_to_const_41"),
	RunBackgroundEvent(event_id=E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND, return_on_level_exit=True),
	SetBit(UNUSED_7061_4),
	Jmp(["EVENT_529_pause_action_script_27"])
])
