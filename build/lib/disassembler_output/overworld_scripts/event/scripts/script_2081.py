# E2081_MUSTY_FEARS_LAMP

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
	MoveScriptToMainThread(),
	SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(2),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(2),
	TintLayers(layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB], red=112, green=104, blue=16, speed=0),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB]),
	FadeOutMusicToVolume(duration=8, volume=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(FAST),
		A_WalkToXYCoords(x=5, y=49),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(120),
		A_WalkNorthwestPixels(32)
	]),
	Pause(5),
	CircleMaskShrinkToObject(target=NPC_5, width=0, speed=3, static=True),
	PlaySound(sound=SO054_GOODNIGHT, channel=6),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(120),
	ApplyTileModToLevel(use_alternate=True, room_id=R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, mod_id=32),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastPixels(16),
		A_WalkSouthPixels(2),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	Pause(5),
	FadeInFromBlack(sync=False, duration=120),
	JmpIfBitSet(INVISIBLE_ITEMS_HAVE_BEEN_SPAWNED, ["EVENT_2082_pause_0"]),
	SetBit(INVISIBLE_ITEMS_HAVE_BEEN_SPAWNED),
	Pause(150),
	SetSyncActionScript(NPC_0, A0568_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI2966_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	SetSyncActionScript(NPC_1, A0568_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI2964_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	SetSyncActionScript(NPC_2, A0568_EMPTY),
	Pause(60),
	RunDialog(dialog_id=DI2965_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	RunDialog(dialog_id=DI2967_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast(),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI2968_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FaceNorthwest(),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI2969_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2970_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FaceSouthwest()
	]),
	Pause(20),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownSteps(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownSteps(1)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownSteps(1)
	]),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2),
		A_FaceNorthwest()
	]),
	Pause(45),
	SetSyncActionScript(NPC_1, A0870_EMPTY),
	RunDialog(dialog_id=DI2989_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_1, A0871_EMPTY),
	Pause(20),
	SetSyncActionScript(NPC_0, A0872_EMPTY),
	RunDialog(dialog_id=DI2990_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_0, A0873_EMPTY),
	Pause(20),
	SetSyncActionScript(NPC_2, A0874_EMPTY),
	RunDialog(dialog_id=DI2991_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_2, A0875_EMPTY),
	Pause(20),
	RunDialog(dialog_id=DI2992_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(NPC_0, A0569_EMPTY),
	SetSyncActionScript(NPC_1, A0569_EMPTY),
	SetSyncActionScript(NPC_2, A0569_EMPTY),
	Pause(110),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_Pause(20),
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=5, y=47)
	]),
	RunDialog(dialog_id=DI2993_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkToXYCoords(x=8, y=46),
		A_Pause(2),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(110),
	SetSyncActionScript(NPC_0, A0568_EMPTY),
	Pause(45),
	RunDialog(dialog_id=DI2994_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	SetSyncActionScript(NPC_2, A0568_EMPTY),
	Pause(45),
	RunDialog(dialog_id=DI2995_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	SetSyncActionScript(NPC_1, A0568_EMPTY),
	Pause(45),
	RunDialog(dialog_id=DI2996_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	RunDialog(dialog_id=DI2997_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2081_run_dialog_87"),
	SetSyncActionScript(NPC_0, A0569_EMPTY),
	SetSyncActionScript(NPC_1, A0569_EMPTY),
	SetSyncActionScript(NPC_2, A0569_EMPTY),
	Pause(60),
	TintLayers(layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB], red=0, green=0, blue=0, speed=0),
	ResetPrioritySet(),
	FadeOutMusicToVolume(duration=0, volume=100),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True),
		A_Pause(15),
		A_SetSequenceSpeed(NORMAL)
	]),
	FadeOutMusicToVolume(duration=6, volume=100),
	Set7000ToTappedButton(identifier="EVENT_2081_set_7000_to_tapped_button_98"),
	Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_2081_apply_tile_mod_103"]),
	Jmp(["EVENT_2081_set_7000_to_tapped_button_98"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN, mod_id=32, identifier="EVENT_2081_apply_tile_mod_103"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_JumpToHeight(120),
		A_WalkSouthPixels(32),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(1),
	PlaySound(sound=SO058_INSERT, channel=6),
	ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
	Return()
])
