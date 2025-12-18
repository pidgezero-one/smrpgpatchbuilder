# E3831_MUSHROOM_KINGDOM_SHOP_CELLAR_MOD

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
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, ["EVENT_3831_set_7000_to_current_level_25"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, ["EVENT_3831_set_7000_to_current_level_25"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_3831_set_7000_to_current_level_25"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff()
	]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, ["EVENT_3831_set_7000_to_current_level_34"], identifier="EVENT_3831_jmp_if_object_trigger_disabled_4"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, ["EVENT_3831_set_7000_to_current_level_34"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_3831_set_7000_to_current_level_34"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	JmpIfBitSet(BUCKET_WARP_ENABLED, ["EVENT_3831_jmp_if_bit_clear_10"], identifier="EVENT_3831_jmp_if_bit_set_8"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=15, y=42, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	JmpIfBitClear(BUCKET_WARP_ENABLED, ["EVENT_3831_fade_in_from_black_async_12"], identifier="EVENT_3831_jmp_if_bit_clear_10"),
	SetSyncActionScript(NPC_2, A0128_WALK_RANDOM_DIRECTIONS),
	FadeInFromBlack(sync=False, identifier="EVENT_3831_fade_in_from_black_async_12"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3584_ret_0"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_1, R053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, ["EVENT_3831_clear_bit_22"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_1, R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, ["EVENT_3831_clear_bit_22"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_1, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_3831_clear_bit_22"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_0, R053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, ["EVENT_3831_clear_bit_22"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_0, R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, ["EVENT_3831_clear_bit_22"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_0, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["EVENT_3831_clear_bit_22"]),
	Return(),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_3831_clear_bit_22"),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	Return(),
	Set7000ToCurrentLevel(identifier="EVENT_3831_set_7000_to_current_level_25"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 484, ["EVENT_3831_apply_tile_mod_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 492, ["EVENT_3831_apply_tile_mod_32"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, mod_id=0),
	Jmp(["EVENT_3831_jmp_if_object_trigger_disabled_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, mod_id=0, identifier="EVENT_3831_apply_tile_mod_30"),
	Jmp(["EVENT_3831_jmp_if_object_trigger_disabled_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, mod_id=0, identifier="EVENT_3831_apply_tile_mod_32"),
	Jmp(["EVENT_3831_jmp_if_object_trigger_disabled_4"]),
	Set7000ToCurrentLevel(identifier="EVENT_3831_set_7000_to_current_level_34"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 484, ["EVENT_3831_apply_tile_mod_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 492, ["EVENT_3831_apply_tile_mod_41"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R053_MUSHROOM_KINGDOM_BEFORE_CROCO_ITEM_SHOP_BASEMENT, mod_id=1),
	Jmp(["EVENT_3831_jmp_if_bit_set_8"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, mod_id=1, identifier="EVENT_3831_apply_tile_mod_39"),
	Jmp(["EVENT_3831_jmp_if_bit_set_8"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, mod_id=1, identifier="EVENT_3831_apply_tile_mod_41"),
	Jmp(["EVENT_3831_jmp_if_bit_set_8"])
])
