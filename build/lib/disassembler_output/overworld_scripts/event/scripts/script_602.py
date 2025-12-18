# E0602_MARRYMORE_INN_MANAGER

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
	JmpIfBitSet(TEMP_7042_0, ["EVENT_602_run_dialog_80"]),
	StoreItemAmountTo7000(BaneBombItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_602_jmp_if_bit_set_19"]),
	RunDialog(dialog_id=DI0560_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(25),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSouthwest(),
		A_Pause(35),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(35),
		A_FaceSoutheast()
	]),
	Pause(70),
	RunDialog(dialog_id=DI0978_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_JumpToHeight(90)
	]),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	Pause(25),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkSoutheastSteps(3),
		A_WalkNortheastSteps(2),
		A_VisibilityOff()
	]),
	Inc(MARRYMORE_SUITE_LEGAL_COUNT),
	SetBit(TEMP_7042_0),
	SetBit(UNKNOWN_709D_1),
	Return(),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_602_jmp_if_bit_set_156"], identifier="EVENT_602_jmp_if_bit_set_19"),
	JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_602_jmp_if_bit_set_156"]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_602_run_dialog_154"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_602_run_dialog_152"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_602_run_dialog_152"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_602_run_dialog_80"]),
	RunDialog(dialog_id=DI2470_MARRYMORE_HOTEL_MENU, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBOrCSelected(['EVENT_602_copy_var_to_var_31', 'EVENT_602_run_dialog_78']),
	CloseDialog(),
	OpenShop(SH05_MARRYMORE),
	FadeInFromBlack(sync=False),
	Return(),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000, identifier="EVENT_602_copy_var_to_var_31"),
	CompareVarToConst(PRIMARY_TEMP_7000, 1),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_602_run_dialog_37"]),
	RunDialog(dialog_id=DI2471_MARRYMORE_HOTEL_ROOM_CHOICE_1ST_TIME, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBOrCSelected(['EVENT_602_set_var_to_const_50', 'EVENT_602_run_dialog_78']),
	Jmp(["EVENT_602_set_var_to_const_39"]),
	RunDialog(dialog_id=DI2508_MARRYMORE_HOTEL_ROOM_CHOICE, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_37"),
	JmpIfDialogOptionBOrCSelected(['EVENT_602_set_var_to_const_50', 'EVENT_602_run_dialog_78']),
	SetVarToConst(SECONDARY_TEMP_7024, 10, identifier="EVENT_602_set_var_to_const_39"),
	ClearBit(UNKNOWN_7049_4),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_602_run_dialog_48"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	RunDialog(dialog_id=DI0974_ENJOY_YOUR_STAY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(MARRYMORE_REGULAR_INN),
	Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
	RunDialog(dialog_id=DI2475_CANT_AFFORD_MARRYMORE_HOTEL, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_48"),
	Return(),
	SetVarToConst(SECONDARY_TEMP_7024, 200, identifier="EVENT_602_set_var_to_const_50"),
	ClearBit(UNKNOWN_7049_4),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_602_run_dialog_48"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_602_set_bit_82"]),
	Inc(MARRYMORE_SUITE_LEGAL_COUNT),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_602_set_bit_82"]),
	RunDialog(dialog_id=DI2472_CHOSE_SUITE_1ST_TIME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_Walk1StepNorthwest(),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_SLOW),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastPixels(4),
		A_SequenceLoopingOff(),
		A_Pause(60),
		A_SequenceLoopingOn(),
		A_WalkNorthwestPixels(4),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(SLOW),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSouthwest(),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(60),
		A_Walk1StepSouthwest(),
		A_WalkSoutheastPixels(12)
	]),
	Pause(80),
	RunDialog(dialog_id=DI0977_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO085_FLOWER, channel=6),
	SetVarToConst(ITEM_ID, FlowerTabItem),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(FlowerTabItem),
	RunDialog(dialog_id=DI0978_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7042_0, identifier="EVENT_602_set_bit_74"),
	SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
	SetSyncActionScript(NPC_5, A0301_MARRYMORE_BELLHOP_WHILE_PLAYER_WORKING),
	Return(),
	RunDialog(dialog_id=DI0976_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_78"),
	Return(),
	RunDialog(dialog_id=DI0973_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_80"),
	Return(),
	SetBit(TEMP_7043_0, identifier="EVENT_602_set_bit_82"),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_602_set_7010_to_object_xyz_91"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_602_pause_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_602_pause_112"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_602_pause_119"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["EVENT_602_pause_128"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 200),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_602_jmp_if_bit_set_139"]),
	Set70107015ToObjectXYZ(target=NPC_5, bit_7=True, identifier="EVENT_602_set_7010_to_object_xyz_91"),
	CompareVarToConst(X_COORD_1, 5),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_602_start_embedded_action_script_100"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOff(),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	RunDialog(dialog_id=DI2473_STAYED_X_TIMES_IN_SUITE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_96"),
	UnsyncDialog(),
	RememberLastObject(),
	Jmp(["EVENT_602_set_bit_74"]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOff(),
		A_Walk1StepNorthwest(),
		A_WalkToXYCoords(x=6, y=61),
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW)
	], identifier="EVENT_602_start_embedded_action_script_100"),
	Jmp(["EVENT_602_run_dialog_96"]),
	Pause(10, identifier="EVENT_602_pause_102"),
	SetVarToConst(PRIMARY_TEMP_7000, 3),
	RunDialog(dialog_id=DI2477_MARRYMORE_SUITE_PRIZE_GRANT_REPEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_Pause(40),
		A_SetSequenceSpeed(SLOW),
		A_WalkSoutheastPixels(12)
	]),
	RunDialog(dialog_id=DI1022_HERE_YOU_GO, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, FlowerJarItem),
	SetVarToConst(PRIMARY_TEMP_7000, 524),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	Pause(10),
	Jmp(["EVENT_602_set_7010_to_object_xyz_91"]),
	Pause(10, identifier="EVENT_602_pause_112"),
	SetVarToConst(PRIMARY_TEMP_7000, 5),
	RunDialog(dialog_id=DI2477_MARRYMORE_SUITE_PRIZE_GRANT_REPEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	AddFrogCoins(1),
	RunDialog(dialog_id=DI0526_GOT_A_FROG_COIN, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Jmp(["EVENT_602_set_7010_to_object_xyz_91"]),
	Pause(10, identifier="EVENT_602_pause_119"),
	SetVarToConst(PRIMARY_TEMP_7000, 10),
	RunDialog(dialog_id=DI2477_MARRYMORE_SUITE_PRIZE_GRANT_REPEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	Pause(30),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	AddFrogCoins(2),
	RunDialog(dialog_id=DI0526_GOT_A_FROG_COIN, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Jmp(["EVENT_602_set_7010_to_object_xyz_91"]),
	Pause(10, identifier="EVENT_602_pause_128"),
	SetVarToConst(PRIMARY_TEMP_7000, 15),
	RunDialog(dialog_id=DI2477_MARRYMORE_SUITE_PRIZE_GRANT_REPEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	Pause(30),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	Pause(30),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	AddFrogCoins(3),
	RunDialog(dialog_id=DI0526_GOT_A_FROG_COIN, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Jmp(["EVENT_602_set_7010_to_object_xyz_91"]),
	JmpIfBitSet(UNKNOWN_709F_4, ["EVENT_602_set_7010_to_object_xyz_91"], identifier="EVENT_602_jmp_if_bit_set_139"),
	Pause(10),
	SetVarToConst(PRIMARY_TEMP_7000, 200),
	RunDialog(dialog_id=DI2477_MARRYMORE_SUITE_PRIZE_GRANT_REPEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartLoopNTimes(19),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	Pause(20),
	EndLoop(),
	AddFrogCoins(20),
	RunDialog(dialog_id=DI0526_GOT_A_FROG_COIN, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	SetVarToConst(MARRYMORE_SUITE_LEGAL_COUNT, 255),
	SetBit(UNKNOWN_709F_4),
	Jmp(["EVENT_602_set_7010_to_object_xyz_91"]),
	RunDialog(dialog_id=DI0998_THANK_YOU_VERY_MUCH, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_152"),
	Return(),
	RunDialog(dialog_id=DI1004_BREAK_EVERY_BONE_IN_YOUR_BODY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_154"),
	Return(),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_602_run_dialog_176"], identifier="EVENT_602_jmp_if_bit_set_156"),
	Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_602_run_dialog_181"]),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	Dec(PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_602_run_dialog_168"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	RunDialog(dialog_id=DI1019_NOT_OFF_THE_HOOK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=3, y=55),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SequenceLoopingOn()
	]),
	ClearBit(EMPLOYMENT_704C_2),
	RunBackgroundEvent(event_id=E0617_MARIO_AS_BELLHOP_MAIN_EVENT, return_on_level_exit=True),
	Return(),
	RunDialog(dialog_id=DI1020_FINISHED_WORKING_AT_MARRYMORE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_168"),
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	ClearBit(EMPLOYMENT_704C_2),
	SetVarToConst(TEMP_70AC, 0),
	SetVarToConst(TEMP_70B8, 0),
	SetBit(EMPLOYMENT_704C_3),
	Return(),
	RunDialog(dialog_id=DI1014_SEE_GUEST_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_176"),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_256_ret_0"]),
	RunBackgroundEvent(event_id=E0623_MARRYMORE_INN_EMPLOYED_GUEST_LEAVES, return_on_level_exit=True),
	SetBit(TEMP_7044_4),
	Return(),
	RunDialog(dialog_id=DI1021_MARRYMORE_INNKEEPER_TELLS_YOU_TO_GO_BEHIND_COUNTER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_181"),
	Return()
])
