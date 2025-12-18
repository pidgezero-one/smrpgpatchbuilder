# E0332_EMPTY

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
	JmpIfBitClear(SIGNAL_RING_STAR_PIECE_2, ["EVENT_256_ret_0"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_4, ["EVENT_256_ret_0"]),
	SetBit(SIGNAL_RING_STAR_PIECE_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	PauseActionScript(NPC_8),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_BounceToXYWithHeight(x=16, y=104, height=4)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FixedFCoordOff(),
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_332_action_queue_6_SUBSCRIPT_pause_4"),
		A_JmpIfObjectInAir(NPC_8, ["EVENT_332_action_queue_6_SUBSCRIPT_pause_4"])
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SummonObjectToCurrentLevel(NPC_10),
	SummonObjectToCurrentLevel(NPC_9),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_VisibilityOff(),
		A_TransferToXYZF(x=19, y=119, z=4, direction=EAST)
	]),
	SetVarToConst(TEMP_70AA, 28),
	SetVarToConst(TEMP_70A9, 28),
	SetVarToConst(ACTIVE_NPC, 28),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_332_action_queue_20"]),
	RunEventAsSubroutine(E0260_UNKNOWN),
	RunDialog(dialog_id=DI0599_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSouthwest()
	], identifier="EVENT_332_action_queue_20"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=19, y=119),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=19, y=119, z=4, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(12),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_8, A0099_LOOPED_JUMPING),
	Pause(20),
	RunDialog(dialog_id=DI0600_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PauseActionScript(NPC_8),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_332_action_queue_27_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(NPC_8, ["EVENT_332_action_queue_27_SUBSCRIPT_pause_3"])
	]),
	RunDialog(dialog_id=DI0594_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(40),
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_Pause(40),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=26, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=26, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(56),
		A_VisibilityOn(),
		A_Pause(2),
		A_StartLoopNTimes(5),
		A_TurnClockwise45DegreesNTimes(2),
		A_Pause(2),
		A_EndLoop(),
		A_StopSound()
	]),
	Pause(30),
	SetSyncActionScript(NPC_8, A0099_LOOPED_JUMPING),
	Pause(30),
	RunDialog(dialog_id=DI0595_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_9, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=10, y=98, z=4, direction=EAST)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI0596_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(20),
	PauseActionScript(NPC_8),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	Pause(30),
	RunDialog(dialog_id=DI0597_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(13),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_Pause(50),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(13),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(50),
		A_ResetProperties()
	]),
	Pause(60),
	RunDialog(dialog_id=DI0567_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_PlaySound(sound=SO000_SILENCE, channel=6),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOff(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(14),
		A_FaceNorthwest(),
		A_Pause(20)
	]),
	RunDialog(dialog_id=DI0598_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(2),
		A_Pause(8),
		A_ShiftZDownPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(8),
		A_SetWalkingSpeed(FASTEST),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
		A_WalkSoutheastSteps(9),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_Pause(56),
		A_StartLoopNTimes(11),
		A_TurnClockwise45DegreesNTimes(2),
		A_Pause(3),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(2),
		A_Pause(5),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(2),
		A_Pause(10),
		A_EndLoop(),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest(),
		A_Pause(80),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_Pause(56),
		A_StartLoopNTimes(11),
		A_TurnClockwise45DegreesNTimes(6),
		A_Pause(3),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(6),
		A_Pause(5),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(6),
		A_Pause(10),
		A_EndLoop(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_Pause(56),
		A_StartLoopNTimes(11),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(3),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(5),
		A_EndLoop(),
		A_StartLoopNTimes(13),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(10),
		A_EndLoop(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0601_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=12, is_mold=True, looping=True),
		A_ShiftZUpPixels(10),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(6),
		A_SetSpriteSequence(index=13, is_mold=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_DecZCoord1Step(),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_Pause(20),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_Pause(10)
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_WalkNorthwestPixels(12),
		A_VisibilityOff()
	]),
	SummonObjectToCurrentLevel(NPC_5),
	SetSyncActionScript(NPC_5, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ApplyTileModToLevel(use_alternate=True, room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, mod_id=0),
	SetBit(MAP_BANDITS_WAY),
	SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
	ClearBit(TEMP_7043_3),
	RemoveObjectFromSpecificLevel(NPC_10, R023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_9, R023_MUSHROOM_KINGDOM_BEFORE_CROCO_OUTSIDE),
	Return()
])
