# E3074_COIN_CHEST_MULTI_HIT_1

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
	DisableObjectTrigger(MEM_70A8),
	JmpIfVarEqualsConst(ITEM_ID, DUMMYItem66, ["EVENT_3074_play_sound_3"]),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_3074_play_sound_3"),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	Mem7000AndConst(0x0003),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
	AddConstToVar(PRIMARY_TEMP_7000, 288),
	JmpIfMem704XAt7000BitSet(["EVENT_3074_jmp_if_var_equals_const_23"]),
	SetMem704XAt7000Bit(),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000F),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 1, ["EVENT_3074_copy_var_to_var_18"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 2, ["EVENT_3074_copy_var_to_var_20"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 3, ["EVENT_3074_copy_var_to_var_22"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_COUNTER_1),
	Jmp(["EVENT_3074_jmp_if_var_equals_const_23"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_COUNTER_2, identifier="EVENT_3074_copy_var_to_var_18"),
	Jmp(["EVENT_3074_jmp_if_var_equals_const_23"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_COUNTER_3, identifier="EVENT_3074_copy_var_to_var_20"),
	Jmp(["EVENT_3074_jmp_if_var_equals_const_23"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_COUNTER_4, identifier="EVENT_3074_copy_var_to_var_22"),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 1, ["EVENT_3074_jmp_if_var_not_equals_const_28"], identifier="EVENT_3074_jmp_if_var_equals_const_23"),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 2, ["EVENT_3074_jmp_if_var_not_equals_const_30"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 3, ["EVENT_3074_jmp_if_var_not_equals_const_32"]),
	JmpIfVarNotEqualsConst(COIN_COUNTER_1, 1, ["EVENT_3074_set_temp_action_script_35"]),
	Jmp(["EVENT_3074_set_action_script_33"]),
	JmpIfVarNotEqualsConst(COIN_COUNTER_2, 1, ["EVENT_3074_set_temp_action_script_35"], identifier="EVENT_3074_jmp_if_var_not_equals_const_28"),
	Jmp(["EVENT_3074_set_action_script_33"]),
	JmpIfVarNotEqualsConst(COIN_COUNTER_3, 1, ["EVENT_3074_set_temp_action_script_35"], identifier="EVENT_3074_jmp_if_var_not_equals_const_30"),
	Jmp(["EVENT_3074_set_action_script_33"]),
	JmpIfVarNotEqualsConst(COIN_COUNTER_4, 1, ["EVENT_3074_set_temp_action_script_35"], identifier="EVENT_3074_jmp_if_var_not_equals_const_32"),
	SetSyncActionScript(MEM_70AA, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED, identifier="EVENT_3074_set_action_script_33"),
	Jmp(["EVENT_3074_set_7010_to_object_xyz_36"]),
	SetTempSyncActionScript(MEM_70AA, A0008_HIT_TREASURE_CHEST_CONTENTS_REMAINING, identifier="EVENT_3074_set_temp_action_script_35"),
	Set70107015ToObjectXYZ(target=MEM_70AA, identifier="EVENT_3074_set_7010_to_object_xyz_36"),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x00F0),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_3074_play_sound_76"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 160, ["EVENT_3074_play_sound_46"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_3074_play_sound_61"]),
	Jmp(["EVENT_3074_ret_80"]),
	PlaySound(sound=SO013_COIN, channel=6, identifier="EVENT_3074_play_sound_46"),
	CreatePacketAt7010(packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_3074_ret_80"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	AddCoins(10),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 1, ["EVENT_3074_dec_55"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 2, ["EVENT_3074_dec_57"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 3, ["EVENT_3074_dec_59"]),
	Dec(COIN_COUNTER_1),
	Jmp(["EVENT_3074_ret_80"]),
	Dec(COIN_COUNTER_2, identifier="EVENT_3074_dec_55"),
	Jmp(["EVENT_3074_ret_80"]),
	Dec(COIN_COUNTER_3, identifier="EVENT_3074_dec_57"),
	Jmp(["EVENT_3074_ret_80"]),
	Dec(COIN_COUNTER_4, identifier="EVENT_3074_dec_59"),
	Jmp(["EVENT_3074_ret_80"]),
	PlaySound(sound=SO013_COIN, channel=6, identifier="EVENT_3074_play_sound_61"),
	CreatePacketAt7010(packet=P018_SMALL_COIN_BEING_COLLECTED, destinations=["EVENT_3074_ret_80"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	AddCoins(1),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 1, ["EVENT_3074_dec_70"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 2, ["EVENT_3074_dec_72"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 3, ["EVENT_3074_dec_74"]),
	Dec(COIN_COUNTER_1),
	Jmp(["EVENT_3074_ret_80"]),
	Dec(COIN_COUNTER_2, identifier="EVENT_3074_dec_70"),
	Jmp(["EVENT_3074_ret_80"]),
	Dec(COIN_COUNTER_3, identifier="EVENT_3074_dec_72"),
	Jmp(["EVENT_3074_ret_80"]),
	Dec(COIN_COUNTER_4, identifier="EVENT_3074_dec_74"),
	Jmp(["EVENT_3074_ret_80"]),
	PlaySound(sound=SO013_COIN, channel=6, identifier="EVENT_3074_play_sound_76"),
	CreatePacketAt7010(packet=P018_SMALL_COIN_BEING_COLLECTED, destinations=["EVENT_3074_ret_80"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	AddCoins(1),
	Return(identifier="EVENT_3074_ret_80")
])
