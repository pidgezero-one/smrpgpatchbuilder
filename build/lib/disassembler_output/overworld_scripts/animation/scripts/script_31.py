#A0031_EMPTY

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
	A_StartLoopNTimes(1, identifier="ACTION_31_start_loop_n_times_0"),
	A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=1, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=2, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=3, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(2),
	A_SetSpriteSequence(index=4, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_PlaySound(sound=SO057_FINGER_SNAP, channel=4),
	A_Pause(2),
	A_SetSpriteSequence(index=3, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=4, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_SetSpriteSequence(index=2, sprite_offset=5, is_mold=True, is_sequence=True, looping=True),
	A_Pause(4),
	A_EndLoop(),
	A_ResetProperties(),
	A_Pause(2),
	A_FaceSoutheast(),
	A_Pause(2),
	A_FaceSouthwest(),
	A_SetBit(TEMP_7043_1),
	A_Pause(8),
	A_SetSequenceSpeed(VERY_FAST),
	A_SetWalkingSpeed(FAST),
	A_FixedFCoordOn(),
	A_WalkNortheastPixels(8),
	A_ClearBit(TEMP_7043_1),
	A_WalkNortheastPixels(8),
	A_WalkNortheastSteps(2),
	A_SequenceLoopingOff(),
	A_Pause(4),
	A_SetWalkingSpeed(FASTEST),
	A_WalkSouthwestPixels(2),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_StartLoopNTimes(3),
	A_WalkNortheastPixels(4),
	A_WalkSouthwestPixels(4),
	A_EndLoop(),
	A_WalkNortheastPixels(2),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
	A_Pause(30),
	A_ResetProperties(),
	A_WalkSouthwestSteps(3),
	A_FaceNortheast(),
	A_Pause(40),
	A_Jmp(["ACTION_31_start_loop_n_times_0"])
])
