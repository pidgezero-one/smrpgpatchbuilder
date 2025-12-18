# E0320_MUSHROOM_KINGDOM_MAIN_HALL_LOADER

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
	Set0158Bit7Offset(0x015C),
	Set0158Bit7Offset(0x015E),
	ClearBit(TEMP_7042_7),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, ["EVENT_320_stop_sound_5"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	StopSound(identifier="EVENT_320_stop_sound_5"),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_320_summon_to_current_level_31"]),
	JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_320_remove_from_current_level_42"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(MIMIC_3_STAR_PIECE, ["EVENT_320_jmp_if_bit_set_28"]),
	SetBit(MIMIC_3_STAR_PIECE),
	JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_2, ["EVENT_320_action_queue_20"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=True),
	RememberLastObject(),
	RunDialog(dialog_id=DI0550_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0343_EMPTY, return_on_level_exit=True),
	SetSyncActionScript(NPC_0, A0065_EMPTY),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=2, y=36, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetWalkingSpeed(SLOW)
	], identifier="EVENT_320_action_queue_20"),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkNortheastSteps(2),
		A_WalkNorthwestSteps(1),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI0667_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RunBackgroundEvent(event_id=E0343_EMPTY, return_on_level_exit=True),
	SetSyncActionScript(NPC_0, A0065_EMPTY),
	Return(),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_320_summon_to_current_level_31"], identifier="EVENT_320_jmp_if_bit_set_28"),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_320_summon_to_current_level_31"]),
	Jmp(["EVENT_257_fade_in_from_black_async_0"]),
	SummonObjectToCurrentLevel(NPC_1, identifier="EVENT_320_summon_to_current_level_31"),
	SummonObjectToCurrentLevel(NPC_2),
	SetSyncActionScript(NPC_1, A0128_WALK_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_2, A0128_WALK_RANDOM_DIRECTIONS),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_256_ret_0"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, ["EVENT_256_ret_0"]),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_320_remove_from_current_level_42"),
	RemoveObjectFromCurrentLevel(NPC_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=True),
	RememberLastObject(),
	PauseScriptUntilEffectDone(),
	RunDialog(dialog_id=DI2244_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=2, y=34, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(10),
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(8),
		A_Walk1StepSouthwest(),
		A_Pause(10),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2245_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2246_EMPTY, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2247_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceEast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2248_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2249_EMPTY, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1])
	]),
	SetSyncActionScript(NPC_0, A0065_EMPTY),
	RunBackgroundEvent(event_id=E0343_EMPTY, return_on_level_exit=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceNorthwest()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2250_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(20),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkNorthwestPixels(10),
		A_TransferToXYZF(x=4, y=59, z=0, direction=EAST)
	]),
	SetBit(PROGRESSIVE_FIREWORKS_ENABLED),
	Return()
])
