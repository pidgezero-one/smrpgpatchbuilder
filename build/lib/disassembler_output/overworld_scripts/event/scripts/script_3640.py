# E3640_STATUE_GAME

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
	JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["EVENT_3584_ret_0"]),
	ClearBit(INVISIBLE_ITEMS_SUMMONED),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=6, y=18),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10, identifier="EVENT_3640_pause_4"),
	RunDialog(dialog_id=DI2439_EMPTY, above_object=NPC_0, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3640_pause_205"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI2438_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(GARRO_SEQUENCE_COMPLETED, identifier="EVENT_3640_set_bit_11"),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_Pause(10),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(VERY_FAST),
		A_FaceSoutheast(),
		A_Pause(60),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkSouthPixels(6),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(6),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SequenceLoopingOn(),
		A_WalkEastPixels(14),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkEastPixels(14),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkWestPixels(14),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkWestPixels(14),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SequenceLoopingOn(),
		A_WalkNorthPixels(6),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNorthPixels(6),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff(),
		A_FaceNorthwest(),
		A_TransferToXYZF(x=6, y=19, z=0, direction=EAST),
		A_TransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
		A_VisibilityOn(),
		A_Pause(20),
		A_VisibilityOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOff(),
		A_FaceNortheast(),
		A_TransferToXYZF(x=5, y=19, z=0, direction=EAST),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_VisibilityOn(),
		A_Pause(20),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_Pause(8),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_Pause(8),
		A_VisibilityOff()
	]),
	StartLoopNTimes(5),
	Pause(4),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff()
	]),
	Pause(4),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff()
	]),
	Pause(4),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	EndLoop(),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=111, row=8),
	StartLoopNTimes(9),
	Pause(2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff()
	]),
	Pause(2),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff()
	]),
	Pause(2),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	EndLoop(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_Pause(60),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOff(),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2428_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceWest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(10),
		A_WalkSouthwestPixels(2),
		A_FloatingOff(),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI2429_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_WalkNortheastPixels(2),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2430_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(64),
		A_Pause(1, identifier="EVENT_3640_action_queue_52_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3640_action_queue_52_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(64),
		A_Pause(1, identifier="EVENT_3640_action_queue_52_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_3640_action_queue_52_SUBSCRIPT_pause_4"])
	]),
	Pause(10),
	RunDialog(dialog_id=DI2431_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_SequenceLoopingOn(),
		A_Walk1StepSouth(),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_WalkSouthwestSteps(2),
		A_Walk1StepSoutheast(),
		A_Pause(60)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestSteps(5)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(72),
		A_Walk1StepSouthwest(),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_Walk1StepNorthwest(),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(4),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(3),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(4)
	]),
	Pause(126),
	FadeOutToBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	RemoveObjectFromSpecificLevel(NPC_5, R341_NIMBUS_LAND_GARROS_HOUSE),
	SetBit(TEMP_704C_0),
	EnterArea(room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, face_direction=SOUTHEAST, x=13, y=36, z=2, run_entrance_event=True),
	ApplySolidityModToLevel(permanent=True, room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, mod_id=0),
	PaletteSet(palette_set=111, row=1, bit_3=True),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(6),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Walk1StepEast(),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ShadowOn(),
		A_TransferToXYZF(x=13, y=37, z=4, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SequencePlaybackOff(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(5),
		A_WalkEastSteps(1),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ShadowOn(),
		A_TransferToXYZF(x=14, y=38, z=4, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(4),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepEast(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_WalkNortheastSteps(2)
	]),
	FadeInFromBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	RunDialog(dialog_id=DI2445_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI2446_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_14, subscript=[
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(20),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(32),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(32),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(32),
		A_Walk1StepNortheast()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2064_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(10),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_WalkSouthwestSteps(2),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2447_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_14, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestPixels(8),
		A_FixedFCoordOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(72),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(60),
		A_SetWalkingSpeed(FAST),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepWest(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2448_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_FaceNortheast(),
		A_Pause(60),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(4),
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(20),
		A_FaceSoutheast(),
		A_Pause(10),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2449_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_14, subscript=[
		A_Pause(30),
		A_WalkNortheastPixels(4)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepEast(),
		A_SequenceLoopingOff(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(3)
	]),
	Pause(32),
	FadeOutToBlack(sync=True, duration=60),
	PauseScriptUntilEffectDone(),
	FadeOutMusicToVolume(duration=2, volume=0),
	Pause(4),
	EnterArea(room_id=R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, face_direction=NORTHEAST, x=3, y=31, z=2),
	PlayMusicAtDefaultVolume(M0061_VALENTINA),
	PaletteSet(palette_set=111, row=1, bit_3=True),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(7)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(7),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepSouth(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkNortheastSteps(7)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(7),
		A_Pause(40),
		A_ResetProperties(),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	FadeInFromBlack(sync=True, duration=60),
	RememberLastObject(),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI2450_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_SequencePlaybackOff(),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SequencePlaybackOn(),
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_Pause(30),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_Pause(30),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2465_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(4)
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, mod_id=0),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSouthwest(),
		A_TransferToXYZF(x=11, y=16, z=4, direction=EAST)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(5)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(32),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(3)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2451_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	RunDialog(dialog_id=DI2452_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_FaceSoutheast(),
		A_Pause(2),
		A_WalkSouthwestSteps(2),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(16),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepSouth(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	Pause(16),
	RunDialog(dialog_id=DI2453_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2454_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_SequencePlaybackOff(),
		A_Pause(30),
		A_StartLoopNTimes(1),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_Pause(4),
		A_EndLoop(),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(90),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2456_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Pause(8),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2457_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(80),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2458_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceNortheast(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(80),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2459_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4),
		A_Pause(60),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkSoutheastPixels(4),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2460_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2461_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI2452_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn(),
		A_Walk1StepNorthwest(),
		A_SequenceLoopingOff(),
		A_Pause(60),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_StartLoopNTimes(1),
		A_WalkNortheastPixels(3),
		A_WalkSouthwestPixels(3),
		A_Pause(10),
		A_EndLoop(),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkSouthwestSteps(9)
	]),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_7, R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI2466_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2462_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(90),
	RunDialog(dialog_id=DI2463_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=11, y=16, z=4, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(SLOW),
		A_VisibilityOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(4),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(4),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2464_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SequencePlaybackOff(),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownPixels(10),
		A_SequencePlaybackOn(),
		A_Pause(120),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(5)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(24),
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_EndLoop(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(120),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(80)
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_EndLoop(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(84),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(22),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(90),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(3),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=26, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=26, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(17),
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkSoutheastPixels(2),
		A_PlaySound(sound=SO145_BLACKSMITH_HAMMER_STRIKE, channel=4),
		A_StartLoopNTimes(3),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_EndLoop(),
		A_WalkNorthwestPixels(2),
		A_Pause(100),
		A_WalkSoutheastPixels(2),
		A_PlaySound(sound=SO145_BLACKSMITH_HAMMER_STRIKE, channel=4),
		A_StartLoopNTimes(3),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_EndLoop(),
		A_WalkNorthwestPixels(2),
		A_Pause(4),
		A_WalkSoutheastPixels(2),
		A_PlaySound(sound=SO145_BLACKSMITH_HAMMER_STRIKE, channel=4),
		A_StartLoopNTimes(3),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_EndLoop(),
		A_WalkNorthwestPixels(2)
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(84),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkNortheastSteps(5)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(5)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(5)
	]),
	Pause(60),
	FadeOutToBlack(sync=True, duration=60),
	PauseScriptUntilEffectDone(),
	RemoveObjectFromSpecificLevel(NPC_6, R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL),
	ClearBit(TEMP_704C_0),
	EnterArea(room_id=R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, face_direction=NORTHEAST, x=5, y=69, z=1),
	JmpToEvent(E2112_NIMBUS_CASTLE_STATUE_GAME_ROOM_LOADER),
	Pause(10, identifier="EVENT_3640_pause_205"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	RunDialog(dialog_id=DI2440_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
