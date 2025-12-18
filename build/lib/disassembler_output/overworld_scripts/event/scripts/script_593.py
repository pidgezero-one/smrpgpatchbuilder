# E0593_MINES_BOSS_ROOM_LOADER_AFTER_DEFEAT

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
	JmpIfBitSet(POST_MINES_LEVEL_MODS_COMPLETED, ["EVENT_257_fade_in_from_black_async_0"]),
	PaletteSet(palette_set=81, row=1, bit_3=True),
	PaletteSet(palette_set=82, row=1, bit_2=True, bit_3=True),
	PaletteSet(palette_set=83, row=1, bit_0=True, bit_2=True, bit_3=True),
	Pause(2),
	FadeOutMusicToVolume(duration=0, volume=1),
	StartBattleAtBattlefield(PACK140_PUNCHINELLO_STATIC, BF05_MOLEVILLE_MINES),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
	PlayMusicAtCurrentVolume(M0023_GOTASTARPIECE_PART1),
	Pause(1),
	StopMusicFDA2(),
	RemoveObjectFromSpecificLevel(NPC_0, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_1, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_5, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_6, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_7, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE),
	SetBit(MINES_BOSS_2_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferXYZFPixels(x=0, y=0, z=8, direction=EAST)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=6, y=19, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, mod_id=0),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, mod_id=1),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, mod_id=0),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, mod_id=0),
	Pause(1),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=18, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ShadowOn()
	]),
	Store02To0248(),
	FadeInFromColour(duration=90, colour=WHITE),
	Pause(40),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2)
	]),
	PauseScriptUntilEffectDone(),
	Store00To0248(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(6),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=18, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=18, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_EndLoop(),
		A_Pause(30),
		A_FaceSoutheast(),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0960_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=19, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=19, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_EndLoop(),
		A_Pause(10),
		A_FaceNorthwest(),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	Pause(30),
	RunDialog(dialog_id=DI0961_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(4),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(2)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_WalkWestSteps(1)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(134),
		A_SetWalkingSpeed(FAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastPixels(4),
		A_SequenceLoopingOff(),
		A_ResetProperties(),
		A_Pause(2),
		A_SequenceLoopingOn(),
		A_WalkNorthwestPixels(4),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_Pause(74),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(2),
		A_SetWalkingSpeed(FAST),
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_WalkNorthwestPixels(4),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(8),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_ResetProperties(),
		A_Pause(40),
		A_FaceNorthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(2),
		A_Pause(30),
		A_ShiftZDownPixels(2)
	]),
	RememberLastObject(),
	Pause(60),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FloatingOn(),
		A_Pause(10),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(10),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(10),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_ResetProperties()
	]),
	RememberLastObject(),
	Pause(90),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI0962_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	UnsyncDialog(),
	Pause(10),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepWest(),
		A_FaceSoutheast(),
		A_Pause(10),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(40),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0963_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FaceNortheast(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(4)
	]),
	Pause(12),
	RememberLastObject(),
	SetSyncActionScript(NPC_9, A0120_EMBEDDED_ROUTINE),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(FAST),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(2),
		A_Pause(60),
		A_FaceNortheast(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_ShadowOn()
	]),
	UnknownCommand(bytearray(b'\xfd\x8e\x99\x07\xff')),
	PauseScriptUntilEffectDone(),
	SetSyncActionScript(NPC_8, A0294_EMPTY),
	Pause(30),
	PauseActionScript(NPC_9),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouth(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouth()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetPriority(3),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	Pause(10),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(30),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_ResetProperties(),
		A_FaceSouth()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(10),
		A_FaceSouthwest()
	]),
	Pause(6),
	PlayMusicAtDefaultVolume(M0023_GOTASTARPIECE_PART1),
	RememberLastObject(),
	Pause(120),
	SetSyncActionScript(NPC_4, A0295_EMPTY),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(6),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_VisibilityOff(),
		A_TransferToObjectXY(NPC_9),
		A_TransferXYZFPixels(x=0, y=0, z=16, direction=SOUTHEAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(12),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_SetAllSpeeds(SLOW),
		A_ShiftZDownPixels(10),
		A_VisibilityOff()
	]),
	Pause(30),
	SetSyncActionScript(MARIO, A0296_EMPTY),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(4),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_VisibilityOff(),
		A_TransferToObjectXY(NPC_9),
		A_TransferXYZFPixels(x=0, y=0, z=16, direction=SOUTHEAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(12),
		A_SetAllSpeeds(SLOW),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_ShiftZDownPixels(10),
		A_VisibilityOff()
	]),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=86, row=12),
	Pause(30),
	SetSyncActionScript(NPC_6, A0297_EMPTY),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_VisibilityOff(),
		A_TransferToObjectXY(NPC_9),
		A_TransferXYZFSteps(x=0, y=0, z=4, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(12),
		A_SetAllSpeeds(SLOW),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_ShiftZDownPixels(10),
		A_VisibilityOff()
	]),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=84, row=8),
	Pause(30),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=85, row=13),
	RememberLastObject(),
	Pause(370),
	PauseActionScript(NPC_9),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_BPL262728(),
		A_FloatingOff(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkWestPixels(2),
		A_WalkSouthwestPixels(4)
	]),
	UnknownCommand(bytearray(b'\xfd\x8c2\n0')),
	SetSyncActionScript(NPC_9, A0120_EMBEDDED_ROUTINE),
	Pause(180),
	PauseActionScript(NPC_9),
	ActionQueueSync(target=NPC_9, subscript=[
		A_BPL262728(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(4),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(1)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(4),
		A_TransferToXYZF(x=5, y=29, z=14, direction=EAST),
		A_TransferXYZFPixels(x=2, y=0, z=0, direction=EAST),
		A_SetPriority(3),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(4),
		A_Pause(10),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(120),
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_SetSequenceSpeed(FASTEST)
	]),
	Pause(60),
	PauseActionScript(MARIO),
	FreezeCamera(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(131),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownPixels(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
		A_Pause(2),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(3),
		A_SetSpriteSequence(index=0, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x04\xf0\xff')),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(2),
		A_WalkSouthPixels(4),
		A_FloatingOff(),
		A_BPL262728(),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(6),
		A_SetSpriteSequence(index=2, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=31, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkWestPixels(12)
	]),
	Pause(86),
	PlayMusicAtDefaultVolume(M0024_GOTASTARPIECE_PART2),
	RememberLastObject(),
	UnfreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True)
	]),
	Pause(240),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(6),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpSteps(1),
		A_ShiftZUpPixels(8)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(34),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpSteps(5),
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step()
	]),
	Pause(160),
	UnknownCommand(bytearray(b'\xfd\x8e\x00\n\xce')),
	RememberLastObject(),
	SetSyncActionScript(NPC_9, A0120_EMBEDDED_ROUTINE),
	Pause(90),
	PauseActionScript(NPC_9),
	ActionQueueSync(target=NPC_9, subscript=[
		A_BPL262728(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(8)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferToObjectXY(NPC_9),
		A_TransferXYZFSteps(x=0, y=0, z=5, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(4)
	]),
	RememberLastObject(),
	RunStarPieceSequence(3),
	FadeInMusic(M0033_MOLEVILLE),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromSpecificLevel(NPC_9, R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_7, R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_3, R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_5, R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE),
	UnknownCommand(bytearray(b'\xfd\x8er\x00\x00')),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=6, y=21, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest(),
		A_TransferToXYZF(x=7, y=20, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=6, y=20, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	FadeInFromBlack(sync=False),
	Pause(30),
	RunDialog(dialog_id=DI3212_EMPTY, above_object=NPC_4, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(10),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_WalkNortheastPixels(10),
		A_VisibilityOff()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	RemoveObjectFromSpecificLevel(NPC_4, R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE),
	RemoveObjectFromSpecificLevel(NPC_6, R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE),
	ApplyTileModToLevel(use_alternate=True, room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, mod_id=0),
	SetBit(POST_MINES_LEVEL_MODS_COMPLETED),
	Store01To0248(),
	Return()
])
