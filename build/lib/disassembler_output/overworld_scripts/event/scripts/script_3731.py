# E3731_EMPTY

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
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(UNKNOWN_STATUE_ROOM_7090_1, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_6, ["EVENT_3584_ret_0"]),
	RunDialog(dialog_id=DI3643_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_3731_action_queue_5_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_3731_action_queue_5_SUBSCRIPT_pause_3"]),
		A_Pause(30),
		A_ResetProperties(),
		A_WalkToXYCoords(x=30, y=20),
		A_FaceNorthwest(),
		A_Pause(10)
	]),
	SetBit(UNKNOWN_704A_3),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(2),
		A_JumpToHeight(96),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3731_action_queue_8_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_3731_action_queue_8_SUBSCRIPT_pause_6"]),
		A_FaceNorthwest()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_4, subscript=[
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNortheastSteps(4),
		A_FaceSoutheast(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNortheastSteps(4),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3644_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI3645_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3646_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3642_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(120),
		A_SetWalkingSpeed(FASTEST),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_WalkNortheastPixels(1),
		A_StartLoopNTimes(19),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_EndLoop(),
		A_WalkSouthwestPixels(1),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO105_SURPRISE, channel=4),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_JumpToHeight(height=256, silent=True),
		A_Pause(60),
		A_FloatingOff(),
		A_TransferToXYZF(x=28, y=19, z=0, direction=SOUTHEAST)
	]),
	PaletteSet(palette_set=84, row=1, bit_3=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_3731_action_queue_33_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_3731_action_queue_33_SUBSCRIPT_pause_2"]),
		A_StopSound(),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_Pause(30),
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(24),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(24),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3668_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI3669_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3670_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff()
	]),
	RunDialog(dialog_id=DI3671_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkNorthwestSteps(7),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(6),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(UNKNOWN_STATUE_ROOM_7090_1),
	Return()
])
