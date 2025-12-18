# E0629_EMPTY

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
	SetBit(TEMP_7042_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_ShiftZDownPixels(1)
	]),
	Pause(30),
	PauseActionScript(NPC_1),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_WalkToXYCoords(x=4, y=18),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI2058_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	PauseActionScript(NPC_2),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_WalkToXYCoords(x=3, y=19),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2059_EMPTY, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	FreezeCamera(),
	SetSyncActionScript(NPC_1, A0332_EMPTY),
	SetSyncActionScript(NPC_2, A0332_EMPTY),
	RunDialog(dialog_id=DI2060_EMPTY, above_object=NPC_1, closable=True, sync=True, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(64),
		A_WalkSoutheastPixels(8),
		A_FloatingOn(),
		A_WalkSoutheastPixels(8),
		A_Walk1StepSoutheast(),
		A_Pause(1, identifier="EVENT_629_action_queue_16_SUBSCRIPT_pause_7"),
		A_JmpIfMarioInAir(["EVENT_629_action_queue_16_SUBSCRIPT_pause_7"]),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_JumpToHeight(height=64, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSoutheast(),
		A_Pause(1, identifier="EVENT_629_action_queue_16_SUBSCRIPT_pause_13"),
		A_JmpIfMarioInAir(["EVENT_629_action_queue_16_SUBSCRIPT_pause_13"]),
		A_FaceNorthwest(),
		A_Pause(60),
		A_ResetProperties(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	RememberLastObject(),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Walk1StepSoutheast(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	SetSyncActionScript(NPC_1, A0330_MARRYMORE_HEAD_CHEF),
	SetSyncActionScript(NPC_2, A0331_MARRYMORE_2ND_CHEF),
	CloseDialog(),
	RememberLastObject(),
	UnfreezeCamera(),
	Return()
])
