# E2354_EMPTY

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
	JmpIfObjectInSpecificLevel(NPC_8, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, ["EVENT_2354_action_queue_3"]),
	SetBit(UNUSED_708B_1),
	SetBit(UNUSED_708B_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShadowOn()
	], identifier="EVENT_2354_action_queue_3"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetPriority(2),
		A_WalkNortheastPixels(2),
		A_WalkSoutheastPixels(4),
		A_FaceSoutheast(),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetPriority(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkNortheastPixels(8),
		A_FaceSouthwest(),
		A_ShadowOn()
	]),
	FadeInFromBlack(sync=False),
	Return()
])
