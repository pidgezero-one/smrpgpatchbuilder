# E3593_GET_ITEM_FROM_CHAPEL_HENCHMAN_3

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
	JmpToSubroutine(["EVENT_3593_pause_16"]),
	FreezeAllNPCsUntilReturn(),
	JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_3593_jmp_to_subroutine_11"]),
	SetVarToConst(PRIMARY_TEMP_7000, 2),
	RunDialog(dialog_id=DI2497_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI2096_GOT_SHOES, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	UnfreezeAllNPCs(),
	Inc(TEMP_70AF),
	SetBit(EMPLOYMENT_704C_2),
	Return(),
	JmpToSubroutine(["EVENT_3593_pause_16"], identifier="EVENT_3593_jmp_to_subroutine_11"),
	FreezeAllNPCsUntilReturn(),
	SetVarToConst(PRIMARY_TEMP_7000, 2),
	RunDialog(dialog_id=DI2496_WHERES_THE_CROWN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	Pause(1, identifier="EVENT_3593_pause_16"),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3593_pause_16"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3593_pause_16"]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_3593_pause_16"]),
	Return()
])
