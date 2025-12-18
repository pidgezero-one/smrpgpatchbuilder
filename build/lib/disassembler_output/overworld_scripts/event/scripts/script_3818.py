# E3818_WORLD_MAP_MUSHROOM_WAY

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
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_3584_ret_0"]),
	SetBit(TEMP_7043_0),
	JmpToSubroutine(["EVENT_3818_disable_trigger_21"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(6),
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	Pause(1, identifier="EVENT_3818_pause_4"),
	JmpIfMarioInAir(["EVENT_3818_pause_4"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=2, y=91),
		A_FaceNortheast()
	]),
	PauseActionScript(NPC_3),
	StartAsyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=3, y=90),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	RunDialog(dialog_id=DI3755_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_PlaySound(sound=SO013_COIN, channel=4),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_ShiftZUpSteps(2),
		A_TransferToXYZF(x=13, y=91, z=0, direction=EAST)
	]),
	JmpToSubroutine(["EVENT_3818_action_queue_34"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSoutheastSteps(3),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownSteps(2)
	]),
	SetSyncActionScript(NPC_3, A0978_RANDOMLY_FACE_SOUTHWEST),
	AddCoins(10),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Jmp(["EVENT_3818_clear_bit_38"]),
	DisableObjectTrigger(MEM_70A8, identifier="EVENT_3818_disable_trigger_21"),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpSteps(2)
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_PlaySound(sound=SO014_FLOWER, channel=4),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x03\x80\xff')),
		A_Pause(8),
		A_BPL262728(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Set7016701BToObjectXYZ(target=MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_2, to_var=PRIMARY_TEMP_7000),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3818_add_const_to_var_31"]),
	AddConstToVar(PRIMARY_TEMP_7000, 128),
	AddConstToVar(PRIMARY_TEMP_7000, 160, identifier="EVENT_3818_add_const_to_var_31"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_2),
	Return(),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%@\x00\x80\xff')),
		A_Pause(8),
		A_BPL262728(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_SequenceLoopingOff(),
		A_Pause(1),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	], identifier="EVENT_3818_action_queue_34"),
	PauseActionScript(MEM_70A8),
	UnfreezeCamera(),
	Return(),
	ClearBit(TEMP_7043_0, identifier="EVENT_3818_clear_bit_38"),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_1, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_3584_ret_0"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_0, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_3584_ret_0"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_2, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_3584_ret_0"]),
	SetBit(BATTLE_DOOR_BOSS_BIT),
	SetBit(TEMP_7042_7),
	Return()
])
