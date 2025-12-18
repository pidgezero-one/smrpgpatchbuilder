# E2394_EMPTY

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
	JmpIfBitSet(BUCKET_WARP_DIRECTIONAL_BIT, ["EVENT_2394_ret_14"]),
	SetBit(BUCKET_WARP_DIRECTIONAL_BIT),
	SetSyncActionScript(NPC_1, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Pause(8),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_ShiftToXYCoords(x=5, y=107),
		A_Pause(24),
		A_ShiftToXYCoords(x=0, y=0)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_2394_action_queue_5_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_2394_action_queue_5_SUBSCRIPT_pause_0"]),
		A_ReturnQueue()
	]),
	StopEmbeddedActionScript(MARIO),
	SetSyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	Pause(8),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI3127_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(LazyShellItem),
	Pause(1, identifier="EVENT_2394_pause_12"),
	JmpIfObjectActionScriptIsRunning(MARIO, ["EVENT_2394_pause_12"]),
	Return(identifier="EVENT_2394_ret_14")
])
