# E2406_EMPTY

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
	JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_2406_ret_58"]),
	SetBit(TOWER_BOSS_2_DEFEATED),
	RemoveObjectFromSpecificLevel(NPC_9, R159_STAR_HILL_AREA_04),
	FadeOutMusicFDA3(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=23, y=60)
	]),
	Pause(16),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_OverwriteSolidity(),
		A_WalkToXYCoords(x=26, y=77),
		A_FaceNortheast()
	]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_8),
	Pause(32),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthSteps(3),
		A_WalkNorthPixels(8),
		A_Pause(24)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(112),
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_WalkWestPixels(2)
	]),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	Pause(68),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(80),
		A_Pause(32),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(48),
		A_SetSequenceSpeed(FASTER),
		A_Pause(48),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(48),
		A_SetSequenceSpeed(FASTEST)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(80)
	]),
	Pause(24),
	SetSyncActionScript(NPC_8, A0394_EMPTY),
	Pause(1),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	Pause(544),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkWestPixels(1),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouth()
	]),
	Pause(32),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(16),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(48),
		A_SetSequenceSpeed(FASTER),
		A_Pause(48),
		A_SetSequenceSpeed(FAST),
		A_Pause(48),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(68),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(96),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(8),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSequenceSpeed(FASTER),
		A_Pause(10),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(10),
		A_SetSequenceSpeed(FASTEST),
		A_Pause(56)
	]),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	Pause(48),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(64),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	Pause(464),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(32),
		A_Pause(48),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(16)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(67),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(6)
	]),
	Pause(73),
	FadeOutToBlack(sync=False, duration=32),
	RunStarPieceSequence(4),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_ShiftZDownSteps(4),
		A_WalkSouthSteps(5)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	FadeInFromBlack(sync=False),
	Pause(16),
	Set0158Bit7Offset(0x0158),
	Set0158Bit7Offset(0x015A),
	Set0158Bit7Offset(0x015C),
	UnknownCommand(bytearray(b'\xfd\x8e\x80\x07\x01')),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI3442_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(32),
	SetSyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	Pause(52),
	PlaySound(sound=SO013_COIN, channel=6),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8e\xb2\x07\x01')),
	PauseScriptUntilEffectDone(),
	Clear0158Bit7Offset(0x0158),
	Clear0158Bit7Offset(0x015A),
	Clear0158Bit7Offset(0x015C),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(16),
	PlayMusicAtDefaultVolume(M0034_STARHILL),
	UnfreezeCamera(),
	Return(identifier="EVENT_2406_ret_58")
])
