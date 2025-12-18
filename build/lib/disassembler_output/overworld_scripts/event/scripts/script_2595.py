# E2595_ABYSS_SAVE_ROOM_WITH_CHEST_LOADER

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
	SetVarToConst(FACTORY_FALL_1, 237),
	JmpIfBitClear(UNUSED_708F_4, ["EVENT_2595_jmp_if_bit_clear_3"]),
	SetAsyncActionScript(NPC_1, A0690_OPENING_CHEST),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2595_fade_in_from_black_async_6"], identifier="EVENT_2595_jmp_if_bit_clear_3"),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	Jmp(["EVENT_2595_run_event_as_subroutine_7"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2595_fade_in_from_black_async_6"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR, identifier="EVENT_2595_run_event_as_subroutine_7"),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2595_clear_bit_12"]),
	JmpIfBitSet(UNUSED_708F_4, ["EVENT_2595_clear_bit_12"]),
	ClearBit(SIGNAL_RING_BIT),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_2595_clear_bit_12"),
	Return()
])
