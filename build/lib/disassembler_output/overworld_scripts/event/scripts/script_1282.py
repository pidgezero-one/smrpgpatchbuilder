# E1282_TOWER_BALCONY_LOADER_AFTER_MARRYMORE

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
	EnterArea(room_id=R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, face_direction=NORTHEAST, x=4, y=19, z=0, identifier="EVENT_1282_enter_area_0"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_TransferToXYZF(x=7, y=13, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3),
		A_WalkNortheastPixels(10),
		A_WalkNorthPixels(2),
		A_WalkWestPixels(2),
		A_FaceSouthwest()
	]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_1282_jmp_to_event_17"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=16, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=6, y=18, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=7, y=20, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=4, y=21, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True)
	]),
	RemoveObjectFromCurrentLevel(NPC_3),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSouthwestPixels(12)
	]),
	Pause(60),
	RunDialog(dialog_id=DI2571_TOWER_AWAITING_SPOUSE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(80),
	EnterArea(room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, face_direction=SOUTHWEST, x=3, y=26, z=0, run_entrance_event=True),
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
	Return(),
	JmpToEvent(E2278_BALCONY_LOADER_AFTER_NIMBUS_CASTLE, identifier="EVENT_1282_jmp_to_event_17"),
	Return()
])
