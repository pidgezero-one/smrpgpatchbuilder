# E3592_EMPTY

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
	PauseActionScript(MEM_70A8),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1])
	]),
	JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_3592_set_action_script_5"]),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	Pause(60),
	SetAsyncActionScript(MEM_70A8, A0636_54_VELOCITY_SINGLE_JUMP, identifier="EVENT_3592_set_action_script_5"),
	RunDialog(dialog_id=DI0539_EMPTY, above_object=MEM_70A8, closable=True, sync=True, multiline=True, use_background=True),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 51, ["EVENT_3592_action_queue_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 495, ["EVENT_3592_action_queue_28"]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkToXYCoords(x=12, y=117)
	]),
	Pause(30),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_3592_apply_tile_mod_16"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, mod_id=0),
	Jmp(["EVENT_3592_play_sound_17"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R191_MUSHROOM_KINGDOM_OUTSIDE, mod_id=0, identifier="EVENT_3592_apply_tile_mod_16"),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6, identifier="EVENT_3592_play_sound_17"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_Walk1StepNorthwest(),
		A_VisibilityOff()
	]),
	Pause(10),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 191, ["EVENT_3592_apply_tile_mod_24"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE, mod_id=0),
	Jmp(["EVENT_3592_play_sound_25"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R191_MUSHROOM_KINGDOM_OUTSIDE, mod_id=0, identifier="EVENT_3592_apply_tile_mod_24"),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6, identifier="EVENT_3592_play_sound_25"),
	SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
	Return(),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(5),
		A_VisibilityOff()
	], identifier="EVENT_3592_action_queue_28"),
	RemoveObjectFromCurrentLevel(NPC_2),
	ClearBit(UNIVERSAL_CHEST_ANIMATION_BIT),
	Return()
])
