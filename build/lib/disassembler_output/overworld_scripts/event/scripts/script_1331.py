# E1331_TOWER_BREAK_DOWN_DOOR

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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1331_action_queue_2"]),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	], identifier="EVENT_1331_action_queue_2"),
	StopSound(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=2, y=121, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_VisibilityOn(),
		A_Pause(5),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkNortheastSteps(5)
	]),
	RunDialog(dialog_id=DI2812_TOP_OF_TOWER_WITH_FAST_TRAVEL_DISABLED, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	RunDialog(dialog_id=DI2810_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
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
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(25),
		A_SetAllSpeeds(FAST),
		A_FaceEast(),
		A_FixedFCoordOn(),
		A_JumpToHeight(height=101, silent=True),
		A_WalkToXYCoords(x=4, y=114),
		A_SetAllSpeeds(NORMAL),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(2),
		A_Pause(15),
		A_FaceSouthwest(),
		A_Pause(15),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn(),
		A_Pause(15),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(15),
		A_SetSequenceSpeed(FAST),
		A_Pause(15),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(45),
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(18),
		A_WalkSouthwestPixels(12),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(6),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4)
	]),
	Pause(5),
	ApplySolidityModToLevel(permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=32),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromSpecificLevel(NPC_2, R202_BOOSTER_TOWER_ENTRANCE),
	Pause(60),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_SequencePlaybackOn(),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(30)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkToXYCoords(x=5, y=115),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	RunDialog(dialog_id=DI2813_TOP_OF_TOWER_WITH_FAST_TRAVEL_DISABLED, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestPixels(10)
	]),
	RunDialog(dialog_id=DI2814_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestPixels(34),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI2815_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	FadeOutMusicToVolume(duration=2, volume=0),
	Pause(60),
	PlayMusicAtDefaultVolume(M0040_NEWPARTNER),
	Pause(40),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(6),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(60)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(15),
		A_SetPriority(2),
		A_TransferToXYZF(x=8, y=111, z=0, direction=EAST),
		A_SetWalkingSpeed(NORMAL),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(15)
	]),
	Pause(60),
	CloseDialog(),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastPixels(7),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromSpecificLevel(NPC_1, R202_BOOSTER_TOWER_ENTRANCE),
	RemoveObjectFromCurrentLevel(NPC_0),
	SetBit(SWITCH_MENU_UNLOCKED),
	SetBit(TOWER_OPENED),
	CharacterJoinsParty(BOWSER),
	ClearBit(TEMP_7043_0),
	PlayMusicAtDefaultVolume(M0013_ROADISFULLOFDANGERS),
	Pause(45),
	RunDialog(dialog_id=DI2940_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_1331_ret_58"]),
	RunMenuTutorial(TU02_HOW_TO_SWITCH),
	FadeInFromBlack(sync=False),
	Return(identifier="EVENT_1331_ret_58")
])
