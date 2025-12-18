# E3320_EMPTY

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
	SetBit(MAP_BARREL_VOLCANO),
	SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
	SetBit(MAP_NIMBUS_LAND),
	StopAllBackgroundEvents(),
	UnknownCommand(bytearray(b'\xfdD')),
	UnknownCommand(bytearray(b'\xfdE')),
	JmpIfBitSet(TEMP_7042_1, ["EVENT_3320_jmp_to_event_17"]),
	SetBit(TEMP_7042_1),
	RemoveObjectFromCurrentLevel(MARIO),
	StopMusicFDA2(),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthSteps(17)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(60),
		A_WalkSouthSteps(9)
	]),
	Pause(64),
	RunEventAtReturn(E3321_VOLCANO_ENTER_1ST_ROOM),
	Return(),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3320_jmp_to_event_17")
])
