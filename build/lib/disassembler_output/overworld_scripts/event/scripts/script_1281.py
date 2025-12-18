# E1281_EMPTY

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
	EnterArea(room_id=R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, face_direction=NORTHEAST, x=4, y=19, z=0, identifier="EVENT_1281_enter_area_0"),
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
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=4, y=20, z=0, direction=EAST),
		A_WalkNortheastSteps(3),
		A_FaceNortheast(),
		A_SetPriority(3)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSouthwestPixels(12)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=1, looping=False),
		A_Pause(60),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(2)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2827_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	FadeOutMusicToVolume(duration=1, volume=0),
	Pause(45),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(2),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(2),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(2),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4)
	]),
	Pause(60),
	RunDialog(dialog_id=DI2828_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	EnterArea(room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, face_direction=NORTHEAST, x=3, y=26, z=0),
	SetVarToConst(TEMP_7026, 0),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthPixels(22),
		A_WalkEastPixels(7),
		A_SetPriority(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNortheastPixels(5),
		A_WalkNorthwestPixels(4),
		A_FaceSoutheast(),
		A_SetPriority(3),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_WalkEastPixels(8),
		A_WalkNorthPixels(8)
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=2),
	Jmp(["EVENT_1364_freeze_camera_6"])
])
