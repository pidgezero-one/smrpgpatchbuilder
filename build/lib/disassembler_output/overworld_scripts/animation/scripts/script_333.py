#A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH

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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_333_set_animation_speed_0"),
	A_SetSequenceSpeed(VERY_FAST),
	A_AddZCoord1Step(),
	A_ShiftZDownPixels(15),
	A_SetBit(TEMP_7043_1),
	A_ShiftZDownPixels(1),
	A_SetWalkingSpeed(FAST),
	A_WalkNortheastPixels(10),
	A_ClearBit(TEMP_7043_1),
	A_WalkNortheastPixels(10),
	A_WalkNortheastSteps(3),
	A_WalkNortheastPixels(11),
	A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_JumpToHeight(height=88, silent=True),
	A_WalkSouthwestPixels(10),
	A_WalkSouthwestSteps(3),
	A_JumpToHeight(height=80, silent=True),
	A_SetWalkingSpeed(NORMAL),
	A_WalkSouthwestSteps(1),
	A_WalkSouthwestPixels(5),
	A_FaceNortheast(),
	A_ResetProperties(),
	A_SetSolidityBits(cant_walk_through=True),
	A_SetSequenceSpeed(SLOW),
	A_Pause(60),
	A_ClearSolidityBits(cant_walk_through=True),
	A_JmpIfBitSet(TEMP_7044_7, ["ACTION_333_ret_29"]),
	A_Jmp(["ACTION_333_set_animation_speed_0"]),
	A_ReturnQueue(identifier="ACTION_333_ret_29")
])
