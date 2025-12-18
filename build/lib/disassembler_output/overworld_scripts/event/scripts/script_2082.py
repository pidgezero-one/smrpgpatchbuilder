# E2082_EMPTY

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
	Pause(60, identifier="EVENT_2082_pause_0"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=44, z=1, direction=EAST),
		A_FaceSoutheast(),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=5, y=43, z=1, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest(),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=5, y=47, z=1, direction=EAST),
		A_FaceNorthwest(),
		A_Pause(1)
	]),
	JmpIfBitClear(UNUSED_7089_4, ["EVENT_2082_set_action_script_44"]),
	JmpIfBitClear(UNUSED_7089_5, ["EVENT_2082_set_action_script_44"]),
	JmpIfBitClear(UNUSED_7089_6, ["EVENT_2082_set_action_script_44"]),
	SetSyncActionScript(NPC_0, A0568_EMPTY),
	SetSyncActionScript(NPC_1, A0568_EMPTY),
	SetSyncActionScript(NPC_2, A0568_EMPTY),
	JmpIfBitSet(UNKNOWN_7089_7, ["EVENT_2085_pause_0"]),
	Pause(90),
	RunDialog(dialog_id=DI3006_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	SetSyncActionScript(NPC_0, A0872_EMPTY),
	RunDialog(dialog_id=DI3007_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_0, A0873_EMPTY),
	Pause(30),
	SetSyncActionScript(NPC_2, A0874_EMPTY),
	RunDialog(dialog_id=DI3008_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_2, A0875_EMPTY),
	Pause(30),
	SetSyncActionScript(NPC_1, A0870_EMPTY),
	RunDialog(dialog_id=DI3009_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_1, A0871_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI3010_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(45),
	SetSyncActionScript(NPC_0, A0872_EMPTY),
	SetSyncActionScript(NPC_2, A0874_EMPTY),
	SetSyncActionScript(NPC_1, A0870_EMPTY),
	Pause(150),
	SetSyncActionScript(NPC_0, A0873_EMPTY),
	SetSyncActionScript(NPC_2, A0875_EMPTY),
	SetSyncActionScript(NPC_1, A0871_EMPTY),
	Pause(60),
	SetBit(UNKNOWN_7089_7),
	RemoveOneOfItemFromInventory(BigBooFlagItem),
	RemoveOneOfItemFromInventory(DryBonesFlagItem),
	RemoveOneOfItemFromInventory(GreaperFlagItem),
	EquipItemToCharacter(GhostMedalItem, MARIO),
	PlaySound(sound=SO085_FLOWER, channel=6),
	Jmp(["EVENT_2081_run_dialog_87"]),
	Return(),
	SetSyncActionScript(NPC_0, A0568_EMPTY, identifier="EVENT_2082_set_action_script_44"),
	SetSyncActionScript(NPC_1, A0568_EMPTY),
	SetSyncActionScript(NPC_2, A0568_EMPTY),
	Pause(90),
	SetSyncActionScript(NPC_0, A0872_EMPTY),
	JmpIfBitSet(UNUSED_7089_6, ["EVENT_2082_run_dialog_52"]),
	RunDialog(dialog_id=DI2998_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_2082_set_action_script_53"]),
	RunDialog(dialog_id=DI2999_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2082_run_dialog_52"),
	SetSyncActionScript(NPC_0, A0873_EMPTY, identifier="EVENT_2082_set_action_script_53"),
	Pause(30),
	SetSyncActionScript(NPC_2, A0874_EMPTY),
	JmpIfBitSet(UNUSED_7089_5, ["EVENT_2082_run_dialog_59"]),
	RunDialog(dialog_id=DI3000_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_2082_set_action_script_60"]),
	RunDialog(dialog_id=DI3001_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2082_run_dialog_59"),
	SetSyncActionScript(NPC_2, A0875_EMPTY, identifier="EVENT_2082_set_action_script_60"),
	Pause(30),
	SetSyncActionScript(NPC_1, A0870_EMPTY),
	JmpIfBitSet(UNUSED_7089_4, ["EVENT_2082_run_dialog_66"]),
	RunDialog(dialog_id=DI3002_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_2082_set_action_script_67"]),
	RunDialog(dialog_id=DI3003_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2082_run_dialog_66"),
	SetSyncActionScript(NPC_1, A0871_EMPTY, identifier="EVENT_2082_set_action_script_67"),
	Pause(60),
	Jmp(["EVENT_2081_run_dialog_87"])
])
