# E0512_ROSE_TOWN_OCCUPIED_INN_LOADER

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
	FadeOutMusicToVolume(duration=1, volume=96),
	JmpIfBitSet(UNUSED_7084_7, ["EVENT_512_jmp_to_subroutine_201"]),
	SetBit(UNUSED_7084_7),
	PlayMusicAtCurrentVolume(M0028_LET_SPLAYGENO),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(0)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ClearSolidityBits(bit_4=True),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(8),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=7, y=20, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ShadowOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(NORMAL),
		A_SetPriority(2)
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_SetPriority(3)
	]),
	RunDialog(dialog_id=DI0736_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_SetPriority(3)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSoutheast(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(4)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(46),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(4)
	]),
	RunDialog(dialog_id=DI0737_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(11),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW),
		A_Pause(60),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_21_SUBSCRIPT_pause_10"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_512_action_queue_21_SUBSCRIPT_pause_10"]),
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(79),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_22_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_6, ["EVENT_512_action_queue_22_SUBSCRIPT_pause_2"]),
		A_JumpToHeight(height=64, silent=True)
	]),
	Pause(90),
	RunDialog(dialog_id=DI0738_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xf0\xfeh\x00')),
		A_UnknownCommand(bytearray(b'%\x00\x05x\xff')),
		A_PlaySound(sound=SO004_JUMP, channel=6),
		A_Pause(22),
		A_BPL262728(),
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xf0\xfeh\x00')),
		A_UnknownCommand(bytearray(b'%\x00\x05x\xff')),
		A_Pause(22),
		A_BPL262728(),
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True)
	]),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(120),
		A_FaceNortheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_PlaySound(sound=SO000_SILENCE, channel=6),
		A_JumpToHeight(height=80, silent=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouth(),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_Pause(4),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkWestPixels(21),
		A_WalkNortheastPixels(2),
		A_Pause(15),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(4),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(2),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6),
		A_WalkNortheastPixels(2),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(94),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x06`\xff')),
		A_WalkNortheastSteps(3),
		A_WalkNortheastPixels(6),
		A_BPL262728(),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
		A_JumpToHeight(height=0, silent=True)
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(30),
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(30),
		A_JumpToHeight(height=64, silent=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI0739_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkEastPixels(16),
		A_WalkNorthwestPixels(2),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkWestPixels(2),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0740_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestPixels(8),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(6),
		A_WalkNortheastPixels(11),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(14),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestPixels(2)
	]),
	RunDialog(dialog_id=DI0741_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkNorthPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(2),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI0742_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(60),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=80, silent=True)
	]),
	RunDialog(dialog_id=DI0743_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	UnsyncDialog(),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast(),
		A_ResetProperties(),
		A_Pause(30),
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(10),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_SetSequenceSpeed(SLOW)
	]),
	RunDialog(dialog_id=DI0744_EMPTY, above_object=NPC_1, closable=False, sync=True, multiline=True, use_background=True),
	Pause(60),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNortheast(),
		A_Pause(30),
		A_Walk1StepNortheast()
	]),
	Pause(60),
	ActionQueueSync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_SetSpriteSequence(index=7, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_EndLoop(),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_Walk1StepNortheast(),
		A_Pause(30),
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FaceNorthwest(),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI0745_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_FaceEast()
	]),
	RunDialog(dialog_id=DI0746_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_77_SUBSCRIPT_pause_1"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_512_action_queue_77_SUBSCRIPT_pause_1"])
	]),
	RunDialog(dialog_id=DI0747_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_FaceNortheast(),
		A_WalkEastPixels(24),
		A_WalkNortheastPixels(14),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(8),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_Pause(2),
		A_WalkSouthwestPixels(6),
		A_WalkNorthwestPixels(8),
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepWest(),
		A_WalkWestPixels(20),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(10)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(20),
		A_FaceNorthwest(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(10),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(4),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepWest(),
		A_WalkWestPixels(20),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8),
		A_SetSequenceSpeed(SLOW)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0749_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_512_pause_98"]),
	Pause(10),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI0750_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Pause(1, identifier="EVENT_512_action_queue_93_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_512_action_queue_93_SUBSCRIPT_pause_1"])
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_95_SUBSCRIPT_pause_1"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_512_action_queue_95_SUBSCRIPT_pause_1"])
	]),
	RunDialog(dialog_id=DI0751_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_512_action_queue_102"]),
	Pause(10, identifier="EVENT_512_pause_98"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	RunDialog(dialog_id=DI0752_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest()
	], identifier="EVENT_512_action_queue_102"),
	RunDialog(dialog_id=DI0756_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0757_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouthwest()
	]),
	RunDialog(dialog_id=DI0758_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	Pause(30),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_115_SUBSCRIPT_pause_1"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_512_action_queue_115_SUBSCRIPT_pause_1"]),
		A_SetWalkingSpeed(NORMAL),
		A_Pause(30),
		A_FixedFCoordOn(),
		A_Walk1StepSouth(),
		A_BounceToXYWithHeight(x=2, y=19, height=0),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI0753_EMPTY, above_object=NPC_1, closable=False, sync=True, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_FaceSoutheast(),
		A_Pause(30),
		A_WalkSoutheastSteps(2),
		A_Walk1StepNortheast(),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(30),
		A_Walk1StepSoutheast(),
		A_Walk1StepNortheast(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(SLOW),
		A_Pause(30)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(8),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(2),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(1),
		A_SetSequenceSpeed(SLOW),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI0754_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_130_SUBSCRIPT_pause_1"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_512_action_queue_130_SUBSCRIPT_pause_1"])
	]),
	RunDialog(dialog_id=DI0759_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_133_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_512_action_queue_133_SUBSCRIPT_pause_4"]),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_133_SUBSCRIPT_pause_8"),
		A_JmpIfMarioInAir(["EVENT_512_action_queue_133_SUBSCRIPT_pause_8"]),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_134_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(NPC_5, ["EVENT_512_action_queue_134_SUBSCRIPT_pause_3"]),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_134_SUBSCRIPT_pause_6"),
		A_JmpIfObjectInAir(NPC_5, ["EVENT_512_action_queue_134_SUBSCRIPT_pause_6"])
	]),
	Pause(20),
	StartLoopNTimes(1),
	SetBit(TEMP_7043_1),
	SetAsyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	EndLoop(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(2),
		A_WalkNortheastPixels(2)
	]),
	RunDialog(dialog_id=DI0755_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2)
	]),
	RunDialog(dialog_id=DI0760_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	SetSyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	SetAsyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestSteps(3)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSouthwestSteps(3)
	]),
	PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouthwest(),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouthwest(),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(4),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(2)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_ResetProperties()
	]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(30),
	SetSyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	SetAsyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0761_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouthwest(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(VERY_FAST),
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
		A_WalkNortheastPixels(4),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouthwest(),
		A_SetWalkingSpeed(VERY_FAST),
		A_Pause(30),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(3),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(3),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(12),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(8),
		A_WalkNortheastPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(2)
	]),
	Pause(60),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(10),
		A_FaceNorthwest(),
		A_Pause(2),
		A_WalkWestPixels(16),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOff(),
		A_Pause(3),
		A_FaceNorthwest(),
		A_Pause(5),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0762_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkEastPixels(16),
		A_FaceNorthwest(),
		A_Pause(2),
		A_WalkNorthPixels(10),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(4),
		A_FaceNorthwest(),
		A_Pause(3),
		A_FaceSouthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0763_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=5, y=15, z=0, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Pause(31),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(1),
		A_PlaySound(sound=SO075_ROCKETING_BLAST, channel=6),
		A_WalkSouthwestPixels(1),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestPixels(4),
		A_TransferXYZFPixels(x=0, y=0, z=1, direction=EAST),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(8),
		A_TransferXYZFPixels(x=0, y=0, z=2, direction=EAST),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(4),
		A_TransferXYZFPixels(x=0, y=0, z=2, direction=EAST),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(8),
		A_TransferXYZFPixels(x=0, y=0, z=3, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(8),
		A_TransferXYZFPixels(x=0, y=0, z=4, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(10)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetSpriteSequence(index=21, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(FASTEST),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x04\x80\x00')),
		A_Walk1StepSouthwest(),
		A_BPL262728()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FloatingOff(),
		A_SetWalkingSpeed(FASTEST),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x04\x80\x00')),
		A_Walk1StepSouthwest(),
		A_BPL262728(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(8),
		A_Walk1StepSoutheast(),
		A_WalkNorthwestPixels(12),
		A_StartLoopNTimes(1),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(8),
		A_WalkNorthwestPixels(6),
		A_WalkSoutheastPixels(4),
		A_WalkNorthwestPixels(4),
		A_EndLoop()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0764_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_DecZCoord1Step(),
		A_Pause(30),
		A_FaceNortheast(),
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=22, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(14),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(14),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=22, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(14),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=19, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=22, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=25, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_Pause(20),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_512_action_queue_183_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_512_action_queue_183_SUBSCRIPT_pause_3"]),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(3),
		A_Walk1StepSoutheast()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(40),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(6),
		A_BPL262728(),
		A_FloatingOn()
	]),
	Pause(20),
	RunDialog(dialog_id=DI0765_EMPTY, above_object=NPC_12, closable=False, sync=True, multiline=True, use_background=False),
	Pause(100),
	SlowDownMusic(),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=15, duration=4, bit_6=True, bit_7=True),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=0, duration=4, bit_6=True, bit_7=True),
	Pause(19),
	Pause(19),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=15, duration=4, bit_6=True, bit_7=True),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=0, duration=4, bit_6=True, bit_7=True),
	Pause(25),
	FadeOutToBlack(sync=True, duration=120),
	PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=15, duration=7, bit_6=True, bit_7=False),
	PauseScriptUntilEffectDone(),
	FadeOutMusicToVolume(duration=2, volume=1),
	JmpToEvent(E0513_EMPTY),
	JmpToSubroutine(["EVENT_512_action_queue_211"], identifier="EVENT_512_jmp_to_subroutine_201"),
	JmpIfBitClear(UNUSED_7085_0, ["EVENT_512_fade_in_from_black_async_221"]),
	Set70107015ToObjectXYZ(target=MARIO, bit_7=True),
	CompareVarToConst(X_COORD_1, 3),
	JmpIfComparisonResultIsLesser(["EVENT_512_fade_out_music_to_volume_207"]),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
	FadeOutMusicToVolume(duration=1, volume=96, identifier="EVENT_512_fade_out_music_to_volume_207"),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI0000_INN_BANNER, above_object=NPC_12, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	Return(),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=7, y=21, z=0, direction=EAST)
	], identifier="EVENT_512_action_queue_211"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=7, y=20, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=8, y=19, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	JmpIfBitClear(UNUSED_7085_0, ["EVENT_512_action_queue_218"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=5, y=16, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(NPC_1, A0128_WALK_RANDOM_DIRECTIONS),
	Jmp(["EVENT_512_remember_last_object_219"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=1, y=21, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOff()
	], identifier="EVENT_512_action_queue_218"),
	RememberLastObject(identifier="EVENT_512_remember_last_object_219"),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_512_fade_in_from_black_async_221"),
	JmpToEvent(E0515_EMPTY)
])
