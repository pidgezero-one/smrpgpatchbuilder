# E1077_EMPTY

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
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY, identifier="EVENT_1077_set_action_script_0"),
	JmpIfBitClear(UNKNOWN_7093_0, ["EVENT_1077_ret_17"]),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_FaceSouthwest()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2582_TOADOFSKY_UNUSED, above_object=NPC_12, closable=False, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSoutheast()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkToXYCoords(x=16, y=29),
		A_WalkSoutheastSteps(5),
		A_WalkSouthwestSteps(19),
		A_WalkNorthwestSteps(2)
	]),
	Jmp(["EVENT_1071_jmp_if_bit_clear_0"]),
	Return(identifier="EVENT_1077_ret_17")
])
