# E2048_MONSTRO_TOWN_EXTERIOR_LOADER

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
	RemoveObjectFromCurrentLevel(NPC_3, identifier="EVENT_2048_remove_from_current_level_0"),
	DisableObjectTrigger(NPC_3),
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_2048_set_bit_8"]),
	JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2048_set_bit_8"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=2),
	JmpIfBitSet(UNKNOWN_709E_7, ["EVENT_2048_set_bit_8"]),
	SummonObjectToCurrentLevel(NPC_3),
	EnableObjectTrigger(NPC_3),
	SetBit(UNUSED_7093_5, identifier="EVENT_2048_set_bit_8"),
	JmpIfBitSet(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, ["EVENT_2048_set_bit_17"]),
	CopyVarToVar(from_var=MONSTRO_THWOMP_COUNTER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2048_action_queue_13"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_LoadMemory(PRIMARY_TEMP_7000),
		A_WalkSouthwestPixels(2),
		A_EndLoop()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	], identifier="EVENT_2048_action_queue_13"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2079_enable_controls_until_return_0"]),
	FadeInFromBlack(sync=False),
	Return(),
	SetBit(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN, identifier="EVENT_2048_set_bit_17"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=11, y=62, z=8, direction=EAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2079_enable_controls_until_return_0"]),
	FadeInFromBlack(sync=False),
	Return()
])
