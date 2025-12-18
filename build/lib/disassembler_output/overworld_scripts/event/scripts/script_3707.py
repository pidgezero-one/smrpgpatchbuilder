# E3707_NIMBUS_CASTLE_WEST_STAIRCASE_LOADER

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
	JmpIfBitClear(TEMP_704C_0, ["EVENT_3707_jmp_if_object_trigger_disabled_2"]),
	SetBit(GUEST_DROPPED_OFF),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ["EVENT_3707_jmp_if_object_trigger_disabled_4"], identifier="EVENT_3707_jmp_if_object_trigger_disabled_2"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff()
	]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ["EVENT_3707_apply_solidity_mod_7"], identifier="EVENT_3707_jmp_if_object_trigger_disabled_4"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, mod_id=1, identifier="EVENT_3707_apply_solidity_mod_7"),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3584_ret_0"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_0, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ["EVENT_3707_clear_bit_14"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_1, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ["EVENT_3707_clear_bit_14"]),
	Jmp(["EVENT_3584_ret_0"]),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_3707_clear_bit_14"),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	Return()
])
