# E3388_SHIP_BOSS_ROOM_PERISCOPE

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
	JmpIfBitClear(SEASIDE_LIBERATED, ["EVENT_3388_ret_64"], identifier="EVENT_3388_jmp_if_bit_clear_0"),
	Jmp(["EVENT_3388_copy_var_to_var_23"]),
	Pause(1, identifier="EVENT_3388_pause_2"),
	Set7000ToTappedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 32, ["EVENT_3388_play_sound_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_3388_play_sound_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_3388_play_sound_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_3388_play_sound_62"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3388_play_sound_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3388_play_sound_17"]),
	Jmp(["EVENT_3388_pause_2"]),
	PlaySound(sound=SO003_MENU_SCROLL, channel=6, identifier="EVENT_3388_play_sound_11"),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 0, ["EVENT_3388_set_var_to_const_15"]),
	Dec(UNKNOWN_70AD),
	Jmp(["EVENT_3388_copy_var_to_var_23"]),
	SetVarToConst(UNKNOWN_70AD, 6, identifier="EVENT_3388_set_var_to_const_15"),
	Jmp(["EVENT_3388_copy_var_to_var_23"]),
	PlaySound(sound=SO003_MENU_SCROLL, channel=6, identifier="EVENT_3388_play_sound_17"),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 6, ["EVENT_3388_set_var_to_const_21"]),
	Inc(UNKNOWN_70AD),
	Jmp(["EVENT_3388_copy_var_to_var_23"]),
	SetVarToConst(UNKNOWN_70AD, 0, identifier="EVENT_3388_set_var_to_const_21"),
	Jmp(["EVENT_3388_copy_var_to_var_23"]),
	CopyVarToVar(from_var=UNKNOWN_70AD, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3388_copy_var_to_var_23"),
	AddConstToVar(PRIMARY_TEMP_7000, 1952),
	RunDialog(dialog_id=PRIMARY_TEMP_7000, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=True),
	Jmp(["EVENT_3388_pause_2"]),
	PlaySound(sound=SO001_MENU_SELECT, channel=6, identifier="EVENT_3388_play_sound_27"),
	CloseDialog(),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 0, ["EVENT_3388_enter_area_36"]),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 1, ["EVENT_3388_enter_area_38"]),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 2, ["EVENT_3388_enter_area_40"]),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 3, ["EVENT_3388_enter_area_42"]),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 4, ["EVENT_3388_enter_area_44"]),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 5, ["EVENT_3388_enter_area_46"]),
	JmpIfVarEqualsConst(UNKNOWN_70AD, 6, ["EVENT_3388_enter_area_48"]),
	EnterArea(room_id=R180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM, face_direction=SOUTH, x=27, y=21, z=4, identifier="EVENT_3388_enter_area_36"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	EnterArea(room_id=R182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES, face_direction=SOUTH, x=25, y=95, z=2, identifier="EVENT_3388_enter_area_38"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	EnterArea(room_id=R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, face_direction=SOUTH, x=3, y=35, z=0, identifier="EVENT_3388_enter_area_40"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	EnterArea(room_id=R188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL, face_direction=SOUTH, x=2, y=79, z=5, identifier="EVENT_3388_enter_area_42"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	EnterArea(room_id=R188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL, face_direction=SOUTH, x=10, y=81, z=0, identifier="EVENT_3388_enter_area_44"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	EnterArea(room_id=R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING, face_direction=SOUTH, x=30, y=49, z=0, identifier="EVENT_3388_enter_area_46"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	EnterArea(room_id=R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, face_direction=SOUTH, x=5, y=117, z=0, identifier="EVENT_3388_enter_area_48"),
	Jmp(["EVENT_3388_remove_from_current_level_50"]),
	RemoveObjectFromCurrentLevel(MARIO, identifier="EVENT_3388_remove_from_current_level_50"),
	CircleMaskShrinkToObject(target=MARIO, width=96, speed=8, static=True),
	Pause(12),
	Pause(1, identifier="EVENT_3388_pause_53"),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[0, 1, 2, 3, 4, 5, 6, 7], destinations=["EVENT_3388_pause_53"]),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=8, static=True),
	Pause(12),
	EnterArea(room_id=R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, face_direction=NORTHEAST, x=24, y=110, z=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastPixels(4)
	]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_3388_jmp_if_bit_clear_0"]),
	PlaySound(sound=SO002_MENU_CANCEL, channel=6, identifier="EVENT_3388_play_sound_62"),
	CloseDialog(),
	Return(identifier="EVENT_3388_ret_64")
])
