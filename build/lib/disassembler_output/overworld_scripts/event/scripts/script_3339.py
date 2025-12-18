# E3339_VOLCANO_2ND_BOSS_PATH_ROOM_LOADER

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
	JmpIfBitSet(JOHNNY_POSITION, ["EVENT_3339_run_event_as_subroutine_42"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(1)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(4)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_Walk1StepSouthwest(),
		A_SetVarToConst(TEMP_70AF, 7),
		A_CreatePacketAtObjectCoords(packet=P041_UNUSED, target_npc=NPC_6, destinations=["EVENT_3339_action_queue_5_SUBSCRIPT_pause_4"]),
		A_Pause(1, identifier="EVENT_3339_action_queue_5_SUBSCRIPT_pause_4"),
		A_VisibilityOff(),
		A_Pause(45),
		A_ClearBit(TEMP_7044_6),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_SetBit(TEMP_7044_7)
	]),
	RunDialog(dialog_id=DI1814_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_5, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_Walk1StepSouthwest(),
		A_Pause(1, identifier="EVENT_3339_action_queue_7_SUBSCRIPT_pause_2"),
		A_JmpIfBitClear(TEMP_7044_7, ["EVENT_3339_action_queue_7_SUBSCRIPT_pause_2"]),
		A_ClearBit(TEMP_7044_7),
		A_SetVarToConst(TEMP_70AF, 7),
		A_CreatePacketAtObjectCoords(packet=P042_UNUSED, target_npc=NPC_5, destinations=["EVENT_3339_action_queue_7_SUBSCRIPT_pause_7"]),
		A_Pause(1, identifier="EVENT_3339_action_queue_7_SUBSCRIPT_pause_7"),
		A_VisibilityOff(),
		A_Pause(45),
		A_ClearBit(TEMP_7044_6),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_SetBit(TEMP_7044_7)
	]),
	RunDialog(dialog_id=DI1815_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_Walk1StepSoutheast(),
		A_Pause(1, identifier="EVENT_3339_action_queue_10_SUBSCRIPT_pause_2"),
		A_JmpIfBitClear(TEMP_7044_7, ["EVENT_3339_action_queue_10_SUBSCRIPT_pause_2"]),
		A_ClearBit(TEMP_7044_7),
		A_SetVarToConst(TEMP_70AF, 135),
		A_CreatePacketAtObjectCoords(packet=P043_UNUSED, target_npc=NPC_4, destinations=["EVENT_3339_action_queue_10_SUBSCRIPT_pause_7"]),
		A_Pause(1, identifier="EVENT_3339_action_queue_10_SUBSCRIPT_pause_7"),
		A_VisibilityOff(),
		A_Pause(45),
		A_ClearBit(TEMP_7044_6),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff(),
		A_SetBit(TEMP_7044_7)
	]),
	RunDialog(dialog_id=DI1816_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_3, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_Walk1StepSoutheast(),
		A_FaceSouthwest(),
		A_Pause(1, identifier="EVENT_3339_action_queue_12_SUBSCRIPT_pause_3"),
		A_JmpIfBitClear(TEMP_7044_7, ["EVENT_3339_action_queue_12_SUBSCRIPT_pause_3"]),
		A_ClearBit(TEMP_7044_7),
		A_SetVarToConst(TEMP_70AF, 7),
		A_CreatePacketAtObjectCoords(packet=P044_UNUSED, target_npc=NPC_3, destinations=["EVENT_3339_action_queue_12_SUBSCRIPT_pause_8"]),
		A_Pause(1, identifier="EVENT_3339_action_queue_12_SUBSCRIPT_pause_8"),
		A_VisibilityOff(),
		A_Pause(45),
		A_ClearBit(TEMP_7044_6),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_Pause(1),
		A_FixedFCoordOn(),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(1),
		A_SetBit(TEMP_7044_7)
	]),
	RunDialog(dialog_id=DI1817_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_2, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_FaceSouthwest(),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(8),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(8),
		A_Pause(1, identifier="EVENT_3339_action_queue_14_SUBSCRIPT_pause_6"),
		A_JmpIfBitClear(TEMP_7044_7, ["EVENT_3339_action_queue_14_SUBSCRIPT_pause_6"]),
		A_ClearBit(TEMP_7044_7),
		A_SetVarToConst(TEMP_70AF, 7),
		A_CreatePacketAtObjectCoords(packet=P040_UNUSED, target_npc=NPC_2, destinations=["EVENT_3339_action_queue_14_SUBSCRIPT_pause_11"]),
		A_Pause(1, identifier="EVENT_3339_action_queue_14_SUBSCRIPT_pause_11"),
		A_VisibilityOff(),
		A_Pause(45),
		A_ClearBit(TEMP_7044_6),
		A_VisibilityOn(),
		A_SetBit(TEMP_7044_7),
		A_SetBit(TEMP_7043_4)
	]),
	RunDialog(dialog_id=DI1818_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1, identifier="EVENT_3339_pause_16"),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_3339_pause_16"]),
	Pause(20),
	ClearBit(TEMP_7044_0),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Walk1StepNorthwest()
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_2, destinations=["EVENT_3339_create_packet_at_npc_coords_24"]),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_1, destinations=["EVENT_3339_pause_25"], identifier="EVENT_3339_create_packet_at_npc_coords_24"),
	Pause(8, identifier="EVENT_3339_pause_25"),
	RemoveObjectFromCurrentLevel(NPC_6),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_6, destinations=["EVENT_3339_pause_28"]),
	Pause(8, identifier="EVENT_3339_pause_28"),
	RemoveObjectFromCurrentLevel(NPC_4),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_4, destinations=["EVENT_3339_pause_31"]),
	Pause(8, identifier="EVENT_3339_pause_31"),
	RemoveObjectFromCurrentLevel(NPC_5),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_5, destinations=["EVENT_3339_pause_34"]),
	Pause(8, identifier="EVENT_3339_pause_34"),
	RemoveObjectFromCurrentLevel(NPC_3),
	CreatePacketAtObjectCoords(packet=P045_TELEPORTATION_SHINE, target_npc=NPC_3, destinations=["EVENT_3339_pause_37"]),
	Pause(8, identifier="EVENT_3339_pause_37"),
	SetBit(JOHNNY_POSITION),
	Pause(20),
	PlayMusicAtDefaultVolume(M0063_AXEMRANGERSDROPIN),
	Return(),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3339_run_event_as_subroutine_42"),
	Return()
])
