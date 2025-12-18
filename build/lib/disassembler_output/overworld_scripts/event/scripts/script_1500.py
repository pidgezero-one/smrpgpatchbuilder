# E1500_CLONE_RESERVED

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
		A_WalkToXYCoords(x=6, y=20),
		A_FaceSouthwest()
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_4),
	Pause(30),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(40)
	]),
	JmpIfBitSet(UNKNOWN_709E_3, ["EVENT_1500_run_dialog_34"]),
	RunDialog(dialog_id=DI3955_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToObjectXY(MARIO),
		A_Walk1StepSoutheast(),
		A_SetSpriteSequence(index=13, sprite_offset=2, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToObjectXY(MARIO),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3956_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=8, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3957_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(80)
	]),
	Pause(60),
	RunDialog(dialog_id=DI3958_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=8, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3959_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=2, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3960_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3961_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI3962_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1500_run_dialog_34"),
	JmpIfDialogOptionBSelected(["EVENT_1500_set_action_script_92"]),
	SetSyncActionScript(MARIO, A0670_NOD_YES),
	Pause(60),
	RunDialog(dialog_id=DI3964_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK253_SMITHY_HENCHMEN_PACK_1, BF12_BOOSTER_TOWER),
	JmpIfBitClear(GAME_OVER, ["EVENT_1500_apply_solidity_mod_42"]),
	ResetAndChooseGame(),
	ApplySolidityModToLevel(permanent=False, room_id=R293_UNMAPPED_HOUSE_ROOM, mod_id=1, identifier="EVENT_1500_apply_solidity_mod_42"),
	RemoveObjectFromCurrentLevel(NPC_0),
	ActionQueueSync(target=NPC_1, subscript=[
		A_DecZCoord1Step()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_DecZCoord1Step(),
		A_DecZCoord1Step()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=4, y=24)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=4, y=25)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=3, y=23),
		A_FaceNortheast()
	]),
	JmpIfBitClear(UNKNOWN_709E_3, ["EVENT_1500_fade_in_from_black_async_52"]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_VisibilityOn(),
		A_ShiftToXYCoords(x=5, y=19),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOn(),
		A_ShiftToXYCoords(x=6, y=21),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_1500_fade_in_from_black_async_52"),
	Pause(40),
	RunDialog(dialog_id=DI3965_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_JumpToHeight(60)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3966_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3967_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3968_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO014_FLOWER, channel=6),
	AddToInventory(FearBombItem),
	RunDialog(dialog_id=DI3969_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3970_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, looping=True),
		A_Pause(12),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3971_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(height=60, silent=True)
	]),
	Pause(50),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3958_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=8, looping=True),
		A_Pause(42),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3972_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI0920_FOUND_A_COOKIE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(60)
	]),
	Pause(50),
	RunDialog(dialog_id=DI0923_SEE_YOU_AROUND, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Walk1StepSoutheast(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SetAllSpeeds(FASTER),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
		A_WalkNortheastSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(2),
		A_WalkNortheastSteps(2)
	]),
	SetBit(UNKNOWN_709E_4),
	EnterArea(room_id=R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT, face_direction=NORTHEAST, x=27, y=91, z=0, run_entrance_event=True),
	Return(),
	SetSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_1500_set_action_script_92"),
	Pause(60),
	RunDialog(dialog_id=DI3963_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(UNKNOWN_709E_3, ["EVENT_1500_action_queue_98"]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Walk1StepSoutheast(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=6, y=21),
		A_WalkToXYCoords(x=7, y=19)
	], identifier="EVENT_1500_action_queue_98"),
	ResumeActionScript(NPC_2),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, looping=True)
	]),
	SetBit(UNKNOWN_709E_3),
	Return()
])
