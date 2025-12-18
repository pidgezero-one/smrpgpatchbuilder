# E1358_CURTAIN_GAME_BEGINS_NPCS_WALK_INTO_ROOM

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
	RemoveObjectFromSpecificLevel(NPC_1, R202_BOOSTER_TOWER_ENTRANCE, identifier="EVENT_1358_remove_from_level_0"),
	RemoveObjectFromSpecificLevel(NPC_6, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM),
	RemoveObjectFromSpecificLevel(NPC_3, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	RemoveObjectFromSpecificLevel(NPC_8, R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS),
	RemoveObjectFromSpecificLevel(NPC_4, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
	MoveScriptToBackgroundThread2(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	RunDialog(dialog_id=DI2780_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(120),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(3),
		A_WalkNorthwestSteps(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(70),
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(2),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(7),
		A_WalkNorthwestSteps(5),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(70),
		A_Pause(40),
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(2),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(7),
		A_WalkNorthwestSteps(3),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(70),
		A_Pause(40),
		A_Pause(120),
		A_TransferToXYZF(x=9, y=18, z=0, direction=EAST),
		A_SetPriority(2),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(7),
		A_WalkNorthwestSteps(1),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	Pause(70),
	SetSyncActionScript(NPC_1, A0573_EMPTY),
	RunDialog(dialog_id=DI2776_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_1, A0574_EMPTY),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(FAST),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(1),
		A_WalkNorthwestSteps(1),
		A_SetAllSpeeds(NORMAL),
		A_Pause(30),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2772_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_2, A0573_EMPTY),
	RunDialog(dialog_id=DI2773_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_2, A0574_EMPTY),
	RunDialog(dialog_id=DI2774_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_3, A0573_EMPTY),
	RunDialog(dialog_id=DI2775_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_3, A0574_EMPTY),
	RunDialog(dialog_id=DI2777_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(3),
		A_WalkSoutheastSteps(2),
		A_WalkNortheastSteps(1),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkNortheastSteps(5),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(2),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(1),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkSoutheastSteps(3),
		A_WalkNortheastSteps(2),
		A_WalkNorthwestSteps(3)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(30),
		A_SetVRAMPriority(PRIORITY_3),
		A_TransferToXYZF(x=7, y=26, z=3, direction=EAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(3)
	]),
	Pause(45),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(64),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI2778_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(1),
		A_WalkNorthwestPixels(5)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(1),
		A_WalkNorthwestPixels(5)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(1),
		A_WalkNorthwestPixels(5)
	]),
	RunDialog(dialog_id=DI2779_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(NORMAL),
		A_FixedFCoordOff(),
		A_WalkNorthwestPixels(8),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(4),
		A_WalkSoutheastSteps(2),
		A_Pause(25),
		A_WalkSoutheastSteps(2),
		A_Pause(15),
		A_WalkSouthwestSteps(2),
		A_WalkNorthwestSteps(5),
		A_WalkSouthwestSteps(1),
		A_Pause(35),
		A_WalkNortheastSteps(2),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff(),
		A_WalkNortheastPixels(8),
		A_WalkNortheastSteps(3),
		A_Pause(15),
		A_WalkSouthwestSteps(3),
		A_Pause(35),
		A_WalkSoutheastSteps(2),
		A_FaceNortheast(),
		A_Pause(25),
		A_JumpToHeight(48),
		A_Pause(20),
		A_WalkSouthwestSteps(2),
		A_FaceNortheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff(),
		A_WalkSoutheastPixels(8),
		A_WalkSoutheastSteps(3),
		A_WalkNortheastSteps(2),
		A_Pause(35),
		A_WalkNorthwestSteps(3),
		A_FaceNortheast(),
		A_Pause(25),
		A_WalkSouthwestSteps(6),
		A_Pause(15),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(1),
		A_FaceNortheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_JumpToHeight(96),
		A_Pause(20),
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkSoutheastPixels(8),
		A_WalkSoutheastSteps(3),
		A_TransferToXYZF(x=6, y=25, z=1, direction=EAST),
		A_ShadowOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	Pause(30),
	SetSyncActionScript(NPC_1, A0573_EMPTY),
	SetSyncActionScript(NPC_2, A0573_EMPTY),
	SetSyncActionScript(NPC_3, A0573_EMPTY),
	RunDialog(dialog_id=DI2781_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_1, A0574_EMPTY),
	SetSyncActionScript(NPC_2, A0574_EMPTY),
	SetSyncActionScript(NPC_3, A0574_EMPTY),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(40),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2782_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	FadeOutMusicToVolume(duration=5, volume=0),
	Pause(70),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2783_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	], identifier="EVENT_1358_action_queue_60"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	Pause(60),
	Jmp(["EVENT_1365_play_music_default_volume_0"])
])
