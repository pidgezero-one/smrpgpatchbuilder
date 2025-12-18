# E3499_BOOSTER_HILL_1ST_PASS_LOADER

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
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7034, 16),
	SetVarToConst(TEMP_7026, 1),
	SetVarToConst(BOOSTER_HILL_70B1, 0),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=11, y=67, z=0, direction=EAST)
	]),
	ActionQueueSync(target=LAYER_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(18)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x01\x00\x01\x00\x00\x00 \x80')),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_ShiftZUpPixels(9),
		A_WalkSoutheastPixels(8)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkNorthwestSteps(11)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(11),
		A_SetSequenceSpeed(NORMAL)
	]),
	SetSyncActionScript(NPC_8, A0715_FOREVER_PAUSE_LOOP),
	RunDialog(dialog_id=DI1178_FOUND_AN_70A7_AUTO_TERMINATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3499_action_queue_96"]),
	RunDialog(dialog_id=DI1179_MARIO_JOINS, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpToSubroutine(["EVENT_3499_action_queue_99"]),
	Pause(20),
	JmpToSubroutine(["EVENT_3499_action_queue_96"]),
	RunDialogForDuration(dialog_id=DI1180_MALLOW_JOINS, duration=1, sync=True),
	PauseScriptResumeOnNextDialogPageB(),
	JmpToSubroutine(["EVENT_3499_action_queue_99"]),
	PauseScriptResumeOnNextDialogPageB(),
	JmpToSubroutine(["EVENT_3499_action_queue_96"]),
	PauseScriptResumeOnNextDialogPageB(),
	JmpToSubroutine(["EVENT_3499_action_queue_99"]),
	UnsyncDialog(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(8),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI1181_GENO_JOINS, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	JmpToSubroutine(["EVENT_3499_action_queue_96"]),
	UnsyncDialog(),
	JmpToSubroutine(["EVENT_3499_action_queue_99"]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(40),
		A_SetSequenceSpeed(NORMAL)
	]),
	JmpToSubroutine(["EVENT_3499_action_queue_96"]),
	RunDialog(dialog_id=DI1182_BOWSER_JOINS, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequenceLoopingOn()
	]),
	SetVarToConst(TEMP_70AE, 3),
	JmpToSubroutine(["EVENT_3499_action_queue_99"]),
	SetSyncActionScript(NPC_3, A0707_BOOSTER_HILL_HENCHMAN),
	SetSyncActionScript(NPC_4, A0707_BOOSTER_HILL_HENCHMAN),
	SetSyncActionScript(NPC_5, A0707_BOOSTER_HILL_HENCHMAN),
	Pause(60),
	FreezeAllNPCsUntilReturn(),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=7),
	Pause(16),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=11, y=65, z=0, direction=EAST),
		A_SetPriority(3),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(6),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_JumpToHeight(64)
	]),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	RunDialog(dialog_id=DI1188_EMPTY, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3499_run_dialog_duration_75"]),
	RunDialog(dialog_id=DI1183_TOADSTOOL_JOINS, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_StartLoopNTimes(3),
		A_PlaySound(sound=SO003_MENU_SCROLL, channel=6),
		A_WalkNortheastPixels(8),
		A_EndLoop(),
		A_JumpToHeight(107),
		A_Pause(30),
		A_StartLoopNTimes(7),
		A_PlaySound(sound=SO003_MENU_SCROLL, channel=6),
		A_WalkSouthwestPixels(8),
		A_EndLoop(),
		A_StartLoopNTimes(1),
		A_JumpToHeight(107),
		A_Pause(30),
		A_EndLoop()
	]),
	RunDialogForDuration(dialog_id=DI1184_EMPTY, duration=0, sync=False),
	JmpToSubroutine(["EVENT_3499_action_queue_102"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(36),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_JumpToHeight(height=112, silent=True),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_StartLoopNTimes(15),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(1),
		A_EndLoop(),
		A_ResetProperties(),
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestPixels(16)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
		A_JumpToHeight(56),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_Pause(32),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(84),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_JumpToHeight(height=112, silent=True),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(23),
		A_VisibilityOff(),
		A_WalkSoutheastPixels(2),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(2),
		A_EndLoop(),
		A_ResetProperties(),
		A_Pause(30),
		A_TransferToXYZF(x=7, y=59, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_ShiftXYSteps(x=3, y=6)
	]),
	RunDialogForDuration(dialog_id=DI1185_EMPTY, duration=0, sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2)
	]),
	JmpToSubroutine(["EVENT_3499_action_queue_102"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(17),
		A_JumpToHeight(108),
		A_Pause(23),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_FloatingOff(),
		A_JumpToHeight(height=108, silent=True),
		A_WalkNorthwestPixels(32),
		A_Pause(30),
		A_TransferToXYZF(x=7, y=59, z=0, direction=EAST)
	]),
	RunDialogForDuration(dialog_id=DI1186_EMPTY, duration=0, sync=False),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_PlaySound(sound=SO050_WATER_DROPLET, channel=4),
		A_JumpToHeight(56),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_Pause(32),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4),
		A_SetAllSpeeds(VERY_FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkSoutheastSteps(8)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(72),
		A_JumpToHeight(108),
		A_Pause(23),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_FloatingOff(),
		A_JumpToHeight(height=108, silent=True),
		A_WalkNorthwestPixels(32)
	]),
	SetAsyncActionScript(NPC_9, A0716_BOOSTER_HILL_BUMP_FLOWER),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(30),
		A_ShiftXYSteps(x=254, y=252)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_TransferToXYZF(x=7, y=59, z=0, direction=EAST),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	RunDialogForDuration(dialog_id=DI1187_EMPTY, duration=1, sync=False, identifier="EVENT_3499_run_dialog_duration_75"),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	FadeOutMusicToVolume(duration=2, volume=0),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_WalkSoutheastSteps(6),
		A_VisibilityOff()
	]),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=97, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=98, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=99, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=100, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=101, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=102, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=103, row=7),
	Pause(32),
	UnfreezeAllNPCs(),
	RunBackgroundEvent(event_id=E3500_BOOSTER_HILL_1ST_PASS_SNIFIT_JUMPS, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E3503_BOOSTER_HILL_BARREL_SUMMONER, return_on_level_exit=True, bit_6=True),
	SetSyncActionScript(LAYER_1, A0704_BOOSTER_HILL_LAYER_1),
	SetSyncActionScript(LAYER_2, A0655_BOOSTER_HILL_LAYER_2),
	SetSyncActionScript(LAYER_3, A0705_BOOSTER_HILL_LAYER_3),
	PlayMusicAtDefaultVolume(M0038_BOOSTERHILL),
	RunEventAtReturn(E3502_BOOSTER_HILL_END),
	Return(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkNorthPixels(4),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkNorthPixels(4),
		A_WalkWestPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkWestPixels(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	], identifier="EVENT_3499_action_queue_96"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceSoutheast()
	]),
	Return(),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthPixels(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	], identifier="EVENT_3499_action_queue_99"),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceNorthwest()
	]),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=5, y=54, z=0, direction=EAST),
		A_SetPriority(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(FASTER),
		A_WalkSouthwestPixels(36),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_VisibilityOn(),
		A_JumpToHeight(24, identifier="EVENT_3499_action_queue_102_SUBSCRIPT_jump_to_height_9"),
		A_Walk1StepSoutheast(),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
		A_CompareVarToConst(PRIMARY_TEMP_700C, 5888),
		A_JmpIfComparisonResultIsLesser(["EVENT_3499_action_queue_102_SUBSCRIPT_jump_to_height_9"])
	], identifier="EVENT_3499_action_queue_102"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(50),
		A_JumpToHeight(112)
	]),
	Return()
])
