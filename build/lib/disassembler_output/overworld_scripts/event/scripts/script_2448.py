# E2448_FOREST_BOSS_FIGHT

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
	JmpIfBitSet(FOREST_LIBERATED, ["EVENT_2448_ret_255"]),
	ClearBit(DIRECTIONAL_7045_0),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ClearBit(DIRECTIONAL_7045_3),
	ClearBit(DIRECTIONAL_7045_4),
	ClearBit(DIRECTIONAL_7045_5),
	ClearBit(DIRECTIONAL_7045_6),
	ClearBit(DIRECTIONAL_7045_7),
	ClearBit(DIRECTIONAL_7046_0),
	ClearBit(DIRECTIONAL_7046_1),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_WalkNorthwestSteps(2)
	]),
	RunDialog(dialog_id=DI3184_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_11),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_FaceNortheast(),
		A_Pause(48),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(24),
	RunDialog(dialog_id=DI3185_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_FaceSouthwest()
	]),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_11, subscript=[
		A_ResetProperties(),
		A_Pause(34),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_EndLoop(),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthwestSteps(10)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3186_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_0, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_5, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_1, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_6, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_2, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_7, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_3, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_8, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_4, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	SetSyncActionScript(NPC_9, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
	RunBackgroundEvent(event_id=E2446_FOREST_BOSS_HENCHMEN_BOUNCE, return_on_level_exit=True),
	RunDialog(dialog_id=DI3187_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetPriority(3),
		A_SetSequenceSpeed(FASTER)
	]),
	SetBit(TEMP_7043_0),
	StopAllBackgroundEvents(),
	Pause(16),
	RunDialog(dialog_id=DI3188_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(48),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(10)
	]),
	Pause(48),
	ActionQueueSync(target=NPC_11, subscript=[
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_2448_action_queue_46_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2448_action_queue_46_SUBSCRIPT_pause_1"]),
		A_Pause(16),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_SetSequenceSpeed(FASTER),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI3189_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_EndLoop()
	]),
	RunBackgroundEvent(event_id=E2465_EMPTY, return_on_level_exit=True, run_as_second_script=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(8)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3190_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(5),
	SetBit(DIRECTIONAL_7045_0),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_OverwriteSolidity(),
		A_FaceWest(),
		A_Pause(4),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI3192_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(96),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(56),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(128),
		A_Pause(48),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(2)
	]),
	RunDialog(dialog_id=DI3191_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SequenceLoopingOn(),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=14, y=37),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(24),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(6),
		A_WalkNorthwestSteps(3),
		A_WalkNorthwestPixels(8),
		A_WalkSouthwestPixels(8),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(72),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=15, y=35),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestPixels(8)
	]),
	Pause(32),
	UnfreezeCamera(),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_ShiftToXYCoords(x=17, y=40),
		A_WalkNorthwestPixels(17),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_17, subscript=[
		A_Pause(2),
		A_ShiftToXYCoords(x=17, y=40),
		A_WalkSouthwestPixels(13),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SequencePlaybackOff(),
		A_StartLoopNTimes(30),
		A_WalkNorthwestPixels(5),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_17, subscript=[
		A_SequencePlaybackOff(),
		A_Pause(4),
		A_StartLoopNTimes(30),
		A_WalkNorthwestPixels(5),
		A_Pause(5),
		A_EndLoop()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(112),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(10)
	]),
	Pause(48),
	RunDialog(dialog_id=DI3193_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_17),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3194_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	RunDialog(dialog_id=DI3195_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(16),
		A_SequenceLoopingOff()
	]),
	Pause(112),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=10, y=29, z=0, direction=SOUTHEAST),
		A_VisibilityOn(),
		A_SequencePlaybackOff(),
		A_FloatingOn(),
		A_JumpToHeight(1),
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1, identifier="EVENT_2448_action_queue_83_SUBSCRIPT_pause_6"),
		A_JmpIfObjectInAir(NPC_13, ["EVENT_2448_action_queue_83_SUBSCRIPT_pause_6"]),
		A_PlaySound(sound=SO058_INSERT, channel=6),
		A_Pause(8),
		A_SequencePlaybackOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=17, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3196_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=17, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FASTER),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI3197_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	CharacterJoinsParty(GENO),
	StartBattleAtBattlefield(PACK181_BOWYER_FIGHT_STATIC, BF01_FOREST_MAZE_BOWYERS_PAD),
	JmpIfBitClear(GAME_OVER, ["EVENT_2448_set_bit_92"]),
	ResetAndChooseGame(),
	SetBit(FOREST_LIBERATED, identifier="EVENT_2448_set_bit_92"),
	SetBit(MAP_DIRECTIONAL_ROSE_TOWN_PIPE_VAULT_MOLEVILLE),
	SetBit(MAP_PIPE_VAULT),
	SetBit(MAP_YOSTER_ISLE),
	SetBit(MAP_MOLEVILLE),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_16),
	RemoveObjectFromCurrentLevel(NPC_17),
	RemoveObjectFromSpecificLevel(NPC_0, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_1, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_2, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_3, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_4, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_5, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_6, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_7, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_8, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_9, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_11, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_13, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_16, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_17, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
	RemoveObjectFromSpecificLevel(NPC_13, R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09),
	RemoveObjectFromSpecificLevel(NPC_1, R228_FOREST_MAZE_AREA_04),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetPriority(0),
		A_ShiftToXYCoords(x=12, y=29)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=12, y=29)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_ShiftToXYCoords(x=13, y=31)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ShiftToXYCoords(x=11, y=34),
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetPriority(3),
		A_ShiftToXYCoords(x=11, y=26),
		A_WalkNorthPixels(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=9, y=16),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6])
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=8, y=17)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3198_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(32),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_Pause(96),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_EndLoop()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_Pause(32),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
		A_Pause(64),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(48),
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetSpriteSequence(index=4, sprite_offset=1, looping=False),
		A_Pause(48),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3199_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(32),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True),
		A_SequencePlaybackOff(),
		A_JumpToHeight(144),
		A_Pause(1, identifier="EVENT_2448_action_queue_142_SUBSCRIPT_pause_7"),
		A_JmpIfMarioInAir(["EVENT_2448_action_queue_142_SUBSCRIPT_pause_7"]),
		A_Pause(16),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_SequencePlaybackOff(),
		A_JumpToHeight(144),
		A_Pause(1, identifier="EVENT_2448_action_queue_143_SUBSCRIPT_pause_7"),
		A_JmpIfMarioInAir(["EVENT_2448_action_queue_143_SUBSCRIPT_pause_7"]),
		A_Pause(16),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3200_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3201_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(32),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(64),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3202_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_EndLoop()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_EndLoop()
	]),
	Pause(16),
	RunDialog(dialog_id=DI3203_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(8),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(32),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True),
		A_SequencePlaybackOff(),
		A_JumpToHeight(144),
		A_Pause(1, identifier="EVENT_2448_action_queue_164_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_2448_action_queue_164_SUBSCRIPT_pause_3"]),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_SequencePlaybackOff(),
		A_JumpToHeight(144),
		A_Pause(1, identifier="EVENT_2448_action_queue_165_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_2448_action_queue_165_SUBSCRIPT_pause_3"]),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(24),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_WalkNorthwestSteps(4),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3204_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(24),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(32),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(64),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(64),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3205_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(48),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_2448_action_queue_173_SUBSCRIPT_set_sprite_sequence_1"),
		A_Pause(28),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(28),
		A_JmpIfBitSet(TEMP_7044_7, ["EVENT_2448_action_queue_173_SUBSCRIPT_set_sprite_sequence_7"]),
		A_Jmp(["EVENT_2448_action_queue_173_SUBSCRIPT_set_sprite_sequence_1"]),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_2448_action_queue_173_SUBSCRIPT_set_sprite_sequence_7")
	]),
	RunDialog(dialog_id=DI3206_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetAsyncActionScript(NPC_11, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(32),
	StopEmbeddedActionScript(NPC_13),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_2448_action_queue_180_SUBSCRIPT_set_sprite_sequence_1"),
		A_Pause(16),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_JmpIfBitSet(TEMP_7044_6, ["EVENT_2448_run_dialog_181"]),
		A_Jmp(["EVENT_2448_action_queue_180_SUBSCRIPT_set_sprite_sequence_1"])
	]),
	RunDialog(dialog_id=DI3207_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2448_run_dialog_181"),
	SetBit(TEMP_7044_6),
	Pause(32),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, sprite_offset=1, looping=False),
		A_Pause(62),
		A_SetSpriteSequence(index=27, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(64),
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3208_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3210_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	FadeOutMusicFDA3(),
	Pause(16),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	Pause(74),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthSteps(2),
		A_Pause(40)
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ShiftZUpPixels(80),
		A_Pause(16),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(48),
		A_SetSequenceSpeed(FASTER),
		A_Pause(48),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(48),
		A_SetSequenceSpeed(FASTEST)
	]),
	SetSyncActionScript(NPC_9, A0393_EMPTY),
	Pause(50),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[1, 2])
	]),
	StopEmbeddedActionScript(NPC_9),
	Pause(448),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(7),
		A_Pause(384),
		A_SetSpriteSequence(index=31, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(16),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(48),
		A_SetSequenceSpeed(FASTER),
		A_Pause(48),
		A_SetSequenceSpeed(FAST),
		A_Pause(48),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(56),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	StopEmbeddedActionScript(NPC_15),
	Pause(96),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_Pause(8),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSequenceSpeed(FASTER),
		A_Pause(10),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(10),
		A_SetSequenceSpeed(FASTEST),
		A_Pause(48),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(44),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(1),
		A_ShiftZDownPixels(2),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Pause(40),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	Pause(256),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(32),
		A_Pause(48),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(16)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(67),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(4)
	]),
	Pause(73),
	FadeOutToBlack(sync=False, duration=32),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_15),
	RunStarPieceSequence(2),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=8, y=17)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(7),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(NPC_13, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI3212_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_OverwriteSolidity(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(2),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(10),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_OverwriteSolidity(),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Walk1StepNorthwest(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(3),
		A_WalkNortheastPixels(12),
		A_VisibilityOff()
	]),
	Pause(16),
	RunDialog(dialog_id=DI3209_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	PlayMusicAtDefaultVolume(M0040_NEWPARTNER),
	Pause(48),
	SetAsyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(11)
	]),
	ClearBit(TEMP_7043_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_PlaySound(sound=SO077_EXOTIC_BIRD_CALLS, channel=4),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x18\xff@\x00')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(30),
		A_PlaySound(sound=SO077_EXOTIC_BIRD_CALLS, channel=4),
		A_UnknownCommand(bytearray(b'$\x18\xff@\x00')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(30),
		A_PlaySound(sound=SO077_EXOTIC_BIRD_CALLS, channel=4),
		A_UnknownCommand(bytearray(b'$\x18\xff@\x00')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(30),
		A_BPL262728(),
		A_PlaySound(sound=SO077_EXOTIC_BIRD_CALLS, channel=4)
	]),
	SetSyncActionScript(NPC_0, A0484_EMPTY),
	RunDialog(dialog_id=DI3211_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_0),
	Pause(16),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetPriority(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(FASTEST),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkNorthwestSteps(5),
		A_VisibilityOff()
	]),
	Pause(32),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(10),
		A_Walk1StepEast()
	]),
	RestoreAllHP(),
	RestoreAllFP(),
	UnknownCommand(bytearray(b'\xfd\x8e\x80\x07\x01')),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI3440_DUPLICATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(32),
	SetSyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	Pause(52),
	PlaySound(sound=SO013_COIN, channel=6),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8e\xb2\x07\x01')),
	PauseScriptUntilEffectDone(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	PlayMusicAtDefaultVolume(M0026_FORESTMAZE),
	UnfreezeCamera(),
	Return(identifier="EVENT_2448_ret_255")
])
