# E0677_MARRYMORE_UNOCCUPIED_SANCTUARY_LOADER

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
	ActionQueueAsync(target=NPC_8, subscript=[
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST)
	]),
	Pause(1),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferXYZFPixels(x=4, y=4, z=0, direction=EAST)
	]),
	JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_677_summon_to_current_level_8"]),
	JmpIfBitClear(TEMP_7042_3, ["EVENT_677_fade_in_from_black_async_6"]),
	SetSyncActionScript(NPC_8, A0119_SLOW_SEQUENCE_LOOP),
	FadeInFromBlack(sync=False, identifier="EVENT_677_fade_in_from_black_async_6"),
	Return(),
	SummonObjectToCurrentLevel(NPC_11, identifier="EVENT_677_summon_to_current_level_8"),
	SummonObjectToCurrentLevel(NPC_12),
	SummonObjectToCurrentLevel(NPC_9),
	SummonObjectToCurrentLevel(NPC_6),
	ActionQueueSync(target=NPC_9, subscript=[
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=18, y=88, z=0, direction=EAST),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=17, y=76, z=0, direction=EAST),
		A_TransferXYZFPixels(x=2, y=252, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=22, y=73, z=2, direction=EAST)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferXYZFPixels(x=2, y=252, z=0, direction=EAST)
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_6, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_12, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_11, A0119_SLOW_SEQUENCE_LOOP),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=0, y=120, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	FadeInFromBlack(sync=False),
	Return()
])
