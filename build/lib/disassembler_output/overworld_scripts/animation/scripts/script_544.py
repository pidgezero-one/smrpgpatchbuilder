#A0544_EMPTY

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
	A_ShadowOn(),
	A_SequenceLoopingOn(),
	A_Pause(232),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_UnknownCommand(bytearray(b' \x07')),
	A_EmbeddedAnimationRoutine(bytearray(b'&p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	A_Pause(80),
	A_UnknownCommand(bytearray(b'\xfd\x9c\x17')),
	A_Pause(122),
	A_EmbeddedAnimationRoutine(bytearray(b'&\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
	A_Pause(16),
	A_EmbeddedAnimationRoutine(bytearray(b'&\xc0\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
	A_Pause(99),
	A_BPL262728(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
