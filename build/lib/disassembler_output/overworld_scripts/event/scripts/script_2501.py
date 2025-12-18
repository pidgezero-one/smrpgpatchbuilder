# E2501_EMPTY

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
	Pause(12),
	SetSyncActionScript(NPC_10, A0550_EMPTY),
	SetSyncActionScript(NPC_11, A0551_EMPTY),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	Pause(8),
	SetSyncActionScript(NPC_8, A0550_EMPTY),
	SetSyncActionScript(NPC_9, A0551_EMPTY),
	Pause(7),
	SetSyncActionScript(NPC_6, A0550_EMPTY),
	SetSyncActionScript(NPC_7, A0551_EMPTY),
	Pause(6),
	SetSyncActionScript(NPC_4, A0550_EMPTY),
	SetSyncActionScript(NPC_5, A0551_EMPTY),
	Pause(5),
	SetSyncActionScript(NPC_2, A0550_EMPTY),
	SetSyncActionScript(NPC_3, A0551_EMPTY),
	Pause(4),
	SetSyncActionScript(NPC_0, A0550_EMPTY),
	SetSyncActionScript(NPC_1, A0551_EMPTY),
	Pause(32),
	SetBit(TEMP_7043_1),
	Pause(304),
	SetSyncActionScript(NPC_17, A0558_EMPTY),
	Return()
])
