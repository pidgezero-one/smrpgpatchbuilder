# E0347_TOADSTOOLS_ROOM_LOADER

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
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(4)
	]),
	JmpIfBitSet(UNKNOWN_709C_2, ["EVENT_347_pause_action_script_13"]),
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_347_pause_action_script_6"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_347_pause_action_script_6"]),
	FadeInFromBlack(sync=False),
	Return(),
	PauseActionScript(NPC_0, identifier="EVENT_347_pause_action_script_6"),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=3, y=64, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
	JmpIfBitClear(UNUSED_705D_1, ["EVENT_347_fade_in_from_black_async_11"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=3, y=63, z=0, direction=EAST),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_FaceSouthwest()
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_347_fade_in_from_black_async_11"),
	Return(),
	PauseActionScript(NPC_0, identifier="EVENT_347_pause_action_script_13"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=16, y=66, z=0, direction=EAST),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=4, y=57, z=2, direction=EAST),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4])
	]),
	FadeInFromBlack(sync=False),
	Return()
])
