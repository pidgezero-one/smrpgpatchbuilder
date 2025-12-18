# E0663_INITIATE_MARRYMORE_BOSS_FIGHT_IF_ALL_GEAR_COLLECTED

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
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7042_1),
	ClearBit(TEMP_7042_2),
	CopyVarToVar(from_var=TEMP_70AF, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_663_adjust_music_tempo_12"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	SetVarToConst(PRIMARY_TEMP_7000, 4),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=TEMP_70AF, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI2504_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	SlowDownMusicTempoBy(duration=0, change=0, identifier="EVENT_663_adjust_music_tempo_12"),
	StopBackgroundEvent(TIMER_701C),
	StopBackgroundEvent(TIMER_701E),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 6),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_663_set_var_to_const_24"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_663_set_var_to_const_26"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_663_set_var_to_const_28"]),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	Jmp(["EVENT_663_action_queue_29"]),
	SetVarToConst(SECONDARY_TEMP_7024, 4, identifier="EVENT_663_set_var_to_const_24"),
	Jmp(["EVENT_663_action_queue_29"]),
	SetVarToConst(SECONDARY_TEMP_7024, 3, identifier="EVENT_663_set_var_to_const_26"),
	Jmp(["EVENT_663_action_queue_29"]),
	SetVarToConst(SECONDARY_TEMP_7024, 2, identifier="EVENT_663_set_var_to_const_28"),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_BounceToXYWithHeight(x=21, y=73, height=1),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True)
	], identifier="EVENT_663_action_queue_29"),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2505_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_VisibilityOff(),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_TransferToXYZF(x=21, y=73, z=1, direction=EAST),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSoutheastPixels(4),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(14),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2138_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	Pause(10),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2139_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_JumpToHeight(height=240, silent=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkNorthwestSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(40),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepNorth(),
		A_Walk1StepNorthwest(),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_StopSound(),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(SLOW),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(4),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_TransferXYZFPixels(x=2, y=254, z=0, direction=EAST)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2106_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Walk1StepNorthwest(),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2131_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(2),
		A_FaceSouthwest(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2128_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetWalkingSpeed(VERY_SLOW),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
		A_WalkNorthwestPixels(4),
		A_StopSound(),
		A_ResetProperties(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2129_EMPTY, above_object=NPC_13, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueSync(target=NPC_13, subscript=[
		A_WalkNortheastPixels(4),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2130_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2127_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2132_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_FaceSouthwest(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2133_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(4),
		A_SetSpriteSequence(index=19, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=20, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(4),
		A_ResetProperties(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkNorthPixels(4)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4)
	]),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	PauseScriptUntilEffectDone(),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_663_set_bit_111"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 3, ["EVENT_663_set_bit_127"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 2, ["EVENT_663_set_bit_142"]),
	EnterArea(room_id=R063_MARRYMORE_SCENE, face_direction=SOUTH, x=12, y=18, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	CircleMaskShrinkToObject(target=MARIO, width=72, speed=2, static=True),
	PauseScriptUntilEffectDone(),
	PlaySound(sound=SO107_DRUM_ROLL, channel=6),
	Pause(120),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(6)
	]),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(4),
		A_StopSound(),
		A_PlaySound(sound=SO108_DRUM_ROLL_END, channel=6),
		A_WalkEastPixels(16)
	]),
	Pause(120),
	PlaySound(sound=SO107_DRUM_ROLL, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R063_MARRYMORE_SCENE, mod_id=0),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R063_MARRYMORE_SCENE, mod_id=1),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R063_MARRYMORE_SCENE, mod_id=3),
	Pause(1),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestSteps(3),
		A_SetWalkingSpeed(FAST),
		A_WalkWestSteps(2),
		A_StopSound(),
		A_PlaySound(sound=SO108_DRUM_ROLL_END, channel=6),
		A_WalkWestPixels(12)
	]),
	Pause(180),
	RunEventAsSubroutine(E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED),
	Jmp(["EVENT_663_circle_mask_static_155"]),
	SetBit(TEMP_7042_0, identifier="EVENT_663_set_bit_111"),
	EnterArea(room_id=R063_MARRYMORE_SCENE, face_direction=SOUTH, x=12, y=18, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(16)
	]),
	CircleMaskShrinkToObject(target=MARIO, width=48, speed=2, static=True),
	PauseScriptUntilEffectDone(),
	PlaySound(sound=SO107_DRUM_ROLL, channel=6),
	Pause(120),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(2),
		A_StopSound(),
		A_PlaySound(sound=SO108_DRUM_ROLL_END, channel=6),
		A_WalkEastPixels(16)
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Pause(30),
		A_WalkWestPixels(4)
	]),
	Pause(30),
	StopMusic(),
	RememberLastObject(),
	Pause(180),
	RunEventAsSubroutine(E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED),
	Jmp(["EVENT_663_circle_mask_static_155"]),
	SetBit(TEMP_7042_1, identifier="EVENT_663_set_bit_127"),
	EnterArea(room_id=R063_MARRYMORE_SCENE, face_direction=SOUTH, x=12, y=18, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R063_MARRYMORE_SCENE, mod_id=2),
	Pause(1),
	CircleMaskShrinkToObject(target=MARIO, width=48, speed=2, static=True),
	PauseScriptUntilEffectDone(),
	PlaySound(sound=SO107_DRUM_ROLL, channel=6),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(6)
	]),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(4),
		A_WalkEastPixels(10),
		A_StopSound(),
		A_PlaySound(sound=SO108_DRUM_ROLL_END, channel=6),
		A_WalkEastPixels(16)
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Pause(60),
		A_WalkEastPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkEastPixels(10)
	]),
	Pause(30),
	Pause(180),
	RunEventAsSubroutine(E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED),
	Jmp(["EVENT_663_circle_mask_static_155"]),
	SetBit(TEMP_7042_2, identifier="EVENT_663_set_bit_142"),
	EnterArea(room_id=R063_MARRYMORE_SCENE, face_direction=SOUTH, x=12, y=18, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	CircleMaskShrinkToObject(target=MARIO, width=48, speed=2, static=True),
	PauseScriptUntilEffectDone(),
	PlaySound(sound=SO107_DRUM_ROLL, channel=6),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(6)
	]),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(4),
		A_WalkEastPixels(13),
		A_StopSound(),
		A_PlaySound(sound=SO108_DRUM_ROLL_END, channel=6),
		A_WalkEastPixels(16)
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Pause(60),
		A_WalkEastPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_WalkEastPixels(7)
	]),
	Pause(30),
	Pause(180),
	RunEventAsSubroutine(E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED),
	Jmp(["EVENT_663_circle_mask_static_155"]),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=2, static=True, identifier="EVENT_663_circle_mask_static_155"),
	PauseScriptUntilEffectDone(),
	EnterArea(room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, face_direction=SOUTHWEST, x=21, y=71, z=1),
	PlayMusicAtDefaultVolume(M0039_MARRYMORE),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_663_palette_set_200"]),
	JmpIfBitSet(TEMP_7042_1, ["EVENT_663_action_queue_240"]),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_663_action_queue_277"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_TransferToXYZF(x=20, y=68, z=2, direction=EAST),
		A_FaceSoutheast(),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=21, y=70, z=2, direction=EAST),
		A_FaceSoutheast(),
		A_TransferXYZFPixels(x=12, y=252, z=0, direction=EAST),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_TransferToXYZF(x=22, y=72, z=2, direction=EAST),
		A_TransferXYZFPixels(x=0, y=252, z=0, direction=EAST),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI2134_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkWestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(8),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2135_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2136_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_Walk1StepEast(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2137_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(9),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouth(),
		A_WalkSouthwestSteps(2)
	]),
	JmpToEvent(E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM),
	PaletteSet(palette_set=142, row=1, bit_3=True, identifier="EVENT_663_palette_set_200"),
	ActionQueueSync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=22, y=72, z=2, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_TransferToXYZF(x=22, y=73, z=2, direction=EAST),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=21, y=70, z=2, direction=EAST)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_TransferToXYZF(x=21, y=71, z=2, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=20, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI2134_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(4)
	]),
	Pause(60),
	ActionQueueSync(target=NPC_16, subscript=[
		A_WalkSoutheastPixels(4),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(VERY_FAST),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_StartLoopNTimes(1),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_EndLoop(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(60),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(60),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(60)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=4),
		A_Pause(2),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_StopSound()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(4)
	]),
	PaletteSet(palette_set=84, row=1, bit_3=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2135_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI2136_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2137_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(8),
		A_TransferToXYZF(x=20, y=116, z=0, direction=EAST)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast()
	]),
	RememberLastObject(),
	Pause(60),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(12),
		A_TransferToXYZF(x=20, y=116, z=0, direction=EAST)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	JmpToEvent(E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=21, y=70, z=2, direction=EAST),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	], identifier="EVENT_663_action_queue_240"),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_TransferToXYZF(x=20, y=68, z=2, direction=EAST),
		A_FaceSoutheast(),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=21, y=71, z=2, direction=EAST),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_TransferToXYZF(x=22, y=73, z=2, direction=EAST),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI2151_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastPixels(4),
		A_Pause(30),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2135_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2136_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_Walk1StepEast(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2137_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(12),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(12),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(40),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(13),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8)
	]),
	JmpToEvent(E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=21, y=70, z=2, direction=EAST),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	], identifier="EVENT_663_action_queue_277"),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_TransferToXYZF(x=20, y=68, z=2, direction=EAST),
		A_FaceSoutheast(),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=22, y=72, z=2, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_TransferToXYZF(x=21, y=71, z=2, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=True, duration=90),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI2152_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2135_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2136_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_Walk1StepEast(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2137_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(50),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(6)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(9),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkSoutheastPixels(8)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkSoutheastPixels(8),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2123_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastPixels(12),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	JmpToEvent(E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM)
])
