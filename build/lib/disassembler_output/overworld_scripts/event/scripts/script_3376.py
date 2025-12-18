# E3376_KEEP_6_DOOR_LOBBY_LOADER

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
	SpeedUpMusicToDefault(),
	CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3376_jmp_if_7000_all_bits_clear_5"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=0),
	JmpIf7000AllBitsClear(bits=[3], destinations=["EVENT_3376_copy_var_to_var_8"], identifier="EVENT_3376_jmp_if_7000_all_bits_clear_5"),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=1),
	CopyVarToVar(from_var=UNKNOWN_70E8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3376_copy_var_to_var_8"),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3376_jmp_if_7000_all_bits_clear_12"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=2),
	JmpIf7000AllBitsClear(bits=[3], destinations=["EVENT_3376_copy_var_to_var_15"], identifier="EVENT_3376_jmp_if_7000_all_bits_clear_12"),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=3),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=3),
	CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3376_copy_var_to_var_15"),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3376_jmp_if_7000_all_bits_clear_19"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=4),
	JmpIf7000AllBitsClear(bits=[3], destinations=["EVENT_3376_jmp_if_bit_set_22"], identifier="EVENT_3376_jmp_if_7000_all_bits_clear_19"),
	ApplyTileModToLevel(use_alternate=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=5),
	ApplySolidityModToLevel(permanent=True, room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, mod_id=5),
	JmpIfBitSet(UNKNOWN_BOWSERS_KEEP_707F_0, ["EVENT_3356_clear_bit_5"], identifier="EVENT_3376_jmp_if_bit_set_22"),
	JmpIfVarEqualsConst(KEEP_DOORS_EXIT_TYPE_1, 0, ["EVENT_3376_run_event_as_subroutine_26"]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return(),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3376_run_event_as_subroutine_26"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(5),
		A_Walk1StepEast()
	]),
	RunDialog(dialog_id=DI1944_DUPLICATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3376_action_queue_50"]),
	RunDialog(dialog_id=DI1945_NEED_ELDER_KEY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	EnterArea(room_id=R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, face_direction=NORTHEAST, x=4, y=58, z=5),
	RemoveObjectFromCurrentLevel(MARIO),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(6)
	]),
	RunDialog(dialog_id=DI1946_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	EnterArea(room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, face_direction=NORTHEAST, x=2, y=63, z=0),
	RemoveObjectFromCurrentLevel(MARIO),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(6)
	]),
	RunDialog(dialog_id=DI1947_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	EnterArea(room_id=R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, face_direction=NORTHEAST, x=3, y=106, z=0),
	RemoveObjectFromCurrentLevel(MARIO),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(6)
	]),
	RunDialog(dialog_id=DI1948_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	EnterArea(room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS, face_direction=NORTHEAST, x=6, y=33, z=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=2, y=39),
		A_FaceNortheast(),
		A_Pause(1)
	]),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI1949_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Walk1StepWest(),
		A_WalkSouthwestSteps(4)
	], identifier="EVENT_3376_action_queue_50"),
	Return(),
	Mem7000AndConst(0x0007, identifier="EVENT_3376_mem_7000_and_const_52"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000),
	Mem7000OrVar(ROSE_WAY_703E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=KEEP_DOORS_EXIT_TYPE_2),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3376_enter_area_65"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_3376_enter_area_67"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_3376_enter_area_69"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3376_enter_area_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3376_enter_area_73"]),
	EnterArea(room_id=R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, face_direction=NORTHEAST, x=4, y=58, z=5, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, face_direction=NORTHEAST, x=8, y=115, z=2, run_entrance_event=True, identifier="EVENT_3376_enter_area_65"),
	Return(),
	EnterArea(room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, face_direction=NORTHEAST, x=2, y=63, z=0, run_entrance_event=True, identifier="EVENT_3376_enter_area_67"),
	Return(),
	EnterArea(room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA, face_direction=NORTHEAST, x=2, y=63, z=0, run_entrance_event=True, identifier="EVENT_3376_enter_area_69"),
	Return(),
	EnterArea(room_id=R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, face_direction=NORTHEAST, x=3, y=106, z=0, run_entrance_event=True, identifier="EVENT_3376_enter_area_71"),
	Return(),
	EnterArea(room_id=R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING, face_direction=NORTHEAST, x=22, y=83, z=0, run_entrance_event=True, identifier="EVENT_3376_enter_area_73"),
	Return()
])
