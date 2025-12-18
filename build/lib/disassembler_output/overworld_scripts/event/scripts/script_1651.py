# E1651_MARIO_CRASH_THRU_MOLEVILLE_ROOF

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
	EnterArea(room_id=R338_MOLEVILLE_DYNA_AND_MITES_HOUSE, face_direction=SOUTHWEST, x=4, y=41, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_TransferXYZFSteps(x=0, y=0, z=20, direction=EAST)
	]),
	CircleMaskExpandFromScreenCenter(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=3, y=38, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=2, y=38, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(SLOW)
	]),
	PauseScriptUntilEffectDone(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(2),
		A_WalkSouthwestSteps(4),
		A_SetSequenceSpeed(SLOW)
	]),
	SetSyncActionScript(NPC_0, A0650_BLUE_CLOUD_MOVEMENT),
	RunDialog(dialog_id=DI1104_MA_MOLE_KIDS_HURRY_HOME, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_1, A0650_BLUE_CLOUD_MOVEMENT),
	RunDialog(dialog_id=DI1105_MUSTY_FEARS_EXPLANATION, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW)
	]),
	SetSyncActionScript(NPC_0, A0650_BLUE_CLOUD_MOVEMENT),
	RunDialog(dialog_id=DI1106_INVISIBLE_ITEMS_CONFIRMED_PLACED, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTHWEST, x=30, y=43, z=2, run_entrance_event=True),
	Return()
])
