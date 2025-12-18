# E1618_EMPTY

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
	Pause(1, identifier="EVENT_1618_pause_0"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 7424),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1618_pause_0"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 7936),
	JmpIfComparisonResultIsLesser(["EVENT_1618_pause_0"]),
	EnableControlsUntilReturn([]),
	JmpIfBitClear(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, ["EVENT_1618_set_bit_10"]),
	Return(),
	SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL, identifier="EVENT_1618_set_bit_10"),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	Pause(1, identifier="EVENT_1618_pause_12"),
	JmpIfMarioInAir(["EVENT_1618_pause_12"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceSouth(),
		A_Pause(20),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_FixedFCoordOff(),
		A_FaceSouthwest7D(arg=0x1A)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=23, y=16, height=0)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_StartLoopNTimes(1),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, looping=False),
		A_Walk1StepSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
		A_Walk1StepSoutheast(),
		A_Pause(10),
		A_Walk1StepNortheast(),
		A_Pause(10),
		A_EndLoop(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=11, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(80),
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48),
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=0, sprite_offset=3, looping=False),
		A_Pause(80),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(30),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_JumpToHeight(64),
		A_Pause(24)
	]),
	FreezeAllNPCsUntilReturn(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_JumpToHeight(64),
		A_Pause(24),
		A_ResetProperties()
	]),
	StartSyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=27, y=42),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=26, y=44),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_8, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=27, y=43),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=26, y=45),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=28, y=44),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartAsyncEmbeddedActionScript(target=NPC_4, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=27, y=46),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_Pause(1, identifier="EVENT_1618_action_queue_26_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_6, ["EVENT_1618_action_queue_26_SUBSCRIPT_pause_2"]),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(2)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_WalkSouthwestSteps(2),
		A_WalkSoutheastSteps(2),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
		A_Pause(100)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_Walk1StepNorthwest(),
		A_FaceNortheast(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI1092_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Pause(16),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI1093_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI1094_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(FAST),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_WalkSouthwestSteps(5),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(64),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=3, looping=False),
		A_WalkSouthwestSteps(4),
		A_WalkSoutheastSteps(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(64),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(4),
		A_WalkSoutheastSteps(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(64),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(4),
		A_WalkSouthwestSteps(4),
		A_WalkSoutheastSteps(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(80),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestSteps(6),
		A_WalkSoutheastSteps(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(80),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(6),
		A_WalkSoutheastSteps(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(80),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(4),
		A_WalkSouthwestSteps(6),
		A_WalkSoutheastSteps(4),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(48),
	StartLoopNTimes(17),
	PlaySoundBalance(sound=SO046_CRUMBLING_NOISE, balance=130),
	Pause(16),
	EndLoop(),
	FadeOutSoundToVolume(duration=0, volume=96),
	StartLoopNTimes(1),
	PlaySoundBalance(sound=SO046_CRUMBLING_NOISE, balance=110),
	Pause(16),
	EndLoop(),
	FadeOutSoundToVolume(duration=0, volume=80),
	StartLoopNTimes(1),
	PlaySoundBalance(sound=SO046_CRUMBLING_NOISE, balance=90),
	Pause(16),
	EndLoop(),
	FadeOutSoundToVolume(duration=0, volume=64),
	StartLoopNTimes(1),
	PlaySoundBalance(sound=SO046_CRUMBLING_NOISE, balance=70),
	Pause(16),
	EndLoop(),
	FadeOutSoundToVolume(duration=0, volume=48),
	StartLoopNTimes(1),
	PlaySoundBalance(sound=SO046_CRUMBLING_NOISE, balance=50),
	Pause(16),
	EndLoop(),
	FadeOutSoundToVolume(duration=0, volume=32),
	StartLoopNTimes(1),
	PlaySoundBalance(sound=SO046_CRUMBLING_NOISE, balance=30),
	Pause(16),
	EndLoop(),
	StopSound(),
	FadeOutSoundToVolume(duration=0, volume=127),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
