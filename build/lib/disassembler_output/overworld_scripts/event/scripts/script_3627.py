# E3627_EMPTY

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
	ClearBit(TEMP_7042_0),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
	ApplySolidityModToLevel(permanent=True, room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R061_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA_RIGHT_BEFORE_FIGHT, mod_id=0),
	SetSyncActionScript(NPC_0, A0803_INC_PALETTE_ROW),
	SetSyncActionScript(NPC_1, A0805_INC_PALETTE_ROW_4),
	SetSyncActionScript(NPC_4, A0804_INC_PALETTE_ROW_15),
	SetAsyncActionScript(NPC_5, A0806_INC_PALETTE_ROW_3),
	SetSyncActionScript(NPC_4, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_1, A0376_TURN_RANDOMLY_IN_PLACE),
	Pause(10),
	SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_3, A0376_TURN_RANDOMLY_IN_PLACE),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(140),
		A_WalkNortheastSteps(3),
		A_WalkNortheastPixels(12)
	]),
	FadeInFromBlack(sync=True),
	PauseScriptUntilEffectDone(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(10)
	]),
	Pause(90),
	RunDialog(dialog_id=DI2384_REFILLED_CHEST_HINT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNorthwestSteps(2),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_Walk1StepSoutheast(),
		A_ShadowOn(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(90),
		A_ShadowOn(),
		A_TransferToXYZF(x=20, y=36, z=4, direction=EAST),
		A_FaceSouthwest(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestSteps(2)
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI2385_NIMBUS_BOSS_2_IS_STILL_THERE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_3),
	Pause(1),
	SetSyncActionScript(NPC_0, A0628_EMPTY),
	SetAsyncActionScript(NPC_2, A0628_EMPTY),
	Pause(1),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_2, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_1, A0628_EMPTY),
	Pause(8),
	SetAsyncActionScript(NPC_3, A0628_EMPTY),
	SetSyncActionScript(NPC_1, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_3, A0119_SLOW_SEQUENCE_LOOP),
	Pause(10),
	SetAsyncActionScript(NPC_4, A0628_EMPTY),
	SetSyncActionScript(NPC_4, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_10, A0119_SLOW_SEQUENCE_LOOP),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_Walk1StepNortheast()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	Pause(60),
	RunDialog(dialog_id=DI2386_NIMBUS_NPC, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(NPC_1, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_0, A0626_EMPTY),
	SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_5, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_4, A0376_TURN_RANDOMLY_IN_PLACE),
	Pause(120),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_4),
	Pause(1),
	SetSyncActionScript(NPC_4, A0628_EMPTY),
	SetSyncActionScript(NPC_0, A0628_EMPTY),
	SetSyncActionScript(NPC_1, A0628_EMPTY),
	SetSyncActionScript(NPC_2, A0628_EMPTY),
	SetAsyncActionScript(NPC_5, A0628_EMPTY),
	RunDialog(dialog_id=DI2387_NIMBUS_NPC, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Walk1StepSouthwest(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2388_FERTILIZER_LOCATION_HINT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSouthwest()
	]),
	Pause(90),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2389_TALK_TO_NPCS_AGAIN_HINT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	SetSyncActionScript(NPC_1, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_0, A0626_EMPTY),
	SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_5, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_4, A0376_TURN_RANDOMLY_IN_PLACE),
	Pause(120),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_4),
	Pause(1),
	SetSyncActionScript(NPC_1, A0628_EMPTY),
	SetSyncActionScript(NPC_2, A0628_EMPTY),
	SetSyncActionScript(NPC_5, A0628_EMPTY),
	SetSyncActionScript(NPC_0, A0628_EMPTY),
	SetAsyncActionScript(NPC_4, A0628_EMPTY),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2390_NIMBUS_NPC, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_FaceNorthwest(),
		A_Pause(2),
		A_WalkNortheastSteps(3)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2391_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2392_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True),
		A_TransferToXYZF(x=20, y=36, z=4, direction=EAST),
		A_ShadowOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepSouthwest(),
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(2),
		A_Pause(30),
		A_WalkSouthwestPixels(2),
		A_Pause(30),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(4),
		A_Pause(10),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_StartLoopNTimes(3),
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(1),
		A_SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(1),
		A_EndLoop(),
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_EndLoop(),
		A_Pause(30),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(180),
		A_Walk1StepSouthwest(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2)
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI2406_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2393_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2394_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2395_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FixedFCoordOff()
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_WalkSouthwestPixels(8),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2396_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNorthwestPixels(4)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_StartLoopNTimes(2),
		A_ResetProperties(),
		A_Pause(4),
		A_SetSpriteSequence(index=25, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_EndLoop(),
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastPixels(8)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2397_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2398_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2399_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2400_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2401_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2402_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_Pause(30),
		A_FaceNorthwest()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2403_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(6),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownPixels(10),
		A_Pause(120),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(3),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(24),
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_SetSpriteSequence(index=24, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_EndLoop(),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Walk1StepNortheast(),
		A_SetSpriteSequence(index=29, is_mold=True, is_sequence=True, looping=True),
		A_WalkNortheastPixels(2),
		A_Pause(10),
		A_SetSpriteSequence(index=30, is_mold=True, is_sequence=True, looping=True),
		A_WalkNortheastPixels(2),
		A_Pause(10),
		A_SetSpriteSequence(index=31, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(4),
		A_SetWalkingSpeed(SLOW),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	Pause(120),
	SetSyncActionScript(NPC_3, A0810_NIMBUS_NPC_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_2, A0813_NIMBUS_NPC_RANDOM_DIRECTIONS),
	Pause(10),
	SetSyncActionScript(NPC_1, A0811_NIMBUS_NPC_RANDOM_DIRECTIONS),
	ActionQueueSync(target=NPC_6, subscript=[
		A_BPL262728(),
		A_Walk1StepSouthwest(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW),
		A_SetPriority(3)
	]),
	Pause(20),
	SetSyncActionScript(NPC_5, A0812_NIMBUS_NPC_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_4, A0815_NIMBUS_NPC_RANDOM_DIRECTIONS),
	SetSyncActionScript(NPC_0, A0626_EMPTY),
	Pause(40),
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkSoutheastSteps(2),
		A_Walk1StepNortheast(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ShadowOff(),
		A_WalkNorthwestSteps(2),
		A_Walk1StepNortheast(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkWestPixels(8),
		A_WalkSouthwestSteps(8)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=13, y=55, z=4, direction=EAST),
		A_TransferXYZFPixels(x=248, y=0, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_Walk1StepNorthwest(),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2404_EMPTY, above_object=NPC_11, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2405_EMPTY, above_object=NPC_11, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastPixels(8),
		A_VisibilityOff()
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(UNUSED_705E_7),
	SetBit(MAP_DIRECTIONAL_BEAN_VALLEY_NIMBUS_LAND),
	Return()
])
