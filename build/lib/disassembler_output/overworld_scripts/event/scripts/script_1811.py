# E1811_TEMPLE_FOUR_CHEST_ROOM_LOADER

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
	ClearBit(TEMPLE_ELEVATOR_DIRECTION),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_2, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_1811_jmp_if_object_trigger_disabled_3"]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOff()
	]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_1811_run_event_as_subroutine_5"], identifier="EVENT_1811_jmp_if_object_trigger_disabled_3"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff()
	]),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS, identifier="EVENT_1811_run_event_as_subroutine_5"),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1811_clear_bit_12"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_2, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_1811_play_sound_11"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_3, R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM, ["EVENT_1811_clear_bit_12"]),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6, identifier="EVENT_1811_play_sound_11"),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_1811_clear_bit_12"),
	Return()
])
