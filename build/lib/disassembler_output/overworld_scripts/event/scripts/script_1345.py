# E1345_EMPTY

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
	JmpIfBitSet(TOWER_LOBBY_MOVEMENT, ["EVENT_1345_ret_32"]),
	FadeOutMusicToVolume(duration=0, volume=0),
	Pause(30),
	PlaySound(sound=SO076_BOOSTERS_TRAIN_HORN, channel=6),
	Pause(60),
	RunDialog(dialog_id=DI2568_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthSteps(2)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=3, y=113),
		A_FaceNorth()
	]),
	PlaySound(sound=SO074_BOOSTERS_TRAIN, channel=6),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShadowOn(),
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=1, y=104, z=8, direction=EAST),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(5),
		A_WalkSouthwestPixels(3),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetSpriteSequence(index=15, is_sequence=True, looping=True, mirror_sprite=True),
		A_SequencePlaybackOff(),
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShadowOn(),
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=1, y=104, z=8, direction=EAST),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetPriority(3),
		A_WalkNorthwestSteps(1),
		A_WalkSouthwestPixels(6),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(7),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkSoutheastSteps(1)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(7),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkSoutheastSteps(1)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSoutheastSteps(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastSteps(1)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSoutheastSteps(1),
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(SLOW),
		A_WalkSoutheastPixels(8),
		A_SetSequenceSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(8),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Pause(80),
	RunDialog(dialog_id=DI2569_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	UnsyncDialog(),
	CloseDialog(),
	PlayMusicAtDefaultVolume(M0032_ANDMYNAME_SBOOSTER),
	SetSyncActionScript(NPC_0, A0525_SPINNING_CARD),
	SetSyncActionScript(NPC_1, A0526_EMPTY),
	UnfreezeCamera(),
	SetBit(TOWER_LOBBY_MOVEMENT),
	Return(identifier="EVENT_1345_ret_32")
])
