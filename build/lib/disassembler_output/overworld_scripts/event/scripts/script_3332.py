# E3332_VOLCANO_1ST_BOSS_PATH_ROOM_LOADER

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
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	JmpIfBitSet(UNUSED_707E_1, ["EVENT_3332_jmp_if_bit_clear_143"]),
	StopMusicFDA2(),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=18, y=102),
		A_Walk1StepNortheast()
	]),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8e\x19\x08\xff')),
	Pause(60),
	SetSyncActionScript(NPC_1, A0015_DO_NOTHING),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShadowOn(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(1),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShadowOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00@\x00@\x00\x01\xe8\xffp\xfe\x80')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00 \x00\x01\xf4\xffp\xfe\x80")),
		A_Pause(682),
		A_BPL262728()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpSteps(2)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(16),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	PauseActionScript(NPC_0),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	SetSyncActionScript(NPC_1, A0120_EMBEDDED_ROUTINE),
	Pause(120),
	SetSyncActionScript(NPC_1, A0015_DO_NOTHING),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(10),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(6),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(1),
		A_Pause(248)
	]),
	Pause(77),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_SetSequenceSpeed(FASTEST),
		A_Pause(90)
	]),
	Pause(90),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_ShiftZDownSteps(4),
		A_SetBit(TEMP_7043_1),
		A_CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=DUMMY_0X07, destinations=["EVENT_3332_start_embedded_action_script_24_SUBSCRIPT_jump_to_height_silent_5"]),
		A_JumpToHeight(height=144, silent=True, identifier="EVENT_3332_start_embedded_action_script_24_SUBSCRIPT_jump_to_height_silent_5"),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkNorthwestSteps(4),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False, mirror_sprite=True),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(14),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Pause(120),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(12),
		A_ResetProperties(),
		A_FaceWest(),
		A_Pause(12),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(24),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetBit(TEMP_7043_2)
	]),
	Pause(1, identifier="EVENT_3332_pause_27"),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3332_pause_27"]),
	StopMusicFDA2(),
	Pause(8),
	SummonObjectToCurrentLevel(NPC_2),
	Pause(1, identifier="EVENT_3332_pause_32"),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_3332_pause_32"]),
	UnknownCommand(bytearray(b'\xfd\x8e2\x08\xff')),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(128),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(15),
		A_WalkSoutheastPixels(2),
		A_WalkNorthwestPixels(2),
		A_EndLoop(),
		A_Pause(20),
		A_FaceNorthwest(),
		A_SetAllSpeeds(NORMAL),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(6),
		A_StartLoopNTimes(3),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_EndLoop()
	]),
	PlayMusicAtDefaultVolume(M0015_HERE_SSOMEWEAPONS),
	SetBit(TEMP_7044_0),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(128),
		A_FloatingOn(),
		A_WalkSoutheastSteps(2),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	CreatePacketAtObjectCoords(packet=P040_UNUSED, target_npc=NPC_2, destinations=["EVENT_3332_pause_41"]),
	Pause(1, identifier="EVENT_3332_pause_41"),
	RemoveObjectFromCurrentLevel(NPC_2),
	Pause(48),
	PlaySound(sound=SO120_METAL_BOLT_STRIKE, channel=4),
	StartLoopNTimes(3),
	ScreenFlashesWithColour(RED),
	Pause(4),
	EndLoop(),
	Pause(16),
	ClearBit(TEMP_7044_6),
	SummonObjectToCurrentLevel(NPC_2),
	RunDialog(dialog_id=DI1808_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(2)
	]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_3, destinations=["EVENT_3332_pause_55"]),
	Pause(8, identifier="EVENT_3332_pause_55"),
	SummonObjectToCurrentLevel(NPC_3),
	Pause(20),
	CreatePacketAtObjectCoords(packet=P044_UNUSED, target_npc=NPC_3, destinations=["EVENT_3332_pause_59"]),
	Pause(1, identifier="EVENT_3332_pause_59"),
	RemoveObjectFromCurrentLevel(NPC_3),
	Pause(48),
	PlaySound(sound=SO120_METAL_BOLT_STRIKE, channel=4),
	StartLoopNTimes(3),
	ScreenFlashesWithColour(GREEN),
	Pause(4),
	EndLoop(),
	Pause(16),
	ClearBit(TEMP_7044_6),
	SummonObjectToCurrentLevel(NPC_3),
	RunDialog(dialog_id=DI1809_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthwestSteps(4)
	]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_4, destinations=["EVENT_3332_pause_73"]),
	Pause(8, identifier="EVENT_3332_pause_73"),
	SummonObjectToCurrentLevel(NPC_4),
	Pause(20),
	CreatePacketAtObjectCoords(packet=P043_UNUSED, target_npc=NPC_4, destinations=["EVENT_3332_pause_77"]),
	Pause(1, identifier="EVENT_3332_pause_77"),
	RemoveObjectFromCurrentLevel(NPC_4),
	Pause(48),
	PlaySound(sound=SO120_METAL_BOLT_STRIKE, channel=4),
	StartLoopNTimes(3),
	ScreenFlashesWithColour(YELLOW),
	Pause(4),
	EndLoop(),
	Pause(16),
	ClearBit(TEMP_7044_6),
	SummonObjectToCurrentLevel(NPC_4),
	RunDialog(dialog_id=DI1810_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(3)
	]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_5, destinations=["EVENT_3332_pause_91"]),
	Pause(8, identifier="EVENT_3332_pause_91"),
	SummonObjectToCurrentLevel(NPC_5),
	Pause(20),
	CreatePacketAtObjectCoords(packet=P042_UNUSED, target_npc=NPC_5, destinations=["EVENT_3332_pause_95"]),
	Pause(1, identifier="EVENT_3332_pause_95"),
	RemoveObjectFromCurrentLevel(NPC_5),
	Pause(48),
	PlaySound(sound=SO120_METAL_BOLT_STRIKE, channel=4),
	StartLoopNTimes(3),
	ScreenFlashesWithColour(PINK),
	Pause(4),
	EndLoop(),
	Pause(16),
	ClearBit(TEMP_7044_6),
	SummonObjectToCurrentLevel(NPC_5),
	RunDialog(dialog_id=DI1811_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(2),
		A_WalkNorthSteps(2)
	]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_6, destinations=["EVENT_3332_pause_109"]),
	Pause(8, identifier="EVENT_3332_pause_109"),
	SummonObjectToCurrentLevel(NPC_6),
	Pause(20),
	CreatePacketAtObjectCoords(packet=P041_UNUSED, target_npc=NPC_6, destinations=["EVENT_3332_pause_113"]),
	Pause(1, identifier="EVENT_3332_pause_113"),
	RemoveObjectFromCurrentLevel(NPC_6),
	Pause(48),
	PlaySound(sound=SO120_METAL_BOLT_STRIKE, channel=4),
	StartLoopNTimes(3),
	ScreenFlashesWithColour(WHITE),
	Pause(4),
	EndLoop(),
	Pause(16),
	ClearBit(TEMP_7044_6),
	SummonObjectToCurrentLevel(NPC_6),
	RunDialog(dialog_id=DI1812_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthSteps(14),
		A_SetWalkingSpeed(NORMAL)
	]),
	PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_6),
	PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_5),
	PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_4),
	PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_3),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FaceNorthwest(),
		A_Pause(8),
		A_JumpToHeight(height=48, silent=True),
		A_Walk1StepNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=144, silent=True),
		A_Pause(16),
		A_CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_1, destinations=["EVENT_3332_action_queue_139_SUBSCRIPT_visibility_off_3"]),
		A_VisibilityOff(identifier="EVENT_3332_action_queue_139_SUBSCRIPT_visibility_off_3")
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_JumpToHeight(height=144, silent=True),
		A_Pause(16),
		A_CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_2, destinations=["EVENT_3332_action_queue_140_SUBSCRIPT_visibility_off_3"]),
		A_VisibilityOff(identifier="EVENT_3332_action_queue_140_SUBSCRIPT_visibility_off_3")
	]),
	RemoveObjectFromCurrentLevel(NPC_2),
	JmpIfBitClear(UNUSED_707E_1, ["EVENT_3332_set_bit_146"]),
	JmpIfBitClear(JOHNNY_POSITION, ["EVENT_3331_play_music_default_volume_25"], identifier="EVENT_3332_jmp_if_bit_clear_143"),
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_3332_set_bit_146"]),
	PlayMusicAtDefaultVolume(M0063_AXEMRANGERSDROPIN),
	SetBit(UNUSED_707E_1, identifier="EVENT_3332_set_bit_146"),
	Return()
])
