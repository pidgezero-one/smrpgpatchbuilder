# E2489_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_LOADER

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
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	JmpIfObjectNotInSpecificLevel(NPC_6, R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE, ["EVENT_2489_freeze_camera_3"]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	FreezeCamera(identifier="EVENT_2489_freeze_camera_3"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(11),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(3)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(3)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(3)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_2489_action_queue_11_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2489_action_queue_11_SUBSCRIPT_pause_1"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	UnfreezeCamera(),
	Return()
])
