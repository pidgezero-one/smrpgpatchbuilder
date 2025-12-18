#A0525_SPINNING_CARD

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SetSpriteSequence(index=6, is_mold=True, looping=True),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(6),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_WalkSoutheastSteps(3),
	A_Pause(120),
	A_Pause(30),
	A_ResetProperties(),
	A_FixedFCoordOff(),
	A_SequencePlaybackOn(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSouthwestPixels(6),
	A_SetPriority(3),
	A_WalkNorthwestSteps(10),
	A_SetBit(TEMP_7044_3),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_WalkNorthwestSteps(5),
	A_VisibilityOff(),
	A_ReturnQueue()
])
