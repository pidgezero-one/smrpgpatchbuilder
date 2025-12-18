# E2421_EMPTY

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
	JmpIfBitSet(UNUSED_708B_2, ["EVENT_2421_enter_area_34"]),
	JmpIfBitClear(UNUSED_708B_1, ["EVENT_2421_enter_area_34"]),
	EnableControls([]),
	RemoveObjectFromCurrentLevel(MARIO),
	RemoveObjectFromCurrentLevel(NPC_10),
	Pause(24),
	StopAllBackgroundEvents(),
	RunBackgroundEvent(event_id=E2419_EMPTY, return_on_level_exit=True, bit_6=True),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=10, y=59)
	]),
	RunDialog(dialog_id=DI3083_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
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
	RunDialog(dialog_id=DI3087_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_9),
	Pause(24),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	RemoveObjectFromSpecificLevel(NPC_0, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_1, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_2, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_3, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_4, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_5, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_6, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	RemoveObjectFromSpecificLevel(NPC_7, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS),
	EnterArea(room_id=R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, face_direction=SOUTHWEST, x=28, y=55, z=0, run_entrance_event=True, identifier="EVENT_2421_enter_area_34"),
	Return()
])
