# E3000_CLONE_RESERVED

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
	RemoveObjectFromCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6])
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastSteps(2)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2)
	]),
	JmpIfBitSet(UNKNOWN_709D_7, ["EVENT_3000_action_queue_7"]),
	RunDialog(dialog_id=DI3763_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True),
		A_Walk1StepSouth()
	], identifier="EVENT_3000_action_queue_7"),
	SetBit(UNKNOWN_709D_7),
	RunDialog(dialog_id=DI3771_NIMBUS_INNKEEPER_AFTER_DREAM_CUSHION, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3000_set_action_script_35"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1174_CANT_WAIT_TO_GET_OLDER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	CharacterLeavesParty(TOADSTOOL),
	CharacterLeavesParty(BOWSER),
	CharacterLeavesParty(GENO),
	CharacterLeavesParty(MALLOW),
	StartBattleAtBattlefield(PACK249_AXEM_PINK_ALONE, BF04_SUNKEN_SHIP),
	JmpIfBitClear(GAME_OVER, ["EVENT_3000_action_queue_20"]),
	ResetAndChooseGame(),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=25, y=117),
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	], identifier="EVENT_3000_action_queue_20"),
	FadeInFromBlack(sync=False),
	CharacterJoinsParty(TOADSTOOL),
	CharacterJoinsParty(BOWSER),
	CharacterJoinsParty(GENO),
	CharacterJoinsParty(MALLOW),
	RunDialog(dialog_id=DI1338_40_POINTS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2767_FROGFUCIUS_SEA_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO014_FLOWER, channel=6),
	AddToInventory(MuteBombItem),
	RunDialog(dialog_id=DI2820_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_SetSpriteSequence(index=1, looping=True),
		A_WalkToXYCoords(x=24, y=110),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI2829_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_709D_4),
	Return(),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_3000_set_action_script_35"),
	Pause(20),
	RunDialog(dialog_id=DI3789_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	EnterArea(room_id=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, face_direction=SOUTHWEST, x=16, y=117, z=2),
	JmpToEvent(E3281_SHIP_UPPER_HENCHMAN_ROOM_LOADER),
	Return()
])
