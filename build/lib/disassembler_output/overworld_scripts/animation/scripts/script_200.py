#A0200_COIN_SNAKE_TAIL

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
	A_SetSpriteSequence(index=3, looping=False, identifier="ACTION_200_set_sprite_sequence_0"),
	A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6),
	A_Pause(12),
	A_SetSpriteSequence(index=7, is_mold=True, looping=True),
	A_Pause(100),
	A_Jmp(["ACTION_200_set_sprite_sequence_0"])
])
