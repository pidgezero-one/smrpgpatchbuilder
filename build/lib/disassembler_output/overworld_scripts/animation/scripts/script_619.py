#A0619_MINES_CENTER_CROOK

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
	A_Set700CToPressedButton(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_617_visibility_off_10"]),
	A_JmpIfBitSet(MINES_HENCHMAN_MIDDLE_DEFEATED, ["ACTION_617_visibility_off_10"]),
	A_JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["ACTION_617_visibility_off_10"]),
	A_JmpIfBitClear(UNUSED_7057_3, ["ACTION_617_visibility_off_10"]),
	A_TransferToXYZF(x=7, y=47, z=0, direction=EAST),
	A_WalkSouthPixels(4),
	A_FaceSouthwest(),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
