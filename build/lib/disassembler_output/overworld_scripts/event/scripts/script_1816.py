# E1816_TROOPA_CLIFF_FINISH

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
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1816_ret_77"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1816_ret_77"]),
	SetBit(TEMP_7044_2),
	StopAllBackgroundEvents(),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_1),
	StopSound(),
	Pause(1),
	PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
	FadeOutMusicToVolume(duration=2, volume=127),
	SetVarToConst(TEMP_70AB, 21),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=25, y=112),
		A_FaceNortheast(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_Pause(20),
		A_PlaySound(sound=SO133_CLOSE_HIT_DOOR, channel=4),
		A_Pause(20)
	]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1263_TROOPA_CLIFF_TIME, above_object=MARIO, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties()
	]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 1800),
	JmpIfComparisonResultIsLesser(["EVENT_1816_compare_var_to_const_22"]),
	RunDialogForDuration(dialog_id=DI1271_EMPTY, duration=1, sync=False),
	Return(),
	CompareVarToConst(PRIMARY_TEMP_7000, 840, identifier="EVENT_1816_compare_var_to_const_22"),
	JmpIfComparisonResultIsLesser(["EVENT_1816_compare_var_to_const_26"]),
	RunDialogForDuration(dialog_id=DI1264_EMPTY, duration=1, sync=False),
	Return(),
	CompareVarToConst(PRIMARY_TEMP_7000, 720, identifier="EVENT_1816_compare_var_to_const_26"),
	JmpIfComparisonResultIsLesser(["EVENT_1816_compare_var_to_const_32"]),
	RunDialogForDuration(dialog_id=DI1265_EMPTY, duration=0, sync=False),
	JmpIfRandom2of3(['EVENT_1816_run_dialog_duration_76', 'EVENT_1816_run_dialog_duration_76']),
	SetVarToConst(TEMP_7028, 1),
	Jmp(["EVENT_1816_run_dialog_duration_66"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 660, identifier="EVENT_1816_compare_var_to_const_32"),
	JmpIfComparisonResultIsLesser(["EVENT_1816_run_dialog_duration_63"]),
	RunDialogForDuration(dialog_id=DI1266_EMPTY, duration=0, sync=False),
	JmpIfBitSet(UNKNOWN_LARGE_CONVEYOR_ROOM, ["EVENT_1816_set_var_to_const_57"]),
	SetBit(UNKNOWN_LARGE_CONVEYOR_ROOM, identifier="EVENT_1816_set_bit_36"),
	RunDialogForDuration(dialog_id=DI1268_EMPTY, duration=1, sync=False),
	StoreCharacterEquipmentTo7000(MARIO, AccessoryItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_1816_action_queue_44"]),
	SetVarToConst(ITEM_ID, TroopaPinItem),
	SetVarToConst(PRIMARY_TEMP_7000, 1219),
	RunEventAsSubroutine(E3829_EMPTY),
	Return(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(5),
		A_EndLoop()
	], identifier="EVENT_1816_action_queue_44"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_AddZCoord1Step(),
		A_WalkSouthwestSteps(2),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_ShiftZDownSteps(2),
		A_StartLoopNTimes(2),
		A_PlaySound(sound=SO057_FINGER_SNAP, channel=4),
		A_WalkSouthwestPixels(6),
		A_WalkNortheastPixels(6),
		A_Pause(1),
		A_EndLoop(),
		A_PlaySound(sound=SO134_SWIPE, channel=4),
		A_WalkEastPixels(16),
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_WalkEastPixels(16),
		A_StartLoopNTimes(2),
		A_PlaySound(sound=SO057_FINGER_SNAP, channel=4),
		A_WalkSoutheastPixels(6),
		A_WalkNorthwestPixels(6),
		A_Pause(1),
		A_EndLoop(),
		A_Pause(30),
		A_ShiftZUpSteps(2),
		A_FixedFCoordOff(),
		A_Walk1StepNorth(),
		A_DecZCoord1Step(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(5),
		A_EndLoop()
	]),
	PlaySound(sound=SO085_FLOWER, channel=6),
	SetBit(NIMBUS_HOUSE_ITEM_RETRIEVED),
	SetSyncActionScript(MARIO, A0510_EMPTY),
	SetVarToConst(ITEM_ID, TroopaPinItem),
	SetVarToConst(PRIMARY_TEMP_7000, 1219),
	RunDialog(dialog_id=PRIMARY_TEMP_7000, above_object=BOWSER, closable=True, sync=True, multiline=False, use_background=False),
	EquipItemToCharacter(TroopaPinItem, MARIO),
	UnsyncActionScript(MARIO),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	SetVarToConst(TEMP_7028, 1, identifier="EVENT_1816_set_var_to_const_57"),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 690),
	JmpIfComparisonResultIsLesser(["EVENT_1816_jmp_62"]),
	JmpIfRandom1of2(["EVENT_1816_run_dialog_duration_76"]),
	Jmp(["EVENT_1816_run_dialog_duration_66"], identifier="EVENT_1816_jmp_62"),
	RunDialogForDuration(dialog_id=DI1267_EMPTY, duration=0, sync=False, identifier="EVENT_1816_run_dialog_duration_63"),
	JmpIfBitClear(UNKNOWN_LARGE_CONVEYOR_ROOM, ["EVENT_1816_set_bit_36"]),
	SetVarToConst(TEMP_7028, 5),
	RunDialogForDuration(dialog_id=DI1269_EMPTY, duration=1, sync=False, identifier="EVENT_1816_run_dialog_duration_66"),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	SetObjectMemoryToVar(TEMP_7028),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_PlaySound(sound=SO094_FROG_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_UnknownCommand(bytearray(b'\x97\x15')),
		A_SetAllSpeeds(FASTEST),
		A_ShiftZUpPixels(16),
		A_SetAllSpeeds(NORMAL),
		A_VisibilityOn(),
		A_FloatingOff(),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepSouthwest(),
		A_Pause(6),
		A_VisibilityOff()
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	AddFrogCoins(PRIMARY_TEMP_7000),
	EndLoop(),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	Return(),
	RunDialogForDuration(dialog_id=DI1270_EMPTY, duration=1, sync=False, identifier="EVENT_1816_run_dialog_duration_76"),
	Return(identifier="EVENT_1816_ret_77")
])
