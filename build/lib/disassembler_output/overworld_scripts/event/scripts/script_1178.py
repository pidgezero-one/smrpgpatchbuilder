# E1178_SEASIDE_GRANT_SHED_ITEM

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
	Pause(40, identifier="EVENT_1178_pause_0"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_JumpToHeight(height=85, silent=True),
		A_Pause(45)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_JumpToHeight(height=112, silent=True),
		A_Pause(45)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI2883_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI2884_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI2885_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=5, y=20, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(FAST)
	]),
	RunDialog(dialog_id=DI2886_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(1),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2887_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(15),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(2),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2888_DR_TOPPER_PROMPT_TO_QUIT_BUTTON_PUZZLE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	CopyVarToVar(from_var=COIN_CHEST_MULTIPLIER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1178_run_dialog_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1178_run_dialog_42"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1178_run_dialog_47"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1178_run_dialog_52"]),
	RunDialog(dialog_id=DI2889_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1178_run_dialog_37"),
	SetVarToConst(ITEM_ID, FlowerBoxItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2894),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	Jmp(["EVENT_1178_action_queue_58"]),
	RunDialog(dialog_id=DI2890_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1178_run_dialog_42"),
	SetVarToConst(ITEM_ID, FlowerJarItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2895),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	Jmp(["EVENT_1178_action_queue_58"]),
	RunDialog(dialog_id=DI2891_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1178_run_dialog_47"),
	SetVarToConst(ITEM_ID, FlowerTabItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2896),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	Jmp(["EVENT_1178_action_queue_58"]),
	RunDialog(dialog_id=DI2892_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1178_run_dialog_52"),
	PlaySound(sound=SO013_COIN, channel=6),
	RunDialog(dialog_id=DI2897_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	AddCoins(PRIMARY_TEMP_7000),
	Jmp(["EVENT_1178_action_queue_58"]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	], identifier="EVENT_1178_action_queue_58"),
	SetBit(SEASIDE_SHED_EMPTIED),
	Pause(80),
	Return()
])
