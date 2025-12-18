# E4000_CLONE_RESERVED

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
	EnterArea(room_id=R189_MARIOS_PIPEHOUSE, face_direction=EAST, x=4, y=10, z=1),
	PaletteSet(palette_set=33, row=7, bit_0=True, bit_1=True, bit_2=True, bit_3=True),
	ApplyTileModToLevel(use_alternate=True, room_id=R189_MARIOS_PIPEHOUSE, mod_id=0),
	PlayMusicAtDefaultVolume(M0014_MARIO_SPAD),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_PlaySound(sound=SO047_SNOOZE, channel=6)
	]),
	CircleMaskShrinkToObject(target=NPC_2, width=40, speed=3, static=True),
	Pause(90),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True),
		A_Pause(15),
		A_SetSequenceSpeed(NORMAL)
	]),
	Set7000ToTappedButton(identifier="EVENT_4000_set_7000_to_tapped_button_8"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_4000_apply_tile_mod_13"]),
	Jmp(["EVENT_4000_set_7000_to_tapped_button_8"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R189_MARIOS_PIPEHOUSE, mod_id=0, identifier="EVENT_4000_apply_tile_mod_13"),
	CircleMaskShrinkToObject(target=MARIO, width=255, speed=5, static=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_JumpToHeight(120),
		A_WalkSouthPixels(18),
		A_Pause(1, identifier="EVENT_4000_action_queue_15_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_4000_action_queue_15_SUBSCRIPT_pause_4"])
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=1, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6),
		A_WalkNortheastSteps(3),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2225_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	AddToInventory(BaneBombItem),
	RunDialog(dialog_id=DI0514_SHOPKEEPER_YELLS_AT_YOU_ON_SHELF, above_object=MEM_70A8, closable=True, sync=False, multiline=False, use_background=False),
	RunDialog(dialog_id=DI2226_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=True),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6)
	]),
	Return()
])
