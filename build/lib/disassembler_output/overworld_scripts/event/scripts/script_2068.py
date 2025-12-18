# E2068_DOJO_BOSS_2

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
	JmpIfBitSet(UNKNOWN_709D_6, ["EVENT_2068_run_dialog_86"]),
	JmpIfBitSet(UNKNOWN_709D_5, ["EVENT_2068_pause_action_script_77"]),
	JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2068_run_dialog_75"]),
	RunDialog(dialog_id=DI3043_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2068_run_dialog_71"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=5, y=16),
		A_FaceNortheast()
	]),
	JmpIfBitSet(DOJO_BOSS_3_DEFEATED, ["EVENT_2068_run_dialog_13"]),
	JmpIfBitSet(DOJO_BOSS_2_DEFEATED, ["EVENT_2068_run_dialog_11"]),
	RunDialog(dialog_id=DI3046_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2068_pause_14"]),
	RunDialog(dialog_id=DI3049_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_11"),
	Jmp(["EVENT_2068_pause_14"]),
	RunDialog(dialog_id=DI3050_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_13"),
	Pause(30, identifier="EVENT_2068_pause_14"),
	FreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkNortheastSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_Pause(45)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkSouthwestSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=False),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
		A_Pause(15),
		A_PlaySound(sound=SO096_SWINGING_FIST, channel=6),
		A_Pause(30)
	]),
	JmpIfBitSet(DOJO_BOSS_3_DEFEATED, ["EVENT_2068_start_battle_24"]),
	JmpIfBitSet(DOJO_BOSS_2_DEFEATED, ["EVENT_2068_start_battle_22"]),
	StartBattleAtBattlefield(PACK178_JINX1_FIGHT_STATIC, BF46_JINXS_DOJO),
	Jmp(["EVENT_2068_restore_all_hp_26"]),
	StartBattleAtBattlefield(PACK187_JINX2_FIGHT_STATIC, BF46_JINXS_DOJO, identifier="EVENT_2068_start_battle_22"),
	Jmp(["EVENT_2068_restore_all_hp_26"]),
	StartBattleAtBattlefield(PACK188_JINX3_FIGHT_STATIC, BF46_JINXS_DOJO, identifier="EVENT_2068_start_battle_24"),
	Jmp(["EVENT_2068_restore_all_hp_26"]),
	RestoreAllHP(identifier="EVENT_2068_restore_all_hp_26"),
	RestoreAllFP(),
	Pause(1),
	StopMusicFDA2(),
	FadeOutMusicToVolume(duration=0, volume=100),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	Pause(1),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastSteps(1),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(NORMAL)
	]),
	UnfreezeCamera(),
	Pause(30),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2068_run_dialog_73"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2068_run_dialog_69"]),
	JmpIfBitSet(DOJO_BOSS_3_DEFEATED, ["EVENT_2068_run_dialog_48"]),
	JmpIfBitSet(DOJO_BOSS_2_DEFEATED, ["EVENT_2068_run_dialog_45"]),
	RunDialog(dialog_id=DI3051_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(DOJO_BOSS_2_DEFEATED),
	Return(),
	RunDialog(dialog_id=DI3052_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_45"),
	SetBit(DOJO_BOSS_3_DEFEATED),
	Return(),
	RunDialog(dialog_id=DI3339_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_48"),
	Pause(30),
	SetVarToConst(ITEM_ID, JinxBeltItem),
	SetVarToConst(PRIMARY_TEMP_7000, 3341),
	RunEventAsSubroutine(E3829_EMPTY),
	Pause(30),
	RunDialog(dialog_id=DI3340_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(15),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_FixedFCoordOff(),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(4),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestSteps(1),
		A_VisibilityOff(),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6),
		A_Pause(75),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_Pause(60),
		A_PlaySound(sound=SO058_INSERT, channel=6),
		A_Pause(45),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(40),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(8),
		A_PlaySound(sound=SO025_HEEL_CLICK, channel=6),
		A_Pause(70),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6),
		A_VisibilityOn(),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(4),
		A_WalkNorthwestSteps(1),
		A_FaceSouthwest()
	]),
	Pause(45),
	RunDialog(dialog_id=DI3342_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOn(),
		A_ShadowOn(),
		A_WalkSoutheastSteps(1),
		A_ShadowOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=5, y=14),
		A_FaceSouthwest(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(60),
	RunDialog(dialog_id=DI3343_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(15),
	SetSyncActionScript(NPC_0, A1006_DOJO_PERMA_JUMP),
	SetSyncActionScript(NPC_1, A1006_DOJO_PERMA_JUMP),
	ApplyTileModToLevel(use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=32),
	SetBit(DOJO_BOSS_4_DEFEATED),
	Return(),
	RunDialog(dialog_id=DI3048_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_69"),
	Return(),
	RunDialog(dialog_id=DI3045_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_71"),
	Return(),
	RunDialog(dialog_id=DI3053_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_73"),
	Return(),
	RunDialog(dialog_id=DI3353_DOJO_BOSS_2_FULLY_DEFEATED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_75"),
	Return(),
	PauseActionScript(NPC_1, identifier="EVENT_2068_pause_action_script_77"),
	PauseActionScript(NPC_0),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkToXYCoords(x=5, y=9),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI0815_JUST_YOU_WAIT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2068_run_dialog_84"]),
	JmpToEvent(E4015_CLONE_RESERVED),
	Return(),
	RunDialog(dialog_id=DI2236_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_84"),
	Return(),
	RunDialog(dialog_id=DI3681_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2068_run_dialog_86"),
	Return()
])
