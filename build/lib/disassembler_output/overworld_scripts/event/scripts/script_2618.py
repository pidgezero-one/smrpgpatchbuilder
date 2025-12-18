# E2618_FACTORY_2ND_BOSS

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
	JmpIfBitSet(INNER_FACTORY_ROOM_3_COMPLETED, ["EVENT_2618_ret_118"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=3, y=17)
	]),
	SetSyncActionScript(NPC_12, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetSyncActionScript(NPC_13, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	SetSyncActionScript(NPC_14, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3237_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(16),
		A_ShiftToXYCoords(x=11, y=49)
	]),
	UnsyncDialog(),
	SetSyncActionScript(NPC_12, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetSyncActionScript(NPC_13, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_14, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_13, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3234_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(NPC_13, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_12, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3235_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(NPC_12, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	SetAsyncActionScript(NPC_14, A0960_FACTORY_2ND_BOSS_HENCHMAN),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3236_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(NPC_14, A0961_FACTORY_2ND_BOSS_HENCHMAN),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3238_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3239_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestSteps(2),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FAST),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_WalkNortheastSteps(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FAST),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_WalkNortheastPixels(6),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FASTER),
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_WalkSoutheastSteps(3),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(4)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3240_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_12, A0401_SEQUENCE_LOOPING_OFF),
	SetSyncActionScript(NPC_13, A0401_SEQUENCE_LOOPING_OFF),
	SetAsyncActionScript(NPC_14, A0401_SEQUENCE_LOOPING_OFF),
	Pause(32),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3267_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3241_EMPTY, above_object=TOADSTOOL, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3268_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(24),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3242_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_15),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=5, y=23)
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(2)
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueSync(target=NPC_12, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3243_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(16),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_Walk1StepNortheast(),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(8),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3244_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3245_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_15, subscript=[
		A_Pause(16),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3246_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_15, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3247_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(2)
	]),
	Pause(24),
	StartBattleAtBattlefield(PACK147_MANAGER_STATIC, BF48_FACTORY_GROUNDS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2618_restore_all_hp_90"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2618_restore_all_hp_90"),
	RestoreAllFP(),
	SetBit(INNER_FACTORY_ROOM_3_COMPLETED),
	RemoveObjectFromCurrentLevel(NPC_12),
	RemoveObjectFromCurrentLevel(NPC_13),
	RemoveObjectFromCurrentLevel(NPC_14),
	RemoveObjectFromCurrentLevel(NPC_16),
	RemoveObjectFromSpecificLevel(NPC_12, R471_FACTORY_GROUNDS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_13, R471_FACTORY_GROUNDS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_14, R471_FACTORY_GROUNDS_AREA_02),
	RemoveObjectFromSpecificLevel(NPC_16, R471_FACTORY_GROUNDS_AREA_02),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ResetProperties()
	]),
	FadeInFromBlack(sync=False),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3142_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(32),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(32)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3269_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(5),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(128),
		A_FaceNorthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(6),
		A_FaceSoutheast(),
		A_ResetProperties()
	]),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3142_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_VisibilityOff()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(identifier="EVENT_2618_ret_118")
])
