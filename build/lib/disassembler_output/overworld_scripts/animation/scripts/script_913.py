#A0913_KEY_APPEARS_BRIEFLY

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
	A_FloatingOff(),
	A_VisibilityOff(),
	A_Pause(9),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
	A_VisibilityOn(),
	A_FloatingOn(),
	A_JumpToHeight(height=0, silent=True),
	A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	A_SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_913_set_vram_priority_8"),
	A_Pause(1),
	A_Jmp(["ACTION_913_set_vram_priority_8"])
])
