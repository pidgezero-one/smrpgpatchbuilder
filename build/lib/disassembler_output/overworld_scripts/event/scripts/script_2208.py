# E2208_KEEP_1ST_BOSS_ROOM_LOADER

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
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2208_palette_set_4"]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_2209_pause_0"]),
	Return(),
	PaletteSet(palette_set=138, row=1, bit_0=True, bit_1=True, bit_3=True, identifier="EVENT_2208_palette_set_4"),
	PaletteSet(palette_set=139, row=1, bit_0=True, bit_3=True),
	SetSyncActionScript(NPC_0, A0014_FLOATING_CHEST),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=24, y=98),
		A_VisibilityOn(),
		A_FaceSoutheast(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=27, y=104, z=7, direction=EAST),
		A_VisibilityOn()
	]),
	FadeInFromBlack(sync=False),
	Return()
])
