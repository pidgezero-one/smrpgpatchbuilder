# E3729_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_LOADER

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
	JmpIfBitSet(TEMP_7076_0, ["EVENT_3732_action_queue_2"]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3729_fade_in_from_black_async_155"]),
	JmpIfBitSet(NIMBUS_BOSS_IN_TOWN_SQUARE, ["EVENT_3585_fade_in_from_black_async_0"]),
	FreezeCamera(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(1),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepNortheast(),
		A_Walk1StepNorth()
	]),
	FadeInFromBlack(sync=True, duration=60),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(10)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceNortheast(),
		A_TransferToXYZF(x=4, y=57, z=6, direction=EAST),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(60),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownPixels(10),
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(80),
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
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PauseScriptUntilEffectDone(),
	Pause(60),
	RunDialog(dialog_id=DI3616_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	RunDialog(dialog_id=DI3617_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3618_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3619_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(30),
	RunDialog(dialog_id=DI3620_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	PaletteSet(palette_set=111, row=1, bit_3=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=8, y=52, z=4, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(1),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(1),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_VisibilityOff(),
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_Pause(90),
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(30),
		A_StartLoopNTimes(1),
		A_VisibilityOff(),
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(1),
		A_EndLoop(),
		A_VisibilityOff(),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_TransferToXYZF(x=1, y=63, z=0, direction=EAST),
		A_VisibilityOn()
	]),
	PaletteSet(palette_set=84, row=1, bit_3=True),
	Pause(30),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FixedFCoordOn(),
		A_SequencePlaybackOff(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(6),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_SequenceLoopingOff(),
		A_WalkNortheastPixels(6),
		A_Pause(10),
		A_Pause(20),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3621_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Walk1StepSoutheast(),
		A_StartLoopNTimes(1),
		A_ResetProperties(),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_EndLoop(),
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3622_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3623_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(60),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_Pause(50),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_Walk1StepSoutheast(),
		A_SequenceLoopingOff(),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_Pause(4),
		A_FaceNorthwest(),
		A_Pause(60),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownPixels(10),
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(84),
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
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI3624_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(120),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_Pause(4),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI3625_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(60),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(11)
	]),
	Pause(30),
	RunDialog(dialog_id=DI3626_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(12),
		A_VisibilityOff(),
		A_TransferToXYZF(x=1, y=63, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceNortheast(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3627_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(3),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(4),
		A_Pause(60),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(88),
		A_WalkNortheastSteps(6),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(8)
	]),
	Pause(88),
	RunDialog(dialog_id=DI2530_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3628_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3629_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_SequencePlaybackOff(),
		A_WalkNortheastPixels(6),
		A_WalkSouthwestPixels(6),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3630_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(4),
		A_FaceSoutheast(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3631_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI3632_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_SequenceLoopingOn(),
		A_WalkNortheastPixels(8),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(2)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3633_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, mod_id=0),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Walk1StepNorthwest()
	]),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_7, R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA),
	Pause(30),
	RunDialog(dialog_id=DI3635_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3636_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(1),
		A_SetVRAMPriority(PRIORITY_3),
		A_WalkNortheastSteps(5),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=30, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromSpecificLevel(NPC_8, R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA),
	Pause(30),
	CloseDialog(),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Walk1StepNortheast(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Walk1StepNortheast(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkNortheastSteps(3),
		A_Jmp(["EVENT_3729_non_embedded_action_queue_132"])
	]),
	Jmp(["EVENT_3729_remove_from_current_level_133"]),
	NonEmbeddedActionQueue(required_offset=0x3C4, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_StartLoopNTimes(3),
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(1),
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(1),
		A_EndLoop(),
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_EndLoop(),
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_VisibilityOff(),
		A_ReturnQueue()
	], identifier="EVENT_3729_non_embedded_action_queue_132"),
	RemoveObjectFromCurrentLevel(NPC_9, identifier="EVENT_3729_remove_from_current_level_133"),
	RemoveObjectFromSpecificLevel(NPC_9, R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA),
	Pause(10),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthwestSteps(4)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(60),
	RunDialog(dialog_id=DI3637_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3638_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNorthwestPixels(4),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=6, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=4, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_3729_action_queue_147"),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(2),
		A_TransferToXYZF(x=26, y=80, z=0, direction=EAST)
	]),
	RememberLastObject(identifier="EVENT_3729_remember_last_object_149"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouth()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	SetBit(NIMBUS_BOSS_IN_TOWN_SQUARE),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_3729_fade_in_from_black_async_155"),
	Return()
])
