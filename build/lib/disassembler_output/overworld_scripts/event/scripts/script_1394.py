# E1394_FOUR_DIGIT_COIN_VALUE_HANDLER

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
	JmpIfBitSet(UNKNOWN_7053_0, ["EVENT_1394_run_dialog_19"]),
	PauseActionScript(NPC_1),
	RunDialog(dialog_id=DI2760_FROGFUCIUS_MIDAS_HINT, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SequenceLoopingOff(),
		A_FaceSouthwest7D(arg=0x00),
		A_TurnClockwise45DegreesNTimes(4),
		A_Pause(70),
		A_TurnClockwise45DegreesNTimes(4),
		A_FixedFCoordOn(),
		A_TurnClockwise45DegreesNTimes(4),
		A_Pause(5),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkFDirectionPixels(10)
	]),
	Pause(35),
	RunDialog(dialog_id=DI2761_FROGFUCIUS_ROSE_WAY_HINT, above_object=NPC_1, closable=True, sync=True, multiline=True, use_background=True),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceSouthwest7D(arg=0x00),
		A_JumpToHeight(48)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	UnsyncDialog(),
	CloseDialog(),
	ResetCoords(NPC_1),
	Pause(1),
	SetSyncActionScript(NPC_1, A0146_EMPTY),
	SetBit(UNKNOWN_7053_0),
	SetBit(UNUSED_MAP_DIRECTIONAL),
	SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_MARIOS_PAD),
	Return(),
	RunDialog(dialog_id=DI2762_FROGFUCIUS_PIPE_VAULT_HINT, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1394_run_dialog_19"),
	Return()
])
