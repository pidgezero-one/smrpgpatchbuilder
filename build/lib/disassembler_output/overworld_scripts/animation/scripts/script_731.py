#A0731_MINES_CROCO

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
	A_JmpIfBitClear(UNUSED_7057_2, ["ACTION_731_jmp_if_bit_set_55"]),
	A_JmpIfBitClear(UNUSED_7057_3, ["ACTION_730_clear_solidity_bits_54"]),
	A_SetAllSpeeds(FAST),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["ACTION_730_clear_solidity_bits_54"], identifier="ACTION_731_jmp_if_bit_set_4"),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 27, ["ACTION_731_transfer_to_xyzf_30"]),
	A_SetBit(TEMP_7044_6),
	A_JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 23, ["ACTION_731_pause_15"]),
	A_JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 25, ["ACTION_731_pause_18"]),
	A_JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 19, ["ACTION_731_pause_21"]),
	A_JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 21, ["ACTION_731_pause_24"]),
	A_JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 17, ["ACTION_731_pause_27"]),
	A_Pause(100, identifier="ACTION_731_pause_15"),
	A_SetVarToConst(MINES_MIDBOSS_POSITION, 25),
	A_Jmp(["ACTION_731_jmp_if_bit_set_4"]),
	A_Pause(200, identifier="ACTION_731_pause_18"),
	A_SetVarToConst(MINES_MIDBOSS_POSITION, 19),
	A_Jmp(["ACTION_731_jmp_if_bit_set_4"]),
	A_Pause(100, identifier="ACTION_731_pause_21"),
	A_SetVarToConst(MINES_MIDBOSS_POSITION, 21),
	A_Jmp(["ACTION_731_jmp_if_bit_set_4"]),
	A_Pause(200, identifier="ACTION_731_pause_24"),
	A_SetVarToConst(MINES_MIDBOSS_POSITION, 17),
	A_Jmp(["ACTION_731_jmp_if_bit_set_4"]),
	A_Pause(200, identifier="ACTION_731_pause_27"),
	A_SetVarToConst(MINES_MIDBOSS_POSITION, 27),
	A_Jmp(["ACTION_731_jmp_if_bit_set_4"]),
	A_TransferToXYZF(x=10, y=31, z=0, direction=EAST, identifier="ACTION_731_transfer_to_xyzf_30"),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_731_face_northeast_38"]),
	A_SetWalkingSpeed(FASTEST),
	A_WalkNortheastSteps(2),
	A_SetWalkingSpeed(FAST),
	A_SetBit(TEMP_7044_6),
	A_VisibilityOn(),
	A_Jmp(["ACTION_731_object_memory_clear_bit_41"]),
	A_FaceNortheast(identifier="ACTION_731_face_northeast_38"),
	A_VisibilityOn(),
	A_WalkNortheastSteps(2),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="ACTION_731_object_memory_clear_bit_41"),
	A_SetSolidityBits(cant_walk_through=True),
	A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
	A_WalkNortheastSteps(3),
	A_WalkNorthwestSteps(10),
	A_FaceSoutheast(),
	A_SequenceLoopingOn(),
	A_JumpToHeight(48),
	A_Pause(32),
	A_SequenceLoopingOff(),
	A_WalkSouthwestSteps(6),
	A_WalkNorthwestSteps(5),
	A_SetVarToConst(MINES_MIDBOSS_POSITION, 23),
	A_Jmp(["ACTION_731_jmp_if_bit_set_4"]),
	A_JmpIfBitSet(UNUSED_7056_4, ["ACTION_731_ret_59"], identifier="ACTION_731_jmp_if_bit_set_55"),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ReturnQueue(identifier="ACTION_731_ret_59")
])
