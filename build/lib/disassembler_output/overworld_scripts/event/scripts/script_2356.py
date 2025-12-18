# E2356_EMPTY

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
	Pause(48),
	SetAsyncActionScript(NPC_8, A0390_EMPTY),
	SummonObjectToCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	Pause(24),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetBit(TEMP_7043_7),
		A_FloatingOn(),
		A_SetWalkingSpeed(FASTER),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_JumpToHeight(108),
		A_WalkSouthSteps(5),
		A_FloatingOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=14, y=90, z=16, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(3),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_1, A0388_EMPTY),
	SetSyncActionScript(NPC_5, A0388_EMPTY),
	RemoveObjectFromSpecificLevel(NPC_5, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	SetBit(TEMP_7044_2),
	Pause(32),
	SetAsyncActionScript(NPC_8, A0390_EMPTY),
	SummonObjectToCurrentLevel(NPC_3),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	Pause(24),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetBit(TEMP_7044_0),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_JumpToHeight(108),
		A_WalkSouthwestSteps(2),
		A_WalkWestSteps(2),
		A_FaceNorthwest(),
		A_FloatingOff()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=11, y=82, z=16, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(8),
		A_WalkWestPixels(3),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_3, A0388_EMPTY),
	SetSyncActionScript(NPC_7, A0388_EMPTY),
	RemoveObjectFromSpecificLevel(NPC_7, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	SetBit(TEMP_7044_4),
	Pause(32),
	SetAsyncActionScript(NPC_8, A0390_EMPTY),
	SummonObjectToCurrentLevel(NPC_2),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	Pause(24),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetBit(TEMP_7044_1),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_JumpToHeight(108),
		A_Walk1StepSouthwest(),
		A_WalkSouthSteps(2),
		A_FaceNortheast(),
		A_FloatingOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=13, y=85, z=18, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(3),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_2, A0388_EMPTY),
	SetSyncActionScript(NPC_6, A0388_EMPTY),
	RemoveObjectFromSpecificLevel(NPC_6, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	SetBit(TEMP_7044_3),
	Pause(592),
	EnableControls([]),
	DisableObjectTrigger(NPC_0),
	DisableObjectTrigger(NPC_1),
	DisableObjectTrigger(NPC_2),
	DisableObjectTrigger(NPC_3),
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2356_jmp_if_present_in_current_level_46"]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ShiftToXYCoords(x=12, y=83),
		A_VisibilityOn(),
		A_PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	PauseActionScript(NPC_0),
	SetAsyncActionScript(NPC_0, A0192_EMPTY),
	Pause(24),
	RemoveObjectFromCurrentLevel(NPC_10),
	Pause(32),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_2356_jmp_if_present_in_current_level_53"], identifier="EVENT_2356_jmp_if_present_in_current_level_46"),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ShiftToXYCoords(x=14, y=90),
		A_VisibilityOn(),
		A_PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	PauseActionScript(NPC_1),
	SetAsyncActionScript(NPC_1, A0192_EMPTY),
	Pause(24),
	RemoveObjectFromCurrentLevel(NPC_10),
	Pause(32),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2356_jmp_if_present_in_current_level_60"], identifier="EVENT_2356_jmp_if_present_in_current_level_53"),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ShiftToXYCoords(x=11, y=82),
		A_VisibilityOn(),
		A_PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	PauseActionScript(NPC_3),
	SetAsyncActionScript(NPC_3, A0192_EMPTY),
	Pause(24),
	RemoveObjectFromCurrentLevel(NPC_10),
	Pause(32),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_2356_remove_from_current_level_65"], identifier="EVENT_2356_jmp_if_present_in_current_level_60"),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ShiftToXYCoords(x=13, y=85),
		A_VisibilityOn(),
		A_PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	PauseActionScript(NPC_2),
	SetAsyncActionScript(NPC_2, A0192_EMPTY),
	Pause(24),
	RemoveObjectFromCurrentLevel(NPC_10, identifier="EVENT_2356_remove_from_current_level_65"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=10, y=60)
	]),
	RunDialog(dialog_id=DI3081_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Pause(16),
		A_ResetProperties()
	]),
	PlaySound(sound=SO076_BOOSTERS_TRAIN_HORN, channel=6),
	Pause(72),
	ActionQueueSync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO074_BOOSTERS_TRAIN, channel=6),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_SetPriority(2),
		A_WalkNorthwestSteps(3),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkNorthwestSteps(6)
	]),
	RunDialog(dialog_id=DI3086_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_9),
	Pause(32),
	PlaySound(sound=SO000_SILENCE, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthSteps(5)
	]),
	SetBit(UNUSED_708B_2),
	RemoveObjectFromSpecificLevel(NPC_0, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_1, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_2, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_3, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_4, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_5, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_6, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_7, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
