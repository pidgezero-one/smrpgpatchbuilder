# E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1

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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_622_run_dialog_74"]),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_622_run_dialog_76"]),
	RunDialog(dialog_id=DI1018_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=6, y=62),
		A_FaceNorthwest()
	], identifier="EVENT_622_action_queue_5"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(2)
	]),
	Pause(30),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(32),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(2)
	]),
	Pause(30),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R006_MARRYMORE_INN_2F, face_direction=NORTHEAST, x=15, y=52, z=1, z_add_half_unit=True),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepNortheast(),
		A_WalkNorthwestSteps(4),
		A_FaceSoutheast(),
		A_Pause(50),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_TransferToXYZF(x=15, y=52, z=3, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_WalkNorthwestSteps(2),
		A_FaceSoutheast(),
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(SLOW),
		A_StartLoopNTimes(1),
		A_WalkSoutheastPixels(4),
		A_WalkNorthwestPixels(4),
		A_Pause(20),
		A_EndLoop(),
		A_FixedFCoordOff(),
		A_Pause(74)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(46),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_TransferToXYZF(x=15, y=52, z=3, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_Walk1StepNorthwest(),
		A_Pause(74),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(SLOW),
		A_StartLoopNTimes(1),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_Pause(20),
		A_EndLoop(),
		A_FaceNorthwest(),
		A_FixedFCoordOff(),
		A_Pause(30)
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4)
	]),
	Pause(50),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R011_MARRYMORE_INN_3F, face_direction=NORTHEAST, x=12, y=73, z=1, z_add_half_unit=True),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastSteps(3),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(30),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(30),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceNortheast(),
		A_TransferToXYZF(x=12, y=73, z=3, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(46),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceNortheast(),
		A_TransferToXYZF(x=12, y=73, z=3, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastSteps(2)
	]),
	Pause(52),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=1),
	Pause(70),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNortheastSteps(2)
	]),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R012_MARRYMORE_INN_SUITE_ROOM, face_direction=NORTHEAST, x=3, y=21, z=0),
	SetBit(TEMP_7044_5),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(30),
		A_FaceNortheast(),
		A_TransferToXYZF(x=3, y=22, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(60),
		A_FaceNortheast(),
		A_TransferToXYZF(x=3, y=22, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_Walk1StepEast(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	RememberLastObject(),
	FreezeCamera(),
	Pause(30),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNorthwestSteps(3),
		A_FaceSouth()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(20),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(20),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	PlaySound(sound=SO004_JUMP, channel=6),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkEastSteps(7)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(30),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(30),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(30),
	PlaySound(sound=SO004_JUMP, channel=6),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkWestSteps(5),
		A_WalkSouthwestSteps(2),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(12)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetBit(GUEST_DROPPED_OFF),
	UnfreezeCamera(),
	Return(),
	RunDialog(dialog_id=DI2050_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_622_run_dialog_74"),
	Return(),
	RunDialog(dialog_id=DI2052_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_622_run_dialog_76"),
	Return()
])
