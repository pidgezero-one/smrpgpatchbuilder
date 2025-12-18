# E2496_START_GAME

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
	ApplyTileModToLevel(use_alternate=True, room_id=R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=1),
	ApplyTileModToLevel(use_alternate=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=2),
	ApplyTileModToLevel(use_alternate=True, room_id=R226_FOREST_MAZE_AREA_02, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R433_SMITHY_FACTORY_AREA_01_DUMMY, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R442_SMITHY_FACTORY_AREA_11_CONVEYOR_BELTS_SPAWNING_DRILL_BITS_AND_MACKS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, mod_id=0),
	SetBit(SWITCH_MENU_UNLOCKED),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 8),
	RemoveObjectFromCurrentLevel(MARIO),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkNorthwestPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkSouthPixels(12),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthPixels(2),
		A_WalkNortheastPixels(1),
		A_WalkEastPixels(9),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkNortheastPixels(18),
		A_WalkNorthPixels(2),
		A_WalkEastPixels(1),
		A_WalkNorthwestPixels(2),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkNortheastPixels(14),
		A_WalkNorthPixels(2),
		A_WalkEastPixels(1),
		A_WalkNorthwestPixels(2),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=False, duration=128),
	PlaySound(sound=SO020_LIGHTING_BOLT, channel=6),
	ScreenFlashesWithColour(WHITE),
	Pause(88),
	PlaySound(sound=SO020_LIGHTING_BOLT, channel=6),
	ScreenFlashesWithColour(WHITE),
	Pause(16),
	PlaySound(sound=SO020_LIGHTING_BOLT, channel=6),
	ScreenFlashesWithColour(WHITE),
	Pause(72),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthwestSteps(5),
		A_Pause(224),
		A_UnknownCommand(bytearray(b' \x02')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
		A_Pause(64),
		A_BPL262728()
	]),
	Pause(64),
	PlaySound(sound=SO020_LIGHTING_BOLT, channel=6),
	ScreenFlashesWithColour(WHITE),
	Pause(112),
	PlaySound(sound=SO020_LIGHTING_BOLT, channel=6),
	ScreenFlashesWithColour(WHITE),
	Pause(160),
	PlaySound(sound=SO020_LIGHTING_BOLT, channel=6),
	ScreenFlashesWithColour(WHITE),
	Pause(800),
	CharacterJoinsParty(TOADSTOOL),
	CharacterJoinsParty(BOWSER),
	CharacterJoinsParty(GENO),
	CharacterJoinsParty(MALLOW),
	FadeOutToBlack(sync=False, duration=64),
	EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	EnterArea(room_id=R003_BOWSERS_KEEP_1ST_TIME_AREA_01, face_direction=NORTHEAST, x=4, y=37, z=0, run_entrance_event=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSoutheastPixels(8),
		A_FaceNortheast()
	]),
	FadeInFromBlack(sync=False),
	Return()
])
