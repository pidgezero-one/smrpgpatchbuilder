# E2430_FOREST_PREMAZE_SAVE_ROOM_LOADER

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
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(UNUSED_708C_6, ["EVENT_2430_clear_bit_3"]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	ClearBit(DIRECTIONAL_7045_0, identifier="EVENT_2430_clear_bit_3"),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ClearBit(DIRECTIONAL_7045_3),
	ClearBit(DIRECTIONAL_7045_4),
	ClearBit(DIRECTIONAL_7045_5),
	ClearBit(DIRECTIONAL_7045_6),
	ClearBit(DIRECTIONAL_7045_7),
	ClearBit(DIRECTIONAL_7046_0),
	SetBit(DIRECTIONAL_7046_1),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSouthPixels(8)
	]),
	JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2430_jmp_if_bit_clear_27"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FreezeAllNPCsUntilReturn(),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	UnfreezeAllNPCs(),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2430_jmp_26"]),
	JmpIfBitSet(UNUSED_708C_6, ["EVENT_2430_jmp_26"]),
	Pause(24),
	Jmp(["EVENT_2430_jmp_if_bit_clear_30"], identifier="EVENT_2430_jmp_26"),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2430_fade_in_from_black_async_29"], identifier="EVENT_2430_jmp_if_bit_clear_27"),
	JmpToEvent(E0081_MARIO_LANDS_SUBROUTINE),
	FadeInFromBlack(sync=False, identifier="EVENT_2430_fade_in_from_black_async_29"),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2430_clear_bit_34"], identifier="EVENT_2430_jmp_if_bit_clear_30"),
	JmpIfBitSet(UNUSED_708C_6, ["EVENT_2430_clear_bit_34"]),
	ClearBit(SIGNAL_RING_BIT),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_2430_clear_bit_34"),
	Return()
])
