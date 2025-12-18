# E3003_CLONE_RESERVED

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
	JmpIfBitSet(UNKNOWN_709E_1, ["EVENT_3003_ret_70"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=6, y=20),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(2)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=5, looping=False),
		A_Pause(32),
		A_SetSpriteSequence(index=0, looping=True)
	]),
	RunDialog(dialog_id=DI3937_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToObjectXYZ(MARIO),
		A_Walk1StepNorthwest(),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToObjectXY(MARIO),
		A_Walk1StepSoutheast(),
		A_FaceNortheast(),
		A_Pause(10),
		A_PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
		A_SetSpriteSequence(index=3, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3938_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3939_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3940_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3941_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, looping=False),
		A_Pause(12),
		A_SetSpriteSequence(index=5, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3942_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=True)
	]),
	RunDialog(dialog_id=DI3943_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK252_DINGALING_ALONE, BF05_MOLEVILLE_MINES),
	JmpIfBitClear(GAME_OVER, ["EVENT_3003_fade_in_from_black_async_24"]),
	ResetAndChooseGame(),
	FadeInFromBlack(sync=False, identifier="EVENT_3003_fade_in_from_black_async_24"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, looping=False),
		A_Pause(12),
		A_SetSpriteSequence(index=5, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3944_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=13, is_mold=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO057_FINGER_SNAP, channel=6),
		A_Pause(15),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(12),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=0, looping=True),
		A_ShiftToXYCoords(x=7, y=20),
		A_Walk1StepNortheast(),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=0, looping=True)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3945_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, looping=True, mirror_sprite=True),
		A_Pause(33),
		A_SetSpriteSequence(index=13, is_mold=True, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO072_SYRUP_CURE, channel=6),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=4, looping=False)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=True)
	]),
	RunDialog(dialog_id=DI3946_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RunDialog(dialog_id=DI3947_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(DoomBombItem),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=12, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=2, looping=True),
		A_Pause(90),
		A_Walk1StepSouthwest()
	]),
	RemoveObjectFromCurrentLevel(NPC_3),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(50),
		A_SetSpriteSequence(index=0, sprite_offset=4, is_mold=True, looping=True, mirror_sprite=True)
	]),
	PlaySound(sound=SO104_DEEP_SCRAPING, channel=6),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToObjectXY(NPC_1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3948_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(12),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(12),
		A_SetSpriteSequence(index=14, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(12),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3949_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StopSound(),
	RemoveObjectFromCurrentLevel(NPC_4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3950_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, looping=False),
		A_Pause(16)
	]),
	RunDialog(dialog_id=DI3951_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=4, looping=False),
		A_Pause(54),
		A_VisibilityOff(),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6)
	]),
	Pause(30),
	RunDialog(dialog_id=DI3952_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=1, looping=False),
		A_Pause(64),
		A_SetSpriteSequence(index=27, sprite_offset=1, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI3953_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Walk1StepSoutheast(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth()
	]),
	SetBit(UNKNOWN_709E_1),
	Return(identifier="EVENT_3003_ret_70")
])
