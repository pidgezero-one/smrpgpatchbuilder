# E0634_EMPTY

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
	JmpIfBitSet(UNUSED_705D_0, ["EVENT_634_action_queue_93"]),
	JmpIfBitSet(TEMP_7042_1, ["EVENT_634_action_queue_14"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R152_MARRYMORE_CHAPEL_MAIN_HALL, ["EVENT_634_jmp_if_bit_set_5"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferXYZFPixels(x=254, y=1, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferXYZFPixels(x=254, y=1, z=0, direction=EAST)
	]),
	JmpIfBitSet(MARRYMORE_UNKNOWN_7063_2, ["EVENT_634_jmp_if_object_not_in_level_9"], identifier="EVENT_634_jmp_if_bit_set_5"),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_10, R152_MARRYMORE_CHAPEL_MAIN_HALL, ["EVENT_257_fade_in_from_black_async_0"], identifier="EVENT_634_jmp_if_object_not_in_level_9"),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=4, y=32, z=4, direction=EAST),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_10, A0333_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH),
	FadeInFromBlack(sync=False),
	Return(),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=5, y=31, z=4, direction=EAST)
	], identifier="EVENT_634_action_queue_14"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=6, y=32, z=4, direction=EAST)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=4, y=34, z=4, direction=EAST)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=3, y=33, z=4, direction=EAST)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=7, y=34, z=4, direction=EAST)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=6, y=35, z=4, direction=EAST)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=8, y=31, z=4, direction=EAST)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_TransferToXYZF(x=7, y=35, z=4, direction=EAST)
	]),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI2166_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouth()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2167_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(10),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2168_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(SLOW)
	]),
	RunDialog(dialog_id=DI2169_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2170_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	SetSyncActionScript(NPC_3, A0625_EMPTY),
	Pause(10),
	RunDialog(dialog_id=DI2173_EMPTY, above_object=NPC_2, closable=False, sync=False, multiline=True, use_background=True),
	Pause(30),
	PauseActionScript(NPC_8),
	SetSyncActionScript(NPC_6, A0627_EMPTY),
	SetSyncActionScript(NPC_7, A0627_EMPTY),
	SetSyncActionScript(NPC_8, A0627_EMPTY),
	SetSyncActionScript(NPC_9, A0627_EMPTY),
	Pause(10),
	RunDialog(dialog_id=DI2174_EMPTY, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Walk1StepNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, mod_id=1),
	Pause(30),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(4),
		A_VisibilityOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(4),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(5),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkNorthwestSteps(4),
		A_Pause(16),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_Pause(64),
		A_WalkNortheastSteps(7),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(90),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_8, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=8, y=32),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_WalkNorthwestSteps(2),
		A_Pause(100),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_WalkNortheastSteps(4),
		A_WalkNortheastPixels(8),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromSpecificLevel(NPC_2, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_3, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_4, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_5, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_6, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	RemoveObjectFromSpecificLevel(NPC_7, R152_MARRYMORE_CHAPEL_MAIN_HALL),
	SetBit(UNUSED_705D_0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouth()
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R064_MARRYMORE_OUTSIDE, mod_id=0),
	Return(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=8, y=35, z=4, direction=EAST)
	], identifier="EVENT_634_action_queue_93"),
	ActionQueueSync(target=NPC_9, subscript=[
		A_TransferToXYZF(x=9, y=36, z=4, direction=EAST),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
	FadeInFromBlack(sync=False),
	Return()
])
