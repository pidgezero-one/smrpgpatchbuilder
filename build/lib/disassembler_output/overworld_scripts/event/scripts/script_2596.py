# E2596_ABYSS_1ST_BOSS_FIGHT

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
	JmpIfBitSet(ABYSS_BOSS_1_DEFEATED, ["EVENT_2596_ret_41"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_PlaySound(sound=SO029_ALARM_CLOCK, channel=4)
	]),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(1),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_EndLoop()
	]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=4, y=69)
	]),
	Pause(16),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_PlaySound(sound=SO029_ALARM_CLOCK, channel=4)
	]),
	RunDialog(dialog_id=DI3150_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO000_SILENCE, channel=4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(16),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_PlaySound(sound=SO029_ALARM_CLOCK, channel=4)
	]),
	RunDialog(dialog_id=DI3150_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_PlaySound(sound=SO000_SILENCE, channel=4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(16),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	PlaySound(sound=SO029_ALARM_CLOCK, channel=6),
	RunDialog(dialog_id=DI3160_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Pause(16),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_PlaySound(sound=SO029_ALARM_CLOCK, channel=4)
	]),
	SetSyncActionScript(MARIO, A0861_ABYSS_1ST_BOSS_FIGHT_SHOCKED),
	SetSyncActionScript(SCREEN_FOCUS, A0862_ABYSS_1ST_BOSS_FIGHT_CAMERA),
	RunDialog(dialog_id=DI3151_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=False, use_background=False),
	StartBattleAtBattlefield(PACK174_COUNTDOWN_FIGHT_STATIC, BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD),
	SetSyncActionScript(MARIO, A0015_DO_NOTHING),
	SetSyncActionScript(SCREEN_FOCUS, A0015_DO_NOTHING),
	JmpIfBitClear(GAME_OVER, ["EVENT_2596_restore_all_hp_37"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2596_restore_all_hp_37"),
	RestoreAllFP(),
	SetBit(ABYSS_BOSS_1_DEFEATED),
	EnterArea(room_id=R433_SMITHY_FACTORY_AREA_01_DUMMY, face_direction=NORTHEAST, x=7, y=106, z=10, run_entrance_event=True),
	Return(identifier="EVENT_2596_ret_41")
])
