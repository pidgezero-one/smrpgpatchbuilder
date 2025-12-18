# E0328_EMPTY

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
	ClearBit(TEMP_7042_0),
	Set0158Bit7Offset(0x0158),
	JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["EVENT_262_jmp_if_bit_clear_0"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_328_jmp_if_bit_set_19"]),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	PauseActionScript(NPC_3),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_328_summon_to_current_level_10"]),
	JmpToEvent(E0262_FADE_MUSIC_ROOM_LOADER),
	SummonObjectToCurrentLevel(NPC_10, identifier="EVENT_328_summon_to_current_level_10"),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=13, y=96, z=8, direction=EAST),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_3, ["EVENT_328_set_action_script_16"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=14, y=110, z=4, direction=EAST),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=7, y=110, z=0, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_4, A0128_WALK_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_3, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS, identifier="EVENT_328_set_action_script_16"),
	PaletteSet(palette_set=17, row=7, bit_0=True),
	JmpToEvent(E0262_FADE_MUSIC_ROOM_LOADER),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_4, ["EVENT_262_jmp_if_bit_clear_0"], identifier="EVENT_328_jmp_if_bit_set_19"),
	PauseActionScript(NPC_8),
	SetSyncActionScript(NPC_8, A0100_EMPTY),
	JmpIfBitClear(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_262_jmp_if_bit_clear_0"]),
	RemoveObjectFromCurrentLevel(NPC_6),
	JmpToEvent(E0262_FADE_MUSIC_ROOM_LOADER)
])
