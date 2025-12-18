# E2278_BALCONY_LOADER_AFTER_NIMBUS_CASTLE

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
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=4, y=23, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkSouthwestPixels(8),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=22, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=21, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=17, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=4, y=20),
		A_FaceSoutheast(),
		A_SequenceLoopingOn(),
		A_VisibilityOn()
	]),
	RemoveObjectFromCurrentLevel(NPC_3),
	JmpIfBitSet(UNKNOWN_709A_1, ["EVENT_2278_action_queue_33"]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSouthwestPixels(12)
	]),
	Pause(60),
	RunDialog(dialog_id=DI3424_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(6),
		A_Pause(75)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(10),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Pause(45),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(VERY_SLOW),
		A_WalkNortheastPixels(10),
		A_Pause(20),
		A_FixedFCoordOff(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(3)
	]),
	Pause(50),
	RunDialog(dialog_id=DI3425_NIMBUS_BOSS_SWEET_TALKED_BY_TOWER_BOSS, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(3),
		A_Pause(80),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8)
	]),
	Pause(15),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(96),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(96),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(96),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	Pause(90),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNortheastPixels(10)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(20),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(10)
	]),
	Pause(60),
	FadeOutToBlack(sync=False, duration=70),
	EnterArea(room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, face_direction=SOUTHWEST, x=3, y=26, z=0, run_entrance_event=True),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(NORMAL)
	]),
	UnfreezeCamera(),
	SetBit(UNKNOWN_709A_1),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	], identifier="EVENT_2278_action_queue_33"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=4, y=16, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=3, y=17, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_SequenceLoopingOff()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSouthwestPixels(12)
	]),
	Pause(120),
	EnterArea(room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, face_direction=SOUTHWEST, x=3, y=26, z=0, run_entrance_event=True),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(1),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(NORMAL)
	]),
	UnfreezeCamera(),
	Return()
])
