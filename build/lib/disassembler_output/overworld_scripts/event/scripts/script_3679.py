# E3679_NIMBUS_CASTLE_EGG_ROOM_LOADER

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
	JmpIfObjectNotInSpecificLevel(NPC_0, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_3679_jmp_if_object_not_in_level_2"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	JmpIfObjectNotInSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_3679_jmp_if_object_not_in_level_4"], identifier="EVENT_3679_jmp_if_object_not_in_level_2"),
	ApplySolidityModToLevel(permanent=True, room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, mod_id=0),
	JmpIfObjectNotInSpecificLevel(NPC_1, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_3585_fade_in_from_black_async_0"], identifier="EVENT_3679_jmp_if_object_not_in_level_4"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JmpIfBitSet(COIN_CHEST_COMPLETED, ["EVENT_3679_action_queue_5_SUBSCRIPT_transfer_to_xyzf_3"]),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Jmp(["EVENT_3679_remember_last_object_6"]),
		A_TransferToXYZF(x=20, y=49, z=10, direction=EAST, identifier="EVENT_3679_action_queue_5_SUBSCRIPT_transfer_to_xyzf_3"),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RememberLastObject(identifier="EVENT_3679_remember_last_object_6"),
	JmpIfBitClear(COIN_CHEST_COMPLETED, ["EVENT_3679_jmp_if_bit_clear_9"]),
	SetSyncActionScript(NPC_1, A0978_RANDOMLY_FACE_SOUTHWEST),
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_3679_fade_in_from_black_async_12"], identifier="EVENT_3679_jmp_if_bit_clear_9"),
	JmpIfObjectNotInSpecificLevel(NPC_0, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_3679_fade_in_from_black_async_12"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=17, y=56, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_3679_fade_in_from_black_async_12"),
	JmpIfBitSet(COIN_CHEST_COMPLETED, ["EVENT_3584_ret_0"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(8)
	]),
	Pause(120),
	RunDialog(dialog_id=DI3601_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI3602_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_SequenceLoopingOn(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x80\x00\xc0\xff')),
		A_ShiftZDownSteps(2),
		A_BPL262728(),
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_StartLoopNTimes(1),
		A_WalkSouthwestPixels(4),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_WalkNortheastPixels(4),
		A_Pause(30),
		A_EndLoop(),
		A_Pause(60),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3603_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpSteps(4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthwestSteps(2)
	]),
	Pause(60),
	RunDialog(dialog_id=DI3604_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	SetSyncActionScript(NPC_1, A0978_RANDOMLY_FACE_SOUTHWEST),
	SetBit(COIN_CHEST_COMPLETED),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	Return()
])
