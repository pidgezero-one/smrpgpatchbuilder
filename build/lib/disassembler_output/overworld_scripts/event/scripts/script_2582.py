# E2582_EMPTY

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
	JmpIfBitSet(UNKNOWN_708D_5, ["EVENT_2582_ret_16"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(NORMAL)
	]),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	SetSyncActionScript(NPC_4, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Set70107015ToObjectXYZ(target=NPC_4),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	CreatePacketAt7010(packet=P019_FROG_COIN_BEING_COLLECTED, destinations=["EVENT_2582_set_bit_11"]),
	AddFrogCoins(1),
	SetBit(UNKNOWN_708D_5, identifier="EVENT_2582_set_bit_11"),
	SummonObjectToSpecificLevel(NPC_4, R252_BEAN_VALLEY_MAIN_AREA),
	SummonObjectToSpecificLevel(NPC_6, R252_BEAN_VALLEY_MAIN_AREA),
	RemoveObjectFromSpecificLevel(NPC_5, R252_BEAN_VALLEY_MAIN_AREA),
	Inc(HIDDEN_CHEST_COUNTER),
	Return(identifier="EVENT_2582_ret_16")
])
