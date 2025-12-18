# E0273_SLEEP_IN_INNS

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
	RunDialog(dialog_id=DI0519_MUSHROOM_INNKEEPER, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_273_run_event_as_subroutine_3"]),
	Jmp(["EVENT_273_run_event_as_subroutine_8"]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_273_run_event_as_subroutine_3"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	RunDialog(dialog_id=DI0521_NEW_PAGE_GOOD_LUCK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_273_clear_bit_48"]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_273_run_event_as_subroutine_8"),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	SetBit(UNKNOWN_7049_4),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_273_clear_bit_48"]),
	CloseDialog(),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	FadeOutMusicToVolume(duration=2, volume=0, identifier="EVENT_273_fade_out_music_to_volume_17"),
	CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
	Pause(10),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	Pause(50),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=1, static=True),
	PauseScriptUntilEffectDone(),
	SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP, identifier="EVENT_273_set_bit_26"),
	JmpToSubroutine(["EVENT_273_jmp_if_bit_set_64"]),
	RestoreAllHP(),
	RestoreAllFP(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	Pause(60),
	PlaySound(sound=SO029_ALARM_CLOCK, channel=6),
	Pause(92),
	StopSound(),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO047_SNOOZE, channel=4)
	]),
	CircleMaskShrinkToObject(target=MARIO, width=255, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	Pause(30),
	FadeOutMusicToVolume(duration=2, volume=96),
	Pause(30),
	StopSound(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True)
	]),
	RunEventAsSubroutine(E0286_AWAIT_B_PRESS),
	JmpToSubroutine(["EVENT_273_jmp_if_bit_set_131"]),
	PauseActionScript(MARIO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_JumpToHeight(108),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_273_action_queue_47_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_273_action_queue_47_SUBSCRIPT_pause_3"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP, identifier="EVENT_273_clear_bit_48"),
	ClearBit(OCCUPIED_MUSHROOM_KINGDOM_INN),
	ClearBit(OCCUPIED_ROSE_TOWN_INN),
	ClearBit(ROSE_TOWN_LIBERATED_INN),
	ClearBit(MOLEVILLE_INN),
	ClearBit(MARRYMORE_REGULAR_INN),
	ClearBit(MARRYMORE_SUITE_INN),
	ClearBit(OCCUPIED_SEASIDE_INN),
	ClearBit(LIBERATED_SEASIDE_INN),
	ClearBit(MUSHROOM_KINGDOM_INN),
	ClearBit(UNKNOWN_7049_4),
	ClearBit(INSUFFICIENT_COINS),
	ClearBit(NIMBUS_INN),
	ClearBit(TEMP_7042_7),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_273_action_queue_163"]),
	Return(),
	JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_INN, ["EVENT_273_enter_area_77"], identifier="EVENT_273_jmp_if_bit_set_64"),
	JmpIfBitSet(OCCUPIED_ROSE_TOWN_INN, ["EVENT_273_enter_area_80"]),
	JmpIfBitSet(ROSE_TOWN_LIBERATED_INN, ["EVENT_273_enter_area_89"]),
	JmpIfBitSet(MOLEVILLE_INN, ["EVENT_273_enter_area_96"]),
	JmpIfBitSet(MARRYMORE_REGULAR_INN, ["EVENT_273_enter_area_99"]),
	JmpIfBitSet(MARRYMORE_SUITE_INN, ["EVENT_273_enter_area_106"]),
	JmpIfBitSet(OCCUPIED_SEASIDE_INN, ["EVENT_273_enter_area_111"]),
	JmpIfBitSet(LIBERATED_SEASIDE_INN, ["EVENT_273_enter_area_115"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_INN, ["EVENT_273_enter_area_118"]),
	JmpIfBitSet(NIMBUS_INN, ["EVENT_273_enter_area_121"]),
	EnterArea(room_id=R052_MUSHROOM_KINGDOM_INN_2F, face_direction=SOUTH, x=6, y=119, z=3, run_entrance_event=True),
	ApplyTileModToLevel(use_alternate=True, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0),
	Return(),
	EnterArea(room_id=R052_MUSHROOM_KINGDOM_INN_2F, face_direction=SOUTH, x=6, y=119, z=3, run_entrance_event=True, identifier="EVENT_273_enter_area_77"),
	ApplyTileModToLevel(use_alternate=True, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0),
	Return(),
	EnterArea(room_id=R095_ROSE_TOWN_DURING_BOWYER_INN_2F, face_direction=SOUTH, x=6, y=43, z=3, identifier="EVENT_273_enter_area_80"),
	ApplyTileModToLevel(use_alternate=True, room_id=R095_ROSE_TOWN_DURING_BOWYER_INN_2F, mod_id=0),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetPriority(2)
	]),
	JmpIfBitClear(UNUSED_7085_0, ["EVENT_273_ret_88"]),
	JmpIfBitSet(INVISIBLE_ITEMS_ANYWHERE, ["EVENT_273_ret_88"]),
	SetBit(INVISIBLE_ITEMS_ANYWHERE),
	SummonObjectToCurrentLevel(NPC_0),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
	Return(identifier="EVENT_273_ret_88"),
	EnterArea(room_id=R096_ROSE_TOWN_INN_2F, face_direction=SOUTH, x=6, y=43, z=3, identifier="EVENT_273_enter_area_89"),
	ApplyTileModToLevel(use_alternate=True, room_id=R096_ROSE_TOWN_INN_2F, mod_id=0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetPriority(2)
	]),
	SetBit(TEMP_7042_0, identifier="EVENT_273_set_bit_92"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=5, y=40, z=6, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST)
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R096_ROSE_TOWN_INN_2F, mod_id=1),
	Return(),
	EnterArea(room_id=R337_MOLEVILLE_INN, face_direction=SOUTH, x=6, y=11, z=1, identifier="EVENT_273_enter_area_96"),
	ApplyTileModToLevel(use_alternate=True, room_id=R337_MOLEVILLE_INN, mod_id=0),
	Return(),
	EnterArea(room_id=R009_MARRYMORE_INN_REGULAR_ROOM, face_direction=SOUTH, x=17, y=12, z=1, identifier="EVENT_273_enter_area_99"),
	ApplyTileModToLevel(use_alternate=True, room_id=R009_MARRYMORE_INN_REGULAR_ROOM, mod_id=0),
	JmpIfObjectNotInSpecificLevel(NPC_1, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_273_jmp_if_object_trigger_disabled_103"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R009_MARRYMORE_INN_REGULAR_ROOM, mod_id=33),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R009_MARRYMORE_INN_REGULAR_ROOM, ["EVENT_273_ret_105"], identifier="EVENT_273_jmp_if_object_trigger_disabled_103"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff()
	]),
	Return(identifier="EVENT_273_ret_105"),
	EnterArea(room_id=R012_MARRYMORE_INN_SUITE_ROOM, face_direction=SOUTH, x=8, y=13, z=1, identifier="EVENT_273_enter_area_106"),
	ApplyTileModToLevel(use_alternate=True, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=0),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ClearBit(TEMP_7042_0),
	Return(),
	EnterArea(room_id=R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, face_direction=SOUTH, x=6, y=73, z=3, identifier="EVENT_273_enter_area_111"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=78, z=6, direction=EAST),
		A_FaceNortheast()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, mod_id=0),
	Return(),
	EnterArea(room_id=R306_SEASIDE_TOWN_INN_2F, face_direction=SOUTH, x=6, y=73, z=3, identifier="EVENT_273_enter_area_115"),
	ApplyTileModToLevel(use_alternate=True, room_id=R306_SEASIDE_TOWN_INN_2F, mod_id=0),
	Return(),
	EnterArea(room_id=R052_MUSHROOM_KINGDOM_INN_2F, face_direction=SOUTH, x=6, y=119, z=3, run_entrance_event=True, identifier="EVENT_273_enter_area_118"),
	ApplyTileModToLevel(use_alternate=True, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0),
	Return(),
	EnterArea(room_id=R346_NIMBUS_LAND_INN_BEDROOM, face_direction=SOUTH, x=15, y=79, z=1, identifier="EVENT_273_enter_area_121"),
	ApplyTileModToLevel(use_alternate=True, room_id=R346_NIMBUS_LAND_INN_BEDROOM, mod_id=0),
	JmpIfBitClear(VOLCANO_LIBERATED, ["EVENT_273_jmp_if_bit_set_127"]),
	SummonObjectToCurrentLevel(NPC_1),
	ApplyTileModToLevel(use_alternate=True, room_id=R346_NIMBUS_LAND_INN_BEDROOM, mod_id=1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_TransferToXYZF(x=17, y=83, z=2, direction=EAST),
		A_TransferXYZFPixels(x=250, y=250, z=0, direction=EAST)
	]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_273_summon_to_current_level_129"], identifier="EVENT_273_jmp_if_bit_set_127"),
	Return(),
	SummonObjectToCurrentLevel(NPC_0, identifier="EVENT_273_summon_to_current_level_129"),
	Return(),
	JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_INN, ["EVENT_273_apply_tile_mod_143"], identifier="EVENT_273_jmp_if_bit_set_131"),
	JmpIfBitSet(OCCUPIED_ROSE_TOWN_INN, ["EVENT_273_apply_tile_mod_145"]),
	JmpIfBitSet(ROSE_TOWN_LIBERATED_INN, ["EVENT_273_apply_tile_mod_147"]),
	JmpIfBitSet(MOLEVILLE_INN, ["EVENT_273_apply_tile_mod_149"]),
	JmpIfBitSet(MARRYMORE_REGULAR_INN, ["EVENT_273_apply_tile_mod_151"]),
	JmpIfBitSet(MARRYMORE_SUITE_INN, ["EVENT_273_apply_tile_mod_153"]),
	JmpIfBitSet(OCCUPIED_SEASIDE_INN, ["EVENT_273_apply_tile_mod_155"]),
	JmpIfBitSet(LIBERATED_SEASIDE_INN, ["EVENT_273_apply_tile_mod_157"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_INN, ["EVENT_273_apply_tile_mod_159"]),
	JmpIfBitSet(NIMBUS_INN, ["EVENT_273_apply_tile_mod_161"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0, identifier="EVENT_273_apply_tile_mod_143"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R095_ROSE_TOWN_DURING_BOWYER_INN_2F, mod_id=0, identifier="EVENT_273_apply_tile_mod_145"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R096_ROSE_TOWN_INN_2F, mod_id=0, identifier="EVENT_273_apply_tile_mod_147"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R337_MOLEVILLE_INN, mod_id=0, identifier="EVENT_273_apply_tile_mod_149"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R009_MARRYMORE_INN_REGULAR_ROOM, mod_id=0, identifier="EVENT_273_apply_tile_mod_151"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=0, identifier="EVENT_273_apply_tile_mod_153"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, mod_id=0, identifier="EVENT_273_apply_tile_mod_155"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R306_SEASIDE_TOWN_INN_2F, mod_id=0, identifier="EVENT_273_apply_tile_mod_157"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R052_MUSHROOM_KINGDOM_INN_2F, mod_id=0, identifier="EVENT_273_apply_tile_mod_159"),
	Return(),
	ApplyTileModToLevel(use_alternate=False, room_id=R346_NIMBUS_LAND_INN_BEDROOM, mod_id=0, identifier="EVENT_273_apply_tile_mod_161"),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	], identifier="EVENT_273_action_queue_163"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(60),
		A_StartLoopNTimes(2),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(2),
		A_EndLoop(),
		A_Pause(60),
		A_StartLoopNTimes(2),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(2),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(2),
		A_EndLoop(),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_WalkWestSteps(3),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	SetSyncActionScript(MARIO, A0787_PLAYER_COWERS_IN_CORNER),
	RunDialog(dialog_id=DI3797_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_WalkSouthSteps(1),
		A_WalkSouthwestSteps(3),
		A_WalkWestSteps(3),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(FAST),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI3798_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	PauseActionScript(MARIO),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_FixedFCoordOn(),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_SequenceLoopingOn(),
		A_WalkNorthwestPixels(4),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(4)
	]),
	RunDialog(dialog_id=DI3799_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(ITEM_ID, RedEssenceItem),
	SetVarToConst(PRIMARY_TEMP_7000, 524),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	AddToInventory(ITEM_ID),
	RunDialog(dialog_id=DI3796_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(2),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(8),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_FaceEast(),
		A_Pause(30),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceSouth()
	]),
	RememberLastObject(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ClearBit(TEMP_704C_0),
	SetBit(NIMBUS_INN_PRIZE_GRANTED),
	Return()
])
