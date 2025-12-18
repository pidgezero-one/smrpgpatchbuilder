# E2355_EMPTY

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
	JmpIfBitSet(FAST_TRAVEL_ENABLED, ["EVENT_2355_ret_34"]),
	SetBit(FAST_TRAVEL_ENABLED),
	SetBit(UNUSED_708B_1),
	RemoveObjectFromSpecificLevel(NPC_8, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_9, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	PlaySound(sound=SO074_BOOSTERS_TRAIN, channel=6),
	RunDialog(dialog_id=DI3082_SHITPOST, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3077_GOT_BEETLEMANIA, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(5),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(3),
		A_SetPriority(3),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=10, y=60)
	]),
	UnsyncDialog(),
	Pause(64),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3084_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO076_BOOSTERS_TRAIN_HORN, channel=6),
	Pause(64),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_Pause(16),
		A_FaceSouthwest(),
		A_Pause(80),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3078_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	SetAsyncActionScript(NPC_8, A0390_EMPTY),
	SummonObjectToCurrentLevel(NPC_0),
	RunDialog(dialog_id=DI3080_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(108),
		A_WalkSouthwestSteps(3),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=12, y=83, z=18, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(5),
		A_VisibilityOn()
	]),
	Pause(16),
	SetSyncActionScript(NPC_0, A0388_EMPTY),
	SetSyncActionScript(NPC_4, A0388_EMPTY),
	RunBackgroundEvent(event_id=E2356_EMPTY, return_on_level_exit=True),
	Return(identifier="EVENT_2355_ret_34")
])
