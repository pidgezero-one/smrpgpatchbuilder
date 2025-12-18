# E1408_MARIOS_PAD_EXTERIOR_LOADER

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
	SetBit(MAP_MARIOS_PAD),
	JmpIfBitClear(TEMP_7042_0, ["EVENT_1408_action_queue_3"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R016_MARIOS_PAD, mod_id=33),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_ReturnQueue()
	], identifier="EVENT_1408_action_queue_3"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_ReturnQueue()
	]),
	JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_1408_ret_12"]),
	JmpIfBitSet(UNUSED_7053_1, ["EVENT_1408_play_music_default_volume_13"]),
	PlayMusicAtDefaultVolume(M0014_MARIO_SPAD),
	RemoveObjectFromCurrentLevel(NPC_2),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1408_run_event_as_subroutine_25"]),
	JmpIfBitSet(UNKNOWN_7053_0, ["EVENT_1408_reset_coords_19"]),
	FadeInFromBlack(sync=False),
	Return(identifier="EVENT_1408_ret_12"),
	PlayMusicAtDefaultVolume(M0014_MARIO_SPAD, identifier="EVENT_1408_play_music_default_volume_13"),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_1),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1408_run_event_as_subroutine_25"]),
	FadeInFromBlack(sync=False),
	Return(),
	ResetCoords(NPC_1, identifier="EVENT_1408_reset_coords_19"),
	Pause(1),
	SetSyncActionScript(NPC_1, A0146_EMPTY),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1408_run_event_as_subroutine_25"]),
	FadeInFromBlack(sync=False),
	Return(),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_1408_run_event_as_subroutine_25"),
	Return()
])
