# E0351_GAMEBOY_KID

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
	JmpIfBitSet(BEETLEMANIA_UNLOCKED, ["EVENT_351_run_dialog_42"]),
	JmpIfBitSet(UNUSED_7090_6, ["EVENT_351_action_queue_28"]),
	CopyVarToVar(from_var=TEMP_70AF, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_351_jmp_if_bit_set_20"]),
	JmpIfRandom1of2(["EVENT_351_jmp_if_bit_set_13"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_351_run_dialog_10"]),
	RunDialog(dialog_id=DI3732_GAMEBOY_KID, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Inc(TEMP_70AF),
	Return(),
	RunDialog(dialog_id=DI3735_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_10"),
	Inc(TEMP_70AF),
	Return(),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_351_run_dialog_17"], identifier="EVENT_351_jmp_if_bit_set_13"),
	RunDialog(dialog_id=DI3733_GAMEBOY_KID, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Inc(TEMP_70AF),
	Return(),
	RunDialog(dialog_id=DI3736_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_17"),
	Inc(TEMP_70AF),
	Return(),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_351_jmp_if_bit_set_25"], identifier="EVENT_351_jmp_if_bit_set_20"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(1),
		A_StartLoopNTimes(7),
		A_WalkSoutheastPixels(2),
		A_WalkNorthwestPixels(2),
		A_EndLoop(),
		A_WalkSoutheastPixels(1),
		A_FixedFCoordOff()
	]),
	RunDialog(dialog_id=DI3734_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(TEMP_70AF, 0),
	Return(),
	JmpIfBitSet(BEETLEMANIA_UNLOCKED, ["EVENT_351_run_dialog_42"], identifier="EVENT_351_jmp_if_bit_set_25"),
	SetBit(UNUSED_7090_6),
	RunDialog(dialog_id=DI3737_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_UnknownCommand(bytearray(b'\xfd$\x17\x00')),
		A_Mem700CAndConst(0x00C0),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["EVENT_351_run_event_as_subroutine_29"]),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=4, y=0, z=0, direction=EAST),
		A_Jmp(["EVENT_351_run_event_as_subroutine_29"])
	], identifier="EVENT_351_action_queue_28"),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_351_run_event_as_subroutine_29"),
	RunDialog(dialog_id=DI3738_GAMEBOY_KID_SELL_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_351_pause_52"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetVarToConst(SECONDARY_TEMP_7024, 500),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_351_run_dialog_56"]),
	PlaySound(sound=SO013_COIN, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 500),
	Dec7000FromCoins(),
	SetBit(BEETLEMANIA_UNLOCKED),
	CloseDialog(),
	RunDialog(dialog_id=DI3742_GAMEBOY_KID_TUTORIAL_PROMPT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_42"),
	JmpIfDialogOptionBSelected(["EVENT_351_pause_48"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI3744_BEETLEMANIA_TUTORIAL, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_351_action_queue_58"]),
	Pause(10, identifier="EVENT_351_pause_48"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI3743_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_351_action_queue_58"]),
	Pause(10, identifier="EVENT_351_pause_52"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI3739_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_351_action_queue_58"]),
	RunDialog(dialog_id=DI3741_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_56"),
	Jmp(["EVENT_351_action_queue_58"]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_TransferToXYZF(x=9, y=91, z=0, direction=EAST),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_351_action_queue_58"),
	Return()
])
