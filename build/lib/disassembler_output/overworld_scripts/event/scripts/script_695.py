# E0695_MARRYMORE_GREEN_KID

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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65, ["EVENT_695_jmp_if_bit_set_6"]),
	RunDialog(dialog_id=DI2120_SHAKING_TOAD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2121_MARRYMORE_FIELD_NPC, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["EVENT_687_pause_0"]),
	Return(),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_695_run_dialog_12"], identifier="EVENT_695_jmp_if_bit_set_6"),
	RunDialog(dialog_id=DI2172_CHAPEL_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7042_3),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_FixedFCoordOff(),
		A_JumpToHeight(height=64, silent=True),
		A_WalkSoutheastSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(10)
	]),
	RemoveObjectFromCurrentLevel(NPC_8),
	Return(),
	RunDialog(dialog_id=DI2052_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_695_run_dialog_12"),
	Return()
])
