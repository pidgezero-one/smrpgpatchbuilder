# E3117_EMPTY

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
	JmpIfBitSet(UNUSED_707D_6, ["EVENT_3117_ret_15"]),
	PauseActionScript(NPC_0),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_UnknownCommand(bytearray(b'\x9a')),
		A_SetAllSpeeds(NORMAL),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(1),
		A_VisibilityOn(),
		A_PlaySound(sound=SO028_PIPE_ENTRANCE, channel=4),
		A_Pause(4),
		A_ResetProperties(),
		A_AddZCoord1Step(),
		A_Pause(8),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(3),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_SetBit(TEMP_7044_7)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=2, y=25),
		A_FaceNortheast(),
		A_Pause(1)
	]),
	RunDialog(dialog_id=DI1590_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1, identifier="EVENT_3117_pause_5"),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3117_pause_5"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(8),
		A_SequenceLoopingOff(),
		A_SetBit(TEMP_7044_6)
	]),
	RunDialog(dialog_id=DI1591_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1, identifier="EVENT_3117_pause_9"),
	JmpIfBitClear(TEMP_7044_6, ["EVENT_3117_pause_9"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(8),
		A_Walk1StepSouthwest()
	]),
	Pause(8),
	SetBit(UNUSED_707D_6),
	Return(identifier="EVENT_3117_ret_15")
])
