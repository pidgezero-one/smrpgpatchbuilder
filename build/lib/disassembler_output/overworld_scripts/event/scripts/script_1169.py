# E1169_EMPTY

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
	JmpIfBitSet(UNKNOWN_7086_5, ["EVENT_1169_run_dialog_31"]),
	JmpIfBitSet(UNUSED_7086_4, ["EVENT_1169_run_dialog_9"]),
	RunDialog(dialog_id=DI2868_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1169_run_dialog_7"]),
	RunDialog(dialog_id=DI2869_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNUSED_7086_4),
	Return(),
	RunDialog(dialog_id=DI2870_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1169_run_dialog_7"),
	Return(),
	RunDialog(dialog_id=DI2871_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1169_run_dialog_9"),
	RunDialog(dialog_id=DI2872_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1169_run_dialog_7"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 150),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1169_set_var_to_const_17"]),
	RunDialog(dialog_id=DI2873_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1169_run_dialog_15"),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 150, identifier="EVENT_1169_set_var_to_const_17"),
	Dec7000FromCoins(),
	RunDialog(dialog_id=DI2874_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Set7000ToTappedButton(identifier="EVENT_1169_set_7000_to_tapped_button_20"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1169_action_queue_25"]),
	Jmp(["EVENT_1169_set_7000_to_tapped_button_20"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(112),
		A_Pause(60)
	], identifier="EVENT_1169_action_queue_25"),
	RunDialog(dialog_id=DI2875_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7086_5),
	SetBit(UNUSED_7086_3),
	AddToInventory(BeetleBoxItem),
	Return(),
	RunDialog(dialog_id=DI2871_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1169_run_dialog_31"),
	JmpIfBitSet(UNUSED_7086_3, ["EVENT_1169_set_var_to_const_45"]),
	RunDialog(dialog_id=DI2877_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1169_run_dialog_7"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 50),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1169_set_var_to_const_39"]),
	Jmp(["EVENT_1169_run_dialog_15"]),
	SetVarToConst(PRIMARY_TEMP_7000, 50, identifier="EVENT_1169_set_var_to_const_39"),
	Dec7000FromCoins(),
	RunDialog(dialog_id=DI2878_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNUSED_7086_3),
	AddToInventory(BeetleBoxItem),
	Return(),
	SetVarToConst(TEMP_702A, 0, identifier="EVENT_1169_set_var_to_const_45"),
	JmpIfVarEqualsConst(WEDDING_GEAR_COUNTER, 0, ["EVENT_1169_run_dialog_79"]),
	CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000F),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
	VarShiftLeft(PRIMARY_TEMP_7000, 4),
	Mem7000AndConst(0x0007),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
	VarShiftLeft(PRIMARY_TEMP_7000, 7),
	Mem7000AndConst(0x0001),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7028),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_1169_jmp_if_var_equals_const_62"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	AddCoins(PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702A),
	JmpIfVarEqualsConst(TEMP_7026, 0, ["EVENT_1169_copy_var_to_var_67"], identifier="EVENT_1169_jmp_if_var_equals_const_62"),
	SetObjectMemoryToVar(TEMP_7026),
	AddCoins(50),
	AddConstToVar(TEMP_702A, 50),
	EndLoop(),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1169_copy_var_to_var_67"),
	RunDialog(dialog_id=DI2879_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfVarEqualsConst(TEMP_7028, 0, ["EVENT_1169_run_dialog_73"]),
	AddFrogCoins(1),
	RunDialog(dialog_id=DI2880_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	RunDialog(dialog_id=DI2882_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1169_run_dialog_73"),
	ClearBit(UNUSED_7086_3),
	ClearBit(UNUSED_704E_1),
	RemoveOneOfItemFromInventory(BeetleBoxItem2),
	SetVarToConst(WEDDING_GEAR_COUNTER, 0),
	Return(),
	RunDialog(dialog_id=DI2876_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1169_run_dialog_79"),
	Return()
])
