# E0738_NIMBUS_LAND_FINAL_BOSS_FIGHT_TOWN_SQUARE_LOADER

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
	SetSyncActionScript(LAYER_3, A0808_NIMBUS_EXTERIOR_LAYER_3),
	SetTempSyncActionScript(NPC_0, A0803_INC_PALETTE_ROW),
	SetTempSyncActionScript(NPC_2, A0807_INC_PALETTE_ROW_2),
	SetTempSyncActionScript(NPC_6, A0803_INC_PALETTE_ROW),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(3),
		A_WalkNortheastSteps(6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=11, y=59, z=2, direction=EAST),
		A_FloatingOff(),
		A_FaceNortheast(),
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=True, duration=60),
	Pause(10),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(5)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(2),
		A_SetSequenceSpeed(SLOW),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Pause(38),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2481_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceNortheast(),
		A_Pause(60),
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastSteps(3),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(2),
		A_FaceNortheast(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(80),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(4),
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(50),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_Walk1StepSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_Pause(40),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceNorthwest(),
		A_Pause(60),
		A_Walk1StepNortheast(),
		A_WalkNorthwestSteps(4)
	]),
	RememberLastObject(),
	Pause(10),
	SetSyncActionScript(NPC_0, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(10),
	RunDialog(dialog_id=DI2482_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	PauseActionScript(NPC_0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_738_action_queue_26_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_738_action_queue_26_SUBSCRIPT_pause_3"]),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(10),
		A_FaceSouthwest()
	]),
	SetSyncActionScript(NPC_7, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(10),
	RunDialog(dialog_id=DI2483_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_738_action_queue_34_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_738_action_queue_34_SUBSCRIPT_pause_3"]),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(20),
		A_FaceSoutheast()
	]),
	SetSyncActionScript(NPC_4, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(10),
	RunDialog(dialog_id=DI2484_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	PauseActionScript(NPC_4),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_738_action_queue_42_SUBSCRIPT_pause_3"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_738_action_queue_42_SUBSCRIPT_pause_3"]),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_FaceNorthwest(),
		A_Pause(40),
		A_FaceSouthwest(),
		A_Pause(40),
		A_FaceNortheast(),
		A_Pause(40),
		A_FaceSoutheast(),
		A_Pause(40),
		A_FaceNorthwest(),
		A_Pause(40),
		A_FaceNortheast(),
		A_Pause(20),
		A_FaceSouthwest(),
		A_Pause(20),
		A_FaceNortheast(),
		A_Pause(20),
		A_FaceSoutheast(),
		A_Pause(20),
		A_FaceNorthwest(),
		A_Pause(20),
		A_FaceNortheast(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceNorthwest(),
		A_Pause(8),
		A_FaceNortheast(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_Pause(8),
		A_FaceNortheast(),
		A_SetWalkingSpeed(VERY_FAST),
		A_FixedFCoordOn(),
		A_WalkNortheastPixels(2),
		A_StartLoopNTimes(9),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_EndLoop()
	]),
	SetSyncActionScript(NPC_8, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(30),
	RunDialog(dialog_id=DI2485_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(40),
	CloseDialog(),
	SetSyncActionScript(NPC_7, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(30),
	RunDialog(dialog_id=DI2486_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Pause(40),
	CloseDialog(),
	SetSyncActionScript(NPC_4, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(8),
	SetSyncActionScript(NPC_0, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(8),
	SetSyncActionScript(NPC_2, A0880_CROWD_AROUND_NIMBUS_BOSS),
	Pause(14),
	RunDialog(dialog_id=DI2486_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(40),
	CloseDialog(),
	Pause(30),
	RunDialog(dialog_id=DI2485_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Pause(40),
	CloseDialog(),
	RememberLastObject(),
	RunDialog(dialog_id=DI2487_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SequencePlaybackOff(),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZUpPixels(4),
		A_SetWalkingSpeed(VERY_FAST),
		A_DecZCoord1Step(),
		A_ShiftZDownPixels(12),
		A_PlaySound(sound=SO020_LIGHTING_BOLT, channel=4),
		A_SequencePlaybackOn()
	]),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_7),
	PauseActionScript(NPC_8),
	PauseActionScript(NPC_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_JumpToHeight(height=112, silent=True),
		A_FixedFCoordOn(),
		A_SequenceLoopingOff(),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(4)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_JumpToHeight(height=112, silent=True),
		A_FixedFCoordOn(),
		A_SequenceLoopingOff(),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_JumpToHeight(height=112, silent=True),
		A_FixedFCoordOn(),
		A_SequenceLoopingOff(),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(4)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_JumpToHeight(height=112, silent=True),
		A_FixedFCoordOn(),
		A_SequenceLoopingOff(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(2),
		A_WalkSouthPixels(4)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_BPL262728(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_JumpToHeight(height=112, silent=True),
		A_FixedFCoordOn(),
		A_SequenceLoopingOff(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(4)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2488_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(10),
		A_FaceNorthwest(),
		A_Pause(10),
		A_FaceSouthwest(),
		A_Pause(10),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2489_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2490_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	FreezeCamera(),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_WalkSouthPixels(12),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FixedFCoordOff(),
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FixedFCoordOff(),
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOff(),
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_VisibilityOn(),
		A_JumpToHeight(160),
		A_WalkNortheastPixels(1),
		A_FloatingOn(),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(11)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2491_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(4),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(4),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(4),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2492_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2493_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2494_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2495_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(3),
		A_TransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=10, sprite_offset=4, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=11, sprite_offset=4, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_EndLoop(),
		A_SetSpriteSequence(index=10, sprite_offset=4, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSouthwest(),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(50),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceSouthwest(),
		A_Pause(20),
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff()
	]),
	ClearBit(NIMBUS_BOSS_IN_TOWN_SQUARE),
	StartBattleAtBattlefield(PACK171_VALENTINA_FIGHT_STATIC, BF24_NIMBUS_LAND),
	SetVarToConst(TEMP_70A9, 29),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
	RestoreAllHP(),
	RestoreAllFP(),
	RunEventAsSubroutine(E3660_NIMBUS_REPOPULATE_CASTLE_UPON_LIBERATION),
	JmpToEvent(E3658_EMPTY)
])
