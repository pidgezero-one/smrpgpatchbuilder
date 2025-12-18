# E3738_EMPTY

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
	EnterArea(room_id=R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, face_direction=NORTHEAST, x=2, y=62, z=0),
	SetSyncActionScript(NPC_0, A0262_EMPTY),
	SetSyncActionScript(NPC_1, A0263_FIX_F_COORD),
	SetSyncActionScript(NPC_2, A0262_EMPTY),
	SetSyncActionScript(NPC_3, A0263_FIX_F_COORD),
	SetBit(BUCKET_PRIZE_GRANT_NO_WARP),
	FadeInFromBlack(sync=True, duration=60),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(5),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(6)
	]),
	RememberLastObject(),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SequenceLoopingOff()
	]),
	Pause(30),
	RunDialog(dialog_id=DI3683_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3684_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNorthwestPixels(14),
		A_StartLoopNTimes(5),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=5, y=56, z=2, direction=EAST),
		A_TransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_Walk1StepSouth(),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(2),
		A_VisibilityOff(),
		A_TransferToXYZF(x=5, y=56, z=2, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=55, z=2, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_Pause(10),
		A_VisibilityOn(),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3685_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3679_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_WalkNortheastPixels(8)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3686_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3687_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FloatingOff(),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(4),
		A_Pause(8),
		A_ShiftZUpPixels(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkWestPixels(20),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3688_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3689_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepNortheast(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3711_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkNorthwestPixels(8),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3712_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3713_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3714_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	SetAsyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	RunDialog(dialog_id=DI3715_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3716_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3717_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(10),
	StartLoopNTimes(1),
	Pause(1),
	RunEventAsSubroutine(E0275_UNKNOWN),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3738_action_queue_93"]),
	EndLoop(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties(),
		A_JumpToHeight(160),
		A_Pause(12),
		A_FloatingOff(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(24),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_FloatingOn()
	], identifier="EVENT_3738_action_queue_93"),
	Pause(1, identifier="EVENT_3738_pause_94"),
	JmpIfMarioInAir(["EVENT_3738_pause_94"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_Pause(60),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(90),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_Pause(10),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Pause(10),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties()
	]),
	RememberLastObject(),
	SetAsyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_StartLoopNTimes(1),
		A_FaceSoutheast(),
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(2),
		A_EndLoop()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3690_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3691_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(10),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(12),
		A_ResetProperties()
	]),
	Pause(30),
	SetAsyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3692_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(8)
	]),
	RunDialog(dialog_id=DI3693_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3694_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3695_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3696_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3697_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3698_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3699_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True)
	]),
	Pause(22),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties()
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3700_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3701_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3702_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestPixels(4)
	]),
	RunDialog(dialog_id=DI3703_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(4),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3704_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(38),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3720_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(4),
		A_WalkNortheastPixels(10),
		A_TransferToXYZF(x=21, y=118, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(4),
		A_WalkNortheastPixels(8),
		A_TransferToXYZF(x=21, y=118, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(4),
		A_WalkNorthPixels(12),
		A_TransferToXYZF(x=21, y=118, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkSouthwestPixels(4),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Walk1StepNorthwest(),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(4),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	Pause(30),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_WalkNorthwestPixels(12),
		A_TransferToXYZF(x=21, y=118, z=0, direction=EAST)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW)
	]),
	UnfreezeCamera(),
	RemoveObjectFromSpecificLevel(NPC_7, R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA),
	Return()
])
