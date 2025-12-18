# E2225_KEEP_2ND_BOSS

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
	JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["EVENT_2225_ret_30"]),
	RunDialog(dialog_id=DI3417_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(20)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(1),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(11)
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkSouthwestSteps(1),
		A_WalkSouthwestPixels(8)
	]),
	Pause(15),
	RunDialog(dialog_id=DI3418_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=12, y=46, z=0, direction=EAST),
		A_Pause(1),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xe0\xfd\x00\xff')),
		A_UnknownCommand(bytearray(b'%\x00\r\x80\xff')),
		A_Pause(44),
		A_BPL262728(),
		A_SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
		A_Pause(5),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(3),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(48)
	]),
	RunDialog(dialog_id=DI3419_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_FixedFCoordOn(),
		A_WalkNortheastSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_Pause(45)
	]),
	FadeOutMusicToVolume(duration=0, volume=0),
	StartBattleAtBattlefield(PACK210_BOOMER_BOSS_STATIC, BF29_BOWSERS_KEEP_CHANDELIERS),
	JmpIfBitClear(GAME_OVER, ["EVENT_2225_restore_all_hp_16"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2225_restore_all_hp_16"),
	RestoreAllFP(),
	StartBattleAtBattlefield(PACK186_EXOR_FIGHT_STATIC, BF16_BOWSERS_KEEP_TURRET_EXOR),
	JmpIfBitClear(GAME_OVER, ["EVENT_2225_restore_all_hp_21"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2225_restore_all_hp_21"),
	RestoreAllFP(),
	SetBit(KEEP_BOSS_3_DEFEATED),
	SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
	SetBit(MAP_GATE),
	FadeOutMusicToVolume(duration=0, volume=0),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	RunMenuOrEventSequence(SC15_ENTER_GATE_TO_SMITHY_FACTORY),
	EnterArea(room_id=R350_SMITHY_FACTORY_AREA_01, face_direction=SOUTHEAST, x=4, y=27, z=0, run_entrance_event=True),
	Return(identifier="EVENT_2225_ret_30")
])
