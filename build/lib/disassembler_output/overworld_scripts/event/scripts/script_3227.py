# E3227_SHIP_CLONE_ROOM_LOADER

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
	JmpIfObjectNotInSpecificLevel(NPC_0, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["EVENT_3227_jmp_if_object_trigger_enabled_5"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_3227_run_background_event_4"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=19, y=117)
	]),
	RunBackgroundEvent(event_id=E3228_SHIP_CLONE_CONTROL, return_on_level_exit=True, identifier="EVENT_3227_run_background_event_4"),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_2, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["EVENT_3227_run_event_as_subroutine_7"], identifier="EVENT_3227_jmp_if_object_trigger_enabled_5"),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSolidityBits(bit_4=True, cant_walk_through=True),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4])
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3227_run_event_as_subroutine_7"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3227_clear_bit_12"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_2, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["EVENT_3227_clear_bit_12"]),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_3227_clear_bit_12"),
	Return()
])
