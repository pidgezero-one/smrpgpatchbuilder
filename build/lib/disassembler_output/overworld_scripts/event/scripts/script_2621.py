# E2621_FACTORY_3RD_ROOM_LOADER

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
	RunBackgroundEvent(event_id=E2620_FACTORY_3RD_ROOM_BACKGROUND_NPCS_BONK_CONVEYOR, return_on_level_exit=True),
	JmpIfObjectNotInSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["EVENT_2621_jmp_if_bit_clear_3"]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2621_fade_in_from_black_async_14"], identifier="EVENT_2621_jmp_if_bit_clear_3"),
	EnableControls([]),
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
		A_Pause(1, identifier="EVENT_2621_action_queue_8_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2621_action_queue_8_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(108),
		A_ShadowOff(),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_2621_action_queue_8_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_2621_action_queue_8_SUBSCRIPT_pause_6"])
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(TEMP_7044_7),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_2621_fade_in_from_black_async_14"),
	Return()
])
