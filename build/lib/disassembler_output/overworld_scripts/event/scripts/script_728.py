# E0728_EMPTY

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
	EnableControls([]),
	SetBit(TEMP_7044_6),
	FreezeCamera(),
	RunDialog(dialog_id=DI2306_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PaletteSet(palette_set=105, row=1, bit_0=True, bit_1=True, bit_2=True, bit_3=True),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=6, y=84, z=4, direction=SOUTHEAST),
		A_SetSpriteSequence(index=26, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties(),
		A_Pause(2),
		A_SetSpriteSequence(index=26, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_SetPriority(2),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=6, y=84, z=4, direction=SOUTHEAST),
		A_TransferXYZFPixels(x=245, y=0, z=14, direction=EAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES)
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_10, A0793_DEFAULT_SEQUENCE_STATIC),
	SetSyncActionScript(NPC_13, A0793_DEFAULT_SEQUENCE_STATIC),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_BounceToXYWithHeight(x=5, y=50, height=0)
	]),
	Pause(120),
	UnfreezeCamera(),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	UnsyncActionScript(NPC_13),
	ActionQueueSync(target=NPC_10, subscript=[
		A_Pause(8),
		A_FaceNortheast(),
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_Pause(8),
		A_VisibilityOff(),
		A_TransferToXYZF(x=6, y=83, z=12, direction=EAST),
		A_TransferXYZFPixels(x=252, y=2, z=8, direction=EAST),
		A_VisibilityOn(),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_VisibilityOff(),
		A_TransferXYZFPixels(x=242, y=10, z=0, direction=EAST),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_Pause(16),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True),
		A_WalkNorthwestPixels(4),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=64, silent=True),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(10),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	ClearBit(TEMP_7044_6),
	Return()
])
