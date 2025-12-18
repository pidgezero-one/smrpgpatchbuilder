# E3340_VOLCANO_3RD_BOSS_PATH_ROOM_LOADER

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
	JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["EVENT_3340_ret_15"]),
	SetBit(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_VisibilityOn(),
		A_Pause(1, identifier="EVENT_3340_action_queue_2_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3340_action_queue_2_SUBSCRIPT_pause_3"]),
		A_JumpToHeight(40),
		A_Pause(20)
	]),
	SetBit(TEMP_7044_0),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_1, destinations=["EVENT_3340_pause_5"]),
	Pause(8, identifier="EVENT_3340_pause_5"),
	SummonObjectToCurrentLevel(NPC_1),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(24),
		A_FaceSouthwest(),
		A_Pause(16),
		A_JumpToHeight(32),
		A_Pause(16),
		A_JumpToHeight(height=32, silent=True)
	]),
	RunDialog(dialog_id=DI1819_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(32),
	ClearBit(TEMP_7044_0),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_1, destinations=["EVENT_3340_create_packet_at_npc_coords_14"]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_0, destinations=["EVENT_3340_ret_15"], identifier="EVENT_3340_create_packet_at_npc_coords_14"),
	Return(identifier="EVENT_3340_ret_15")
])
