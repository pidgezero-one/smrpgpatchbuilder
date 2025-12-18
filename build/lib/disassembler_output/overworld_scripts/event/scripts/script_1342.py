# E1342_ELDER_KEY_PRIZE_GRANTER

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
	PauseActionScript(NPC_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO160_CHOMP, channel=6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FASTER),
		A_JumpToHeight(128),
		A_BounceToXYWithHeight(x=25, y=123, height=4),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(80),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=26, y=124, z=4, direction=EAST),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthwestSteps(1)
	]),
	Pause(30),
	StopSound(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True, mirror_sprite=True)
	]),
	Pause(100),
	RunDialog(dialog_id=DI2768_FROGFUCIUS_BEANSTALK_HINT, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Pause(15),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthwestSteps(1),
		A_JumpToHeight(144),
		A_BounceToXYWithHeight(x=23, y=119, height=8),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(120),
	FreezeCamera(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2769_FROGFUCIUS_SUPER_JUMP_HINT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(1),
		A_FaceEast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkEastSteps(4),
		A_Pause(20)
	]),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromSpecificLevel(NPC_0, R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=23, y=120, z=10, direction=EAST),
		A_WalkSouthwestPixels(18),
		A_WalkSoutheastPixels(2)
	]),
	RunDialog(dialog_id=DI2816_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkWestSteps(4)
	]),
	RunDialog(dialog_id=DI2817_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PlaySound(sound=SO104_DEEP_SCRAPING, channel=6),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	CloseDialog(),
	Pause(30),
	StopSound(),
	RemoveObjectFromCurrentLevel(NPC_2),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_JumpToHeight(128),
		A_WalkSoutheastSteps(3),
		A_Pause(15),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	SetVarToConst(ITEM_ID, ChompItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2754),
	RunEventAsSubroutine(E3829_EMPTY),
	UnfreezeCamera(),
	Return()
])
