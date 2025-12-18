# E3778_BALL_SOLITAIRE_SET_PUZZLE

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
	JmpIfBitClear(VOLCANO_LIBERATED, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(UNKNOWN_7099_1, ["EVENT_3584_ret_0"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=2, y=39)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=4, y=57),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=57, z=2, direction=EAST),
		A_TransferXYZFPixels(x=4, y=2, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(14),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3791_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3792_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3793_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Walk1StepSouthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI3794_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3795_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Walk1StepSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3854_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3855_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI3856_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3857_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(NPC_4, A0382_EMPTY),
	Pause(10),
	RunDialog(dialog_id=DI3858_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI3859_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI3860_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW)
	]),
	RunDialog(dialog_id=DI3861_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNortheast()
	]),
	RunDialog(dialog_id=DI3862_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3863_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3864_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=False),
		A_Pause(38),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3865_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Walk1StepNortheast(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3866_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RememberLastObject(),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(14),
		A_TransferToXYZF(x=6, y=83, z=0, direction=EAST)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(UNKNOWN_7099_1),
	Return()
])
