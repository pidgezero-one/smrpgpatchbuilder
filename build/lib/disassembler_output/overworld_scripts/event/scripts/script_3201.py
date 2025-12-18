# E3201_MINES_1ST_BOSS_FIGHT

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
	JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["EVENT_3201_run_dialog_26"]),
	SetBit(TEMP_7043_0),
	SetVarToConst(BATTLE_PACK_ID, 164),
	RunEventAsSubroutine(E0018_FIGHT_DO_NOT_REMOVE),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3201_run_dialog_26"]),
	SetBit(MINES_BOSS_1_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000),
	VarShiftLeft(PRIMARY_TEMP_7000, 248),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_1, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(SECONDARY_TEMP_7024),
	AddCoins(PRIMARY_TEMP_7000),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(56),
		A_Pause(32),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ReturnQueue()
	]),
	ResumeActionScript(MEM_70A8),
	Set7000ToCurrentLevel(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 277, ["EVENT_3201_jmp_if_var_not_equals_short_20"]),
	JmpIfBitSet(MINES_HENCHMAN_LEFT_DEFEATED, ["EVENT_3201_run_dialog_26"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetBit(TEMP_7043_1),
		A_Jmp(["EVENT_3192_action_queue_4_SUBSCRIPT_object_memory_set_bit_0"])
	]),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 283, ["EVENT_3201_jmp_if_var_not_equals_short_23"], identifier="EVENT_3201_jmp_if_var_not_equals_short_20"),
	JmpIfBitSet(MINES_HENCHMAN_RIGHT_DEFEATED, ["EVENT_3201_run_dialog_26"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetBit(TEMP_7043_1),
		A_Jmp(["EVENT_3193_action_queue_4_SUBSCRIPT_object_memory_set_bit_0"])
	]),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 273, ["EVENT_3201_run_dialog_26"], identifier="EVENT_3201_jmp_if_var_not_equals_short_23"),
	JmpIfBitSet(MINES_HENCHMAN_MIDDLE_DEFEATED, ["EVENT_3201_run_dialog_26"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetBit(TEMP_7043_1),
		A_Jmp(["EVENT_3194_action_queue_4_SUBSCRIPT_pause_0"])
	]),
	RunDialog(dialog_id=DI1647_EMPTY, above_object=BOWSER, closable=False, sync=True, multiline=True, use_background=False, identifier="EVENT_3201_run_dialog_26"),
	AddToInventory(BambinoBombItem),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_Pause(32),
		A_StartLoopNTimes(15),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(32),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_ResetProperties()
	]),
	CloseDialog(),
	ClearBit(TEMP_7043_0),
	Return()
])
