# E3008_CLONE_RESERVED

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
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=18, y=80)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToObjectXY(MARIO),
		A_WalkToXYCoords(x=18, y=82),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToObjectXY(MARIO),
		A_WalkToXYCoords(x=17, y=80),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI1321_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI1322_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI1323_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(20),
		A_SetSpriteSequence(index=0, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI1324_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=1, looping=True)
	]),
	RunDialog(dialog_id=DI1325_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True),
		A_PlaySound(sound=SO047_SNOOZE, channel=4),
		A_Pause(40),
		A_StopSound()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(20),
		A_SetSpriteSequence(index=0, looping=True)
	]),
	RunDialog(dialog_id=DI1326_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_SetSpriteSequence(index=3, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSpriteSequence(index=0, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI1327_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(20),
		A_SetSpriteSequence(index=1, looping=True)
	]),
	RunDialog(dialog_id=DI1328_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=3, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, looping=True)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, looping=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, looping=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, looping=True)
	]),
	RunDialog(dialog_id=DI1329_10_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK251_AXEM_GREEN_ALONE, BF35_MARRYMORE_CHAPEL_SANCTUARY),
	JmpIfBitClear(GAME_OVER, ["EVENT_3008_action_queue_34"]),
	ResetAndChooseGame(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, looping=True)
	], identifier="EVENT_3008_action_queue_34"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=0, looping=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI1330_30_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(80),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI1331_4_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO014_FLOWER, channel=6),
	AddToInventory(SleepBombItem),
	RunDialog(dialog_id=DI1332_12_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	RunDialog(dialog_id=DI1333_30_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(60),
		A_Pause(30)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_JumpToHeight(60),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI1334_2_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=1, looping=True),
		A_Walk1StepSoutheast(),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=0, looping=True, mirror_sprite=True),
		A_Walk1StepNorthwest(),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Walk1StepSoutheast(),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(25),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(10),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(10),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI1335_2_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI1341_EMPTY_AUTO, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=3, looping=True)
	]),
	RunDialog(dialog_id=DI1336_15_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_709E_5),
	FadeOutToBlack(sync=False, duration=40),
	EnterArea(room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, face_direction=SOUTHWEST, x=20, y=16, z=0, run_entrance_event=True),
	Return()
])
