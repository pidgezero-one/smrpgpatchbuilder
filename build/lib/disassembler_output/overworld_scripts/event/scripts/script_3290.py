# E3290_SHIP_COLLECT_3D_MAZE_PRIZE

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *

script = EventScript([
	JmpIfBitSet(SHIP_MAZE_PRIZE, ["EVENT_3289_ret_6"]),
	SetBit(SHIP_MAZE_PRIZE),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(3),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=False),
		A_Pause(24),
		A_VisibilityOff()
	]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	StopAllBackgroundEvents(),
	SetVarToConst(ITEM_ID, RoyalSyrupItem),
	RunDialog(dialog_id=DI1586_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	RunBackgroundEvent(event_id=E3212_SHIP_3D_MAZE_FORFEIT_LISTENER, return_on_level_exit=True),
	RunDialog(dialog_id=DI1657_3D_MAZE_OVERLAY, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False),
	Return()
])
