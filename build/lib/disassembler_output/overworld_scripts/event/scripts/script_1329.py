# E1329_EMPTY

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
	FadeInFromBlack(sync=False, identifier="EVENT_1329_fade_in_from_black_async_0"),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastPixels(4),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastPixels(4)
	]),
	Pause(30),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(3)
	]),
	Pause(20),
	RunDialog(dialog_id=DI2806_DUPLICATE, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageA(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	CloseDialog(),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_Pause(55),
		A_SetSpriteSequence(index=21, is_mold=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI2807_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageA(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNortheast()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(10),
		A_SetSequenceSpeed(VERY_FAST),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_StopSound(),
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2809_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(28)
	]),
	Pause(145),
	FadeOutToBlack(sync=False, duration=50),
	Jmp(["EVENT_1280_enter_area_0"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, looping=True)
	], identifier="EVENT_1329_action_queue_30"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, looping=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthSteps(31),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthSteps(3),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(1)
	]),
	FadeInFromBlack(sync=False, duration=50),
	Pause(120),
	Pause(25),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2808_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthwestSteps(3),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestSteps(2)
	]),
	RunDialog(dialog_id=DI2810_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TOWER_CHARACTER_RECRUITED),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(80)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(20),
		A_SetWalkingSpeed(FAST),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_WalkSouthPixels(12),
		A_WalkNorthPixels(12),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(5),
		A_WalkNorthPixels(5)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(25),
		A_SetAllSpeeds(NORMAL),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_JumpToHeight(height=96, silent=True),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_0),
	UnfreezeCamera(),
	SetBit(TOWER_CHARACTER_RECRUITED),
	Return()
])
