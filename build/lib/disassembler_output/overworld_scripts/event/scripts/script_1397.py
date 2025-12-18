# E1397_EMPTY

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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequenceLoopingOff()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2763_FROGFUCIUS_BOOSTER_PASS_HINT, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	SetSyncActionScript(NPC_0, A0146_EMPTY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=3, y=18, height=0),
		A_FaceSoutheast(),
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(80),
		A_WalkSoutheastSteps(1),
		A_WalkSoutheastPixels(4),
		A_Pause(10),
		A_FaceNortheast(),
		A_Pause(15),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(VERY_FAST),
		A_FloatingOff(),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(5),
		A_Pause(10),
		A_SetSpriteSequence(index=23, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_SetSpriteSequence(index=24, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(20),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_JumpToHeight(96),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOn(),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(NORMAL),
		A_Pause(30),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(70),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL)
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_JumpToHeight(80),
		A_Pause(15),
		A_SequenceLoopingOff()
	]),
	RunDialog(dialog_id=DI2764_FROGFUCIUS_STAR_HILL_HINT, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SequencePlaybackOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(2),
		A_WalkSouthwestSteps(3),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=4),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_0),
	SetBit(CHAPEL_ITEM_2_RETRIEVED),
	Return()
])
