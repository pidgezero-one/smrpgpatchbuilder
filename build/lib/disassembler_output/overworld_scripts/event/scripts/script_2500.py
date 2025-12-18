# E2500_EMPTY

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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2500_ret_41"]),
	SetBit(TEMP_7043_0),
	RemoveObjectFromCurrentLevel(NPC_12),
	RemoveObjectFromCurrentLevel(NPC_13),
	RemoveObjectFromCurrentLevel(NPC_14),
	RemoveObjectFromCurrentLevel(NPC_15),
	RemoveObjectFromCurrentLevel(NPC_16),
	Pause(48),
	RunBackgroundEvent(event_id=E2501_EMPTY, return_on_level_exit=True),
	SummonObjectToCurrentLevel(NPC_0),
	SummonObjectToCurrentLevel(NPC_1),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_3),
	SummonObjectToCurrentLevel(NPC_4),
	SummonObjectToCurrentLevel(NPC_5),
	SummonObjectToCurrentLevel(NPC_6),
	SummonObjectToCurrentLevel(NPC_7),
	SummonObjectToCurrentLevel(NPC_8),
	SummonObjectToCurrentLevel(NPC_9),
	SummonObjectToCurrentLevel(NPC_10),
	SummonObjectToCurrentLevel(NPC_11),
	Pause(5),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=0),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=1),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=2),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=3),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=4),
	Pause(1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST, identifier="EVENT_2500_action_queue_37_SUBSCRIPT_set_animation_speed_0"),
		A_WalkNorthPixels(2),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(2),
		A_JmpIfBitSet(TEMP_7043_1, ["EVENT_2500_action_queue_37_SUBSCRIPT_set_animation_speed_6"]),
		A_Jmp(["EVENT_2500_action_queue_37_SUBSCRIPT_set_animation_speed_0"]),
		A_SetWalkingSpeed(NORMAL, identifier="EVENT_2500_action_queue_37_SUBSCRIPT_set_animation_speed_6")
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2500_action_queue_38_SUBSCRIPT_set_sprite_sequence_0"),
		A_Pause(1),
		A_JmpIfBitSet(TEMP_7043_1, ["EVENT_2500_action_queue_38_SUBSCRIPT_pause_4"]),
		A_Jmp(["EVENT_2500_action_queue_38_SUBSCRIPT_set_sprite_sequence_0"]),
		A_Pause(32, identifier="EVENT_2500_action_queue_38_SUBSCRIPT_pause_4")
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R261_BOWSERS_KEEP_1ST_TIME_AREA_03_LAVA_ROOM_WBRIDGE, mod_id=0),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(identifier="EVENT_2500_ret_41")
])
