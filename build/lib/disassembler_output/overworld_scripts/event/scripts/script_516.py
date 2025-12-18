# E0516_OCCUPIED_ROSE_TOWN_GAZ

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
	EnableControlsUntilReturn([]),
	UnsyncDialog(),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_1),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_516_jmp_if_bit_set_11"]),
	JmpIfBitSet(UNUSED_7085_0, ["EVENT_516_jmp_if_bit_set_11"]),
	RunDialog(dialog_id=DI0781_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_516_run_dialog_6"),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	ResumeActionScript(NPC_0),
	ResumeActionScript(NPC_1),
	Return(),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_516_run_dialog_6"], identifier="EVENT_516_jmp_if_bit_set_11"),
	JmpIfRandom1of2(["EVENT_516_run_dialog_15"]),
	RunDialog(dialog_id=DI0779_GAZ, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_516_enable_controls_until_return_16"]),
	RunDialog(dialog_id=DI0780_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_516_run_dialog_15"),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B], identifier="EVENT_516_enable_controls_until_return_16"),
	ResumeActionScript(NPC_0),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_516_set_action_script_21"]),
	ResumeActionScript(NPC_1),
	Jmp(["EVENT_256_ret_0"]),
	SetSyncActionScript(NPC_1, A0625_EMPTY, identifier="EVENT_516_set_action_script_21"),
	Return()
])
