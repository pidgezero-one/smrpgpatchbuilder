# E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM

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
	JmpIfBitSet(UNKNOWN_7063_5, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_5),
	StopBackgroundEvent(TIMER_701C),
	StopBackgroundEvent(TIMER_701E),
	RunDialog(dialog_id=DI2100_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_TransferToXYZF(x=9, y=97, z=0, direction=EAST),
		A_TransferXYZFPixels(x=16, y=8, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=9, y=98, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=10, y=95, z=0, direction=EAST),
		A_TransferXYZFPixels(x=254, y=4, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=5, y=85)
	]),
	RememberLastObject(),
	Pause(10),
	SetSyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
	RunDialog(dialog_id=DI2101_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	RunDialog(dialog_id=DI2109_RAZ_OUTSIDE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	Store01To0248(),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[1, 3])
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(19)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(19)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(22),
		A_Walk1StepNorth()
	]),
	RunDialog(dialog_id=DI2110_RAINI_OUTSIDE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI2140_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_1),
	Pause(30),
	ClearBit(TEMP_7043_1),
	SetSyncActionScript(NPC_4, A0376_TURN_RANDOMLY_IN_PLACE),
	Pause(30),
	RunDialog(dialog_id=DI2141_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	PauseActionScript(NPC_4),
	StartAsyncEmbeddedActionScript(target=NPC_4, prefix=0xF1, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_TransferToXYZF(x=20, y=75, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(10),
		A_FaceSouthwest()
	]),
	Pause(10),
	SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI2142_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7043_1),
	Pause(30),
	ClearBit(TEMP_7043_1),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2143_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2144_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	StartSyncEmbeddedActionScript(target=NPC_4, prefix=0xF1, subscript=[
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn()
	]),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2060_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StartBattleAtBattlefield(PACK176_BUNDT_FIGHT_STATIC, BF35_MARRYMORE_CHAPEL_SANCTUARY),
	JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
	RestoreAllHP(),
	RestoreAllFP(),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_14),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_15),
	RemoveObjectFromCurrentLevel(NPC_13),
	RemoveObjectFromSpecificLevel(NPC_0, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_1, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_2, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_15, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_13, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_16, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_ResetProperties(),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_Pause(60),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2103_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2104_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(4),
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_FaceNortheast(),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2149_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2150_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_StartLoopNTimes(1),
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_668_action_queue_100_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_668_action_queue_100_SUBSCRIPT_pause_6"]),
		A_EndLoop()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(16),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	UnfreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	RunDialog(dialog_id=DI2302_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	FadeOutMusicToVolume(duration=2, volume=0),
	Pause(60),
	PlayMusicAtDefaultVolume(M0040_NEWPARTNER),
	Pause(24),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	SetAsyncActionScript(MARIO, A0510_EMPTY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	PlayMusicAtDefaultVolume(M0039_MARRYMORE),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ClearBit(TEMP_704C_0),
	SetBit(MARRYMORE_LIBERATED),
	SetBit(MAP_STAR_HILL),
	SetBit(TEMP_7042_1),
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7042_2),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=1),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=2),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=3),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=5),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=7),
	CharacterJoinsParty(TOADSTOOL),
	SummonObjectToSpecificLevel(NPC_0, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
