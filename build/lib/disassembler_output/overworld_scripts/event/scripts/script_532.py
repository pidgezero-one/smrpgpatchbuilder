# E0532_EMPTY

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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 98, ["EVENT_532_set_bit_28"]),
	SetVarToConst(TEMP_70A9, 21),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"], identifier="EVENT_532_jmp_if_bit_set_3"),
	SetBit(TEMP_7043_0),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownPixels(6),
		A_SetWalkingSpeed(NORMAL)
	]),
	JmpIfBitSet(UNUSED_7060_4, ["EVENT_532_set_bit_16"]),
	SetBit(UNUSED_7060_4),
	Pause(60),
	JmpToSubroutine(["EVENT_532_play_sound_25"]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_532_apply_tile_mod_31"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	Return(),
	SetBit(TEMP_7043_0, identifier="EVENT_532_set_bit_16"),
	ClearBit(UNUSED_7060_4),
	Pause(60),
	JmpToSubroutine(["EVENT_532_play_sound_25"]),
	Pause(60),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_532_apply_tile_mod_34"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	ApplySolidityModToLevel(permanent=False, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	Return(),
	PlaySound(sound=SO021_RUMBLING, channel=6, identifier="EVENT_532_play_sound_25"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
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
	Return(),
	SetBit(TEMP_7044_6, identifier="EVENT_532_set_bit_28"),
	SetVarToConst(TEMP_70A9, 20),
	Jmp(["EVENT_532_jmp_if_bit_set_3"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_532_apply_tile_mod_31"),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_532_apply_tile_mod_34"),
	ApplySolidityModToLevel(permanent=False, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=0),
	Return()
])
