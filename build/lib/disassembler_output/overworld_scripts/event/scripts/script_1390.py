# E1390_EMPTY

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
	ApplyTileModToLevel(use_alternate=True, room_id=R439_BOWSERS_KEEP_OUTSIDE_TALK_TO_EXOR, mod_id=32),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthSteps(1),
		A_WalkSouthPixels(2),
		A_WalkEastPixels(7),
		A_WalkSoutheastPixels(6),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthPixels(12),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthPixels(2),
		A_WalkNortheastPixels(1),
		A_WalkEastPixels(9),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkNortheastPixels(18),
		A_WalkNorthPixels(2),
		A_WalkEastPixels(1),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNortheastPixels(14),
		A_WalkEastPixels(1),
		A_WalkNorthwestPixels(2),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=1, y=46, z=0, direction=EAST),
		A_WalkSouthwestPixels(7),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(MARIO),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetVRAMPriority(PRIORITY_3),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(83),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNortheastPixels(1),
		A_Pause(1),
		A_WalkNortheastPixels(1),
		A_Pause(2),
		A_WalkNortheastPixels(1),
		A_Pause(3),
		A_WalkNortheastPixels(1),
		A_Pause(4),
		A_SetSequenceSpeed(SLOW),
		A_WalkNortheastPixels(1),
		A_Pause(6),
		A_WalkNortheastPixels(1),
		A_Pause(10),
		A_WalkNortheastPixels(1),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(55)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthPixels(1),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthPixels(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthPixels(3),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthPixels(4),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(11),
		A_Pause(2),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthPixels(12),
		A_WalkNorthPixels(12),
		A_WalkSouthPixels(10),
		A_WalkNorthPixels(10),
		A_WalkSouthPixels(9),
		A_WalkNorthPixels(9),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8)
	]),
	Pause(90),
	SetSyncActionScript(NPC_0, A0581_SEQUENCE_1_STATIC),
	RunDialog(dialog_id=DI2570_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageA(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	SetSyncActionScript(NPC_0, A0581_SEQUENCE_1_STATIC),
	PauseScriptResumeOnNextDialogPageB(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	SetSyncActionScript(NPC_0, A0582_EMPTY),
	PauseScriptResumeOnNextDialogPageB(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	SetSyncActionScript(NPC_0, A0582_EMPTY),
	PauseScriptResumeOnNextDialogPageA(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	SetSyncActionScript(NPC_0, A0582_EMPTY),
	PauseScriptResumeOnNextDialogPageB(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	SetSyncActionScript(NPC_0, A0582_EMPTY),
	PauseScriptResumeOnNextDialogPageB(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(35)
	]),
	SetSyncActionScript(NPC_0, A0581_SEQUENCE_1_STATIC),
	UnsyncDialog(),
	CloseDialog(),
	PauseActionScript(NPC_0),
	Pause(1),
	ResetCoords(NPC_0),
	Pause(30),
	SetSyncActionScript(NPC_0, A0583_EMPTY),
	Pause(60),
	FadeOutSoundToVolume(duration=0, volume=0),
	PlaySound(sound=SO091_TUMBLING_BOULDERS, channel=6),
	FadeOutSoundToVolume(duration=7, volume=100),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(34),
		A_WalkSouthPixels(1),
		A_WalkNorthPixels(1),
		A_EndLoop(),
		A_StartLoopNTimes(14),
		A_WalkSouthPixels(2),
		A_WalkNorthPixels(2),
		A_EndLoop(),
		A_StartLoopNTimes(9),
		A_WalkSouthPixels(3),
		A_WalkNorthPixels(3),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(4),
		A_EndLoop(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthSteps(11),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(7),
		A_WalkSouthPixels(5),
		A_WalkNorthPixels(5),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_WalkSouthPixels(6),
		A_WalkNorthPixels(6),
		A_EndLoop()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_StartLoopNTimes(89),
		A_WalkSouthPixels(7),
		A_WalkNorthPixels(7),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(6),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthPixels(12),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(80),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(15),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(6),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthPixels(12),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(80),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(6),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthPixels(12),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(80),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(5),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_ShadowOn(),
		A_StartLoopNTimes(8),
		A_JumpToHeight(height=80, silent=True),
		A_SetWalkingSpeed(FASTER),
		A_WalkSouthwestSteps(3),
		A_Pause(1, identifier="EVENT_1390_action_queue_61_SUBSCRIPT_pause_7"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1390_action_queue_61_SUBSCRIPT_pause_7"]),
		A_JumpToHeight(height=48, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(1),
		A_Pause(1, identifier="EVENT_1390_action_queue_61_SUBSCRIPT_pause_12"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1390_action_queue_61_SUBSCRIPT_pause_12"]),
		A_EndLoop()
	]),
	FadeOutToBlack(sync=False, duration=200),
	FadeOutSoundToVolume(duration=5, volume=0),
	Pause(60),
	ClearBit(UNUSED_MAP_DIRECTIONAL),
	SetBit(MAP_VISTA_HILL),
	SetBit(MAP_DIRECTIONAL_VISTA_HILL_MARIOS_PAD),
	SetBit(UNUSED_7053_1),
	EnterArea(room_id=R015_VISTA_HILL, face_direction=NORTHWEST, x=4, y=16, z=0, run_entrance_event=True),
	Return()
])
