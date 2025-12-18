#A0545_SEQUENCE_5_STATIC

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
	A_SetWalkingSpeed(SLOW),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_Pause(624),
	A_WalkNortheastPixels(43),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	A_PlaySound(sound=SO004_JUMP, channel=4),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\xb0\x00\xa8\xff')),
	A_UnknownCommand(bytearray(b'%\x10\x05\xa0\xff')),
	A_Pause(31),
	A_BPL262728(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_WalkNortheastPixels(3),
	A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	A_PlaySound(sound=SO004_JUMP, channel=4),
	A_UnknownCommand(bytearray(b' \x07')),
	A_UnknownCommand(bytearray(b'$\xb0\x00\xa8\xff')),
	A_UnknownCommand(bytearray(b'%\x10\x05\xa0\xff')),
	A_Pause(31),
	A_BPL262728(),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_WalkNortheastPixels(16),
	A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	A_Pause(208),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSouthwestPixels(16),
	A_Pause(16),
	A_SetAllSpeeds(VERY_FAST),
	A_PlaySound(sound=SO024_TAPPING_FEET, channel=4),
	A_Pause(80),
	A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
	A_WalkNortheastPixels(39),
	A_VisibilityOff(),
	A_ReturnQueue()
])
