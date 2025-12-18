# E2112_NIMBUS_CASTLE_STATUE_GAME_ROOM_LOADER

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
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_2112_action_queue_18"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkNorthwestPixels(3),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkNorthwestPixels(3),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkNorthwestPixels(3),
		A_FaceNortheast()
	]),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_6, ["EVENT_2112_fade_in_from_black_async_16"]),
	JmpIfBitSet(UNKNOWN_STATUE_ROOM_7090_1, ["EVENT_2112_fade_in_from_black_async_16"]),
	JmpIfBitSet(UNKNOWN_STATUE_ROOM_7092_3, ["EVENT_2112_palette_set_13"]),
	PaletteSet(palette_set=111, row=1, bit_3=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=6, y=68, z=2, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=8, y=69, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkSouthwestPixels(9),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkNortheastPixels(5)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=2, y=53)
	]),
	Jmp(["EVENT_2113_fade_in_from_black_sync_duration_0"]),
	PaletteSet(palette_set=111, row=1, bit_3=True, identifier="EVENT_2112_palette_set_13"),
	FadeInFromBlack(sync=False),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_2112_fade_in_from_black_async_16"),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(5),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2112_action_queue_18"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(5),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(5),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=False),
	Return()
])
