# E0375_TALK_TO_CHANCELLOR_AFTER_MUSHROOM_KINGDOM_BOSS

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
	PlayMusicAtDefaultVolume(M0002_MUSHROOMKINGDOM, identifier="EVENT_375_play_music_default_volume_0"),
	PauseActionScript(NPC_13),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkToXYCoords(x=17, y=20),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	JmpIfBitSet(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED, ["EVENT_375_action_queue_117"]),
	RunDialog(dialog_id=DI0630_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_375_action_queue_5_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_375_action_queue_5_SUBSCRIPT_pause_0"]),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_BounceToXYWithHeight(x=16, y=30, height=4),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(4),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI0631_EMPTY, above_object=NPC_13, closable=False, sync=True, multiline=True, use_background=True),
	PauseScriptResumeOnNextDialogPageA(),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0632_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	SummonObjectToCurrentLevel(NPC_10),
	SummonObjectToCurrentLevel(NPC_11),
	SummonObjectToCurrentLevel(NPC_12),
	RunDialog(dialog_id=DI0633_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=12, y=35, z=0, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(7),
		A_WalkSoutheastSteps(1),
		A_FaceNortheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(20),
		A_TransferToXYZF(x=12, y=35, z=0, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(5),
		A_WalkSoutheastSteps(3),
		A_FaceNortheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_Pause(40),
		A_TransferToXYZF(x=12, y=35, z=0, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(5),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	RunDialog(dialog_id=DI0643_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_375_run_dialog_25"),
	Pause(10),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_375_action_queue_30"]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties()
	]),
	Jmp(["EVENT_375_pause_31"]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties()
	], identifier="EVENT_375_action_queue_30"),
	Pause(40, identifier="EVENT_375_pause_31"),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_FaceSouthwest()
	]),
	JmpIfBitClear(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED, ["EVENT_375_run_dialog_35"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI0644_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_375_run_dialog_35"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	FadeOutToBlack(sync=True, duration=100),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	JmpIfBitClear(INVISIBLE_ITEMS_ANYWHERE_EXPLAINED, ["EVENT_375_pause_script_until_effect_done_41"]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2)
	]),
	PauseScriptUntilEffectDone(identifier="EVENT_375_pause_script_until_effect_done_41"),
	EnterArea(room_id=R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, face_direction=NORTHEAST, x=16, y=30, z=2),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkEastPixels(16)
	]),
	FadeInFromBlack(sync=True, duration=200),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(8),
		A_FaceSouthwest(),
		A_Pause(20),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest(),
		A_Pause(20),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_Pause(20),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI0635_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI0637_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=16, y=30, z=4, direction=EAST),
		A_WalkNorthwestPixels(4),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	UnsyncDialog(),
	RunDialog(dialog_id=DI0638_EMPTY, above_object=NPC_8, closable=False, sync=True, multiline=True, use_background=True),
	UnsyncDialog(),
	SetSyncActionScript(NPC_8, A0114_EMPTY),
	RunDialog(dialog_id=DI0639_EMPTY, above_object=NPC_8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(40),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI0645_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	PauseActionScript(NPC_8),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI0646_EMPTY, above_object=NPC_8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(10)
	]),
	RunDialog(dialog_id=DI0647_EMPTY, above_object=NPC_0, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(10),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI0648_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouthwest(),
		A_Pause(30),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI0636_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceSoutheast(),
		A_Pause(10),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(8),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_DecZCoord1Step(),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI0642_EMPTY, above_object=NPC_8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI0877_EMPTY, above_object=NPC_8, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI0878_EMPTY, above_object=NPC_8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(14),
		A_VisibilityOff()
	]),
	Pause(60),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_FixedFCoordOn(),
		A_SequencePlaybackOff(),
		A_Walk1StepNorth()
	]),
	Set0158Bit7Offset(0x0158),
	Set0158Bit7Offset(0x015A),
	UnknownCommand(bytearray(b'\xfd\x8e\x80\x07\x01')),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	RunDialog(dialog_id=DI0640_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOff(),
		A_SequencePlaybackOn(),
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
		A_FaceSouth()
	]),
	SetBit(MUSHROOM_KINGDOM_LIBERATED),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=17, y=27, z=6, direction=EAST),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_FixedFCoordOn(),
		A_SequencePlaybackOff(),
		A_Walk1StepSouth()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Pause(30),
	UnknownCommand(bytearray(b'\xfd\x8e\xb2\x07\x01')),
	PauseScriptUntilEffectDone(),
	Clear0158Bit7Offset(0x0158),
	Clear0158Bit7Offset(0x015A),
	SetBit(UNKNOWN_7065_5),
	SetBit(UNKNOWN_7065_6),
	SetBit(UNKNOWN_7065_7),
	SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_KERO_SEWERS),
	SetBit(TEMP_7042_0),
	Return(),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_375_action_queue_117"),
	RunDialog(dialog_id=DI0641_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=True),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=16, y=22),
		A_FaceSoutheast(),
		A_Pause(32),
		A_WalkSoutheastSteps(3),
		A_WalkSouthSteps(1),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(16),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(4),
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0631_EMPTY, above_object=NPC_13, closable=False, sync=True, multiline=True, use_background=True),
	PauseScriptResumeOnNextDialogPageA(),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0632_EMPTY, above_object=NPC_13, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	SummonObjectToCurrentLevel(NPC_10),
	SummonObjectToCurrentLevel(NPC_11),
	SummonObjectToCurrentLevel(NPC_12),
	RunDialog(dialog_id=DI0633_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(8),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=13, y=34, z=4, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(9),
		A_WalkNortheastPixels(4),
		A_Walk1StepSoutheast(),
		A_FaceNortheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(20),
		A_TransferToXYZF(x=13, y=34, z=0, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(6),
		A_WalkNorthwestSteps(1),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(40),
		A_TransferToXYZF(x=13, y=34, z=4, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(5),
		A_WalkNorthwestSteps(1),
		A_FaceSoutheast(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	CloseDialog(),
	Jmp(["EVENT_375_run_dialog_25"])
])
