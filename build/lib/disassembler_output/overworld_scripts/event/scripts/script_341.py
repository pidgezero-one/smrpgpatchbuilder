# E0341_EMPTY

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
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_341_summon_to_current_level_9"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(UNKNOWN_7083_5, ["EVENT_341_jmp_if_bit_clear_8"]),
	SetBit(UNKNOWN_7083_5),
	RunBackgroundEvent(event_id=E0342_EMPTY, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitClear(SIGNAL_RING_STAR_PIECE_1, ["EVENT_341_jmp_if_bit_set_13"], identifier="EVENT_341_jmp_if_bit_clear_8"),
	SummonObjectToCurrentLevel(NPC_1, identifier="EVENT_341_summon_to_current_level_9"),
	SummonObjectToCurrentLevel(NPC_2),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_341_summon_to_current_level_9"], identifier="EVENT_341_jmp_if_bit_set_13"),
	Jmp(["EVENT_257_fade_in_from_black_async_0"])
])
