# E0637_EMPTY

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
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	StartLoopNTimes(19),
	Pause(1),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_637_enable_controls_6"]),
	EndLoop(),
	JmpToEvent(E0256_RETURN),
	EnableControls([], identifier="EVENT_637_enable_controls_6"),
	PauseActionScript(NPC_10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=1),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastSteps(4)
	]),
	StartSyncEmbeddedActionScript(target=NPC_10, prefix=0xF1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(4)
	]),
	Pause(24),
	PlaySound(sound=SO151_CRASH_HIT, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=0),
	Pause(12),
	EnterArea(room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, face_direction=NORTHEAST, x=18, y=21, z=0),
	RemoveObjectFromSpecificLevel(NPC_0, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_1, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_10, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_TransferXYZFPixels(x=0, y=3, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO018_SUDDEN_STOP, channel=4),
		A_WalkNortheastPixels(12),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(4),
		A_Pause(60),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(5),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(3),
		A_SetWalkingSpeed(FASTER),
		A_WalkNortheastSteps(4),
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=True),
	Pause(10),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, mod_id=0),
	RememberLastObject(),
	RemoveObjectFromSpecificLevel(NPC_2, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	RemoveObjectFromSpecificLevel(NPC_4, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	Pause(40),
	PlaySoundBalance(sound=SO021_RUMBLING, balance=192),
	SetAsyncActionScript(SCREEN_FOCUS, A0334_EMPTY),
	Pause(30),
	RunDialog(dialog_id=DI2070_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI2071_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2072_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=False, room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=0),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	Return()
])
