# E3658_EMPTY

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
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_ShadowOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=15, y=45, z=4, direction=EAST),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_ResetProperties(),
		A_Pause(1),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_SetSpriteSequence(index=18, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_ResetProperties()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(2),
		A_Walk1StepNorthwest()
	]),
	RememberLastObject(),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(2),
		A_WalkSoutheastSteps(5),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SequenceLoopingOn(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(8),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_SetAllSpeeds(SLOW),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(3),
		A_WalkSouthwestPixels(8),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceNorthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_SetAllSpeeds(SLOW),
		A_WalkSoutheastSteps(3),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(7),
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceNorthwest(),
		A_SequenceLoopingOn()
	]),
	Pause(160),
	ActionQueueSync(target=NPC_10, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=15, y=45, z=4, direction=EAST),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_VisibilityOn()
	]),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Walk1StepNorthwest(),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2528_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(NPC_2, A0811_NIMBUS_NPC_RANDOM_DIRECTIONS),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceNortheast(),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(36),
		A_StopSound(),
		A_ResetProperties(),
		A_Pause(10),
		A_FaceNorthwest(),
		A_Pause(10),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_SetSolidityBits(bit_7=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2529_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x9e')),
		A_AddConstToVar(Z_COORD_2, 80),
		A_UnknownCommand(bytearray(b'\x9a')),
		A_TransferXYZFPixels(x=4, y=252, z=0, direction=EAST),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_Pause(1, identifier="EVENT_3658_action_queue_23_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_12, ["EVENT_3658_action_queue_23_SUBSCRIPT_pause_8"]),
		A_StopSound()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_Pause(50),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_WalkNortheastSteps(2)
	]),
	RunDialog(dialog_id=DI2530_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1, identifier="EVENT_3658_pause_27"),
	JmpIfObjectInAir(NPC_12, ["EVENT_3658_pause_27"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2531_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	UnfreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_Pause(40),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_Pause(60),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_FaceNortheast(),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(21),
		A_ResetProperties()
	]),
	Pause(60),
	RunDialog(dialog_id=DI2532_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RememberLastObject(),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(12),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepNorth(),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkEastPixels(32),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_ResetProperties(),
		A_Pause(4),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_Pause(16),
		A_AddZCoord1Step(),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(8)
	]),
	RememberLastObject(),
	Pause(60),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(16),
		A_ResetProperties()
	]),
	RememberLastObject(),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_SetPriority(2),
		A_WalkNortheastSteps(6),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	Pause(120),
	PaletteSet(palette_set=105, row=1, bit_1=True, bit_2=True, bit_3=True),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_ResetProperties(),
		A_Pause(4),
		A_SetSpriteSequence(index=22, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=5, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RemoveObjectFromCurrentLevel(NPC_8),
	Pause(40),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(3),
		A_SetSpriteSequence(index=9, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=10, sprite_offset=5, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_VisibilityOff(),
		A_TransferToObjectXY(MARIO),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=SOUTHEAST),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_VisibilityOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(2),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(4),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10)
	]),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_11),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_TransferXYZFPixels(x=10, y=251, z=8, direction=EAST),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	SummonObjectToCurrentLevel(NPC_11),
	RememberLastObject(),
	FadeOutMusicToVolume(duration=3, volume=1),
	Pause(180),
	PlaySound(sound=SO006_RUNNING_WATER, channel=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=113, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=122, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=123, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=124, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=125, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=126, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=127, row=7),
	Pause(30),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_7),
	PauseActionScript(NPC_8),
	SetSyncActionScript(NPC_0, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_4, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_7, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_8, A0376_TURN_RANDOMLY_IN_PLACE),
	Pause(270),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=114, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=130, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=131, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=132, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=133, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=134, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=135, row=7),
	FadeOutSoundToVolume(duration=3, volume=0),
	FadeOutMusicToVolume(duration=3, volume=127),
	Pause(120),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_7),
	PauseActionScript(NPC_8),
	SetSyncActionScript(NPC_0, A0626_EMPTY),
	SetSyncActionScript(NPC_4, A0627_EMPTY),
	SetSyncActionScript(NPC_7, A0625_EMPTY),
	SetAsyncActionScript(NPC_8, A0627_EMPTY),
	SetSyncActionScript(NPC_2, A0811_NIMBUS_NPC_RANDOM_DIRECTIONS),
	RemoveObjectFromCurrentLevel(NPC_11),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_TransferXYZFPixels(x=246, y=5, z=24, direction=NORTHEAST),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	SummonObjectToCurrentLevel(NPC_11),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(3),
		A_SetSpriteSequence(index=9, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
		A_Pause(3),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(4),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(2)
	]),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_11),
	Pause(120),
	FreezeCamera(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_TransferToXYZF(x=20, y=36, z=4, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(3),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_3658_action_queue_128_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3658_action_queue_128_SUBSCRIPT_pause_1"])
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(22),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_WalkNortheastSteps(10)
	]),
	Pause(30),
	FadeOutToBlack(sync=True, duration=60),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E3738_EMPTY)
])
