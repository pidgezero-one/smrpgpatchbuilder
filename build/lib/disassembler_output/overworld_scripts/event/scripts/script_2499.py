# E2499_EMPTY

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
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SetPriority(3),
		A_WalkNortheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SequenceLoopingOn(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SetPriority(3),
		A_WalkEastPixels(48),
		A_WalkNorthPixels(4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SequenceLoopingOn(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SetPriority(3),
		A_WalkEastPixels(16),
		A_WalkNorthPixels(8),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SequenceLoopingOn(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
		A_SetPriority(3),
		A_WalkEastPixels(32),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=False),
	Return()
])
