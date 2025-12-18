# E0399_EMPTY

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
	JmpIfBitSet(BATTLE_DOOR_BOSS_BIT, ["EVENT_399_run_dialog_9"]),
	JmpIfBitSet(TOWER_BOSS_1_STAR_PIECE, ["EVENT_399_run_dialog_11"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, ["EVENT_399_run_dialog_7"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, ["EVENT_399_run_dialog_7"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_2, R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT, ["EVENT_399_run_dialog_7"]),
	RunDialog(dialog_id=DI0650_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0689_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_399_run_dialog_7"),
	Return(),
	RunDialog(dialog_id=DI3756_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_399_run_dialog_9"),
	Return(),
	RunDialog(dialog_id=DI3749_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_399_run_dialog_11"),
	RunDialog(dialog_id=DI3750_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_VisibilityOff()
	]),
	SetBit(SMITHY_BOSS_HUNT_WIN_CONDITION),
	Return()
])
