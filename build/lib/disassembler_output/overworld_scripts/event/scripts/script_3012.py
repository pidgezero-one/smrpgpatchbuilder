# E3012_CLONE_RESERVED

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
	JmpIfBitSet(UNKNOWN_709E_6, ["EVENT_3012_run_dialog_49"]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3974_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3975_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI0895_GOAL, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=5, looping=True)
	]),
	RunDialog(dialog_id=DI1653_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI1894_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK254_SMITHY_HENCHMEN_PACK_2, BF47_CULEX, identifier="EVENT_3012_start_battle_13"),
	JmpIfBitClear(GAME_OVER, ["EVENT_3012_play_music_default_volume_16"]),
	ResetGame(),
	PlayMusicAtDefaultVolume(M0058_CONVERSATIONWITHCULEX, identifier="EVENT_3012_play_music_default_volume_16"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=29, y=39),
		A_WalkEastPixels(8),
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=8, looping=True)
	]),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(UNKNOWN_709E_6, ["EVENT_3012_run_dialog_22"]),
	RunDialog(dialog_id=DI1015_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Set7000To7FMemVar(0xFFA0),
	RunDialog(dialog_id=DI1023_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3012_run_dialog_22"),
	CompareVarToConst(PRIMARY_TEMP_7000, 25),
	JmpIfComparisonResultIsLesser(["EVENT_3012_run_dialog_30"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 41),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3012_run_dialog_33"]),
	RunDialog(dialog_id=DI2952_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_3012_jmp_if_bit_set_36"]),
	Return(),
	RunDialog(dialog_id=DI2951_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3012_run_dialog_30"),
	Jmp(["EVENT_3012_jmp_if_bit_set_36"]),
	Return(),
	RunDialog(dialog_id=DI2953_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3012_run_dialog_33"),
	Jmp(["EVENT_3012_jmp_if_bit_set_36"]),
	Return(),
	JmpIfBitSet(UNKNOWN_709E_6, ["EVENT_3012_run_dialog_44"], identifier="EVENT_3012_jmp_if_bit_set_36"),
	SetBit(UNKNOWN_709E_6),
	SetSyncActionScript(MARIO, A0510_EMPTY),
	PlaySound(sound=SO014_FLOWER, channel=6),
	AddToInventory(SpareItem2),
	RunDialog(dialog_id=DI1024_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	UnsyncActionScript(MARIO),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunDialog(dialog_id=DI1025_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3012_run_dialog_44"),
	RestoreAllHP(),
	RestoreAllFP(),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4, run_entrance_event=True),
	Return(),
	RunDialog(dialog_id=DI1026_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3012_run_dialog_49"),
	Jmp(["EVENT_3012_start_battle_13"]),
	Return()
])
