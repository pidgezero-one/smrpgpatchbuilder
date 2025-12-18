# E0410_BED_SHYSTER

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
	SetBit(TEMP_704A_2),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	StartBattleAtBattlefield(PACK011_REGULAR_SHYSTERS_BIASED_3, BF11_MUSHROOM_KINGDOM_HOUSE),
	RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_410_fade_in_from_black_async_35"]),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_TransferToXYZF(x=7, y=44, z=6, direction=EAST),
		A_FaceNorthwest()
	]),
	FadeInFromBlack(sync=False),
	PauseActionScript(NPC_2),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(2)
	]),
	RunDialog(dialog_id=DI0706_EMPTY, above_object=NPC_2, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI0730_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	PlaySound(sound=SO085_FLOWER, channel=6),
	SetVarToConst(ITEM_ID, FlowerTabItem),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(FlowerTabItem),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSouthwestSteps(2),
		A_WalkSoutheastSteps(2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	PauseActionScript(NPC_0),
	SetVarToConst(TEMP_70A9, 20),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	RunDialog(dialog_id=DI0707_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
	RunDialog(dialog_id=DI0545_YEAH, above_object=NPC_0, closable=True, sync=True, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(5),
		A_WalkSouthwestSteps(5),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_VisibilityOff()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_410_fade_in_from_black_async_35"),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
