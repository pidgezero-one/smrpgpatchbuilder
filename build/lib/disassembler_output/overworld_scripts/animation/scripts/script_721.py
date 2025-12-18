#A0721_SEQUENCE_2_STATIC

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
	A_SetSequenceSpeed(VERY_FAST, identifier="ACTION_721_set_animation_speed_0"),
	A_SequenceLoopingOn(),
	A_WalkFDirectionSteps(3),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AE),
	A_StartLoopNTimes(5),
	A_JumpToHeight(56, identifier="ACTION_721_jump_to_height_6"),
	A_Pause(1),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_721_jump_to_height_6"]),
	A_TurnRandomDirection(),
	A_EndLoop(),
	A_CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C),
	A_FaceEast7C(),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_721_set_animation_speed_0"])
])
