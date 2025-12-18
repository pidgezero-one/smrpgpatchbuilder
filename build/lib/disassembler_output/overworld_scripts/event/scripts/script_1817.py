# E1817_TROOPA_CLIFF_FALL

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
	Pause(1, identifier="EVENT_1817_pause_0"),
	JmpIfMarioInAir(["EVENT_1817_pause_0"]),
	EnableControlsUntilReturn([]),
	Set7016701BToObjectXYZ(target=MARIO, bit_7=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO123_CHAIN_RUMBLING_NOISE, channel=4),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(2),
		A_ShiftZDownSteps(14),
		A_WalkTo70167018(),
		A_FaceSouthwest(),
		A_StopSound()
	]),
	SetVarToConst(TEMP_70AB, 21),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	RunDialog(dialog_id=DI1262_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO123_CHAIN_RUMBLING_NOISE, channel=4),
		A_Pause(1),
		A_FadeOutSoundToVolume(duration=3, volume=0),
		A_WalkToXYCoords(x=24, y=113),
		A_ShiftZUpSteps(14),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest(),
		A_SetAllSpeeds(NORMAL)
	]),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_1),
	Return()
])
