# E1626_MOLEVILLE_CARBO_COOKIE_TRADER

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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitSet(MINECART_CLEARED, ["EVENT_1626_store_item_amount_7000_5"]),
	RunDialog(dialog_id=DI1156_BEAN_VALLEY_PLATFORM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	StoreItemAmountTo7000(CarboCookieItem, identifier="EVENT_1626_store_item_amount_7000_5"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_9"]),
	StoreItemAmountTo7000(ShinyStoneItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_11"]),
	RunDialog(dialog_id=DI1158_OFFER_TO_RETURN_SHINY_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_9"),
	Return(),
	RunDialog(dialog_id=DI1159_ASK_TO_TRADE_COOKIE_FOR_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_11"),
	JmpIfDialogOptionBSelected(["EVENT_1626_pause_21"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(ShinyStoneItem),
	RunDialog(dialog_id=DI1160_PURTEND_STORE_DISABLED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, CarboCookieItem),
	SetVarToConst(PRIMARY_TEMP_7000, 1161),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	Return(),
	Pause(10, identifier="EVENT_1626_pause_21"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1148_CARBO_COOKIE_DECLINE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
