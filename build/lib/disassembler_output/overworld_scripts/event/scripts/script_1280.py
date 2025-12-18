# E1280_EMPTY

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
	EnterArea(room_id=R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, face_direction=NORTHEAST, x=4, y=19, z=0, identifier="EVENT_1280_enter_area_0"),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3),
		A_WalkNortheastPixels(10),
		A_WalkNorthPixels(2),
		A_WalkWestPixels(2),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceSouthwest(),
		A_TransferToXYZF(x=4, y=20, z=0, direction=EAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_SequenceLoopingOn()
	]),
	FadeInFromBlack(sync=False, duration=80),
	Pause(100),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=22, is_mold=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SequenceLoopingOff()
	]),
	RunDialog(dialog_id=DI2823_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=16, is_mold=True, looping=True),
		A_Pause(5)
	]),
	RunDialog(dialog_id=DI2824_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_JumpToHeight(height=37, silent=True),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(10)
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(12),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2825_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(20),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI2826_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	EnterArea(room_id=R202_BOOSTER_TOWER_ENTRANCE, face_direction=NORTHEAST, x=2, y=120, z=0),
	FreezeCamera(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(40)
	]),
	SetSyncActionScript(NPC_1, A0519_TOWER_BOSS_PEEKING_BEHIND_ENTRANCE),
	Jmp(["EVENT_1329_action_queue_30"]),
	Return()
])
