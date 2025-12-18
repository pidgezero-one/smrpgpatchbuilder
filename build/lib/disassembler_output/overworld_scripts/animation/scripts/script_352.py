#A0352_EMPTY

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
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="ACTION_352_object_memory_clear_bit_0"),
	A_SetVarToConst(TIMER_701E, 400),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_SetWalkingSpeed(FASTER),
	A_SetSequenceSpeed(NORMAL),
	A_JmpIfVarNotEqualsConst(TEMP_70AF, 0, ["ACTION_352_dec_14"]),
	A_SetVarToConst(TEMP_70AF, 3),
	A_ClearBit(TEMP_7044_0),
	A_Dec(TEMP_702C),
	A_JmpIfVarNotEqualsConst(TEMP_702C, 0, ["ACTION_352_jmp_if_bit_set_13"]),
	A_SetVarToConst(TEMP_702E, 128),
	A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
	A_Jmp(["ACTION_352_visibility_on_27"]),
	A_JmpIfBitSet(TEMP_7043_6, ["ACTION_352_ret_68"], identifier="ACTION_352_jmp_if_bit_set_13"),
	A_Dec(TEMP_70AF, identifier="ACTION_352_dec_14"),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 65535),
	A_JmpIfVarNotEqualsConst(TEMP_70AF, 0, ["ACTION_352_jmp_if_700C_all_bits_clear_19"]),
	A_JmpIfBitSet(TEMP_7044_0, ["ACTION_352_set_var_to_const_25"]),
	A_Jmp(["ACTION_352_set_bit_21"]),
	A_JmpIf700CAllBitsClear(bits=[0], destinations=["ACTION_352_set_var_to_const_25"], identifier="ACTION_352_jmp_if_700C_all_bits_clear_19"),
	A_JmpIfBitSet(TEMP_7044_0, ["ACTION_352_set_var_to_const_25"]),
	A_SetBit(TEMP_7044_0, identifier="ACTION_352_set_bit_21"),
	A_SetVarToConst(TEMP_702E, 16),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_Jmp(["ACTION_352_visibility_on_27"]),
	A_SetVarToConst(TEMP_702E, 1, identifier="ACTION_352_set_var_to_const_25"),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_VisibilityOn(identifier="ACTION_352_visibility_on_27"),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 24576),
	A_JmpIfComparisonResultIsLesser(["ACTION_352_transfer_to_xyzf_36"]),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 45056),
	A_JmpIfComparisonResultIsLesser(["ACTION_352_transfer_to_xyzf_40"]),
	A_TransferToXYZF(x=1, y=50, z=7, direction=EAST),
	A_WalkSoutheastSteps(7),
	A_SetWalkingSpeed(SLOW),
	A_Jmp(["ACTION_352_pause_60"]),
	A_TransferToXYZF(x=2, y=48, z=7, direction=EAST, identifier="ACTION_352_transfer_to_xyzf_36"),
	A_WalkSoutheastSteps(7),
	A_SetWalkingSpeed(SLOW),
	A_Jmp(["ACTION_352_jmp_if_random_above_128_44"]),
	A_TransferToXYZF(x=3, y=46, z=7, direction=EAST, identifier="ACTION_352_transfer_to_xyzf_40"),
	A_WalkSoutheastSteps(7),
	A_SetWalkingSpeed(SLOW),
	A_Jmp(["ACTION_352_pause_55"]),
	A_JmpIfRandom1of2(["ACTION_352_pause_50"], identifier="ACTION_352_jmp_if_random_above_128_44"),
	A_Pause(6),
	A_WalkNortheastSteps(2),
	A_CompareVarToConst(TIMER_701E, 170),
	A_JmpIfComparisonResultIsLesser(["ACTION_352_set_animation_speed_65"]),
	A_Jmp(["ACTION_352_pause_55"]),
	A_Pause(6, identifier="ACTION_352_pause_50"),
	A_WalkSouthwestSteps(2),
	A_CompareVarToConst(TIMER_701E, 170),
	A_JmpIfComparisonResultIsLesser(["ACTION_352_set_animation_speed_65"]),
	A_Jmp(["ACTION_352_pause_60"]),
	A_Pause(6, identifier="ACTION_352_pause_55"),
	A_WalkSouthwestSteps(2),
	A_CompareVarToConst(TIMER_701E, 170),
	A_JmpIfComparisonResultIsLesser(["ACTION_352_set_animation_speed_65"]),
	A_Jmp(["ACTION_352_jmp_if_random_above_128_44"]),
	A_Pause(6, identifier="ACTION_352_pause_60"),
	A_WalkNortheastSteps(2),
	A_CompareVarToConst(TIMER_701E, 170),
	A_JmpIfComparisonResultIsLesser(["ACTION_352_set_animation_speed_65"]),
	A_Jmp(["ACTION_352_jmp_if_random_above_128_44"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_352_set_animation_speed_65"),
	A_WalkNorthwestSteps(7),
	A_Jmp(["ACTION_352_object_memory_clear_bit_0"]),
	A_ReturnQueue(identifier="ACTION_352_ret_68")
])
