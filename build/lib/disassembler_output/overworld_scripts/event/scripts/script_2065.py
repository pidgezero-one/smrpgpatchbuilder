# E2065_DOJO_LOADER_FIRST_TIME_ANIMATION

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
	Pause(45, identifier="EVENT_2065_pause_0"),
	RunDialog(dialog_id=DI3028_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_Pause(15),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3029_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=3, y=19, z=0, direction=EAST),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkSoutheastPixels(8),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(8)
	]),
	Pause(20),
	RunDialog(dialog_id=DI3030_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_ResetProperties(),
		A_FixedFCoordOff()
	]),
	Pause(20),
	RunDialog(dialog_id=DI3031_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	RunDialog(dialog_id=DI3032_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(8),
		A_VisibilityOff()
	]),
	SetBit(INITIAL_DOJO_CUTSCENE_COMPLETED),
	Return()
])
