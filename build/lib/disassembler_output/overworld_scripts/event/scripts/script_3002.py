# E3002_CLONE_RESERVED

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
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=7, y=37),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToObjectXY(MARIO),
		A_Walk1StepSoutheast(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToObjectXY(MARIO),
		A_Walk1StepNorthwest(),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3922_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=19, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=11, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3923_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=0, looping=True)
	]),
	Pause(25),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=2, is_mold=True, looping=True)
	]),
	Pause(60),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3924_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, looping=True, mirror_sprite=True)
	]),
	SetSyncActionScript(NPC_1, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3925_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=4, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	RunDialog(dialog_id=DI3926_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(20),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3927_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=5, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3928_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK250_AXEM_YELLOW_ALONE, BF42_BELOME_TEMPLE),
	JmpIfBitClear(GAME_OVER, ["EVENT_3002_set_7010_to_object_xyz_39"]),
	ResetAndChooseGame(),
	Set70107015ToObjectXYZ(target=NPC_4, identifier="EVENT_3002_set_7010_to_object_xyz_39"),
	CreatePacketAt7010(packet=P005_BRIEF_POOF_BAG, destinations=["EVENT_3002_remove_from_current_level_41"]),
	RemoveObjectFromCurrentLevel(NPC_4, identifier="EVENT_3002_remove_from_current_level_41"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI3929_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=8, y=35),
		A_Pause(15),
		A_SetSpriteSequence(index=9, sprite_offset=2, looping=True)
	]),
	RunDialog(dialog_id=DI3930_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3931_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3932_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=15, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3933_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_SetSpriteSequence(index=2, sprite_offset=2, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	AddToInventory(DebugBombItem),
	RunDialog(dialog_id=DI3934_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3935_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=7, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=15, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(25),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=0, looping=True),
		A_WalkToXYCoords(x=7, y=37),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Walk1StepSoutheast(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, is_mold=True, looping=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ResetProperties()
	]),
	SetBit(UNKNOWN_709E_0),
	Return()
])
