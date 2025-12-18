# E0290_MUSHROOM_KINGDOM_SHOP_LOGIC

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
	SetBit(TEMP_7043_1),
	Set70107015ToObjectXYZ(target=MARIO, bit_7=True),
	CompareVarToConst(Z_COORD_1, 5),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_338_run_dialog_9"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_290_jmp_if_bit_clear_98"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_290_jmp_if_bit_clear_62"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED, ["EVENT_290_jmp_if_bit_set_13"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_2, ["EVENT_290_set_bit_21"]),
	JmpIfBitSet(UNKNOWN_7081_0, ["EVENT_290_jmp_if_bit_set_13"]),
	SetBit(UNKNOWN_7081_0),
	RunDialog(dialog_id=DI0542_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_290_run_dialog_15"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_1, ["EVENT_290_run_dialog_19"], identifier="EVENT_290_jmp_if_bit_set_13"),
	RunDialog(dialog_id=DI0543_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI0544_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_290_run_dialog_15"),
	OpenShop(SH00_MUSHROOM_KINGDOM),
	FadeInFromBlack(sync=False),
	Return(),
	RunDialog(dialog_id=DI0610_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_290_run_dialog_19"),
	Jmp(["EVENT_290_run_dialog_15"]),
	SetBit(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED, identifier="EVENT_290_set_bit_21"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=14, y=20),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=14, y=20, z=4, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(12),
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI0611_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_ResetProperties(),
		A_Pause(60),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI0612_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI0613_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNortheast(),
		A_SequenceLoopingOff(),
		A_FaceSouthwest()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI0614_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageA(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(8)
	]),
	RunDialog(dialog_id=DI0615_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(3),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_EndLoop(),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI0616_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI0617_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkNorthwestPixels(14),
		A_TransferToXYZF(x=8, y=54, z=0, direction=EAST)
	]),
	Pause(1, identifier="EVENT_290_pause_49"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[0, 1, 2, 3], destinations=["EVENT_290_action_queue_53"]),
	Jmp(["EVENT_290_pause_49"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(30),
		A_FaceNortheast()
	], identifier="EVENT_290_action_queue_53"),
	RunDialog(dialog_id=DI0618_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	SetVarToConst(ITEM_ID, PickMeUpItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(PickMeUpItem),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_290_run_dialog_104"], identifier="EVENT_290_jmp_if_bit_clear_62"),
	JmpIfBitSet(UNKNOWN_7083_4, ["EVENT_290_jmp_if_bit_set_13"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=14, y=20),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=14, y=20, z=4, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(12),
		A_FaceNortheast()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	RunDialog(dialog_id=DI0611_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(38),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI0683_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI0684_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(2),
		A_Pause(30),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(12)
	]),
	UnsyncDialog(),
	RunDialog(dialog_id=DI0685_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	SetVarToConst(ITEM_ID, CricketPieItem),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	RunDialog(dialog_id=DI0686_EMPTY, above_object=NPC_0, closable=False, sync=True, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	UnsyncDialog(),
	RunEventAsSubroutine(E0272_PAUSE_ACTIVE_UNTIL_A_PRESSED),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(20),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI0728_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetVarToConst(TEMP_70AE, 20),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(14),
		A_VisibilityOff()
	]),
	SetBit(UNKNOWN_7083_4),
	RemoveOneOfItemFromInventory(RareFrogCoinItem),
	AddToInventory(CricketPieItem),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(NORMAL)
	]),
	Return(),
	JmpIfBitClear(UNKNOWN_7083_4, ["EVENT_290_jmp_if_bit_clear_62"], identifier="EVENT_290_jmp_if_bit_clear_98"),
	RunDialog(dialog_id=DI2241_EMPTY, above_object=NPC_1, closable=False, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI0544_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	OpenShop(SH00_MUSHROOM_KINGDOM),
	FadeInFromBlack(sync=False),
	Return(),
	RunDialog(dialog_id=DI0687_HOW_CAN_YOU_SHOP_AT_A_TIME_LIKE_THIS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_290_run_dialog_104"),
	Return()
])
