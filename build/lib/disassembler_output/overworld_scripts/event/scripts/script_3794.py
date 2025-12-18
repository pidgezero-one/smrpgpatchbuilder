# E3794_FACTORY_FINAL_BOSS_FIGHT

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
	SetSyncActionScript(NPC_9, A0991_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_4, A0240_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_8, A0990_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_5, A0241_SMITHY_COMPONENT),
	SetBit(TEMP_7044_0),
	RunBackgroundEvent(event_id=E3793_FACTORY_SMELTER_ANIMATION, return_on_level_exit=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_3794_action_queue_6_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_6_SUBSCRIPT_pause_2"]),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_Pause(30),
		A_ResetProperties()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouth()
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI3888_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=23, z=0, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_FaceSoutheast(),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(14),
		A_FaceNortheast(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3889_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties()
	]),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_4),
	UnsyncActionScript(NPC_5),
	UnsyncActionScript(NPC_8),
	Pause(1, identifier="EVENT_3794_pause_22"),
	JmpIfBitClear(TEMP_704C_0, ["EVENT_3794_pause_22"]),
	ClearBit(TEMP_704C_0),
	StopAllBackgroundEvents(),
	SetBit(TEMP_7043_2),
	SetSyncActionScript(NPC_4, A0989_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_9, A0988_SMITHY_COMPONENT),
	JmpToSubroutine(["EVENT_3794_set_bit_143"]),
	Pause(10),
	RunDialog(dialog_id=DI3890_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3794_set_bit_148"]),
	SetBit(TEMP_7043_5),
	SetBit(TEMP_7043_1),
	RunBackgroundEvent(event_id=E3793_FACTORY_SMELTER_ANIMATION, return_on_level_exit=True),
	Pause(90),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	Pause(90),
	RunDialog(dialog_id=DI3891_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(10),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=23, z=0, direction=EAST),
		A_TransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(14),
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3892_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(80),
		A_Pause(1, identifier="EVENT_3794_action_queue_50_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_50_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(80),
		A_Pause(1, identifier="EVENT_3794_action_queue_50_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_50_SUBSCRIPT_pause_4"])
	]),
	Pause(60),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_4),
	UnsyncActionScript(NPC_5),
	UnsyncActionScript(NPC_8),
	Pause(1, identifier="EVENT_3794_pause_56"),
	JmpIfBitClear(TEMP_704C_0, ["EVENT_3794_pause_56"]),
	ClearBit(TEMP_704C_0),
	StopAllBackgroundEvents(),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_5),
	SetSyncActionScript(NPC_4, A0989_SMITHY_COMPONENT),
	SetSyncActionScript(NPC_9, A0988_SMITHY_COMPONENT),
	JmpToSubroutine(["EVENT_3794_set_bit_143"]),
	Pause(10),
	RunDialog(dialog_id=DI3893_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3794_set_bit_148"]),
	Pause(30),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceWest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(10),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(10),
		A_FaceNorthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=23, z=0, direction=EAST),
		A_TransferXYZFPixels(x=248, y=0, z=0, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkWestPixels(24),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3894_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(30),
	JmpToSubroutine(["EVENT_3794_set_bit_143"]),
	Pause(10),
	RunDialog(dialog_id=DI3895_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3794_set_bit_148"]),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=23, z=0, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(14),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(4),
		A_ResetProperties(),
		A_Pause(2),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(20),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3896_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties()
	]),
	JmpToSubroutine(["EVENT_3794_set_bit_143"]),
	Pause(10),
	RunDialog(dialog_id=DI3897_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3794_set_bit_148"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(80),
		A_Pause(1, identifier="EVENT_3794_action_queue_113_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_113_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(80),
		A_Pause(1, identifier="EVENT_3794_action_queue_113_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_3794_action_queue_113_SUBSCRIPT_pause_4"])
	]),
	Pause(20),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(40),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(14),
		A_TransferToXYZF(x=7, y=65, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(40),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(14),
		A_TransferToXYZF(x=7, y=69, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(40),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthPixels(14),
		A_TransferToXYZF(x=7, y=67, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(40),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkEastPixels(24),
		A_TransferToXYZF(x=9, y=69, z=0, direction=EAST)
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True)
	]),
	JmpToSubroutine(["EVENT_3794_set_bit_143"]),
	Pause(10),
	RunDialog(dialog_id=DI3898_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3794_set_bit_148"]),
	Pause(30),
	UnfreezeCamera(),
	SetBit(TEMP_7043_5),
	UnsyncActionScript(NPC_9),
	UnsyncActionScript(NPC_4),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(20),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_ResetProperties(),
		A_SetWalkingSpeed(FAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_JumpToHeight(152),
		A_WalkNortheastSteps(2),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(2),
		A_FloatingOff(),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	PauseActionScript(NPC_8),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(4),
		A_WalkSouthwestPixels(6)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(4)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(1),
		A_WalkNorthPixels(2),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(55),
	InitiateBattleMask(),
	EnterArea(room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, face_direction=NORTHEAST, x=4, y=51, z=0, run_entrance_event=True),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_3794_set_bit_143"),
	UnsyncActionScript(NPC_8),
	ClearBit(TEMP_7043_1),
	SetSyncActionScript(NPC_8, A0242_SMITHY_COMPONENT),
	Return(),
	SetBit(TEMP_7043_1, identifier="EVENT_3794_set_bit_148"),
	ClearBit(TEMP_7043_3),
	UnsyncActionScript(NPC_8),
	ClearBit(TEMP_7043_1),
	SetSyncActionScript(NPC_8, A0987_SMITHY_COMPONENT),
	Return()
])
