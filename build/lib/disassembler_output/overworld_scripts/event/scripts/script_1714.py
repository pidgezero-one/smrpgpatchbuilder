# E1714_BANDITS_WAY_1_LOADER

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
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkWestPixels(4)
	]),
	JmpIfBitClear(BANDITS_WAY_CUTSCENE_1_VIEWED, ["EVENT_1714_set_bit_3"]),
	JmpToEvent(E0014_STANDARD_ROOM_LOADER),
	SetBit(BANDITS_WAY_CUTSCENE_1_VIEWED, identifier="EVENT_1714_set_bit_3"),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(135),
		A_ResetProperties()
	]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_6),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepSouthwest(),
		A_Walk1StepSoutheast(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_SetSequenceSpeed(FAST),
		A_ResetProperties(),
		A_Pause(20),
		A_JumpToHeight(height=64, silent=True),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(8),
		A_Walk1StepNortheast(),
		A_FaceNorthwest(),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI1064_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Walk1StepSouthwest(),
		A_FaceSoutheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceNorthwest(),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI1056_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3),
		A_SetAllSpeeds(FAST),
		A_Walk1StepSouthwest(),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_WalkSouthSteps(4),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(108),
		A_WalkSoutheastSteps(6),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetAllSpeeds(FASTER),
		A_WalkEastSteps(6),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthSteps(4),
		A_SetAllSpeeds(FASTER),
		A_WalkSoutheastSteps(6),
		A_Pause(30),
		A_WalkNorthwestSteps(6),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Walk1StepNorthwest(),
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	Return()
])
