# E0560_OLD_KEY_ITEM_MANAGER

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
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_560_jmp_if_random_above_128_191"]),
	JmpIfBitSet(ROSE_TOWN_GAZ_ITEM_GRANTED, ["EVENT_560_jmp_if_random_above_128_191"]),
	SetBit(ROSE_TOWN_GAZ_ITEM_GRANTED),
	PauseActionScript(NPC_1),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(NORMAL),
		A_BounceToXYWithHeight(x=5, y=16, height=0),
		A_WalkNortheastPixels(8),
		A_FaceSouthwest(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1])
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_BounceToXYWithHeight(x=4, y=17, height=0)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=17, z=0, direction=EAST),
		A_WalkNorthwestPixels(4),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=17, z=0, direction=EAST),
		A_Pause(8),
		A_FaceNortheast(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	SetBit(TEMP_7043_1),
	SetAsyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0823_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0857_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastPixels(8),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(4),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(4),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(4),
		A_FaceSoutheast(),
		A_FloatingOn()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(6),
		A_Pause(30),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSoutheastSteps(3),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(40),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(30),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(35),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI0824_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8)
	]),
	RunDialog(dialog_id=DI0825_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI0826_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	ClearBit(TEMP_7043_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties()
	]),
	SetSyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0827_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI0828_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties()
	]),
	SetBit(TEMP_7043_1),
	Pause(10),
	UnsyncActionScript(NPC_1),
	RunDialog(dialog_id=DI0829_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI0830_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(70)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(70),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(5),
		A_ResetProperties()
	]),
	Pause(60),
	FadeOutMusicToVolume(duration=1, volume=0),
	RememberLastObject(),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNorth(),
		A_SequenceLoopingOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0831_EMPTY, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueSync(target=NPC_6, subscript=[
		A_VisibilityOff(),
		A_Pause(16),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_TransferToXYZF(x=3, y=19, z=6, direction=EAST),
		A_TransferXYZFPixels(x=244, y=4, z=0, direction=EAST),
		A_Pause(4),
		A_VisibilityOn(),
		A_PlaySound(sound=SO080_BEEPING, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(3),
		A_WalkNorthwestPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(108),
		A_Pause(10),
		A_FloatingOff(),
		A_SetSpriteSequence(index=0, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=1, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=6, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_ResetProperties(),
		A_Pause(20),
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_FaceNortheast(),
		A_JumpToHeight(108),
		A_Pause(10),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(20),
		A_ResetProperties(),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(20),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=2, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_EndLoop(),
		A_PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(15),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_TransferToXYZF(x=3, y=17, z=4, direction=EAST),
		A_VisibilityOn(),
		A_PlaySound(sound=SO081_STAR, channel=4),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(4),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_ShiftZDownPixels(4),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_560_action_queue_76_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_560_action_queue_76_SUBSCRIPT_pause_2"])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(1),
		A_WalkNortheastSteps(1)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_Walk1StepNortheast(),
		A_Pause(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(10),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0841_GOOMBA_THUMPIN_PITY_MECHANIC, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSouth(),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest(),
		A_Pause(10),
		A_JumpToHeight(108),
		A_Pause(10),
		A_FloatingOff(),
		A_SetSpriteSequence(index=0, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=1, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=6, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_ResetProperties(),
		A_Pause(20),
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(2),
		A_FaceNortheast(),
		A_JumpToHeight(108),
		A_Pause(10),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(42),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_TransferToXYZF(x=3, y=19, z=6, direction=EAST),
		A_TransferXYZFPixels(x=244, y=4, z=0, direction=EAST),
		A_Pause(4),
		A_VisibilityOn(),
		A_PlaySound(sound=SO080_BEEPING, channel=4),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(3),
		A_WalkNorthwestPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(2),
		A_Walk1StepSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(35),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_PlaySound(sound=SO088_WRONG_SIGNAL, channel=4),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(20),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_PlaySound(sound=SO088_WRONG_SIGNAL, channel=4),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties(),
		A_Pause(4),
		A_EndLoop(),
		A_Pause(10),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_EndLoop(),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(40),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_560_action_queue_105_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_560_action_queue_105_SUBSCRIPT_pause_2"])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Walk1StepSouth(),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0842_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	RunDialog(dialog_id=DI0843_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(10),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(10),
		A_SetSpriteSequence(index=8, sprite_offset=1, is_sequence=True, looping=True)
	]),
	Pause(10),
	FadeOutMusicToVolume(duration=1, volume=0),
	Pause(30),
	RememberLastObject(),
	FadeInMusic(M0018_ROSETOWN),
	FadeOutMusicToVolume(duration=0, volume=97),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0844_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetBit(TEMP_7043_1),
	SetAsyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0845_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetSyncActionScript(NPC_3, A0507_SPARKLE_LINE_LOOPED),
	Pause(30),
	RunDialog(dialog_id=DI0846_EMPTY, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	UnsyncDialog(),
	PauseActionScript(NPC_3),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	Pause(20),
	RunDialog(dialog_id=DI0847_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI0848_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Walk1StepNorthwest(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceNorth(),
		A_Pause(4),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_560_action_queue_147_SUBSCRIPT_set_sprite_sequence_3"),
		A_Pause(2),
		A_SetSpriteSequence(index=3, sprite_offset=4, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_Jmp(["EVENT_560_action_queue_147_SUBSCRIPT_set_sprite_sequence_3"])
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepSouth(),
		A_Walk1StepSoutheast(),
		A_WalkNortheastPixels(8),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI0849_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	SetSyncActionScript(NPC_3, A0507_SPARKLE_LINE_LOOPED),
	Pause(18),
	PauseActionScript(NPC_3),
	RunDialog(dialog_id=DI0850_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_FaceNortheast(),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(8),
		A_FixedFCoordOff()
	]),
	Pause(10),
	SetAsyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0851_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestPixels(10),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(4),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestPixels(10),
		A_FaceNortheast(),
		A_ResetProperties(),
		A_SetSpriteSequence(index=21, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(32),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(26),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(18),
		A_StartLoopNTimes(3),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=22, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=22, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_EndLoop(),
		A_ResetProperties()
	]),
	Pause(10),
	SetSyncActionScript(NPC_1, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0852_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_FaceSoutheast(),
		A_Pause(4),
		A_FaceNortheast(),
		A_Walk1StepEast(),
		A_WalkNortheastPixels(8),
		A_WalkSoutheastSteps(3),
		A_FaceNortheast(),
		A_Pause(30),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(1),
		A_WalkWestSteps(1),
		A_SetSequenceSpeed(NORMAL),
		A_SetSolidityBits(cant_walk_through=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(FAST)
	]),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_SequenceLoopingOff(),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI0853_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetVarToConst(ITEM_ID, FingerShotItem),
	SetVarToConst(PRIMARY_TEMP_7000, 524),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	SetSyncActionScript(NPC_3, A0507_SPARKLE_LINE_LOOPED),
	Pause(18),
	PauseActionScript(NPC_3),
	Pause(10),
	RunDialog(dialog_id=DI0856_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_WalkSoutheastPixels(6),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(70),
		A_ResetProperties(),
		A_WalkSoutheastPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNortheastPixels(6),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(70),
		A_ResetProperties(),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_Pause(70),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetSyncActionScript(NPC_1, A0128_WALK_RANDOM_DIRECTIONS),
	Pause(10),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(TEMP_7044_5),
	Return(),
	JmpIfRandom1of2(["EVENT_560_run_dialog_194"], identifier="EVENT_560_jmp_if_random_above_128_191"),
	RunDialog(dialog_id=DI0854_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0855_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_560_run_dialog_194"),
	Return()
])
