# E1364_CURTAIN_ROOM_EXIT_TO_BALCONY

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
	JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_1364_jmp_if_bit_clear_72"]),
	JmpIfBitSet(CURTAIN_MINIGAME_COMPLETED, ["EVENT_1364_fade_out_to_black_async_49"]),
	JmpIfBitSet(TOWER_BOSS_1_DEFEATED, ["EVENT_1364_fade_out_to_black_async_49"]),
	FadeOutToBlack(sync=False),
	Pause(5),
	Jmp(["EVENT_1281_enter_area_0"]),
	FreezeCamera(identifier="EVENT_1364_freeze_camera_6"),
	ApplySolidityModToLevel(permanent=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=3),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=0, y=3, height=0)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=3, y=26),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=False),
	Pause(80),
	StopMusic(),
	FadeOutMusicToVolume(duration=0, volume=100),
	Pause(10),
	RunDialog(dialog_id=DI2770_FROGFUCIUS_KEEP_OBSTACLE_PRIZE_HINT, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	Pause(25),
	PlayMusicAtDefaultVolume(M0032_ANDMYNAME_SBOOSTER),
	Pause(10),
	UnsyncDialog(),
	CloseDialog(),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast(),
		A_JumpToHeight(96)
	]),
	Pause(60),
	RunDialog(dialog_id=DI2771_EMPTY, above_object=NPC_12, closable=False, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	UnsyncDialog(),
	CloseDialog(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(15),
		A_FaceNortheast(),
		A_Pause(15),
		A_WalkNortheastSteps(3),
		A_WalkNortheastPixels(8),
		A_Pause(7),
		A_SetSpriteSequence(index=10, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(7),
		A_SetSpriteSequence(index=11, is_mold=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_SetSpriteSequence(index=9, is_mold=True, looping=True),
		A_Pause(7),
		A_SetSpriteSequence(index=8, is_mold=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(20),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkNorthwestSteps(3),
		A_WalkNorthwestPixels(7)
	]),
	Pause(20),
	PlaySound(sound=SO090_CURTAIN, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=39),
	Pause(2),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNorthwestPixels(20),
		A_SetPriority(2),
		A_Pause(15),
		A_FaceSoutheast(),
		A_Pause(10),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(NORMAL)
	]),
	PlaySound(sound=SO090_CURTAIN, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=38),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=37),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, mod_id=36),
	Pause(2),
	Jmp(["EVENT_1358_remove_from_level_0"]),
	Return(),
	FadeOutToBlack(sync=False, identifier="EVENT_1364_fade_out_to_black_async_49"),
	FadeOutMusicToVolume(duration=0, volume=0),
	StartBattleAtBattlefield(PACK177_KGGG_FIGHT_STATIC, BF17_BOOSTER_TOWER_BALCONY),
	JmpIfBitClear(GAME_OVER, ["EVENT_1364_fade_out_music_to_volume_54"]),
	ResetAndChooseGame(),
	FadeOutMusicToVolume(duration=0, volume=0, identifier="EVENT_1364_fade_out_music_to_volume_54"),
	RemoveObjectFromSpecificLevel(NPC_4, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT),
	SetBit(TOWER_CHARACTER_RECRUITED),
	SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT_7089_2),
	EnterArea(room_id=R202_BOOSTER_TOWER_ENTRANCE, face_direction=SOUTHWEST, x=5, y=114, z=23),
	PlayMusicAtDefaultVolume(M0037_BOOSTERHILL_START),
	RemoveObjectFromCurrentLevel(NPC_0),
	FadeInFromBlack(sync=False),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(50),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO058_INSERT, channel=6),
		A_Pause(45),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
		A_Pause(25),
		A_ResetProperties(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_PlaySound(sound=SO024_TAPPING_FEET, channel=6),
		A_WalkNortheastPixels(24),
		A_JumpToHeight(height=69, silent=True),
		A_Pause(15),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
		A_SetWalkingSpeed(FASTEST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff()
	]),
	Pause(15),
	RestoreAllHP(),
	RestoreAllFP(),
	EnterArea(room_id=R054_BOOSTER_HILL_DUMMY, face_direction=NORTHWEST, x=7, y=57, z=0, run_entrance_event=True),
	Return(),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_1283_enter_area_0"], identifier="EVENT_1364_jmp_if_bit_clear_72"),
	Jmp(["EVENT_1282_enter_area_0"])
])
