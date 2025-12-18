# E0331_EMPTY

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
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_3, ["EVENT_331_action_queue_136"]),
	PauseActionScript(NPC_4),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=12, y=98),
		A_WalkNortheastPixels(4)
	]),
	FreezeCamera(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_BounceToXYWithHeight(x=9, y=86, height=13)
	]),
	StartAsyncEmbeddedActionScript(target=NPC_4, prefix=0xF1, subscript=[
		
	]),
	SetSyncActionScript(NPC_4, A0097_EMPTY),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0570_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(20),
	FadeOutSoundToVolume(duration=2, volume=0),
	Set0158Bit7Offset(0x015A),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=41, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=42, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=43, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=44, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=45, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=46, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=47, row=7),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	RunDialog(dialog_id=DI0571_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0593_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=False),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(40),
		A_ResetProperties()
	]),
	SetSyncActionScript(NPC_10, A0096_EMPTY),
	Pause(30),
	RunDialog(dialog_id=DI0574_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(60),
	Clear0158Bit7Offset(0x015A),
	PauseActionScript(NPC_10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_331_action_queue_36_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_10, ["EVENT_331_action_queue_36_SUBSCRIPT_pause_2"]),
		A_Pause(60),
		A_ResetProperties(),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0575_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	UnsyncActionScript(NPC_4),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceWest()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0576_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108)
	]),
	Pause(1, identifier="EVENT_331_pause_47"),
	JmpIfMarioInAir(["EVENT_331_pause_47"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI0577_EMPTY, above_object=MEM_70A8, closable=True, sync=True, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_331_action_queue_51_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(NPC_10, ["EVENT_331_action_queue_51_SUBSCRIPT_pause_3"])
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	Pause(60),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0581_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0582_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(50),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0583_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_331_fade_out_sound_to_volume_95"]),
	CloseDialog(identifier="EVENT_331_close_dialog_62"),
	Pause(30),
	RememberLastObject(),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True),
		A_ShiftZUpPixels(10),
		A_SetWalkingSpeed(FAST),
		A_SetSpriteSequence(index=7, is_mold=True, looping=True),
		A_ShiftZUpPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, looping=True),
		A_DecZCoord1Step(),
		A_Pause(40),
		A_SetWalkingSpeed(NORMAL),
		A_FaceSouthwest(),
		A_ResetProperties(),
		A_WalkSouthwestPixels(18),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouth()
	]),
	RemoveObjectFromCurrentLevel(NPC_10),
	CharacterJoinsParty(MALLOW),
	RunDialog(dialog_id=DI0584_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	FadeOutMusicToVolume(duration=2, volume=0),
	Pause(60),
	PlayMusicAtDefaultVolume(M0040_NEWPARTNER),
	Pause(24),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(6),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	SetAsyncActionScript(MARIO, A0510_EMPTY),
	PlayMusicAtDefaultVolume(M0002_MUSHROOMKINGDOM),
	Pause(3),
	ClearBit(SIGNAL_RING_STAR_PIECE_1),
	SetBit(SIGNAL_RING_STAR_PIECE_2),
	ClearBit(SIGNAL_RING_STAR_PIECE_3),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_5),
	SummonObjectToCurrentLevel(NPC_6),
	SetSyncActionScript(NPC_2, A0128_WALK_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_5, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_6, A0064_KINGDOM_FAST_KID),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	PauseActionScript(NPC_8),
	SetSyncActionScript(NPC_8, A0100_EMPTY),
	ClearBit(TEMP_7043_1),
	UnfreezeCamera(),
	Clear0158Bit7Offset(0x015A),
	Return(),
	FadeOutSoundToVolume(duration=1, volume=111, identifier="EVENT_331_fade_out_sound_to_volume_95"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI0585_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_331_set_action_script_104"]),
	Jmp(["EVENT_331_close_dialog_62"]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_331_set_action_script_104"),
	RememberLastObject(),
	PauseActionScript(NPC_10),
	SetSyncActionScript(NPC_10, A0076_EMPTY),
	RunDialog(dialog_id=DI0586_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_331_fade_out_sound_to_volume_111"]),
	Jmp(["EVENT_331_close_dialog_62"]),
	FadeOutSoundToVolume(duration=1, volume=111, identifier="EVENT_331_fade_out_sound_to_volume_111"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	RunDialog(dialog_id=DI0587_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PauseActionScript(NPC_10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_331_action_queue_116_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_10, ["EVENT_331_action_queue_116_SUBSCRIPT_pause_2"])
	]),
	Pause(30),
	PauseActionScript(NPC_10),
	SetSyncActionScript(NPC_10, A0077_EMPTY),
	Set0158Bit7Offset(0x015A),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=17, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=18, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=19, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=20, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=21, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=22, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=23, row=7),
	PlaySound(sound=SO006_RUNNING_WATER, channel=4),
	SetBit(SIGNAL_RING_STAR_PIECE_1),
	SetBit(SIGNAL_RING_STAR_PIECE_3),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	PauseScriptUntilEffectDone(),
	Clear0158Bit7Offset(0x015A),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=12, y=98),
		A_WalkNortheastPixels(4)
	], identifier="EVENT_331_action_queue_136"),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	FadeOutSoundToVolume(duration=2, volume=0),
	Set0158Bit7Offset(0x015A),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=41, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=42, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=43, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=44, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=45, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=46, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=47, row=7),
	RunDialog(dialog_id=DI0589_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_331_fade_out_sound_to_volume_111"]),
	Jmp(["EVENT_331_close_dialog_62"])
])
