# E2063_SUPER_JUMP_PRIZE_GRANT

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
	Set7000To7FMemVar(0xF8C0),
	JmpIfBitSet(SUPER_JUMP_PRIZE_2_GRANTED, ["EVENT_2063_run_dialog_43"]),
	JmpIfBitSet(SUPER_JUMP_PRIZE_1_GRANTED, ["EVENT_2063_run_dialog_33"]),
	JmpIfBitSet(UNUSED_7092_1, ["EVENT_2063_run_dialog_19"]),
	SetBit(UNUSED_7092_1),
	RunDialog(dialog_id=DI2624_DUPLICATE, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_10"]),
	RunDialog(dialog_id=DI2625_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI2626_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_10"),
	SetVarToConst(ITEM_ID, AttackScarfItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2630),
	RunEventAsSubroutine(E3829_EMPTY),
	SetBit(SUPER_JUMP_PRIZE_1_GRANTED),
	Set7000To7FMemVar(0xF8C0),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_37"]),
	Return(),
	RunDialog(dialog_id=DI2627_SUPERJUMP_RECORD, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_19"),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_24"]),
	RunDialog(dialog_id=DI2628_SUPERJUMP_CHALLENGE, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI2629_SUPER_JUMP_PRIZE_1, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_24"),
	SetVarToConst(ITEM_ID, AttackScarfItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2630),
	RunEventAsSubroutine(E3829_EMPTY),
	SetBit(SUPER_JUMP_PRIZE_1_GRANTED),
	Set7000To7FMemVar(0xF8C0),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_37"]),
	Return(),
	RunDialog(dialog_id=DI2627_SUPERJUMP_RECORD, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_33"),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2063_run_dialog_37"]),
	Return(),
	RunDialog(dialog_id=DI2631_SUPER_JUMP_PRIZE_2, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_37"),
	SetVarToConst(ITEM_ID, SuperSuitItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2633),
	RunEventAsSubroutine(E3829_EMPTY),
	SetBit(SUPER_JUMP_PRIZE_2_GRANTED),
	Return(),
	RunDialog(dialog_id=DI2632_DOG_OUT_OF_PRIZES, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2063_run_dialog_43"),
	Return()
])
