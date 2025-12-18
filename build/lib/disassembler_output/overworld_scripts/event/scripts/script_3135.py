# E3135_SEWERS_GENERIC_LOADER

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
	ClearBit(TEMP_707C_5),
	SetVarToConst(TIMER_701C, 300),
	StopBackgroundEvent(TIMER_701C),
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 14, ["EVENT_3135_jmp_if_bit_set_7"]),
	JmpToSubroutine(["EVENT_3134_summon_to_level_15"]),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 14),
	Jmp(["EVENT_3135_jmp_if_bit_clear_9"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3135_jmp_if_bit_clear_9"], identifier="EVENT_3135_jmp_if_bit_set_7"),
	JmpToSubroutine(["EVENT_3134_summon_to_level_15"]),
	JmpIfBitClear(SEWER_WATER_LEVEL, ["EVENT_3135_reset_priority_set_14"], identifier="EVENT_3135_jmp_if_bit_clear_9"),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 62, ["EVENT_3135_run_event_as_subroutine_15"]),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[]),
	Jmp(["EVENT_3135_run_event_as_subroutine_15"]),
	ResetPrioritySet(identifier="EVENT_3135_reset_priority_set_14"),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3135_run_event_as_subroutine_15"),
	Set7000ToCurrentLevel(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 333, ["EVENT_3135_ret_32"]),
	JmpIfBitSet(UNUSED_7055_0, ["EVENT_3135_ret_32"]),
	SetBit(UNUSED_7055_0),
	EnableControlsUntilReturn([A, Y]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastSteps(4),
		A_FaceEast()
	]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Walk1StepSoutheast(),
		A_Walk1StepNortheast(),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(24),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_SetBit(TEMP_7043_1),
		A_Pause(1, identifier="EVENT_3135_action_queue_23_SUBSCRIPT_pause_7"),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_3135_action_queue_23_SUBSCRIPT_pause_7"]),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Pause(16),
		A_ResetProperties(),
		A_JumpToHeight(height=108, silent=True),
		A_Walk1StepNorthwest(),
		A_Pause(1, identifier="EVENT_3135_action_queue_23_SUBSCRIPT_pause_14"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3135_action_queue_23_SUBSCRIPT_pause_14"]),
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32),
		A_PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
		A_SetSpriteSequence(index=30, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_DecZCoord1Step(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_3135_action_queue_24_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_0, ["EVENT_3135_action_queue_24_SUBSCRIPT_pause_0"]),
		A_Pause(64),
		A_FaceNortheast(),
		A_Pause(64),
		A_JumpToHeight(108),
		A_Walk1StepNortheast(),
		A_FaceSouth(),
		A_Pause(1),
		A_SetBit(TEMP_7043_3)
	]),
	Pause(1, identifier="EVENT_3135_pause_25"),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3135_pause_25"]),
	RunDialog(dialog_id=DI1584_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_0),
	Pause(1, identifier="EVENT_3135_pause_29"),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3135_pause_29"]),
	Pause(30),
	Return(identifier="EVENT_3135_ret_32")
])
