# E2364_TOWER_TOP_FLOOR_CHEST_ROOM_LOADER

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
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthPixels(8),
		A_WalkNorthwestPixels(1),
		A_WalkSouthwestPixels(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNorthwestPixels(1),
		A_WalkSouthwestPixels(3)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8)
	]),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2364_fade_in_from_black_async_18"]),
	EnableControlsUntilReturn([]),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_ResetProperties(),
		A_FaceSouth(),
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_SetPriority(3)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_2364_action_queue_12_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2364_action_queue_12_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(108),
		A_ShadowOff(),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_2364_action_queue_12_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_2364_action_queue_12_SUBSCRIPT_pause_6"])
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(TEMP_7044_7),
	Jmp(["EVENT_2364_run_event_as_subroutine_19"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2364_fade_in_from_black_async_18"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR, identifier="EVENT_2364_run_event_as_subroutine_19"),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2364_clear_bit_25"]),
	JmpIfBitClear(UNKNOWN_7048_1, ["EVENT_2364_clear_bit_23"]),
	JmpIfBitSet(UNUSED_7091_5, ["EVENT_2364_clear_bit_25"]),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_2364_clear_bit_23"),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_2364_clear_bit_25"),
	Return()
])
