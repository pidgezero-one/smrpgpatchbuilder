# E3282_SHIP_BOSS_ROOM_LOADER

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
	JmpIfBitSet(UNKNOWN_709D_4, ["EVENT_3282_jmp_if_bit_set_3"]),
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_3282_jmp_if_bit_set_3"]),
	JmpToEvent(E3000_CLONE_RESERVED),
	JmpIfBitSet(SHIP_LIBERATED, ["EVENT_3282_jmp_if_bit_set_122"], identifier="EVENT_3282_jmp_if_bit_set_3"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_SetPriority(3)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_25"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_2, subscript=[
		A_TransferToObjectXY(MARIO),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_VisibilityOn(),
		A_WalkEastSteps(2)
	]),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_25"]),
	ClearBit(TEMP_7044_0),
	Set7000ToIDOfMemberInSlot(2),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_3282_clear_bit_16"]),
	SetBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1, identifier="EVENT_3282_clear_bit_16"),
	Set7000ToIDOfMemberInSlot(1),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3282_clear_bit_20"]),
	SetBit(TEMP_7044_1),
	ClearBit(TEMP_7044_2, identifier="EVENT_3282_clear_bit_20"),
	Set7000ToIDOfMemberInSlot(2),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3282_action_queue_24"]),
	SetBit(TEMP_7044_2),
	ActionQueueSync(target=CHARACTER_IN_SLOT_3, subscript=[
		A_TransferToObjectXY(MARIO),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_VisibilityOn(),
		A_WalkNorthSteps(2),
		A_JmpIfBitSet(TEMP_7044_0, ["EVENT_3282_action_queue_24_SUBSCRIPT_set_sprite_sequence_8"]),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_ReturnQueue(),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3282_action_queue_24_SUBSCRIPT_set_sprite_sequence_8"),
		A_ReturnQueue()
	], identifier="EVENT_3282_action_queue_24"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	], identifier="EVENT_3282_action_queue_25"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Walk1StepSouthwest(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Walk1StepSouthwest(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNortheast()
	]),
	RunDialog(dialog_id=DI1776_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_Walk1StepSouth(),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SequenceLoopingOff(),
		A_Pause(50),
		A_WalkSouthwestSteps(2)
	]),
	StartBattleAtBattlefield(PACK166_JOHNNY_FIGHT_STATIC, BF04_SUNKEN_SHIP),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	ClearBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	StopMusicFDA2(),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	SetBit(SHIP_LIBERATED),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_Pause(120),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI1777_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RestoreAllHP(),
	RestoreAllFP(),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	Pause(1),
	UnknownCommand(bytearray(b'\xfd\x8e\x19\x08/')),
	Pause(60),
	SetSyncActionScript(NPC_1, A0015_DO_NOTHING),
	ActionQueueSync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_TransferToObjectXY(NPC_1),
		A_Pause(7),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(6),
		A_VisibilityOff()
	]),
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
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00@\x00@\x00\x01\xe0\xffp\xfe\x80')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00 \x00\x01\xf0\xffp\xfe\x80")),
		A_Pause(512),
		A_BPL262728()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(16),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	PauseActionScript(NPC_0),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_64"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_3, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_64"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_2, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	], identifier="EVENT_3282_action_queue_64"),
	SetSyncActionScript(NPC_1, A0120_EMBEDDED_ROUTINE),
	Pause(120),
	SetSyncActionScript(NPC_1, A0015_DO_NOTHING),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(1),
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
		A_Pause(88),
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_SetSequenceSpeed(FASTEST),
		A_Pause(90)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToObjectXY(NPC_1),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(7),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(6),
		A_VisibilityOff()
	]),
	Pause(165),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	Pause(102),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_ShiftZDownSteps(4),
		A_ShiftZDownPixels(4),
		A_UnknownCommand(bytearray(b'\xc8\x00')),
		A_AddConstToVar(Z_COORD_2, 544),
		A_UnknownCommand(bytearray(b'\x99')),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_81"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_3, subscript=[
		A_Pause(14),
		A_JmpIfBitSet(TEMP_7044_2, ["EVENT_3282_action_queue_77_SUBSCRIPT_set_sprite_sequence_4"]),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_ReturnQueue(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3282_action_queue_77_SUBSCRIPT_set_sprite_sequence_4")
	]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_81"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_2, subscript=[
		A_Pause(14),
		A_JmpIfBitSet(TEMP_7044_1, ["EVENT_3282_action_queue_80_SUBSCRIPT_set_sprite_sequence_4"]),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True),
		A_ReturnQueue(),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, identifier="EVENT_3282_action_queue_80_SUBSCRIPT_set_sprite_sequence_4")
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(14),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	], identifier="EVENT_3282_action_queue_81"),
	Pause(240),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpSteps(2)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToObjectXY(NPC_1),
		A_TransferXYZFPixels(x=0, y=0, z=8, direction=NORTHEAST),
		A_Pause(24),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[1])
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(34),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpSteps(4),
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step()
	]),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\x0c(')),
	SetSyncActionScript(NPC_1, A0120_EMBEDDED_ROUTINE),
	Pause(60),
	SetSyncActionScript(NPC_1, A0015_DO_NOTHING),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(8),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	Pause(2),
	RunStarPieceSequence(5),
	Pause(2),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromSpecificLevel(NPC_1, R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownSteps(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_104"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_3, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_104"]),
	ActionQueueSync(target=CHARACTER_IN_SLOT_2, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth()
	], identifier="EVENT_3282_action_queue_104"),
	UnknownCommand(bytearray(b'\xfd\x8er\x00(')),
	FadeOutMusicToVolume(duration=0, volume=1),
	FadeInFromBlack(sync=False),
	Pause(30),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_118"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_Pause(16),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=CHARACTER_IN_SLOT_3, subscript=[
		A_Pause(32),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_Jmp(["EVENT_3282_action_queue_113_SUBSCRIPT_reset_properties_7"]),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_ResetProperties(identifier="EVENT_3282_action_queue_113_SUBSCRIPT_reset_properties_7"),
		A_Pause(12),
		A_WalkSoutheastSteps(2),
		A_VisibilityOff()
	]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsLesser(["EVENT_3282_action_queue_118"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_Pause(16),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=CHARACTER_IN_SLOT_2, subscript=[
		A_Pause(32),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(8),
		A_Jmp(["EVENT_3282_action_queue_117_SUBSCRIPT_reset_properties_7"]),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceNorthwest(),
		A_ResetProperties(identifier="EVENT_3282_action_queue_117_SUBSCRIPT_reset_properties_7"),
		A_Pause(12),
		A_WalkNorthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest(),
		A_Pause(100),
		A_FaceSouth()
	], identifier="EVENT_3282_action_queue_118"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkNorthwestSteps(6),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_Pause(2)
	]),
	FadeInMusic(M0041_SUNKENSHIP),
	Return(),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_3282_jmp_to_event_126"], identifier="EVENT_3282_jmp_if_bit_set_122"),
	SetSyncActionScript(NPC_2, A0015_DO_NOTHING),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=24, y=110),
		A_ResetProperties(),
		A_SequencePlaybackOn(),
		A_FaceNorthwest()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3282_jmp_to_event_126")
])
