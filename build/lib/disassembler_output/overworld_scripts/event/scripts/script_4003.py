# E4003_CLONE_RESERVED

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
	JmpIfBitSet(UNKNOWN_709D_3, ["EVENT_4003_ret_9"]),
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_4003_ret_9"]),
	SummonObjectToCurrentLevel(NPC_16),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=15, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI0673_LOTS_OF_NOISE_OUT_THERE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, looping=True),
		A_Pause(70),
		A_SetSpriteSequence(index=18, is_mold=True, looping=True),
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI0675_SHAKEN_NOT_STIRRED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8),
		A_VisibilityOff()
	]),
	SetBit(UNKNOWN_709D_3),
	Return(identifier="EVENT_4003_ret_9")
])
