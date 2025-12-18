# E1652_EMPTY

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
	ApplySolidityModToLevel(permanent=True, room_id=R108_MOLEVILLE_OUTSIDE, mod_id=1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepSouth(),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=False),
	SummonObjectToCurrentLevel(NPC_8),
	SummonObjectToCurrentLevel(NPC_9),
	SummonObjectToCurrentLevel(NPC_10),
	SummonObjectToCurrentLevel(NPC_11),
	RunDialog(dialog_id=DI1166_TEMPLE_BLOCKED_PIPE_HINT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_Pause(120),
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(8),
		A_EndLoop(),
		A_Pause(30),
		A_FaceWest(),
		A_Pause(30),
		A_StartLoopNTimes(2),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(4),
		A_EndLoop(),
		A_Pause(80),
		A_StartLoopNTimes(3),
		A_Pause(4),
		A_TurnClockwise45DegreesNTimes(1),
		A_EndLoop(),
		A_Pause(40),
		A_FaceWest()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetPriority(3),
		A_ShadowOff(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(9),
		A_WalkWestSteps(4)
	]),
	Pause(140),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(6),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(108),
		A_WalkNorthwestSteps(5),
		A_StartLoopNTimes(3),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_WalkSouthwestSteps(6)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(16),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(6),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(108),
		A_WalkNorthwestSteps(4),
		A_WalkNorthwestPixels(8),
		A_FixedFCoordOn(),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_StartLoopNTimes(3),
		A_WalkEastPixels(4),
		A_WalkWestPixels(4),
		A_EndLoop(),
		A_FaceNorthwest(),
		A_FixedFCoordOff(),
		A_WalkNorthwestPixels(8),
		A_WalkSouthwestSteps(6)
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_Pause(16),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(2),
		A_StartLoopNTimes(4),
		A_Walk1StepNorthwest(),
		A_ShiftZUpPixels(2),
		A_ShiftZDownPixels(2),
		A_EndLoop(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(NORMAL),
		A_Walk1StepSoutheast(),
		A_StartLoopNTimes(1),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(88),
		A_Pause(30),
		A_EndLoop(),
		A_SetAllSpeeds(FAST),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(108),
		A_WalkNorthwestSteps(5),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_Pause(5),
		A_FaceSoutheast(),
		A_Pause(5),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(1),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(6)
	]),
	SetSyncActionScript(NPC_11, A0654_EMPTY),
	Pause(4),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_Pause(140),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(72),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=8, looping=True),
		A_Pause(40),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_TransferToXYZF(x=13, y=77, z=8, direction=EAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkNortheastSteps(9),
		A_Pause(20),
		A_StartLoopNTimes(2),
		A_WalkSoutheastPixels(4),
		A_Pause(8),
		A_WalkNorthwestPixels(4),
		A_Pause(8),
		A_EndLoop(),
		A_SetVRAMPriority(PRIORITY_3),
		A_ShiftZDownPixels(17),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Pause(170),
	ActionQueueSync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=13, y=71, z=4, direction=EAST),
		A_SetAllSpeeds(FAST),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(4),
		A_WalkNortheastSteps(4),
		A_FaceNorthwest(),
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_TransferToXYZF(x=13, y=71, z=4, direction=EAST),
		A_Pause(16),
		A_SetAllSpeeds(FAST),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(3),
		A_WalkNortheastSteps(3),
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=13, y=71, z=4, direction=EAST),
		A_SetAllSpeeds(FAST),
		A_WalkNortheastSteps(2),
		A_StartLoopNTimes(7),
		A_WalkNortheastPixels(8),
		A_ShiftZUpPixels(2),
		A_ShiftZDownPixels(2),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_WalkSoutheastPixels(8),
		A_ShiftZUpPixels(2),
		A_ShiftZDownPixels(2),
		A_EndLoop(),
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOn()
	]),
	JmpToSubroutine(["EVENT_1652_set_var_to_const_47"]),
	RunDialog(dialog_id=DI1167_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_1652_set_var_to_const_47"]),
	RunDialog(dialog_id=DI1168_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_1652_set_var_to_const_47"]),
	RunDialog(dialog_id=DI1169_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_11, A0160_SEQUENCE_LOOPING_ON),
	Pause(4),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_AddZCoord1Step()
	]),
	JmpToSubroutine(["EVENT_1652_set_var_to_const_47"]),
	RunDialog(dialog_id=DI1170_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestSteps(2),
		A_WalkWestSteps(4),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(14),
		A_ResetProperties(),
		A_FaceWest(),
		A_Pause(4),
		A_FaceNorthwest(),
		A_Pause(70),
		A_FaceWest()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceNorthwest(),
		A_Pause(44),
		A_SetAllSpeeds(FAST),
		A_StartLoopNTimes(2),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_FloatingOn(),
		A_WalkSouthwestSteps(10),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceNorthwest(),
		A_Pause(54),
		A_SetAllSpeeds(FAST),
		A_StartLoopNTimes(2),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_FloatingOn(),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceSouthwest(),
		A_Pause(20),
		A_FaceNorthwest(),
		A_Pause(70),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_SetAllSpeeds(FAST),
		A_StartLoopNTimes(2),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(4),
		A_EndLoop(),
		A_FloatingOn(),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R108_MOLEVILLE_OUTSIDE, mod_id=0),
	Pause(1),
	ClearBit(KEEP_GATED_BY_VOLCANO),
	SetBit(MAP_DIRECTIONAL_MOLEVILLE_BOOSTER_PASS),
	SetBit(MAP_MOLEVILLE),
	SetBit(MAP_BOOSTER_PASS),
	SetBit(MAP_BOOSTER_TOWER),
	Return(),
	SetVarToConst(ACTIVE_NPC, 28, identifier="EVENT_1652_set_var_to_const_47"),
	StartLoopNTimes(2),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(72)
	]),
	Pause(10),
	Inc(ACTIVE_NPC),
	EndLoop(),
	Return()
])
