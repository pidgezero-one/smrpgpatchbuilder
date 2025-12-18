# E3011_CLONE_RESERVED

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
	JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_3011_ret_16"]),
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_3011_ret_16"]),
	RunDialog(dialog_id=DI3335_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(ITEM_ID, MuteBombItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3011_ret_16"]),
	Pause(15),
	RunDialog(dialog_id=DI3973_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	ApplySolidityModToLevel(permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0),
	PlaySound(sound=SO081_STAR, channel=6),
	Pause(15),
	RunDialog(dialog_id=DI3337_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromSpecificLevel(NPC_3, R324_MONSTRO_TOWN_OUTSIDE),
	SetBit(UNKNOWN_709E_7),
	Return(identifier="EVENT_3011_ret_16")
])
