# E0329_EMPTY

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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
	JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["EVENT_256_ret_0"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_256_ret_0"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_0),
	RunDialog(dialog_id=DI0567_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	Pause(60),
	FreezeCamera(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_BounceToXYWithHeight(x=9, y=87, height=13)
	]),
	SummonObjectToCurrentLevel(NPC_9),
	SummonObjectToCurrentLevel(NPC_10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(6),
		A_FaceNorthwest(),
		A_Pause(30),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_329_action_queue_12_SUBSCRIPT_pause_5"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_329_action_queue_12_SUBSCRIPT_pause_5"]),
		A_ObjectMemoryClearBit(arg_1=0x09, bits=[7]),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(6),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(1, identifier="EVENT_329_action_queue_12_SUBSCRIPT_pause_14"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_329_action_queue_12_SUBSCRIPT_pause_14"]),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(8)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=108, silent=True),
		A_WalkSouthwestSteps(4),
		A_TransferToXYZF(x=8, y=106, z=0, direction=EAST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(100),
		A_WalkSoutheastSteps(3),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_Pause(10),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(6),
		A_SetWalkingSpeed(NORMAL)
	]),
	Pause(50),
	PlaySoundBalance(sound=SO068_MALLOW_YELLING_AT_CROCO, balance=64),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_Pause(50),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(6)
	]),
	StopSound(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(1, identifier="EVENT_329_action_queue_19_SUBSCRIPT_pause_22"),
		A_JmpIfObjectInAir(NPC_10, ["EVENT_329_action_queue_19_SUBSCRIPT_pause_22"]),
		A_Pause(30),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_Walk1StepSoutheast(),
		A_SetSpriteSequence(index=1, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO069_MALLOW_FALLING_LANDING, channel=6),
	Pause(30),
	PlaySoundBalance(sound=SO068_MALLOW_YELLING_AT_CROCO, balance=192),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(7)
	]),
	RememberLastObject(),
	Pause(20),
	StopSound(),
	Pause(30),
	RunDialog(dialog_id=DI0567_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_TransferToXYZF(x=17, y=100, z=8, direction=EAST),
		A_WalkSouthwestSteps(2),
		A_WalkNorthwestSteps(6),
		A_FaceSoutheast(),
		A_Pause(30),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_329_action_queue_29_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_329_action_queue_29_SUBSCRIPT_pause_8"]),
		A_JumpToHeight(height=108, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_Pause(1, identifier="EVENT_329_action_queue_29_SUBSCRIPT_pause_13"),
		A_JmpIfObjectInAir(NPC_9, ["EVENT_329_action_queue_29_SUBSCRIPT_pause_13"]),
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_WalkNorthwestSteps(12),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_Pause(50),
		A_PlaySoundBalance(sound=SO068_MALLOW_YELLING_AT_CROCO, balance=192),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties(),
		A_Pause(18),
		A_TransferToXYZF(x=17, y=100, z=8, direction=EAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_WalkNorthwestSteps(6),
		A_StopSound(),
		A_ResetProperties(),
		A_StartLoopNTimes(1),
		A_FaceNorthwest(),
		A_Pause(8),
		A_FaceNortheast(),
		A_Pause(8),
		A_EndLoop(),
		A_FaceNortheast(),
		A_Pause(4),
		A_FaceNorthwest(),
		A_Pause(4),
		A_FaceNortheast(),
		A_Pause(20),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=5, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(50),
		A_SetSpriteSequence(index=5, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(64),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(6),
		A_FloatingOff()
	]),
	PlaySound(sound=SO069_MALLOW_FALLING_LANDING, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(8),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(6),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(2)
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_Pause(60),
		A_PlaySound(sound=SO070_MALLOW_SLIDING_ON_WALL, channel=6),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(12),
		A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(10),
		A_Pause(100),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	RunDialog(dialog_id=DI0572_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_10, A0076_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI0573_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageA(),
	SetBit(TEMP_7043_1),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetSyncActionScript(NPC_10, A0077_EMPTY),
	SetBit(SIGNAL_RING_STAR_PIECE_1),
	RemoveObjectFromCurrentLevel(NPC_9),
	Pause(30),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=17, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=18, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=19, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=20, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=21, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=22, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=23, row=7),
	PlaySound(sound=SO006_RUNNING_WATER, channel=4),
	Pause(60),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	SetSyncActionScript(NPC_3, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ObjectMemorySetBit(arg_1=0x09, bits=[7]),
		A_ObjectMemorySetBit(arg_1=0x09, bits=[7])
	]),
	SetSyncActionScript(NPC_4, A0128_WALK_RANDOM_DIRECTIONS),
	UnfreezeCamera(),
	Return()
])
