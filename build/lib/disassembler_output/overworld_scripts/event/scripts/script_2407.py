# E2407_STAR_HILL_FINAL_EXIT

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
	JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_2407_jmp_if_var_equals_const_26"]),
	JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2407_set_7000_to_object_coord_3"]),
	Return(),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True, identifier="EVENT_2407_set_7000_to_object_coord_3"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2407_freeze_camera_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2407_freeze_camera_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2407_freeze_camera_8"]),
	Return(),
	FreezeCamera(identifier="EVENT_2407_freeze_camera_8"),
	EnableControls([]),
	Pause(1, identifier="EVENT_2407_pause_10"),
	JmpIfMarioInAir(["EVENT_2407_pause_10"]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_7),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetPriority(3),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(SLOW),
		A_WalkToXYCoords(x=26, y=110),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_FloatingOff(),
		A_ShadowOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_FaceNortheast(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3104_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_2),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_2),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkTo70167018(),
		A_VisibilityOff()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return(),
	JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2407_freeze_camera_28"], identifier="EVENT_2407_jmp_if_var_equals_const_26"),
	Return(),
	FreezeCamera(identifier="EVENT_2407_freeze_camera_28"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	Pause(32),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=13),
	PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
	UnfreezeCamera(),
	Pause(32),
	FadeOutToBlack(sync=False, duration=16),
	PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
	SetBit(MAP_DIRECTIONAL_STAR_HILL_SEASIDE_TOWN),
	SetBit(MAP_SEASIDE_TOWN),
	ExitToWorldMap(area=OW31_STAR_HILL, bit_6=True, bit_7=True)
])
