# E3727_NIMBUS_CASTLE_STAIRWAY_GUARD

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
	RunDialog(dialog_id=DI3606_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfBitSet(UNKNOWN_7090_0, ["EVENT_3584_ret_0"]),
	Pause(10),
	RunDialog(dialog_id=DI2188_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=24, y=19),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=21, y=2)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=24, y=19, z=0, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(4),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_WalkNortheastPixels(12),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3607_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkNortheastPixels(8),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, sprite_offset=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(14),
		A_SetSpriteSequence(index=5, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_StartLoopNTimes(1),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_Pause(10),
		A_EndLoop()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3639_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(30),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	], identifier="EVENT_3727_action_queue_15"),
	Pause(30),
	JmpIfBitClear(UNKNOWN_7090_0, ["EVENT_3727_run_dialog_20"]),
	RunDialog(dialog_id=DI3608_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3727_action_queue_21"]),
	RunDialog(dialog_id=DI3640_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3727_run_dialog_20"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_3727_action_queue_21"),
	Pause(60),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	RunDialog(dialog_id=DI3609_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=24, y=19, z=0, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSoutheastPixels(6),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(8),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_WalkSoutheastPixels(14),
		A_FaceNorthwest(),
		A_Pause(10),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3610_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceEast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(20),
		A_FaceSoutheast(),
		A_Pause(20),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3611_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_Walk1StepSouth(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(60),
		A_FaceSoutheast()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOn(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff(),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=1, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=2, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=4, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO057_FINGER_SNAP, channel=4),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=4, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestPixels(8),
		A_SequenceLoopingOff(),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestPixels(8),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(31),
		A_ResetProperties(),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(12),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_FaceEast()
	]),
	Pause(60),
	RunDialog(dialog_id=DI3612_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(12),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3613_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3614_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(4),
		A_TransferToXYZF(x=25, y=51, z=0, direction=EAST)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI3615_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_Pause(8),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3634_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(14),
		A_TransferToXYZF(x=25, y=51, z=0, direction=EAST)
	]),
	JmpIfBitSet(NIMBUS_BOSS_IN_TOWN_SQUARE, ["EVENT_3727_pause_95"]),
	Pause(90),
	RunDialog(dialog_id=DI3616_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetBit(TEMP_7049_2),
	SetBit(UNKNOWN_704A_3),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceNortheast(),
		A_TransferToXYZF(x=22, y=29, z=4, direction=EAST),
		A_SetAllSpeeds(SLOW),
		A_SequenceLoopingOn(),
		A_WalkNortheastSteps(7),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(100),
		A_FaceSouth(),
		A_Pause(80),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties()
	]),
	Pause(90),
	RunDialog(dialog_id=DI3616_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(30),
		A_WalkNortheastSteps(8)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(80),
		A_FaceEast(),
		A_Pause(80),
		A_FaceNortheast()
	]),
	Pause(10),
	CloseDialog(),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(30, identifier="EVENT_3727_pause_95"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_7, R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR),
	RemoveObjectFromSpecificLevel(NPC_1, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
	SetBit(UNKNOWN_7090_0),
	Return()
])
