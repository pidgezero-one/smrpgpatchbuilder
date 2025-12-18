# E2052_EMPTY

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
	Pause(30, identifier="EVENT_2052_pause_0"),
	RunDialog(dialog_id=DI2977_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(1),
		A_PlaySound(sound=SO045_GOOMBA_TAUNT, channel=6),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI2978_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(15),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=13, y=23, z=0, direction=EAST),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkSoutheastPixels(8),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(8)
	]),
	Pause(20),
	RunDialog(dialog_id=DI2979_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(15),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff()
	]),
	Pause(20),
	RunDialog(dialog_id=DI2980_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(6),
		A_TransferToXYZF(x=14, y=16, z=0, direction=EAST),
		A_WalkSoutheastPixels(12),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_VisibilityOn(),
		A_PlaySound(sound=SO077_EXOTIC_BIRD_CALLS, channel=6),
		A_JumpToHeight(112),
		A_WalkSouthwestPixels(20),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=14, y=17, z=0, direction=EAST),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_VisibilityOn(),
		A_JumpToHeight(112),
		A_WalkSouthwestPixels(20),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Pause(8),
		A_TransferToXYZF(x=15, y=18, z=0, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_VisibilityOn(),
		A_JumpToHeight(112),
		A_WalkSouthwestPixels(20),
		A_SequenceLoopingOn(),
		A_FixedFCoordOff()
	]),
	Pause(15),
	RunDialog(dialog_id=DI2981_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(45),
	RunDialog(dialog_id=DI2982_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(15),
	RunDialog(dialog_id=DI2986_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(8),
		A_VisibilityOff()
	]),
	SetBit(RARE_FROG_COIN_EXCHANGE_AVAILABLE),
	SetSyncActionScript(NPC_1, A0878_MONSTRO_GOOMBETTE),
	SetSyncActionScript(NPC_0, A0879_MONSTRO_GOOMBETTE),
	SetSyncActionScript(NPC_2, A0879_MONSTRO_GOOMBETTE),
	ApplySolidityModToLevel(permanent=True, room_id=R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, mod_id=0),
	Return()
])
