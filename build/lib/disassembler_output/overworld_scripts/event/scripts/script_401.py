# E0401_GUEST_ROOM_ANTECHAMBER_LOADER

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
	JmpIfBitSet(TEMP_7042_7, ["EVENT_401_remove_from_current_level_11"]),
	JmpIfBitSet(BATTLE_DOOR_BOSS_BIT, ["EVENT_401_action_queue_3"]),
	JmpIfBitSet(SMITHY_BOSS_HUNT_WIN_CONDITION, ["EVENT_401_remove_from_current_level_11"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSoutheastPixels(8),
		A_FaceNortheast()
	], identifier="EVENT_401_action_queue_3"),
	JmpIfBitSet(UNUSED_705E_7, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_401_summon_to_current_level_8"]),
	FadeInFromBlack(sync=False),
	Return(),
	SummonObjectToCurrentLevel(NPC_1, identifier="EVENT_401_summon_to_current_level_8"),
	FadeInFromBlack(sync=False),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_401_remove_from_current_level_11"),
	FadeInFromBlack(sync=False),
	Return()
])
