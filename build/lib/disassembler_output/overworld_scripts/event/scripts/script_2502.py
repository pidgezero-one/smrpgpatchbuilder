# E2502_EMPTY

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
	FadeOutMusicToVolume(duration=5, volume=0),
	Pause(80),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(48),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=27, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=27, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_EndLoop(),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True)
	]),
	PlayMusicAtDefaultVolume(M0012_FIGHTAGAINSTBOWSER),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(6)
	]),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True),
		A_SequencePlaybackOff(),
		A_StartLoopNTimes(2),
		A_JumpToHeight(108),
		A_Pause(31),
		A_EndLoop()
	]),
	Pause(128),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthSteps(3)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(6),
		A_WalkNorthPixels(8)
	]),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(144),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(64),
	PlaySound(sound=SO004_JUMP, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=12, y=46, z=2, direction=EAST),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xe0\xfd\x00\xff')),
		A_UnknownCommand(bytearray(b'%\x00\r\x80\xff')),
		A_Pause(44),
		A_BPL262728(),
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(9),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=4),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=True),
		A_Pause(16),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=4),
		A_Pause(16),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=4),
		A_Pause(16),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=4),
		A_Pause(16),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=4)
	]),
	Pause(72),
	RestoreAllHP(),
	RestoreAllFP(),
	StartBattleAtBattlefield(PACK160_BOWYER_AERO_HENCHMEN, BF29_BOWSERS_KEEP_CHANDELIERS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2502_enable_controls_23"]),
	ResetGame(),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_2502_enable_controls_23"),
	AddToInventory(WasteBasketItem),
	RestoreAllHP(),
	RestoreAllFP(),
	ClearBit(EXP_STAR_BIT_1),
	ClearBit(EXP_STAR_BIT_2),
	ClearBit(EXP_STAR_BIT_3),
	ClearBit(EXP_STAR_BIT_4),
	SetVarToConst(COIN_COUNTER_1, 0),
	SetVarToConst(COIN_COUNTER_2, 0),
	SetVarToConst(COIN_COUNTER_3, 0),
	SetVarToConst(COIN_COUNTER_4, 0),
	StopMusicFDA2(),
	ExorCrashesIntoKeep(),
	RunEventSequence(scene=SC16_RUN_WORLD_MAP_EVENT_SEQUENCE, value=0),
	StopMusicFDA2(),
	JmpToEvent(E1393_EMPTY),
	Return()
])
