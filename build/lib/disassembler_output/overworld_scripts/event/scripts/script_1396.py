# E1396_EMPTY

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
	JmpIfBitSet(CHAPEL_ITEM_3_RETRIEVED, ["EVENT_1396_open_location_15"]),
	JmpIfBitSet(CHAPEL_ITEM_2_RETRIEVED, ["EVENT_1396_action_queue_17"]),
	JmpIfBitClear(UNKNOWN_7053_0, ["EVENT_1396_open_location_15"]),
	JmpIfBitSet(MONSTRO_SAVE_HOLE, ["EVENT_1396_open_location_15"]),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_JumpToHeight(96)
	]),
	RunDialog(dialog_id=DI2757_FROGFUCIUS_CASINO_HINT, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkToXYCoords(x=6, y=32),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkToXYCoords(x=7, y=38),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(1),
		A_SetAllSpeeds(NORMAL),
		A_WalkNorthwestSteps(1)
	]),
	RunDialog(dialog_id=DI2758_FROGFUCIUS_DEFAULT_STUFF, above_object=NPC_1, closable=True, sync=False, multiline=True, use_background=True),
	ResetCoords(NPC_1),
	Pause(1),
	SetSyncActionScript(NPC_1, A0146_EMPTY),
	SetBit(MONSTRO_SAVE_HOLE),
	Return(),
	ExitToWorldMap(area=OW08_MARIOS_PAD, bit_6=True, bit_7=True, identifier="EVENT_1396_open_location_15"),
	Return(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6),
		A_JumpToHeight(height=96, silent=True),
		A_WalkNorthwestSteps(4),
		A_FixedFCoordOff(),
		A_Pause(20),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=6),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_StopSound(),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	], identifier="EVENT_1396_action_queue_17"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequenceLoopingOff(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_Pause(15),
		A_ShiftToXYCoords(x=11, y=50),
		A_WalkSouthwestPixels(8),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_WalkNorthwestSteps(3),
		A_Pause(60),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(10)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(FAST),
		A_WalkWestPixels(5),
		A_WalkEastPixels(5),
		A_WalkWestPixels(5),
		A_WalkEastPixels(5)
	]),
	Pause(15),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Dec7000FromCurrentHP(MARIO),
	RunDialog(dialog_id=DI2765_FROGFUCIUS_MARRYMORE_HOTEL_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, MushroomItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2752),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	Pause(15),
	RunDialog(dialog_id=DI2766_FROGFUCIUS_FROG_DISCIPLE_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1396_run_dialog_43"]),
	RunDialog(dialog_id=DI2750_FROGFUCIUS_MARRYMORE_HINT, above_object=NPC_1, closable=False, sync=True, multiline=True, use_background=True),
	UnsyncDialog(),
	Set7000ToTappedButton(identifier="EVENT_1396_set_7000_to_tapped_button_32"),
	Pause(1),
	Mem7000AndConst(0x0010),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_1396_close_dialog_37"]),
	Jmp(["EVENT_1396_set_7000_to_tapped_button_32"]),
	CloseDialog(identifier="EVENT_1396_close_dialog_37"),
	RunMenuTutorial(TU01_HOW_TO_USE_ITEMS),
	FadeInFromBlack(sync=False),
	Pause(30),
	RunDialog(dialog_id=DI2942_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_1396_pause_44"]),
	RunDialog(dialog_id=DI2941_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1396_run_dialog_43"),
	Pause(40, identifier="EVENT_1396_pause_44"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	Pause(50),
	RunDialog(dialog_id=DI2943_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=11, y=50),
		A_WalkSouthwestPixels(8),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestPixels(27),
		A_Pause(30),
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
		A_JumpToHeight(48),
		A_Pause(15),
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
		A_JumpToHeight(48),
		A_Pause(15)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(25),
		A_JumpToHeight(96),
		A_Pause(20),
		A_FaceNorthwest(),
		A_Pause(10)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(40),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FASTER),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastPixels(18)
	]),
	RunDialog(dialog_id=DI2944_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2945_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_1396_pause_64"]),
	JmpIfDialogOptionBSelected(["EVENT_1396_pause_64"]),
	Pause(15),
	StartBattleAtBattlefield(PACK205_BLUEBIRD_HENCHMEN, BF09_GRASSLANDS),
	RemoveObjectFromCurrentLevel(NPC_3),
	FadeInFromBlack(sync=False),
	Pause(20),
	RunDialog(dialog_id=DI2947_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	Jmp(["EVENT_1396_action_queue_73"]),
	Pause(20, identifier="EVENT_1396_pause_64"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(20),
		A_JumpToHeight(80)
	]),
	RunDialog(dialog_id=DI2946_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_FixedFCoordOff(),
		A_WalkSoutheastPixels(10),
		A_VisibilityOff()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2949_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(45),
		A_FaceSouthwest()
	], identifier="EVENT_1396_action_queue_73"),
	Pause(50),
	RunDialog(dialog_id=DI2943_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(15),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(80)
	]),
	RunDialog(dialog_id=DI2948_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, MushroomItem),
	SetVarToConst(PRIMARY_TEMP_7000, 2753),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	AddToInventory(MushroomItem),
	AddToInventory(MushroomItem),
	Pause(15),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_Pause(20),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	SetBit(CHAPEL_ITEM_3_RETRIEVED),
	SetBit(MAP_MUSHROOM_KINGDOM),
	SetBit(MAP_MUSHROOM_WAY),
	SetBit(MAP_DIRECTIONAL_MARIOS_PAD_MUSHROOM_WAY),
	Return()
])
