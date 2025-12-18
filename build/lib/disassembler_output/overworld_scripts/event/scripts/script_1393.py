# E1393_EMPTY

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
	StopMusicFDA2(),
	PauseActionScript(NPC_1),
	SetBit(BELOME_TEMPLE_OPEN),
	SetBit(UNUSED_MAP_DIRECTIONAL),
	SetBit(MAP_MARIOS_PAD),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=13, y=13, z=0, direction=EAST),
		A_WalkWestPixels(11),
		A_FloatingOff(),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=11, y=38, z=0, direction=EAST),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthSteps(3),
		A_ReturnQueue()
	]),
	FadeInFromBlack(sync=True, duration=149),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(VERY_SLOW),
		A_PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
		A_WalkNorthwestSteps(2),
		A_Pause(20),
		A_PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
		A_Pause(10),
		A_PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
		A_Pause(15),
		A_WalkSoutheastSteps(2),
		A_Pause(45),
		A_PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
		A_WalkNorthwestSteps(1),
		A_Pause(20),
		A_JumpToHeight(80),
		A_Pause(30),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(2),
		A_ReturnQueue()
	]),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetPriority(0),
		A_SetWalkingSpeed(SLOW),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_ShadowOn(),
		A_SequenceLoopingOn(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthPixels(15),
		A_StartLoopNTimes(13),
		A_WalkNorthPixels(3),
		A_WalkEastPixels(1),
		A_EndLoop(),
		A_StartLoopNTimes(16),
		A_WalkNorthPixels(2),
		A_WalkEastPixels(1),
		A_EndLoop(),
		A_StartLoopNTimes(15),
		A_WalkNorthPixels(1),
		A_WalkEastPixels(1),
		A_EndLoop(),
		A_ReturnQueue()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_ReturnQueue()
	]),
	Pause(80),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FASTER),
		A_WalkSouthSteps(3),
		A_PlaySound(sound=SO028_PIPE_ENTRANCE, channel=4),
		A_WalkSouthSteps(2),
		A_VisibilityOff(),
		A_ReturnQueue()
	]),
	Pause(40),
	PlaySound(sound=SO017_OPEN_FRONT_GATE, channel=6),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthPixels(5),
		A_WalkNorthPixels(5),
		A_WalkSouthPixels(5),
		A_WalkNorthPixels(5),
		A_WalkSouthPixels(5),
		A_WalkNorthPixels(5),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_JumpToHeight(128),
		A_Pause(40),
		A_SequenceLoopingOff(),
		A_Pause(40),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(VERY_SLOW),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(1),
		A_SetWalkingSpeed(FASTER),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
		A_WalkNortheastSteps(4),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R016_MARIOS_PAD, mod_id=33),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNortheastSteps(2),
		A_VisibilityOff()
	]),
	SetBit(TEMP_7042_0),
	Pause(50),
	StopMusicFDA2(),
	EnterArea(room_id=R189_MARIOS_PIPEHOUSE, face_direction=SOUTHEAST, x=3, y=13, z=0),
	PaletteSet(palette_set=33, row=7, bit_0=True),
	StopMusicFDA2(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=3, y=9, z=3, direction=EAST),
		A_WalkSouthwestPixels(6),
		A_ShiftZUpPixels(2),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_VisibilityOff(),
		A_FaceNortheast()
	]),
	SetSyncActionScript(MARIO, A0095_PLAYER_GAME_START),
	FreezeCamera(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(2)
	]),
	FadeInFromBlack(sync=False),
	Pause(80),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_TransferToXYZF(x=1, y=17, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceNortheast(),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=4),
		A_Pause(2),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_WalkNortheastSteps(4),
		A_SequencePlaybackOff(),
		A_SetWalkingSpeed(SLOW),
		A_PlaySound(sound=SO018_SUDDEN_STOP, channel=6),
		A_WalkNortheastPixels(9),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8),
		A_Pause(60),
		A_SetSequenceSpeed(NORMAL),
		A_FaceNorthwest()
	]),
	Pause(20),
	RunDialog(dialog_id=DI2759_FROGFUCIUS_CRICKET_JAM_WITHOUT_PIE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequencePlaybackOn(),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(5),
		A_VisibilityOff()
	]),
	PlayMusicAtDefaultVolume(M0014_MARIO_SPAD),
	Pause(1),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(10),
	Set7000ToTappedButton(identifier="EVENT_1393_set_7000_to_tapped_button_47"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1393_pause_action_script_52"]),
	Jmp(["EVENT_1393_set_7000_to_tapped_button_47"]),
	PauseActionScript(MARIO, identifier="EVENT_1393_pause_action_script_52"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_FaceSoutheast(),
		A_ShadowOff(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(69),
		A_FloatingOn(),
		A_WalkSoutheastSteps(2),
		A_Pause(35),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=6),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(1),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_StopSound(),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(30),
	Return()
])
