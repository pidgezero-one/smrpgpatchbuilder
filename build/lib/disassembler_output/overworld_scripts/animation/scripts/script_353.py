#A0353_EMPTY

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
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_353_play_sound_10"]),
	A_JmpIfVarEqualsConst(TEMP_702E, 16, ["ACTION_353_play_sound_7"]),
	A_PlaySound(sound=SO085_FLOWER, channel=4),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
	A_Jmp(["ACTION_353_set_animation_speed_12"]),
	A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4, identifier="ACTION_353_play_sound_7"),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_Jmp(["ACTION_353_set_animation_speed_12"]),
	A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4, identifier="ACTION_353_play_sound_10"),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetWalkingSpeed(VERY_FAST, identifier="ACTION_353_set_animation_speed_12"),
	A_AddZCoord1Step(),
	A_StartLoopNTimes(8),
	A_VisibilityOn(),
	A_Pause(2),
	A_VisibilityOff(),
	A_Pause(1),
	A_EndLoop(),
	A_Pause(1, identifier="ACTION_353_pause_20"),
	A_CompareVarToConst(TIMER_701E, 96),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_353_pause_20"]),
	A_Jmp(["ACTION_352_object_memory_clear_bit_0"])
])
