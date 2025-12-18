#A0722_MINES_ENTRANCE_MOLES

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
	A_JmpIfBitSet(PROGRESSIVE_BOSS_EXP_ENABLED, ["ACTION_722_ret_4"], identifier="ACTION_722_jmp_if_bit_set_0"),
	A_FaceSouthwest7D(arg=0x14),
	A_Pause(1),
	A_Jmp(["ACTION_722_jmp_if_bit_set_0"]),
	A_ReturnQueue(identifier="ACTION_722_ret_4")
])
