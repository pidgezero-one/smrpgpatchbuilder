# E0476_INITIATE_MUSHROOM_DERBY_FROM_TALKING_TO_BOSHI

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
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
	PauseScriptUntilEffectDone(),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_3),
	PauseActionScript(NPC_5),
	PauseActionScript(NPC_9),
	PauseActionScript(NPC_10),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=16, y=77, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4])
	]),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=10, y=81, z=0, direction=EAST),
		A_FaceSoutheast(),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=11, y=83, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=11, y=75, z=0, direction=EAST),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=10, y=81, z=0, direction=EAST),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartSyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=20, y=69, z=0, direction=EAST),
		A_FaceNorthwest()
	]),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=15, y=67, z=0, direction=EAST),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=19, y=60, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_13),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	UnknownCommand(bytearray(b'\xfd\x8e@\x00\xb1')),
	PauseScriptUntilEffectDone(),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ShadowOn(),
		A_TransferToXYZF(x=14, y=75, z=0, direction=EAST),
		A_SetPriority(3),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True),
		A_WalkWestSteps(3),
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	RunDialog(dialog_id=DI0922_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_476_clear_bit_183"]),
	Pause(30),
	SetAsyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	PauseActionScript(NPC_8),
	UnsyncDialog(),
	RunDialog(dialog_id=DI2555_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False, identifier="EVENT_476_run_dialog_32"),
	Pause(10),
	SetAsyncActionScript(NPC_9, A0678_SAMUS),
	SetAsyncActionScript(NPC_9, A0678_SAMUS),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SequenceLoopingOff()
	]),
	RunDialog(dialog_id=DI2556_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetAsyncActionScript(NPC_9, A0679_EMPTY),
	SetAsyncActionScript(NPC_9, A0679_EMPTY),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SequenceLoopingOff()
	]),
	RunDialog(dialog_id=DI2557_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_476_run_dialog_45"]),
	Jmp(["EVENT_476_run_dialog_32"]),
	RunDialog(dialog_id=DI0924_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_476_run_dialog_45"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_476_play_music_default_volume_49"]),
	FadeOutMusicToVolume(duration=3, volume=0),
	Pause(120),
	PlayMusicAtDefaultVolume(M0019_RACETRAINING, identifier="EVENT_476_play_music_default_volume_49"),
	SlowDownMusicTempoBy(duration=0, change=2),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_0),
	Pause(1, identifier="EVENT_476_pause_53"),
	JmpIfAudioMemoryEquals(4, ["EVENT_476_pause_53"]),
	RunDialog(dialog_id=DI0925_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_57"),
	JmpIfAudioMemoryEquals(5, ["EVENT_476_pause_57"]),
	RunDialog(dialog_id=DI0929_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_61"),
	JmpIfAudioMemoryEquals(6, ["EVENT_476_pause_61"]),
	RunDialog(dialog_id=DI0925_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_65"),
	JmpIfAudioMemoryEquals(7, ["EVENT_476_pause_65"]),
	RunDialog(dialog_id=DI0926_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_69"),
	JmpIfAudioMemoryEquals(8, ["EVENT_476_pause_69"]),
	RunDialog(dialog_id=DI0925_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_73"),
	JmpIfAudioMemoryEquals(9, ["EVENT_476_pause_73"]),
	RunDialog(dialog_id=DI0926_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_77"),
	JmpIfAudioMemoryEquals(10, ["EVENT_476_pause_77"]),
	RunDialog(dialog_id=DI0927_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(1, identifier="EVENT_476_pause_81"),
	JmpIfAudioMemoryEquals(11, ["EVENT_476_pause_81"]),
	RunDialog(dialog_id=DI0928_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
	SetVarToConst(TEMP_70AE, 0),
	SetVarToConst(TEMP_7032, 0),
	SetVarToConst(ROSE_WAY_7038, 120),
	Set7000ToTappedButton(identifier="EVENT_476_set_7000_to_tapped_button_89"),
	Pause(1),
	JmpIf7000AnyBitsSet(bits=[5], destinations=["EVENT_476_clear_bit_130"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_476_clear_bit_130"]),
	JmpIfAudioMemoryEquals(1, ["EVENT_476_set_7000_to_tapped_button_89"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_476_clear_bit_99"]),
	SetBit(TEMP_7043_0),
	RunDialog(dialog_id=DI0947_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	ClearBit(TEMP_7043_0, identifier="EVENT_476_clear_bit_99"),
	RunDialog(dialog_id=DI0948_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Set7000ToTappedButton(identifier="EVENT_476_set_7000_to_tapped_button_102"),
	Pause(1),
	JmpIf7000AnyBitsSet(bits=[5], destinations=["EVENT_476_set_bit_144"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_476_set_bit_148"]),
	JmpIfAudioMemoryEquals(2, ["EVENT_476_set_7000_to_tapped_button_102"]),
	Pause(1, identifier="EVENT_476_pause_107"),
	JmpIf7000AnyBitsSet(bits=[5], destinations=["EVENT_476_clear_bit_130"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_476_clear_bit_130"]),
	JmpIfAudioMemoryEquals(1, ["EVENT_476_pause_107"]),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_476_set_bit_116"]),
	ClearBit(TEMP_7043_0),
	RunDialog(dialog_id=DI0948_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Jmp(["EVENT_476_set_7000_to_tapped_button_119"]),
	SetBit(TEMP_7043_0, identifier="EVENT_476_set_bit_116"),
	RunDialog(dialog_id=DI0947_EMPTY, above_object=NPC_14, closable=False, sync=True, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	Set7000ToTappedButton(identifier="EVENT_476_set_7000_to_tapped_button_119"),
	Pause(1),
	JmpIf7000AnyBitsSet(bits=[5], destinations=["EVENT_476_jmp_if_bit_set_134"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_476_jmp_if_bit_set_139"]),
	JmpIfAudioMemoryEquals(2, ["EVENT_476_set_7000_to_tapped_button_119"]),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_0),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_1),
	Inc(TEMP_70AE),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_476_fade_out_music_to_volume_172"]),
	Jmp(["EVENT_476_set_7000_to_tapped_button_89"]),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_0, identifier="EVENT_476_clear_bit_130"),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_1),
	SetVarToConst(TEMP_7032, 0),
	Jmp(["EVENT_476_set_7000_to_tapped_button_89"]),
	JmpIfBitSet(UNKNOWN_MUSHROOM_DERBY_704A_0, ["EVENT_476_set_var_to_const_152"], identifier="EVENT_476_jmp_if_bit_set_134"),
	JmpIfBitSet(UNKNOWN_MUSHROOM_DERBY_704A_1, ["EVENT_476_set_bit_154"]),
	SetBit(UNKNOWN_MUSHROOM_DERBY_704A_0),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_1),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	JmpIfBitSet(UNKNOWN_MUSHROOM_DERBY_704A_1, ["EVENT_476_set_var_to_const_152"], identifier="EVENT_476_jmp_if_bit_set_139"),
	JmpIfBitSet(UNKNOWN_MUSHROOM_DERBY_704A_0, ["EVENT_476_set_bit_161"]),
	SetBit(UNKNOWN_MUSHROOM_DERBY_704A_1),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_0),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	SetBit(UNKNOWN_MUSHROOM_DERBY_704A_0, identifier="EVENT_476_set_bit_144"),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_1),
	SetSyncActionScript(NPC_9, A0678_SAMUS),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	SetBit(UNKNOWN_MUSHROOM_DERBY_704A_1, identifier="EVENT_476_set_bit_148"),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_0),
	SetSyncActionScript(NPC_9, A0678_SAMUS),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	SetVarToConst(TEMP_7032, 0, identifier="EVENT_476_set_var_to_const_152"),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	SetBit(UNKNOWN_MUSHROOM_DERBY_704A_0, identifier="EVENT_476_set_bit_154"),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_1),
	Inc(TEMP_7032),
	CompareVarToConst(TEMP_7032, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_476_compare_var_to_const_168"]),
	SetSyncActionScript(NPC_9, A0678_SAMUS),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	SetBit(UNKNOWN_MUSHROOM_DERBY_704A_1, identifier="EVENT_476_set_bit_161"),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_704A_0),
	Inc(TEMP_7032),
	CompareVarToConst(TEMP_7032, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_476_compare_var_to_const_168"]),
	SetSyncActionScript(NPC_9, A0678_SAMUS),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	CompareVarToConst(TEMP_7032, 8, identifier="EVENT_476_compare_var_to_const_168"),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_476_fade_out_music_to_volume_172"]),
	SetSyncActionScript(NPC_9, A0679_EMPTY),
	Jmp(["EVENT_476_set_7000_to_tapped_button_102"]),
	FadeOutMusicToVolume(duration=3, volume=0, identifier="EVENT_476_fade_out_music_to_volume_172"),
	Pause(120),
	StopMusic(),
	CompareVarToConst(TEMP_7032, 6),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_476_run_dialog_182"]),
	JmpIfVarEqualsConst(TEMP_7032, 0, ["EVENT_476_set_bit_207"]),
	SetBit(TEMP_7043_2),
	RunDialog(dialog_id=DI0931_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_476_clear_bit_183"]),
	Jmp(["EVENT_476_run_dialog_45"]),
	RunDialog(dialog_id=DI0932_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False, identifier="EVENT_476_run_dialog_182"),
	ClearBit(TEMP_7043_2, identifier="EVENT_476_clear_bit_183"),
	SetAsyncActionScript(NPC_8, A0636_54_VELOCITY_SINGLE_JUMP),
	RunDialog(dialog_id=DI0933_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkEastSteps(3),
		A_WalkEastPixels(16),
		A_SequencePlaybackOff(),
		A_VisibilityOff()
	]),
	CloseDialog(),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_476_db_190"]),
	SummonObjectToCurrentLevel(NPC_13),
	UnknownCommand(bytearray(b'\xfd\x8e\xb2\x07\xb1'), identifier="EVENT_476_db_190"),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceNorthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	PauseScriptUntilEffectDone(),
	Pause(30),
	PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
	RunDialog(dialog_id=DI0908_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FaceNortheast()
	]),
	Pause(60),
	JmpToSubroutine(["EVENT_457_action_queue_0"]),
	RunBackgroundEvent(event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC, return_on_level_exit=True, run_as_second_script=True),
	EnableControls([]),
	Return(),
	SetBit(TEMP_7043_2, identifier="EVENT_476_set_bit_207"),
	RunDialog(dialog_id=DI0930_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_476_clear_bit_183"]),
	Jmp(["EVENT_476_run_dialog_45"])
])
