# E1119_SEASIDE_OCCUPIED_EXTERIOR_LOADER

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
	FreezeCamera(identifier="EVENT_1119_freeze_camera_0"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=14, y=58, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=13, y=56, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=13, y=57, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=14, y=59, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=15, y=60, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=12, y=63, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_0, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_1, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_2, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_3, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_4, A0147_SEASIDE_HENCHMAN),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(1),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(5)
	]),
	Pause(30),
	UnfreezeCamera(),
	RunDialog(dialog_id=DI2850_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_JumpToHeight(85),
		A_Pause(30)
	]),
	UnsyncDialog(),
	CloseDialog(),
	Pause(20),
	RunDialog(dialog_id=DI2851_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI2852_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1119_run_dialog_26"),
	Pause(30),
	JmpIfDialogOptionBSelected(["EVENT_1119_jmp_if_var_equals_const_30"]),
	Jmp(["EVENT_1118_pause_0"]),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 1, ["EVENT_1119_pause_54"], identifier="EVENT_1119_jmp_if_var_equals_const_30"),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 2, ["EVENT_1119_pause_76"]),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 3, ["EVENT_1119_pause_76"]),
	Pause(30),
	RunDialog(dialog_id=DI2853_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNorthwest()
	]),
	Pause(15),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestSteps(15)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(17),
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=33),
	Pause(60),
	RunDialog(dialog_id=DI2854_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=False),
	Pause(100),
	ApplyTileModToLevel(use_alternate=False, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=33),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(5),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(15)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(17),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 1),
	Pause(60),
	RunDialog(dialog_id=DI2855_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_1119_run_dialog_26"]),
	Pause(30, identifier="EVENT_1119_pause_54"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNorthwest()
	]),
	Pause(15),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestSteps(15)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(17),
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(18),
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=33),
	Pause(60),
	RunDialog(dialog_id=DI2856_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=False),
	Pause(100),
	ApplyTileModToLevel(use_alternate=False, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=33),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(15)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(18),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(5),
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(17),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 2),
	Pause(60),
	RunDialog(dialog_id=DI2855_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_1119_run_dialog_26"]),
	Pause(30, identifier="EVENT_1119_pause_76"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNorthwest()
	]),
	Pause(15),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestSteps(15)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(17)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(17)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(18)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(18)
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=33),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkNorthwestSteps(2),
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(1),
		A_VisibilityOff()
	]),
	Pause(60),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 3, ["EVENT_1119_run_dialog_95"]),
	RunDialog(dialog_id=DI2857_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=False),
	Pause(100),
	Jmp(["EVENT_1119_apply_tile_mod_97"]),
	RunDialog(dialog_id=DI2858_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1119_run_dialog_95"),
	Pause(60),
	ApplyTileModToLevel(use_alternate=False, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=33, identifier="EVENT_1119_apply_tile_mod_97"),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(15)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(21),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(5),
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(20),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(10),
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(18),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(15),
		A_TransferToXYZF(x=5, y=40, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(5),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(17),
		A_SetSequenceSpeed(FAST),
		A_FaceSouthwest()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetVarToConst(COIN_CHEST_MULTIPLIER, 3),
	Pause(60),
	RunDialog(dialog_id=DI2855_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_1119_run_dialog_26"])
])
