# E0463_FREE_COOKIE_YOSHI

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
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_463_enable_controls_until_return_16"]),
	RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
	JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_463_jmp_if_bit_set_19"]),
	RunDialog(dialog_id=DI0905_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_463_run_dialog_41"]),
	JmpIfBitSet(GOT_FREE_COOKIES, ["EVENT_463_run_dialog_44"]),
	SetBit(GOT_FREE_COOKIES),
	RunDialog(dialog_id=DI0938_TAKE_MY_COOKIES, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	Pause(10),
	PlaySound(sound=SO063_YOSHI_TALK, channel=6),
	RunDialog(dialog_id=DI0955_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI0956_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B], identifier="EVENT_463_enable_controls_until_return_16"),
	Pause(32),
	Return(),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_463_run_dialog_39"], identifier="EVENT_463_jmp_if_bit_set_19"),
	RunDialog(dialog_id=DI0904_BABY_YOSHI_HINT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	StoreItemAmountTo7000(YoshiCookieItem, identifier="EVENT_463_store_item_amount_7000_21"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=UNKNOWN_70D8, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(SECONDARY_TEMP_7024),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_463_run_dialog_29"]),
	CloseDialog(),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	RunDialog(dialog_id=DI0941_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_463_run_dialog_29"),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 3),
	RunDialog(dialog_id=DI0943_GOT_X_COOKIES, above_object=NPC_12, closable=True, sync=False, multiline=False, use_background=False),
	StartLoopNTimes(2),
	AddToInventory(YoshiCookieItem),
	EndLoop(),
	RunDialog(dialog_id=DI0945_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	RunDialog(dialog_id=DI2367_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_463_run_dialog_39"),
	Jmp(["EVENT_463_store_item_amount_7000_21"]),
	RunDialog(dialog_id=DI0939_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_463_run_dialog_41"),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	RunDialog(dialog_id=DI2368_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_463_run_dialog_44"),
	RunBackgroundEvent(event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, run_as_second_script=True),
	Return()
])
