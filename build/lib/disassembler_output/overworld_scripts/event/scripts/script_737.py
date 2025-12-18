# E0737_GARROS_HOUSE_LOADER

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
	PaletteSet(palette_set=110, row=1, bit_0=True, bit_1=True, bit_2=True, bit_3=True),
	JmpIfBitClear(SHINY_STONE_TRADED, ["EVENT_737_set_action_script_14"]),
	SetVarToRandom(PRIMARY_TEMP_7000, 6),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_737_action_queue_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_737_set_action_script_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_737_action_queue_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_737_set_action_script_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_737_action_queue_13"]),
	Jmp(["EVENT_737_set_action_script_14"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_737_action_queue_9"),
	Jmp(["EVENT_737_set_action_script_14"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_737_action_queue_11"),
	Jmp(["EVENT_737_set_action_script_14"]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_737_action_queue_13"),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP, identifier="EVENT_737_set_action_script_14"),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_737_palette_set_22"]),
	JmpIfBitSet(INVISIBLE_ITEMS_SUMMONED, ["EVENT_737_action_queue_19"]),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=5, y=17, z=0, direction=EAST),
		A_FaceSoutheast()
	], identifier="EVENT_737_action_queue_19"),
	FadeInFromBlack(sync=False),
	Return(),
	PaletteSet(palette_set=109, row=1, bit_2=True, bit_3=True, identifier="EVENT_737_palette_set_22"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=6, y=22, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=23, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	SetSyncActionScript(NPC_3, A0263_FIX_F_COORD),
	SetSyncActionScript(NPC_4, A0263_FIX_F_COORD),
	SetSyncActionScript(NPC_5, A0263_FIX_F_COORD),
	UnsyncActionScript(NPC_3),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=6, y=22, z=0, direction=EAST),
		A_TransferXYZFPixels(x=254, y=4, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=False),
	Return()
])
