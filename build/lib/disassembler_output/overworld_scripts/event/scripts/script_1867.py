# E1867_EMPTY

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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=6, y=25, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	JmpIfBitSet(CRICKET_PIE_EXCHANGED, ["EVENT_1867_jmp_to_event_7"]),
	JmpIfBitClear(STAR_HILL_CHECKED, ["EVENT_1867_jmp_to_event_7"]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=5, y=28, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_SetAllSpeeds(FAST),
		A_StartLoopNTimes(1),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_EndLoop(),
		A_FaceNorthwest(),
		A_Pause(6),
		A_WalkNortheastSteps(3),
		A_FaceNorthwest(),
		A_Pause(6),
		A_FaceSouthwest(),
		A_SetAllSpeeds(NORMAL)
	]),
	SetBit(CRICKET_PIE_EXCHANGED),
	Return(),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1867_jmp_to_event_7")
])
