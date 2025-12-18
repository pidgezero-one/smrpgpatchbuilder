#A0388_EMPTY

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
	A_SequenceLoopingOn(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_SetPriority(3),
	A_SetSequenceSpeed(NORMAL),
	A_UnknownCommand(bytearray(b' \x07')),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x04\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x04\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x08\x80')),
	A_SetWalkingSpeed(SLOW),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_388_shadow_off_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_388_shadow_off_31"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_388_shadow_off_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_388_shadow_off_31"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_388_shift_z_down_steps_44"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_388_shift_z_down_steps_49"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 26, ["ACTION_388_shift_z_down_steps_44"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_388_shift_z_down_steps_44"]),
	A_ShadowOff(identifier="ACTION_388_shadow_off_18"),
	A_ShiftZDownSteps(8),
	A_BPL262728(),
	A_ShadowOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(32),
	A_SequencePlaybackOn(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_388_set_sprite_sequence_29"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, identifier="ACTION_388_set_sprite_sequence_29"),
	A_ReturnQueue(),
	A_ShadowOff(identifier="ACTION_388_shadow_off_31"),
	A_ShiftZDownSteps(7),
	A_BPL262728(),
	A_ShadowOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(32),
	A_SequencePlaybackOn(),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_388_set_sprite_sequence_42"]),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
	A_ReturnQueue(),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="ACTION_388_set_sprite_sequence_42"),
	A_ReturnQueue(),
	A_ShiftZDownSteps(8, identifier="ACTION_388_shift_z_down_steps_44"),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_ShiftZDownPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_ShiftZDownSteps(7, identifier="ACTION_388_shift_z_down_steps_49"),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_ShiftZDownPixels(8),
	A_VisibilityOff(),
	A_ReturnQueue()
])
