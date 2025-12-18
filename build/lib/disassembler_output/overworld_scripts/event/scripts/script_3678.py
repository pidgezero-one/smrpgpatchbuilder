# E3678_ROYAL_BUS_ATTENDANT

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
	JmpIfBitSet(UNKNOWN_STAR_PIECE, ["EVENT_3678_action_queue_98"]),
	JmpIfBitSet(UNKNOWN_7099_1, ["EVENT_3678_pause_4"]),
	RunDialog(dialog_id=DI3725_KEEP_ACCESS_HINT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	Pause(1, identifier="EVENT_3678_pause_4"),
	JmpIfMarioInAir(["EVENT_3678_pause_4"]),
	RunDialog(dialog_id=DI3809_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=4, y=37)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceWest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=37, z=2, direction=EAST),
		A_FaceSouthwest(),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestPixels(12),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_Pause(60),
		A_SetWalkingSpeed(VERY_FAST),
		A_SequenceLoopingOff(),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI3810_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3811_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3812_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_PlaySound(sound=SO059_HOVERING_FROGFUCIUS, channel=4)
	], identifier="EVENT_3678_action_queue_18"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3678_action_queue_22"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(120),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST)
	]),
	RunDialog(dialog_id=DI3808_DREAM, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestSteps(5),
		A_WalkSouthwestSteps(4),
		A_WalkSouthwestSteps(4),
		A_WalkSouthwestSteps(4),
		A_FadeOutSoundToVolume(duration=2, volume=0)
	], identifier="EVENT_3678_action_queue_22"),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkNortheastSteps(17),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_Pause(60),
		A_FaceNortheast(),
		A_Pause(270),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_FaceNortheast(),
		A_Pause(270),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_Pause(60),
		A_FaceNortheast(),
		A_Pause(270),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(280),
		A_SetWalkingSpeed(SLOW),
		A_WalkWestSteps(2)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkSouthwestSteps(3),
		A_BPL262728(),
		A_JmpIfBitSet(TEMP_7043_0, ["EVENT_3678_action_queue_30_SUBSCRIPT_face_northeast_8"]),
		A_FaceNorthwest(),
		A_Jmp(["EVENT_3678_action_queue_31"]),
		A_FaceNortheast(identifier="EVENT_3678_action_queue_30_SUBSCRIPT_face_northeast_8")
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_FaceWest(),
		A_Pause(2),
		A_FaceSouthwest()
	], identifier="EVENT_3678_action_queue_31"),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3678_action_queue_36"]),
	RememberLastObject(),
	Pause(30),
	Jmp(["EVENT_3678_action_queue_59"]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_ResetProperties(),
		A_FaceSouthwest()
	], identifier="EVENT_3678_action_queue_36"),
	Pause(10),
	RunDialog(dialog_id=DI3813_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST)
	]),
	RunDialog(dialog_id=DI3814_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3815_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3816_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(60),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepWest(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_JmpIfBitSet(TEMP_7043_0, ["EVENT_3678_action_queue_59_SUBSCRIPT_walk_1_step_southwest_4"]),
		A_WalkSouthwestSteps(2),
		A_Jmp(["EVENT_3678_action_queue_59_SUBSCRIPT_face_west_5"]),
		A_Walk1StepSouthwest(identifier="EVENT_3678_action_queue_59_SUBSCRIPT_walk_1_step_southwest_4"),
		A_FaceWest(identifier="EVENT_3678_action_queue_59_SUBSCRIPT_face_west_5"),
		A_Pause(2),
		A_FaceNorthwest()
	], identifier="EVENT_3678_action_queue_59"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3678_action_queue_65"]),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=5, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=5, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=94, silent=True),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestPixels(4),
		A_ShadowOn(),
		A_FloatingOff()
	]),
	SetSyncActionScript(NPC_4, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNorth(),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(94),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestPixels(4),
		A_FloatingOn(),
		A_WalkNorthwestSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestPixels(4),
		A_ShadowOn(),
		A_FloatingOff()
	], identifier="EVENT_3678_action_queue_65"),
	SetSyncActionScript(NPC_3, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_Pause(60),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3817_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3818_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3678_action_queue_78"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	], identifier="EVENT_3678_action_queue_78"),
	Pause(60),
	FreezeCamera(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_Pause(120),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_Pause(2),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_WalkSouthwestSteps(10),
		A_BPL262728()
	]),
	ActionQueueSync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x03\x00\x01\x00\x00\x00\x08\x80')),
		A_PlaySound(sound=SO059_HOVERING_FROGFUCIUS, channel=4),
		A_WalkNortheastSteps(10),
		A_BPL262728()
	]),
	Pause(200),
	SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BOWSERS_KEEP),
	SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_VISTA_HILL),
	FadeOutToBlack(sync=True, duration=60),
	PauseScriptUntilEffectDone(),
	RunEventSequence(scene=SC16_RUN_WORLD_MAP_EVENT_SEQUENCE, value=2),
	FadeOutSoundToVolume(duration=2, volume=0),
	JmpIfBitSet(UNKNOWN_STAR_PIECE, ["EVENT_3678_open_location_96"]),
	SetBit(UNKNOWN_STAR_PIECE),
	JmpToEvent(E2277_EMPTY),
	ExitToWorldMap(area=OW04_BOWSERS_KEEP, bit_6=True, bit_7=True, identifier="EVENT_3678_open_location_96"),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=4, y=38),
		A_FaceNorthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_3678_action_queue_98"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceSoutheast()
	]),
	SetVarToConst(TEMP_70AE, 16),
	RunDialog(dialog_id=DI3872_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3678_pause_108"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI3873_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_0),
	Jmp(["EVENT_3678_action_queue_18"]),
	Pause(10, identifier="EVENT_3678_pause_108"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI3874_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ClearBit(TEMP_7043_0),
	Return()
])
