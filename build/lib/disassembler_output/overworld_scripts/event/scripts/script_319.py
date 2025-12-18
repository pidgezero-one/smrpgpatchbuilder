# E0319_TOADSTOOL_ANTECHAMBER_LOADER

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
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_319_summon_to_current_level_4"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitClear(SIGNAL_RING_STAR_PIECE_1, ["EVENT_319_jmp_if_bit_set_7"]),
	SummonObjectToCurrentLevel(NPC_0, identifier="EVENT_319_summon_to_current_level_4"),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_319_summon_to_current_level_4"], identifier="EVENT_319_jmp_if_bit_set_7"),
	JmpToEvent(E0257_FADE_IN_ASYNC)
])
