# E3591_EMPTY

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
	FadeOutMusicToVolume(duration=1, volume=96),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["EVENT_3591_fade_in_from_black_async_3"]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_3591_fade_in_from_black_async_3"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR, identifier="EVENT_3591_run_event_as_subroutine_4"),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3591_enable_controls_9"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R087_ROSE_TOWN_ITEM_SHOP, ["EVENT_3591_enable_controls_9"]),
	ClearBit(SIGNAL_RING_BIT),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_3591_enable_controls_9"),
	Return()
])
