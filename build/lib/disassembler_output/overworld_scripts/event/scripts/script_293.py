# E0293_WALLET_TOAD_1

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
	JmpIfBitSet(WALLET_SOLD, ["EVENT_395_run_dialog_37"], identifier="EVENT_293_jmp_if_bit_set_0"),
	JmpIfBitSet(WALLET_RETURNED, ["EVENT_293_run_dialog_45"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_293_jmp_if_bit_clear_30"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_395_jmp_if_bit_set_0"]),
	PauseActionScript(MEM_70A8),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_293_pause_action_script_20"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_293_pause_action_script_20"]),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_293_run_dialog_10"]),
	RunDialog(dialog_id=DI0532_EMPTY, above_object=NPC_3, closable=False, sync=True, multiline=True, use_background=True, identifier="EVENT_293_run_dialog_8"),
	Jmp(["EVENT_293_action_queue_11"]),
	RunDialog(dialog_id=DI0064_GOT_AN_70A7_AUTO_TERMINATE, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_293_run_dialog_10"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_JmpIfBitSet(TEMP_7043_6, ["EVENT_293_action_queue_11_SUBSCRIPT_start_loop_n_times_6"]),
		A_Set700CToObjectCoord(target_npc=NPC_3, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0007),
		A_FaceEast7C(),
		A_Pause(48),
		A_StartLoopNTimes(1, identifier="EVENT_293_action_queue_11_SUBSCRIPT_start_loop_n_times_6"),
		A_AddConstToVar(PRIMARY_TEMP_700C, 6),
		A_Mem700CAndConst(0x0007),
		A_FaceEast7C(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0007),
		A_FaceEast7C(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_AddConstToVar(PRIMARY_TEMP_700C, 6),
		A_Mem700CAndConst(0x0007),
		A_FaceEast7C(),
		A_Pause(4),
		A_EndLoop(),
		A_FaceMario()
	], identifier="EVENT_293_action_queue_11"),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_293_remember_last_object_15"]),
	RunDialog(dialog_id=DI0065_GOT_AN_70A7_AWAIT_TERMINATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_6),
	RememberLastObject(identifier="EVENT_293_remember_last_object_15"),
	UnsyncDialog(),
	CloseDialog(),
	ResumeActionScript(MEM_70A8),
	Return(),
	PauseActionScript(MEM_70A8, identifier="EVENT_293_pause_action_script_20"),
	SetSyncActionScript(MEM_70A8, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0578_WALLET_GUY_INTRO, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	PauseActionScript(MEM_70A8),
	Pause(1, identifier="EVENT_293_pause_24"),
	JmpIfObjectInAir(MEM_70A8, ["EVENT_293_pause_24"]),
	RunDialog(dialog_id=DI0579_WALLET_GUY_PROMISE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartAsyncEmbeddedActionScript(target=MEM_70A8, prefix=0xF1, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(MEM_70A8, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	Return(),
	JmpIfBitClear(REFUSED_TO_RETURN_WALLET, ["EVENT_395_jmp_if_bit_set_0"], identifier="EVENT_293_jmp_if_bit_clear_30"),
	RunDialog(dialog_id=DI2231_WALLET_GUY_LATER_REWARD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	JmpIfBitSet(TREASURE_HUNTER_HOUSE_PRIZE, ["EVENT_293_set_var_to_const_40"]),
	AddFrogCoins(1),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	SetBit(TREASURE_HUNTER_HOUSE_PRIZE),
	RunDialog(dialog_id=DI2243_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	SetBit(WALLET_RETURNED),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 524, identifier="EVENT_293_set_var_to_const_40"),
	SetVarToConst(ITEM_ID, FlowerJarItem),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	SetBit(WALLET_RETURNED),
	Return(),
	RunDialog(dialog_id=DI2242_TROOPA_CLIFF_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_293_run_dialog_45"),
	Return()
])
