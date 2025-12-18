# E0720_OLD_STAR_PIECE_SCRIPT

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
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=14, y=33, z=2, direction=EAST),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastSteps(4)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(4),
		A_Pause(16)
	]),
	FadeInFromBlack(sync=True),
	RememberLastObject(),
	RunDialog(dialog_id=DI2252_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=13, y=35, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_Pause(16),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(SLOW),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(8),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_6, A0381_EMPTY),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(50),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Walk1StepSoutheast(),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(50),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(50),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(50),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Walk1StepNorthwest(),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(50),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_Pause(10),
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepNorthwest(),
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(6),
		A_WalkSouthwestPixels(4),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkSouthwestPixels(12),
		A_Walk1StepSouthwest(),
		A_FaceSoutheast(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceNorthwest(),
		A_SetVRAMPriority(PRIORITY_3)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2253_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_0, A0017_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI2254_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetBit(TEMP_7043_2),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(10)
	]),
	RunDialog(dialog_id=DI2255_MARRYMORE_SHITPOST, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	Pause(60),
	SetSyncActionScript(NPC_1, A0382_EMPTY),
	SetSyncActionScript(NPC_2, A0382_EMPTY),
	SetSyncActionScript(NPC_3, A0382_EMPTY),
	SetSyncActionScript(NPC_4, A0382_EMPTY),
	SetSyncActionScript(NPC_5, A0382_EMPTY),
	SetAsyncActionScript(NPC_6, A0382_EMPTY),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2256_BANDITS_WAY_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	ClearBit(TEMP_7043_2),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(4),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(30),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(10),
		A_EndLoop(),
		A_Pause(30),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(40),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2257_FOREST_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(60),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkNortheastSteps(3),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(3),
		A_FaceSouthwest(),
		A_Pause(24),
		A_WalkNorthwestSteps(2),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(4),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(3),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(9),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(4),
		A_WalkToXYCoords(x=16, y=30),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(32),
		A_WalkNortheastSteps(4)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkSouthwestPixels(8),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2258_PIPE_VAULT_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2259_BOOSTER_TOWER_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouthwest()
	]),
	RunDialog(dialog_id=DI2260_MARRYMORE_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	ReturnFD(),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkEastPixels(12),
		A_WalkNortheastPixels(4),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=16, y=30, z=4, direction=EAST),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkWestPixels(6),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(8),
		A_WalkNortheastPixels(2),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_VisibilityOff(),
		A_Pause(12),
		A_TransferToXYZF(x=16, y=30, z=4, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_FaceSouthwest(),
		A_WalkSouthPixels(12),
		A_WalkSouthwestPixels(4),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_VisibilityOff(),
		A_Pause(8),
		A_TransferToXYZF(x=16, y=30, z=4, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouthwest(),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkWestPixels(10),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOn(),
		A_WalkNortheastPixels(8)
	]),
	RememberLastObject(),
	Pause(60),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2261_SEA_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast(),
		A_Pause(60),
		A_FaceSouthwest(),
		A_Pause(60),
		A_StartLoopNTimes(1),
		A_FaceSoutheast(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(10),
		A_EndLoop(),
		A_Pause(60),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	RunDialog(dialog_id=DI2262_SEASIDE_TOWN_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(36),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2263_TEMPLE_OPEN, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_0, A0383_EMPTY),
	SetSyncActionScript(NPC_6, A0785_EMPTY),
	SetSyncActionScript(NPC_1, A0787_PLAYER_COWERS_IN_CORNER),
	SetSyncActionScript(NPC_2, A0788_EMPTY),
	SetSyncActionScript(NPC_3, A0789_EMPTY),
	SetSyncActionScript(NPC_4, A0786_EMPTY),
	SetSyncActionScript(NPC_5, A0784_EMPTY),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceNorth()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(30),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2216_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2217_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties()
	]),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_6),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn()
	]),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(2)
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(2),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(2),
		A_FaceNorthwest()
	]),
	StartSyncEmbeddedActionScript(target=NPC_4, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(2)
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_WalkNorthwestSteps(1)
	]),
	StartSyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_SetPriority(3),
		A_WalkSouthwestSteps(2),
		A_WalkSoutheastSteps(1)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_11, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2204_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8)
	]),
	RunDialog(dialog_id=DI2206_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2203_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(60),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(40),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(12),
		A_WalkNortheastPixels(8),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=2, sprite_offset=5, is_sequence=True, looping=True),
		A_Pause(28),
		A_SetSpriteSequence(index=5, sprite_offset=5, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_11, subscript=[
		A_FaceNorthwest(),
		A_Pause(60),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_Pause(30),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(60),
		A_FaceSoutheast(),
		A_Pause(20)
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_Pause(40),
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepEast(),
		A_Walk1StepNorth(),
		A_FixedFCoordOff(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouthwest(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(4),
		A_FaceNorth()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2207_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	FreezeCamera(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(40),
		A_ShadowOn(),
		A_JumpToHeight(240),
		A_Pause(30),
		A_FloatingOff(),
		A_TransferToXYZF(x=16, y=30, z=25, direction=EAST),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=10, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(50),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2208_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=11, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=14, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_SequencePlaybackOn(),
		A_VisibilityOff(),
		A_Pause(38),
		A_TransferToXYZF(x=16, y=31, z=6, direction=EAST),
		A_TransferXYZFPixels(x=252, y=254, z=4, direction=EAST),
		A_VisibilityOn(),
		A_JumpToHeight(height=140, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestPixels(2),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkNorthwestPixels(10),
		A_FloatingOff(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2209_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepEast(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=1, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2210_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_Pause(30),
		A_FloatingOff(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownPixels(1),
		A_StartLoopNTimes(7),
		A_ShiftZUpPixels(2),
		A_ShiftZDownPixels(2),
		A_EndLoop()
	]),
	Pause(17),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(32),
		A_VisibilityOff()
	]),
	RunDialog(dialog_id=DI2211_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(18),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownPixels(1),
		A_StartLoopNTimes(7),
		A_ShiftZUpPixels(2),
		A_ShiftZDownPixels(2),
		A_EndLoop(),
		A_ShiftZUpPixels(1),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_Pause(4)
	]),
	RememberLastObject(),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(10),
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(8),
		A_FixedFCoordOn(),
		A_SequencePlaybackOn(),
		A_JumpToHeight(height=92, silent=True),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FloatingOff(),
		A_Pause(50),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(6),
		A_FaceSouthwest(),
		A_ResetProperties(),
		A_Pause(4),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2212_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2213_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(8),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2219_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(4),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2218_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(60),
		A_FaceNortheast()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=96, silent=True)
	]),
	RunDialog(dialog_id=DI2214_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(96),
		A_WalkNortheastSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(4)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(20),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Walk1StepSouth(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_FaceSouthwest(),
		A_Walk1StepWest(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4),
		A_FaceSoutheast(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4),
		A_FaceSoutheast(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2220_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(12),
		A_FaceEast()
	]),
	Pause(20),
	RunDialog(dialog_id=DI2222_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_WalkNortheastPixels(6)
	]),
	RunDialog(dialog_id=DI2223_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2267_MONSTRO_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	Pause(40),
	RunDialog(dialog_id=DI2290_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(10),
		A_WalkSouthwestPixels(6),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(40),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2221_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2264_KEEP_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2265_GATE_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(6),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2266_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_WalkSouthwestPixels(6)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2267_MONSTRO_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2277_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(10),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	Pause(40),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(80),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=16, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(50),
		A_FaceEast(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2268_VOLCANO_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_10, subscript=[
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(24),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2269_MINES_OPEN, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(24),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2270_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2278_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2279_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2280_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2281_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2282_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2283_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2284_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2285_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2271_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(14),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(6),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(6),
		A_ResetProperties()
	]),
	Pause(10),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2272_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2273_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2286_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2287_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2288_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2274_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2275_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepWest(),
		A_FixedFCoordOff(),
		A_Walk1StepSouthwest(),
		A_SequenceLoopingOff(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouth(),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_FaceEast(),
		A_Pause(16),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_FaceNorthwest(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_Pause(16),
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2276_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueSync(target=NPC_11, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_EndLoop(),
		A_ResetProperties(),
		A_StopSound()
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(6),
		A_VisibilityOff()
	]),
	Pause(20),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(20),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceSoutheast(),
		A_Pause(20),
		A_FaceSouthwest()
	]),
	Pause(20),
	SetSyncActionScript(NPC_1, A0626_EMPTY),
	SetSyncActionScript(NPC_2, A0626_EMPTY),
	SetSyncActionScript(NPC_3, A0626_EMPTY),
	SetSyncActionScript(NPC_4, A0626_EMPTY),
	SetSyncActionScript(NPC_5, A0626_EMPTY),
	SetSyncActionScript(NPC_6, A0626_EMPTY),
	RememberLastObject(),
	RunDialog(dialog_id=DI2291_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(6),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(6),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(6),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Walk1StepNortheast()
	]),
	SetSyncActionScript(NPC_1, A0625_EMPTY),
	SetSyncActionScript(NPC_2, A0625_EMPTY),
	SetSyncActionScript(NPC_3, A0627_EMPTY),
	SetSyncActionScript(NPC_4, A0627_EMPTY),
	SetSyncActionScript(NPC_5, A0627_EMPTY),
	SetSyncActionScript(NPC_6, A0625_EMPTY),
	RememberLastObject(),
	RunDialog(dialog_id=DI2292_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2293_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI2294_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(8),
		A_FaceSouthwest(),
		A_Pause(30),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest(),
		A_Pause(30),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_Pause(30),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_Pause(60),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2295_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	Pause(10),
	SetSyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueSync(target=NPC_11, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_ResetProperties(),
		A_Pause(5),
		A_EndLoop()
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSouth()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkEastPixels(24),
		A_TransferToXYZF(x=21, y=118, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkWestPixels(24),
		A_TransferToXYZF(x=21, y=120, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x80\xff\x80\xff')),
		A_Pause(24),
		A_BPL262728(),
		A_TransferToXYZF(x=21, y=119, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(4)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSoutheastPixels(4)
	]),
	RememberLastObject(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(UNUSED_705D_1),
	ReturnFD(),
	Store01To0248(),
	CharacterLeavesParty(TOADSTOOL),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	RunDialog(dialog_id=DI2301_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	UnfreezeCamera(),
	Return()
])
