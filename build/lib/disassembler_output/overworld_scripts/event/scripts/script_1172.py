# E1172_MUSHROOM_BOY

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
	JmpIfBitSet(UNKNOWN_7087_2, ["EVENT_1172_run_dialog_3"]),
	RunDialog(dialog_id=DI2928_MUSHROOM_BOY_INTRO, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7087_2),
	RunDialog(dialog_id=DI2929_MUSHROOM_BOY_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_3"),
	JmpIfDialogOptionBSelected(["EVENT_1172_run_dialog_35"]),
	StoreItemAmountTo7000(MushroomItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1172_run_dialog_34"]),
	RunDialog(dialog_id=DI2930_MUSHROOM_BOY_CONFIRM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RemoveOneOfItemFromInventory(MushroomItem),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(85),
		A_SequenceLoopingOn()
	]),
	SetVarToRandom(PRIMARY_TEMP_7000, 10000),
	CompareVarToConst(PRIMARY_TEMP_7000, 400),
	JmpIfComparisonResultIsLesser(["EVENT_1172_run_dialog_19"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 1000),
	JmpIfComparisonResultIsLesser(["EVENT_1172_run_dialog_24"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 2400),
	JmpIfComparisonResultIsLesser(["EVENT_1172_run_dialog_29"]),
	RunDialog(dialog_id=DI2931_MUSHROOM_BOY_NO_PRIZE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2934_FLOWER_MUSHROOM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_19"),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2939_RECEIVED_FLOWER_TAB, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(FlowerTabItem),
	Return(),
	RunDialog(dialog_id=DI2933_RIPPIN_MUSHROOM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_24"),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2938_RECEIVED_ROCK_CANDY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(RockCandyItem),
	Return(),
	RunDialog(dialog_id=DI2932_BERRY_MUSHROOM, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_29"),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2937_RECEIVED_MAPLE_SYRUP, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(MapleSyrupItem),
	Return(),
	RunDialog(dialog_id=DI2936_NO_MUSHROOMS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_34"),
	RunDialog(dialog_id=DI2935_MUSHROOM_BOY_GOODBYE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1172_run_dialog_35"),
	Return()
])
