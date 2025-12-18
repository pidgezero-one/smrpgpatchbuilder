# E0322_MUSHROOM_KINGDOM_THRONE_ROOM_LOADER

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
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Set0158Bit7Offset(0x015C),
	Set0158Bit7Offset(0x015E),
	JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_322_jmp_if_bit_set_20"]),
	SetBit(STATUE_KEEPER_STAR_PIECE),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=14, y=33, z=2, direction=EAST),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastSteps(4)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(4),
		A_Pause(16)
	]),
	FadeInFromBlack(sync=True),
	RememberLastObject(),
	RunDialog(dialog_id=DI0554_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(15),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkNorthwestSteps(2),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(4)
	]),
	RememberLastObject(),
	Return(),
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_322_jmp_if_bit_set_32"], identifier="EVENT_322_jmp_if_bit_set_20"),
	JmpIfBitClear(SIGNAL_RING_STAR_PIECE_1, ["EVENT_322_jmp_if_bit_set_32"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_322_remove_from_current_level_22"),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=15, y=29, z=4, direction=EAST)
	]),
	SetSyncActionScript(NPC_6, A0128_WALK_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_0, A0138_CHANCELLOR),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_322_remove_from_current_level_22"], identifier="EVENT_322_jmp_if_bit_set_32"),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_322_remove_from_current_level_22"]),
	JmpToEvent(E0257_FADE_IN_ASYNC)
])
