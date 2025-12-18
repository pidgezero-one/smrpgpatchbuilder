# E3153_OLD_CHEST_GRANTER

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
	JmpIfBitSet(PROGRESSIVE_STAR_EXP_ENABLED, ["EVENT_3153_ret_85"]),
	SetBit(PROGRESSIVE_STAR_EXP_ENABLED),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=26, y=106),
		A_FaceNorth(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x00')),
		A_SetVarToConst(Z_COORD_2, 0),
		A_UnknownCommand(bytearray(b'\x99')),
		A_VisibilityOn(),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=False),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouthwest(),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_JumpToHeight(32),
		A_Pause(24),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(24),
		A_JumpToHeight(height=32, silent=True),
		A_Pause(24),
		A_SetSpriteSequence(index=0, sprite_offset=4, looping=False),
		A_Pause(16),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(150),
		A_ResetProperties(),
		A_SequencePlaybackOn(),
		A_FaceNortheast(),
		A_WalkNortheastSteps(2),
		A_SetSpriteSequence(index=1, sprite_offset=4, looping=False),
		A_Pause(48),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=3, sprite_offset=3, looping=False),
		A_Pause(48),
		A_FaceSoutheast(),
		A_StartLoopNTimes(2),
		A_ResetProperties(),
		A_Pause(1, identifier="EVENT_3153_action_queue_5_SUBSCRIPT_pause_16"),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_3153_action_queue_5_SUBSCRIPT_pause_16"]),
		A_ClearBit(TEMP_7043_0),
		A_SetSpriteSequence(index=14, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(20),
		A_FaceSoutheast(),
		A_Pause(310),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_SetBit(TEMP_7043_0),
		A_Pause(32),
		A_FaceSoutheast(),
		A_Pause(8),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SequencePlaybackOff(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkSoutheastPixels(4),
		A_Pause(30),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(6),
		A_WalkSoutheastPixels(2),
		A_FixedFCoordOff(),
		A_Pause(100),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(170),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(200),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_WalkSouthwestPixels(4),
		A_FaceNorthwest(),
		A_Pause(240),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_WalkNorthwestSteps(4),
		A_FaceNortheast(),
		A_Pause(50),
		A_WalkSoutheastSteps(4),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_Pause(16),
		A_WalkNortheastPixels(4),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SequencePlaybackOff(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(400),
		A_FaceSouthwest(),
		A_Pause(15),
		A_SequencePlaybackOn(),
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestSteps(3),
		A_FaceNorthwest(),
		A_SetBit(TEMP_7043_0),
		A_Pause(15),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(220),
		A_FaceSouthwest(),
		A_Pause(35),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(240),
		A_FaceSouthwest(),
		A_Pause(35),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_WalkSouthwestPixels(4),
		A_FaceSoutheast(),
		A_Pause(40),
		A_FaceSouthwest(),
		A_Pause(25),
		A_FaceNorthwest(),
		A_Pause(80),
		A_WalkNortheastPixels(4),
		A_Pause(95),
		A_FaceSouthwest(),
		A_Pause(15),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(300),
		A_SequencePlaybackOn(),
		A_Walk1StepSouthwest(),
		A_WalkNorthwestSteps(4),
		A_FaceNortheast(),
		A_Pause(24),
		A_WalkSoutheastSteps(4),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_SequencePlaybackOff(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_Pause(280),
		A_FaceSouthwest(),
		A_Pause(60),
		A_SequencePlaybackOn(),
		A_WalkNorthwestSteps(2),
		A_WalkNortheastSteps(3),
		A_FaceNorthwest(),
		A_SetBit(TEMP_7043_0),
		A_Pause(16),
		A_WalkSouthwestSteps(3),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkEastPixels(6),
		A_Pause(110),
		A_FaceNorthwest(),
		A_Pause(15),
		A_FaceSouthwest(),
		A_Pause(35),
		A_FaceNorthwest(),
		A_Pause(8),
		A_WalkWestPixels(6),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(160),
		A_FaceSouthwest(),
		A_Pause(16),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(180),
		A_FaceSouthwest(),
		A_Pause(16),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(200),
		A_SequencePlaybackOn(),
		A_Walk1StepSouthwest(),
		A_WalkNorthwestSteps(4),
		A_FaceNortheast(),
		A_Pause(24),
		A_WalkSoutheastSteps(4),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_SequencePlaybackOff(),
		A_Pause(1)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=21, y=77)
	]),
	RunDialog(dialog_id=DI1600_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(64),
		A_Pause(20),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI1601_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ClearBit(TEMP_7043_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_CreatePacketAtObjectCoords(packet=P027_UNUSED, target_npc=NPC_6, destinations=["EVENT_3153_action_queue_27_SUBSCRIPT_pause_3"]),
		A_Pause(1, identifier="EVENT_3153_action_queue_27_SUBSCRIPT_pause_3"),
		A_VisibilityOff(),
		A_PlaySound(sound=SO101_TERRAPIN_ATTACK, channel=4),
		A_Pause(1, identifier="EVENT_3153_action_queue_27_SUBSCRIPT_pause_6"),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_3153_action_queue_27_SUBSCRIPT_pause_6"]),
		A_VisibilityOn(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	RunDialog(dialog_id=DI1602_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ClearBit(TEMP_7043_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Walk1StepNorthwest(),
		A_CreatePacketAtObjectCoords(packet=P026_UNUSED, target_npc=NPC_11, destinations=["EVENT_3153_action_queue_31_SUBSCRIPT_pause_2"]),
		A_Pause(1, identifier="EVENT_3153_action_queue_31_SUBSCRIPT_pause_2"),
		A_VisibilityOff(),
		A_Pause(1, identifier="EVENT_3153_action_queue_31_SUBSCRIPT_pause_4"),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_3153_action_queue_31_SUBSCRIPT_pause_4"]),
		A_VisibilityOn(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	RunDialog(dialog_id=DI1603_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_FaceNortheast(),
		A_PlaySound(sound=SO045_GOOMBA_TAUNT, channel=4)
	]),
	TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L4, BACKGROUND], red=160, green=32, blue=32, speed=5, bit_15=True),
	Pause(8),
	TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L4, BACKGROUND], red=0, green=0, blue=0, speed=5),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(64),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	ResetPrioritySet(),
	RunDialog(dialog_id=DI1604_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=1, looping=False),
		A_Pause(96),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_Pause(120)
	]),
	RunDialog(dialog_id=DI1605_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_SequencePlaybackOn(),
		A_Pause(48),
		A_FaceNortheast(),
		A_PlaySound(sound=SO057_FINGER_SNAP, channel=4),
		A_SetSpriteSequence(index=4, sprite_offset=1, looping=False),
		A_Pause(48),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_Pause(16),
		A_SetPriority(3),
		A_WalkNortheastSteps(9),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_PlaySound(sound=SO046_CRUMBLING_NOISE, channel=4),
		A_Pause(60),
		A_SetPriority(3),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(9),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_SetPriority(3),
		A_WalkNorthwestSteps(4),
		A_WalkNortheastSteps(9),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_SetPriority(3),
		A_WalkNorthwestSteps(5),
		A_WalkNortheastSteps(9),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_SetPriority(3),
		A_WalkNorthwestSteps(6),
		A_WalkNortheastSteps(9),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_SetPriority(3),
		A_WalkNorthwestSteps(7),
		A_WalkNortheastSteps(9),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(250),
		A_SetPriority(3),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(6),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(250),
		A_SetPriority(3),
		A_WalkNorthwestSteps(4),
		A_WalkNortheastSteps(6),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(250),
		A_SetPriority(3),
		A_WalkNorthwestSteps(5),
		A_WalkNortheastSteps(6),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(250),
		A_SetPriority(3),
		A_WalkNorthwestSteps(6),
		A_WalkNortheastSteps(6),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(250),
		A_SetPriority(3),
		A_WalkNorthwestSteps(7),
		A_WalkNortheastSteps(6),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(300),
		A_SetPriority(3),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(5),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(300),
		A_SetPriority(3),
		A_WalkNorthwestSteps(4),
		A_WalkNortheastSteps(5),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(300),
		A_SetPriority(3),
		A_WalkNorthwestSteps(5),
		A_WalkNortheastSteps(4),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(300),
		A_SetPriority(3),
		A_WalkNorthwestSteps(6),
		A_WalkNortheastSteps(4),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SequencePlaybackOn(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_Pause(300),
		A_SetPriority(3),
		A_WalkNorthwestSteps(7),
		A_WalkNortheastSteps(3),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(380),
		A_WalkSouthSteps(8)
	]),
	FadeOutSoundToVolume(duration=8, volume=0),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_FaceSouthwest(),
		A_Pause(100),
		A_FaceSoutheast(),
		A_Pause(20),
		A_SetSpriteSequence(index=2, sprite_offset=5, looping=False),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(1),
		A_SetBit(TEMP_7043_1)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(20)
	]),
	RunDialog(dialog_id=DI1606_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1, identifier="EVENT_3153_pause_65"),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3153_pause_65"]),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_Walk1StepSouthwest(),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4])
	]),
	RemoveObjectFromSpecificLevel(NPC_0, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_1, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_2, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_3, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_4, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_5, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_6, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_7, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_8, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_9, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_10, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_11, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_12, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_13, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_14, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_15, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	RemoveObjectFromSpecificLevel(NPC_16, R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED),
	Return(identifier="EVENT_3153_ret_85")
])
