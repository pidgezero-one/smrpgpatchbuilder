# E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST

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
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	Mem7000AndConst(0x00F0),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
	SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Set70107015ToObjectXYZ(target=MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 0, ["EVENT_3072_play_sound_16"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 16, ["EVENT_3072_enable_controls_23"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 32, ["EVENT_3072_play_sound_39"]),
	JmpIfVarEqualsConst(CHEST_COIN_SIZE, 48, ["EVENT_3072_play_sound_44"]),
	Jmp(["EVENT_3072_ret_47"]),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3072_play_sound_16"),
	CreatePacketAt7010(packet=P001_FLASHING_POOF_MUSHROOM, destinations=["EVENT_3072_ret_47"]),
	RestoreAllHP(),
	RestoreAllFP(),
	SetVarToConst(TIMER_7020, 8),
	RunBackgroundEventWithPause(event_id=E3075_HEAL_FLASH, timer_var=TIMER_7020, bit_4=True, bit_5=True),
	Jmp(["EVENT_3072_ret_47"]),
	EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B], identifier="EVENT_3072_enable_controls_23"),
	PlaySound(sound=SO014_FLOWER, channel=6),
	CreatePacketAt7010(packet=P003_BRIEF_STAR, destinations=["EVENT_3072_ret_47"]),
	StopMusicFDA0(),
	SetVarToConst(TIMER_7022, 550),
	RunBackgroundEventWithPause(event_id=E3076_EXP_STAR_CHEST_BACKGROUND, timer_var=TIMER_7022, bit_4=True, bit_5=True),
	SetBit(TEMP_7076_0),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000F),
	SetEXPPacketTo7000(),
	MarioGlows(),
	ClearBit(EXP_STAR_BIT_6),
	ClearBit(UNKNOWN_7064_4),
	ClearBit(EXP_STAR_BIT_5),
	CreatePacketAtObjectCoords(packet=P022_RECURSIVE_SPARKLES, target_npc=MARIO, destinations=["EVENT_3072_jmp_38"]),
	Jmp(["EVENT_3072_ret_47"], identifier="EVENT_3072_jmp_38"),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3072_play_sound_39"),
	CreatePacketAt7010(packet=P000_FLASHING_POOF_FLOWER, destinations=["EVENT_3072_ret_47"]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Add7000ToMaxFP(),
	Jmp(["EVENT_3072_ret_47"]),
	PlaySound(sound=SO094_FROG_COIN, channel=6, identifier="EVENT_3072_play_sound_44"),
	CreatePacketAt7010(packet=P019_FROG_COIN_BEING_COLLECTED, destinations=["EVENT_3072_ret_47"]),
	AddFrogCoins(1),
	Return(identifier="EVENT_3072_ret_47")
])
