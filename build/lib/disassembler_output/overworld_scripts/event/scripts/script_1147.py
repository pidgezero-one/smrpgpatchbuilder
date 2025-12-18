# E1147_SEASIDE_INITIATE_BOSS_FIGHT_ANIMATION

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
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(FAST)
	], identifier="EVENT_1147_action_queue_0"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_PlaySound(sound=SO089_LIT_FUSE, channel=6),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(2),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(2),
		A_EndLoop(),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=6, y=26, height=0),
		A_VisibilityOff()
	]),
	PlaySound(sound=SO148_SURGING_ELECTRICITY, channel=6),
	FadeOutMusicToVolume(duration=8, volume=0),
	PaletteSetMorphs(palette_type=NOTHING, duration=2, palette_set=214, row=11),
	Pause(60),
	ScreenFlashesWithColour(WHITE),
	Pause(20),
	ScreenFlashesWithColour(WHITE),
	Pause(10),
	ScreenFlashesWithColour(WHITE),
	Pause(10),
	ScreenFlashesWithColour(WHITE),
	Pause(10),
	ScreenFlashesWithColour(WHITE),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=6, y=26, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_VisibilityOn()
	]),
	SetSyncActionScript(NPC_7, A0527_SEASIDE_BOSS_TRANSFORM),
	Pause(7),
	ScreenFlashesWithColour(WHITE),
	Pause(7),
	ScreenFlashesWithColour(WHITE),
	SetSyncActionScript(NPC_6, A0527_SEASIDE_BOSS_TRANSFORM),
	Pause(10),
	StartLoopNTimes(6),
	ScreenFlashesWithColour(WHITE),
	Pause(5),
	EndLoop(),
	RemoveObjectFromCurrentLevel(NPC_6),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_VisibilityOn(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False, mirror_sprite=True)
	]),
	PlaySound(sound=SO091_TUMBLING_BOULDERS, channel=6),
	Pause(8),
	ScreenFlashesWithColour(WHITE),
	Pause(10),
	ScreenFlashesWithColour(WHITE),
	Pause(45),
	StartBattleAtBattlefield(PACK180_YARIDOVICH_FIGHT_STATIC, BF37_SEASIDE_TOWN_BEACH),
	JmpIfBitClear(GAME_OVER, ["EVENT_1147_play_music_default_volume_42"]),
	ResetAndChooseGame(),
	PlayMusicAtDefaultVolume(M0005_SEASIDETOWN, identifier="EVENT_1147_play_music_default_volume_42"),
	EnterArea(room_id=R316_SEASIDE_TOWN_BEACH, face_direction=NORTHWEST, x=8, y=30, z=0),
	SetBit(SEASIDE_LIBERATED),
	Inc(EXP_STAR_70D5),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=0, y=8)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=4, y=22),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=4, y=20),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_WalkNorthSteps(1),
		A_WalkNorthPixels(1)
	]),
	JmpToSubroutine(["EVENT_1163_action_queue_0"]),
	Pause(90),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOff()
	]),
	Pause(30),
	UnknownCommand(bytearray(b'\xfd\x8e\x80\x07\x01')),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	RunDialog(dialog_id=DI3443_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOff(),
		A_StartLoopNTimes(6),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(2),
		A_EndLoop(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(30),
		A_PlaySound(sound=SO013_COIN, channel=6),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceSouth(),
		A_FixedFCoordOn(),
		A_SequencePlaybackOff()
	]),
	UnknownCommand(bytearray(b'\xfd\x8e\xb2\x07\x01')),
	PauseScriptUntilEffectDone(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RestoreAllHP(),
	RestoreAllFP(),
	Return()
])
