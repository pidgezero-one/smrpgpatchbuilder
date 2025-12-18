# E3480_MIDAS_RIVER_WATERFALL_LOADER

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
	FadeOutMusicToVolume(duration=0, volume=8),
	FadeOutSoundToVolume(duration=0, volume=0),
	PlaySound(sound=SO035_RUNNING_WATER, channel=4),
	FadeOutSoundToVolume(duration=2, volume=127),
	SetVarToConst(TEMP_70A9, 32),
	SetVarToConst(X_COORD_2, 4480),
	SetVarToConst(Y_COORD_2, 256),
	SetVarToConst(Z_COORD_2, 0),
	StartLoopNTimes(2),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	AddConstToVar(X_COORD_2, 128),
	AddConstToVar(Y_COORD_2, 64),
	Inc(TEMP_70A9),
	EndLoop(),
	SetVarToConst(X_COORD_2, 4608),
	SetVarToConst(Y_COORD_2, 512),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	FadeInFromBlack(sync=True, duration=80),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3480_action_queue_22"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_704D_6, ["EVENT_3480_action_queue_22"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(148),
		A_ShiftToXYCoords(x=6, y=73),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(27),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthSteps(34),
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorth(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True)
	], identifier="EVENT_3480_action_queue_22"),
	FadeOutMusicToVolume(duration=1, volume=56),
	JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3480_action_queue_30"]),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_704D_6, ["EVENT_3480_action_queue_28"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=9, y=2),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_WalkNorthPixels(5),
		A_SetWalkingSpeed(NORMAL),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_WalkSouthPixels(1),
		A_EndLoop(),
		A_WalkSouthSteps(5),
		A_FixedFCoordOff()
	]),
	Jmp(["EVENT_3480_action_queue_31"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=10, y=4, z=0, direction=EAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_FloatingOn(),
		A_SetWalkingSpeed(SLOW),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x02\xf0\xff')),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(3),
		A_BPL262728(),
		A_FixedFCoordOff()
	], identifier="EVENT_3480_action_queue_28"),
	Jmp(["EVENT_3480_action_queue_31"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=8),
		A_FaceNortheast(),
		A_FloatingOn(),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(6),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%p\x02\xf5\xff')),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_WalkNortheastSteps(6),
		A_Walk1StepNorth(),
		A_BPL262728()
	], identifier="EVENT_3480_action_queue_30"),
	ActionQueueSync(target=NPC_16, subscript=[
		A_TransferToObjectXY(NPC_1),
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(60),
		A_VisibilityOff()
	], identifier="EVENT_3480_action_queue_31"),
	FadeOutSoundToVolume(duration=4, volume=0),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=26, row=7),
	Pause(30),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[LAYER_L2, NPC_SPRITES], colour_math=[LAYER_L1, BACKGROUND, HALF_INTENSITY]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(3),
		A_TransferToXYZF(x=4, y=4, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(8),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_JumpToHeight(64)
	]),
	StopSound(),
	FadeOutSoundToVolume(duration=0, volume=127),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	RunDialog(dialog_id=DI1083_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3480_run_dialog_duration_53"]),
	RunDialog(dialog_id=DI1084_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(SLOW),
		A_StartLoopNTimes(2),
		A_PlaySound(sound=SO003_MENU_SCROLL, channel=6),
		A_WalkEastPixels(4),
		A_EndLoop(),
		A_Pause(30),
		A_StartLoopNTimes(2),
		A_PlaySound(sound=SO003_MENU_SCROLL, channel=6),
		A_WalkWestPixels(4),
		A_EndLoop()
	]),
	RunDialogForDuration(dialog_id=DI1085_EMPTY, duration=0, sync=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FASTER),
		A_StartLoopNTimes(4),
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=6),
		A_WalkNorthPixels(3),
		A_Pause(20),
		A_EndLoop(),
		A_ResetProperties(),
		A_WalkSouthPixels(15),
		A_FixedFCoordOff()
	]),
	RunDialogForDuration(dialog_id=DI1073_EMPTY, duration=0, sync=False),
	RunDialogForDuration(dialog_id=DI1074_EMPTY, duration=1, sync=False, identifier="EVENT_3480_run_dialog_duration_53"),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_WalkNorthwestSteps(5),
		A_VisibilityOff()
	]),
	FadeOutSoundToVolume(duration=0, volume=0),
	PlaySound(sound=SO035_RUNNING_WATER, channel=4),
	FadeOutSoundToVolume(duration=2, volume=127),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, LAYER_L3, NPC_SPRITES], subscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], colour_math=[LAYER_L3, BACKGROUND, HALF_INTENSITY]),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=57, row=1),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=58, row=2),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=59, row=3),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=60, row=4),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=61, row=5),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=62, row=6),
	PaletteSetMorphs(palette_type=FADE_TO, duration=10, palette_set=63, row=7),
	Pause(24),
	SetSyncActionScript(MARIO, A0466_MIDAS_RIVER_TUNNEL_LEAVE),
	JmpToSubroutine(["EVENT_3480_action_queue_72"]),
	RunEventAtReturn(E3489_MIDAS_RIVER_WATERFALL_LISTEN_FOR_BUTTON_INPUTS),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\x97\x00')),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_ShadowOn(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3])
	], identifier="EVENT_3480_action_queue_72"),
	Return()
])
