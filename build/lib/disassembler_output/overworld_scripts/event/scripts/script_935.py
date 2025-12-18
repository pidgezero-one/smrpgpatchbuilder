# E0935_MARRYMORE_INN_REGULAR_ROOM_LOADER

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
	JmpIfObjectNotInSpecificLevel(NPC_1, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_935_jmp_if_object_trigger_disabled_2"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R009_MARRYMORE_INN_REGULAR_ROOM, mod_id=33),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_935_jmp_if_bit_set_4"], identifier="EVENT_935_jmp_if_object_trigger_disabled_2"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff()
	]),
	JmpIfBitSet(MARRYMORE_REGULAR_INN, ["EVENT_256_ret_0"], identifier="EVENT_935_jmp_if_bit_set_4"),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_256_ret_0"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_256_ret_0"]),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT),
	Return()
])
