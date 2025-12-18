# E3638_EMPTY

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
	JmpIfBitSet(SHINY_STONE_TRADED, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3584_ret_0"]),
	SetBit(TEMP_7043_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(1, identifier="EVENT_3638_action_queue_3_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3638_action_queue_3_SUBSCRIPT_pause_1"]),
		A_WalkToXYCoords(x=3, y=17),
		A_FaceEast()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_VisibilityOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=3, y=17, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=2, z=0, direction=EAST),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_VisibilityOn(),
		A_WalkEastPixels(24),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2420_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2421_EMPTY, above_object=NPC_0, closable=False, sync=True, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_SetSequenceSpeed(SLOW),
		A_FaceNorthwest()
	]),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestPixels(12),
		A_SequenceLoopingOff()
	]),
	RunDialog(dialog_id=DI2432_EMPTY, above_object=NPC_0, closable=False, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2422_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2433_EMPTY, above_object=NPC_9, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_WalkSoutheastPixels(14),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceEast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2434_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI2423_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=240, silent=True),
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_Pause(30),
		A_FloatingOff(),
		A_Pause(60),
		A_FloatingOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNortheast(),
		A_Pause(10),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(90),
		A_ResetProperties()
	]),
	Pause(1, identifier="EVENT_3638_pause_31"),
	JmpIfObjectInAir(NPC_9, ["EVENT_3638_pause_31"]),
	StopSound(),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_Pause(60),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2424_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeOutMusicToVolume(duration=2, volume=0),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	FreezeCamera(),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(20),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkWestPixels(10),
		A_WalkSouthwestPixels(12),
		A_JumpToHeight(height=240, silent=True),
		A_Pause(30),
		A_FloatingOff(),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=20, z=20, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_3638_action_queue_49_SUBSCRIPT_pause_7"),
		A_JmpIfObjectInAir(NPC_11, ["EVENT_3638_action_queue_49_SUBSCRIPT_pause_7"]),
		A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(4)
	]),
	SetSyncActionScript(NPC_11, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(1),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(14),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_Pause(48),
		A_FaceNorthwest(),
		A_TransferToXYZF(x=3, y=19, z=0, direction=EAST),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferXYZFPixels(x=248, y=4, z=2, direction=EAST),
		A_VisibilityOn(),
		A_Pause(8),
		A_ResetProperties(),
		A_FloatingOn(),
		A_FaceWest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSouthwestPixels(6)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast(),
		A_JumpToHeight(height=32, silent=True),
		A_Pause(4),
		A_FloatingOff(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(10),
		A_FaceNortheast(),
		A_SequencePlaybackOff(),
		A_TransferToXYZF(x=3, y=20, z=1, direction=EAST)
	]),
	SetSyncActionScript(NPC_6, A0120_EMBEDDED_ROUTINE),
	Pause(60),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOn(),
		A_FloatingOn()
	]),
	StartSyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_Pause(2),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNortheastPixels(14),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(4),
		A_VisibilityOff()
	]),
	PauseActionScript(NPC_11),
	StartAsyncEmbeddedActionScript(target=NPC_11, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_ResetProperties(),
		A_TransferXYZFPixels(x=8, y=248, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(20),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(60),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_JumpToHeight(height=32, silent=True),
		A_Pause(4),
		A_VisibilityOff()
	]),
	PauseActionScript(NPC_6),
	StartAsyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_ResetProperties(),
		A_TransferToXYZF(x=3, y=18, z=1, direction=EAST),
		A_FaceSoutheast(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(28),
		A_VisibilityOn(),
		A_ShiftZDownPixels(8),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(60),
		A_ResetProperties(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(12),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(67),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_Pause(30)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(8),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(39),
		A_VisibilityOn(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(FASTEST),
		A_Pause(60),
		A_FixedFCoordOn()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_StartLoopNTimes(1),
		A_WalkNorthwestPixels(1),
		A_WalkSoutheastPixels(1),
		A_Pause(30),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_Pause(60),
		A_VisibilityOn(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(68),
		A_VisibilityOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(8),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(10),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=19, z=0, direction=EAST),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_VisibilityOn()
	]),
	FadeOutMusicToVolume(duration=2, volume=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkEastPixels(24),
		A_WalkSoutheastPixels(6),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(16),
		A_FaceSoutheast()
	]),
	PlayMusicAtDefaultVolume(M0050_NIMBUSLAND),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI2435_EMPTY, above_object=NPC_9, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNorthwest(),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2436_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2437_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=31, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(50)
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceEast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(4),
	RunDialog(dialog_id=DI2425_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2426_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_Walk1StepSouth(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_Pause(60),
		A_WalkSouthwestSteps(6),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(40),
		A_FaceSouth(),
		A_Pause(60),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(40),
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	Pause(60),
	RunDialog(dialog_id=DI2419_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
	Pause(30),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceNortheast(),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_VisibilityOn(),
		A_WalkNortheastSteps(6),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_EndLoop()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(100),
		A_FaceSouth(),
		A_Pause(64),
		A_FaceSoutheast(),
		A_Pause(64),
		A_FaceEast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(60),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2427_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	UnfreezeCamera(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn(),
		A_Walk1StepNortheast(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_FaceSoutheast(),
		A_Pause(60),
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNorthwest(),
		A_Pause(20),
		A_WalkNorthwestPixels(12),
		A_TransferToXYZF(x=28, y=85, z=0, direction=EAST)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(INVISIBLE_ITEMS_SUMMONED),
	SetBit(SHINY_STONE_TRADED),
	Return()
])
