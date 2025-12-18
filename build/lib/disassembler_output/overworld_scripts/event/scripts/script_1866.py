# E1866_KEEP_INVISIBLE_FLOOR_CHEST_2

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
	JmpIfBitSet(STAR_HILL_CHECKED, ["EVENT_1866_ret_11"]),
	JmpIfBitClear(UNUSED_7095_2, ["EVENT_1866_ret_11"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkFDirectionPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_WalkSouthSteps(2),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(2),
		A_SequenceLoopingOff()
	]),
	Pause(60),
	RunDialog(dialog_id=DI1281_EMPTY, above_object=BOWSER, closable=False, sync=False, multiline=True, use_background=False),
	Pause(100),
	CloseDialog(),
	FadeOutToBlack(sync=False, duration=40),
	SetBit(STAR_HILL_CHECKED),
	EnterArea(room_id=R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, face_direction=SOUTHWEST, x=25, y=95, z=0, run_entrance_event=True),
	Return(identifier="EVENT_1866_ret_11")
])
