# E1665_EMPTY

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
	DisableObjectTrigger(MEM_70A8),
	EnableControlsUntilReturn([]),
	PauseActionScript(NPC_7),
	ResetCoords(NPC_7),
	SetSyncActionScript(NPC_7, A0353_EMPTY),
	CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(TEMP_702E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=WEDDING_GEAR_COUNTER),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_1665_enable_controls_until_return_12"]),
	RemoveOneOfItemFromInventory(BeetleBoxItem),
	AddToInventory(BeetleBoxItem2),
	SetBit(TEMP_7043_7),
	EnableControlsUntilReturn([B], identifier="EVENT_1665_enable_controls_until_return_12"),
	SetVarToConst(TIMER_701C, 10),
	Return()
])
