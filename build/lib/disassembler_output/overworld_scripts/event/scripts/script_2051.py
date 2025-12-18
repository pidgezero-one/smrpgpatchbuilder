# E2051_MONSTRO_SHOP_LOADER

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
	JmpIfBitSet(RARE_FROG_COIN_EXCHANGE_AVAILABLE, ["EVENT_2051_action_queue_6"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_BounceToXYWithHeight(x=11, y=5, height=0)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=16, y=16, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_WalkSoutheastPixels(16),
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_ShadowOn()
	]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_2052_pause_0"]),
	Return(),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=15, y=19, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastPixels(2),
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_VisibilityOn()
	], identifier="EVENT_2051_action_queue_6"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=13, y=17, z=2, direction=EAST),
		A_WalkSoutheastPixels(12),
		A_WalkSouthwestPixels(4),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=14, y=18, z=2, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(4),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=14, y=19, z=2, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOn()
	]),
	SetSyncActionScript(NPC_1, A0878_MONSTRO_GOOMBETTE),
	SetSyncActionScript(NPC_0, A0879_MONSTRO_GOOMBETTE),
	SetSyncActionScript(NPC_2, A0879_MONSTRO_GOOMBETTE),
	ApplySolidityModToLevel(permanent=True, room_id=R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, mod_id=0),
	FadeInFromBlack(sync=False),
	Return()
])
