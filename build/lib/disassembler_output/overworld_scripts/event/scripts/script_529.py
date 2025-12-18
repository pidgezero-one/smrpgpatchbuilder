# E0529_ROSE_TOWN_OCCUPIED_EXTERIOR_LOADER

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
	UnknownCommand(bytearray(b'\xfdG')),
	CloseDialog(),
	FadeOutMusicToVolume(duration=1, volume=127),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetPriority(2),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4])
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(2),
		A_JmpIfBitSet(UNKNOWN_ROSE_TOWN_7060_0, ["EVENT_529_action_queue_4_SUBSCRIPT_transfer_to_xyzf_4"]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Jmp(["EVENT_529_action_queue_5"]),
		A_TransferToXYZF(x=12, y=47, z=2, direction=EAST, identifier="EVENT_529_action_queue_4_SUBSCRIPT_transfer_to_xyzf_4"),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4])
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
		A_JmpIfBitClear(FREEZE_ROSE_TOWN_NPC_1, ["EVENT_529_action_queue_6"]),
		A_SetPriority(2)
	], identifier="EVENT_529_action_queue_5"),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_SetPriority(3)
	], identifier="EVENT_529_action_queue_6"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetPriority(3)
	]),
	JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_1, ["EVENT_529_jmp_if_bit_clear_14"]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferXYZFPixels(x=240, y=8, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_SetPriority(2)
	]),
	SetSyncActionScript(NPC_7, A0637_ROSE_TOWN_INITIAL_ARROW),
	SetBit(FREEZE_ROSE_TOWN_NPC_1),
	JmpIfBitClear(UNUSED_7060_4, ["EVENT_529_jmp_if_bit_set_177"], identifier="EVENT_529_jmp_if_bit_clear_14"),
	JmpIfBitSet(UNUSED_7061_0, ["EVENT_529_jmp_if_bit_set_177"]),
	JmpIfObjectNotInSpecificLevel(NPC_1, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, ["EVENT_529_jmp_if_bit_set_177"]),
	JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_2, ["EVENT_529_set_bit_21"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(NPC_2, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	Jmp(["EVENT_529_clear_bit_23"]),
	SetBit(TEMP_7043_1, identifier="EVENT_529_set_bit_21"),
	Jmp(["EVENT_529_copy_var_to_var_181"]),
	ClearBit(TEMP_7043_1, identifier="EVENT_529_clear_bit_23"),
	RunBackgroundEvent(event_id=E0530_ROSE_TOWN_OCCUPIED_BACKGROUND_1, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E0551_ROSE_TOWN_OCCUPIED_MODS, return_on_level_exit=True, bit_6=True),
	SetVarToConst(TEMP_70A9, 21),
	PauseActionScript(MEM_70A9, identifier="EVENT_529_pause_action_script_27"),
	StartAsyncEmbeddedActionScript(target=MEM_70A9, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=13, y=28, z=8, direction=EAST),
		A_FaceNortheast()
	]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_FaceNorthwest()
	]),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	RunDialog(dialog_id=DI0792_DUPLICATE, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_529_pause_85"]),
	Pause(10),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_529_jmp_if_object_trigger_disabled_43"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["EVENT_529_run_dialog_75"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["EVENT_529_run_dialog_75"]),
	Jmp(["EVENT_529_run_dialog_45"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ["EVENT_529_run_dialog_75"], identifier="EVENT_529_jmp_if_object_trigger_disabled_43"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ["EVENT_529_run_dialog_75"]),
	RunDialog(dialog_id=DI0794_EMPTY, above_object=MEM_70A9, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_529_run_dialog_45"),
	RunDialog(dialog_id=DI0799_DUPLICATE, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(FOREST_MAZE_SECRET_FOUND, ["EVENT_529_action_queue_58"]),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_5),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_6),
	SetBit(UNKNOWN_ROSE_TOWN_7060_7),
	SetBit(UNUSED_7061_0),
	JmpToSubroutine(["EVENT_529_action_queue_159"]),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_574_summon_to_level_0"]),
	SummonObjectToSpecificLevel(NPC_4, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	SummonObjectToSpecificLevel(NPC_5, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	Return(),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpSteps(2),
		A_ShiftZDownSteps(2),
		A_SetWalkingSpeed(SLOW)
	], identifier="EVENT_529_action_queue_58"),
	RunDialog(dialog_id=DI0806_EMPTY, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	AddFrogCoins(1),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	SetBit(TREASURE_HUNTER_HOUSE_PRIZE),
	RunDialog(dialog_id=DI2243_EMPTY, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	Set7000ToObjectCoord(target_npc=MEM_70A9, coord=COORD_Y, pixel=True, bit_7=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 26),
	JmpIfComparisonResultIsLesser(["EVENT_529_jmp_to_subroutine_73"]),
	JmpToSubroutine(["EVENT_529_action_queue_159"]),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_574_summon_to_level_0"], identifier="EVENT_529_jmp_if_bit_set_68"),
	SummonObjectToSpecificLevel(NPC_4, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	SummonObjectToSpecificLevel(NPC_5, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	Return(),
	JmpToSubroutine(["EVENT_529_action_queue_169"], identifier="EVENT_529_jmp_to_subroutine_73"),
	Jmp(["EVENT_529_jmp_if_bit_set_68"]),
	RunDialog(dialog_id=DI0794_EMPTY, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_529_run_dialog_75"),
	JmpToSubroutine(["EVENT_529_action_queue_159"]),
	SetBit(UNKNOWN_ROSE_TOWN_7060_5),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_6),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_7),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_574_summon_to_level_0"]),
	SummonObjectToSpecificLevel(NPC_4, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	SummonObjectToSpecificLevel(NPC_5, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	Return(),
	Pause(10, identifier="EVENT_529_pause_85"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0796_EMPTY, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNortheast(),
		A_Walk1StepNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_529_apply_tile_mod_97"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=2),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Jmp(["EVENT_529_action_queue_100"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=1, identifier="EVENT_529_apply_tile_mod_97"),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=2),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Walk1StepNorthwest(),
		A_VisibilityOff()
	], identifier="EVENT_529_action_queue_100"),
	Pause(60),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_FaceSoutheast(),
		A_VisibilityOn(),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest(),
		A_Pause(10)
	]),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_529_jmp_if_object_trigger_disabled_107"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["EVENT_529_pause_126"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F, ["EVENT_529_pause_126"]),
	Jmp(["EVENT_529_pause_109"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ["EVENT_529_pause_126"], identifier="EVENT_529_jmp_if_object_trigger_disabled_107"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R094_ROSE_TOWN_TREASURE_HOUSE_1F, ["EVENT_529_pause_126"]),
	Pause(10, identifier="EVENT_529_pause_109"),
	RunDialog(dialog_id=DI0797_LEAVE_NO_STONE_UNTURNED, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_SetSpriteSequence(index=26, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0798_DUPLICATE, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(FOREST_MAZE_SECRET_FOUND, ["EVENT_529_action_queue_58"]),
	JmpToSubroutine(["EVENT_529_action_queue_169"]),
	SetBit(UNKNOWN_ROSE_TOWN_7060_6),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_5),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_7),
	SetBit(UNUSED_7061_0),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_574_summon_to_level_0"]),
	SummonObjectToSpecificLevel(NPC_4, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	SummonObjectToSpecificLevel(NPC_5, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	Return(),
	Pause(10, identifier="EVENT_529_pause_126"),
	RunDialog(dialog_id=DI0795_EMPTY, above_object=MEM_70A9, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_529_pause_144"]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0798_DUPLICATE, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(FOREST_MAZE_SECRET_FOUND, ["EVENT_529_action_queue_58"]),
	JmpToSubroutine(["EVENT_529_action_queue_169"]),
	SetBit(UNKNOWN_ROSE_TOWN_7060_6),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_5),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_7),
	SetBit(UNUSED_7061_0),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_574_summon_to_level_0"]),
	SummonObjectToSpecificLevel(NPC_4, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	SummonObjectToSpecificLevel(NPC_5, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	Return(),
	Pause(10, identifier="EVENT_529_pause_144"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0804_EMPTY, above_object=MEM_70A9, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_SetWalkingSpeed(SLOW)
	]),
	JmpToSubroutine(["EVENT_529_action_queue_169"]),
	SetBit(UNKNOWN_ROSE_TOWN_7060_5),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_6),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_7),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_574_summon_to_level_0"]),
	SummonObjectToSpecificLevel(NPC_4, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	SummonObjectToSpecificLevel(NPC_5, R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F),
	Return(),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorthwest(),
		A_Pause(30)
	], identifier="EVENT_529_action_queue_159"),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_529_apply_tile_mod_165"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=2),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Jmp(["EVENT_529_pause_168"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=1, identifier="EVENT_529_apply_tile_mod_165"),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=2),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(20, identifier="EVENT_529_pause_168"),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_Walk1StepNorthwest()
	], identifier="EVENT_529_action_queue_169"),
	JmpIfBitSet(UNUSED_7061_4, ["EVENT_529_remove_from_current_level_174"]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromSpecificLevel(NPC_1, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_10, identifier="EVENT_529_remove_from_current_level_174"),
	RemoveObjectFromSpecificLevel(NPC_10, R084_ROSE_TOWN_OUTSIDE),
	Return(),
	JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_2, ["EVENT_529_copy_var_to_var_181"], identifier="EVENT_529_jmp_if_bit_set_177"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetSyncActionScript(NPC_2, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	Jmp(["EVENT_529_jmp_if_bit_set_194"]),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_529_copy_var_to_var_181"),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_529_copy_var_to_var_190"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_2, identifier="EVENT_529_copy_var_to_var_183"),
	CopyVarToVar(from_var=ROSE_TOWN_ARROW_POSITION, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_2),
	SetVarToConst(Z_COORD_2, 2),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
		A_UnknownCommand(bytearray(b'\x9a')),
		A_JmpIfBitSet(TEMP_7043_2, ["EVENT_529_action_queue_187_SUBSCRIPT_set_sprite_sequence_6"]),
		A_FaceNorthwest(),
		A_TransferXYZFPixels(x=240, y=248, z=0, direction=EAST),
		A_Jmp(["EVENT_529_action_queue_187_SUBSCRIPT_fixed_f_coord_on_8"]),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_529_action_queue_187_SUBSCRIPT_set_sprite_sequence_6"),
		A_TransferXYZFPixels(x=16, y=8, z=0, direction=EAST),
		A_FixedFCoordOn(identifier="EVENT_529_action_queue_187_SUBSCRIPT_fixed_f_coord_on_8")
	]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_529_clear_bit_23"]),
	Jmp(["EVENT_529_jmp_if_bit_set_194"]),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_529_copy_var_to_var_190"),
	Mem7000AndConst(0x007F),
	SetBit(TEMP_7043_2),
	Jmp(["EVENT_529_copy_var_to_var_183"]),
	JmpIfBitSet(UNUSED_7061_0, ["EVENT_529_jmp_212"], identifier="EVENT_529_jmp_if_bit_set_194"),
	JmpIfObjectNotInSpecificLevel(NPC_1, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, ["EVENT_529_fade_in_from_black_async_197"]),
	SetSyncActionScript(NPC_1, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
	FadeInFromBlack(sync=False, identifier="EVENT_529_fade_in_from_black_async_197"),
	JmpIfBitSet(UNUSED_7060_4, ["EVENT_529_run_background_event_207"]),
	JmpIfObjectInSpecificLevel(NPC_1, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, ["EVENT_529_run_background_event_207"]),
	SetBit(UNUSED_7060_4),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(3),
		A_WalkNorthPixels(1)
	]),
	Pause(8),
	ApplyTileModToLevel(use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=0),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	RememberLastObject(),
	RunBackgroundEvent(event_id=E0530_ROSE_TOWN_OCCUPIED_BACKGROUND_1, return_on_level_exit=True, identifier="EVENT_529_run_background_event_207"),
	RunBackgroundEvent(event_id=E0551_ROSE_TOWN_OCCUPIED_MODS, return_on_level_exit=True, bit_6=True),
	JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_1, ["EVENT_256_ret_0"]),
	Pause(10),
	Return(),
	Jmp(["EVENT_529_fade_in_from_black_async_197"], identifier="EVENT_529_jmp_212")
])
