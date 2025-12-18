# E3730_NIMBUS_CASTLE_OCCUPIED_4_PATH_ROOM_LOADER

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
	RemoveObjectFromSpecificLevel(NPC_13, R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA),
	RemoveObjectFromSpecificLevel(NPC_14, R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3730_set_action_script_16"]),
	JmpIfBitSet(UNKNOWN_STATUE_ROOM_7090_1, ["EVENT_3585_fade_in_from_black_async_0"]),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_5, ["EVENT_3730_palette_set_6"]),
	Jmp(["EVENT_3585_fade_in_from_black_async_0"]),
	PaletteSet(palette_set=111, row=1, bit_3=True, identifier="EVENT_3730_palette_set_6"),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromSpecificLevel(NPC_1, R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=25, y=21, z=3, direction=EAST),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=26, y=22, z=3, direction=EAST),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	FadeInFromBlack(sync=False),
	Return(),
	SetSyncActionScript(NPC_0, A0262_EMPTY, identifier="EVENT_3730_set_action_script_16"),
	SetSyncActionScript(NPC_1, A0263_FIX_F_COORD),
	FadeInFromBlack(sync=False),
	Return()
])
