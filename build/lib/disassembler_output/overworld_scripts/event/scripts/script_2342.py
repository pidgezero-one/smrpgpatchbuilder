# E2342_TOWER_SEESAW_CHEST_CONTD

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
	JmpIfBitClear(TEMP_7043_1, ["EVENT_2342_set_action_script_47"]),
	JmpIfBitSet(TOWER_SEESAW_CHEST_OPENED, ["EVENT_2342_set_action_script_47"]),
	EnableControls([]),
	FreezeCamera(),
	SetSyncActionScript(NPC_4, A0738_TOWER_CHEST_SEESAW_WHEN_ACTIVATED),
	ActionQueueSync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x0f\xe1\xff')),
		A_Pause(56),
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_Pause(199),
		A_BPL262728(),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_ShiftZUpPixels(12)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(32),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(48),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(127),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%P\x0f\x80\xff')),
		A_Pause(74),
		A_BPL262728(),
		A_ShiftToXYCoords(x=18, y=121),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(248),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(15),
		A_Pause(32),
		A_WalkSouthSteps(19)
	]),
	Pause(255),
	SetSyncActionScript(NPC_3, A0739_TOWER_SEESAW_CHEST_ITEM),
	Pause(32),
	SetSyncActionScript(NPC_0, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Pause(8),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkEastPixels(20),
		A_WalkNorthPixels(5),
		A_VisibilityOn(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(NORMAL)
	]),
	StopEmbeddedActionScript(NPC_3),
	PlaySound(sound=SO014_FLOWER, channel=6),
	SetSyncActionScript(NPC_3, A0014_FLOATING_CHEST),
	Pause(16),
	SetSyncActionScript(NPC_4, A0738_TOWER_CHEST_SEESAW_WHEN_ACTIVATED),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(108),
		A_Pause(28)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftZUpPixels(12)
	]),
	Pause(1),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetSyncActionScript(NPC_4, A0739_TOWER_SEESAW_CHEST_ITEM),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Walk1StepSouth()
	]),
	Pause(8),
	PlaySound(sound=SO085_FLOWER, channel=6),
	SetSyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	RunDialog(dialog_id=DI3165_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	PauseActionScript(NPC_3),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_PlaySound(sound=SO019_LONG_FALL, channel=6),
		A_ShiftToXYCoords(x=18, y=123),
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepSoutheast(),
		A_WalkNortheastPixels(5),
		A_WalkWestPixels(6),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(104),
		A_ShiftZDownSteps(19)
	]),
	PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
	SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	Pause(16),
	ActionQueueSync(target=NPC_3, subscript=[
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x80\x00\x80\x00')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(30),
		A_BPL262728(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO012_DIZZINESS, channel=4),
		A_StartLoopNTimes(1),
		A_FaceSoutheast(),
		A_Pause(6),
		A_FaceEast(),
		A_Pause(6),
		A_FaceNortheast(),
		A_Pause(6),
		A_FaceNorth(),
		A_Pause(6),
		A_FaceNorthwest(),
		A_Pause(6),
		A_FaceWest(),
		A_Pause(6),
		A_FaceSouthwest(),
		A_Pause(6),
		A_FaceSouth(),
		A_Pause(6),
		A_EndLoop(),
		A_Pause(48),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_SetSpriteSequence(index=1, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_Pause(80),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_WalkNorthPixels(8),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(TOWER_SEESAW_CHEST_OPENED),
	ClearBit(TEMP_7043_0),
	DisableObjectTriggerInSpecificLevel(NPC_0, R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER),
	RemoveObjectFromCurrentLevel(NPC_3),
	AddToInventory(MasherItem),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	UnfreezeCamera(),
	Return(),
	SetSyncActionScript(NPC_4, A0738_TOWER_CHEST_SEESAW_WHEN_ACTIVATED, identifier="EVENT_2342_set_action_script_47"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(108),
		A_Pause(28)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftZUpPixels(12)
	]),
	Pause(1),
	SetAsyncActionScript(NPC_4, A0739_TOWER_SEESAW_CHEST_ITEM),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2342_freeze_camera_56"]),
	ClearBit(TEMP_7043_0),
	Return(),
	FreezeCamera(identifier="EVENT_2342_freeze_camera_56"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108)
	]),
	UnfreezeCamera(),
	ClearBit(TEMP_7043_0),
	Return()
])
