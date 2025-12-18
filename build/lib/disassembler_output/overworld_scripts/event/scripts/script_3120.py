# E3120_EMPTY

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
	JmpIfBitSet(UNUSED_7055_2, ["EVENT_3120_ret_9"]),
	SetBit(UNUSED_7055_2),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_2),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOn(),
		A_FaceNortheast(),
		A_Pause(32),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SequenceLoopingOff(),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(16),
		A_FaceSoutheast(),
		A_Pause(16),
		A_FaceSouthwest(),
		A_Pause(8)
	]),
	Pause(60),
	RunDialog(dialog_id=DI1587_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Walk1StepSouthwest(),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_2),
	Return(identifier="EVENT_3120_ret_9")
])
