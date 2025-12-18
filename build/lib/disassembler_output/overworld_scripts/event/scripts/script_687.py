# E0687_EMPTY

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
	Pause(10, identifier="EVENT_687_pause_0"),
	RunDialog(dialog_id=DI2155_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	PauseActionScript(NPC_7),
	PauseActionScript(NPC_8),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=13, y=41, height=0)
	]),
	RememberLastObject(),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER, mod_id=0),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(2),
		A_TransferToXYZF(x=18, y=63, z=12, direction=EAST),
		A_FaceNortheast(),
		A_FixedFCoordOn()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetPriority(2),
		A_SequenceLoopingOff(),
		A_TransferToXYZF(x=19, y=64, z=12, direction=EAST),
		A_FaceNortheast(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SequenceLoopingOff(),
		A_JumpToHeight(height=108, silent=True),
		A_SetWalkingSpeed(FASTER),
		A_WalkSouthwestSteps(1),
		A_SetPriority(3),
		A_WalkSouthwestSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSouthwestSteps(3),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepSouthwest(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(12),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_VisibilityOff(),
		A_SetPriority(2),
		A_TransferToXYZF(x=18, y=63, z=12, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_Pause(30),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest7D(arg=0x19),
		A_Pause(10),
		A_FaceSouthwest7D(arg=0x19)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSoutheast(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkToXYCoords(x=16, y=72),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Walk1StepNortheast()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest7D(arg=0x19)
	]),
	Pause(60),
	SetSyncActionScript(MARIO, A0628_EMPTY),
	SetSyncActionScript(NPC_7, A0628_EMPTY),
	SetSyncActionScript(NPC_8, A0628_EMPTY),
	SetSyncActionScript(NPC_2, A0628_EMPTY),
	SetSyncActionScript(NPC_0, A0628_EMPTY),
	SetSyncActionScript(NPC_1, A0628_EMPTY),
	Pause(10),
	RunDialog(dialog_id=DI2122_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_11, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepNortheast()
	]),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=False, room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER, mod_id=0),
	Pause(30),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	SetAsyncActionScript(NPC_7, A0625_EMPTY),
	SetAsyncActionScript(NPC_8, A0625_EMPTY),
	SetAsyncActionScript(NPC_0, A0626_EMPTY),
	SetAsyncActionScript(NPC_1, A0626_EMPTY),
	SetAsyncActionScript(NPC_2, A0627_EMPTY),
	SetSyncActionScript(NPC_7, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_8, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_1, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_2, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_5, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_6, A0376_TURN_RANDOMLY_IN_PLACE),
	RemoveObjectFromSpecificLevel(NPC_11, R005_MARRYMORE_OUTSIDE_DURING_BOOSTER),
	SetBit(MARRYMORE_BACKDOOR_OPEN),
	Return()
])
