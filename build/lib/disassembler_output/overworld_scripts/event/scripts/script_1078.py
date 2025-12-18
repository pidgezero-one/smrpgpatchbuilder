# E1078_MELODY_BAY_FINAL_SONG

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
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1078_copy_var_to_var_0"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_1),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_2),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_3),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_4),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_5),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_6),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_7),
	CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TADPOLE_8),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SequenceLoopingOff(),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3062_TOADOFSKY_FINAL_SONG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10, identifier="EVENT_1078_pause_18"),
	SetBit(TEMP_7044_6),
	SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
	ClearBit(TEMP_7044_6),
	Pause(30),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(VERY_SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=16, y=29),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(15),
	DeactivateSoundChannels([0, 1, 2, 3, 4, 5, 6, 7]),
	PlayMusicAtDefaultVolume(M0052_TOADOFSKY),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(75),
	CopyVarToVar(from_var=TADPOLE_1, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(25),
	CopyVarToVar(from_var=TADPOLE_2, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(25),
	CopyVarToVar(from_var=TADPOLE_3, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(25),
	CopyVarToVar(from_var=TADPOLE_4, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(26),
	CopyVarToVar(from_var=TADPOLE_5, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(26),
	CopyVarToVar(from_var=TADPOLE_6, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(27),
	CopyVarToVar(from_var=TADPOLE_7, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(27),
	CopyVarToVar(from_var=TADPOLE_8, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1078_jmp_if_var_equals_const_119"]),
	Pause(18),
	StopSound(),
	Pause(140),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=14, y=30)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=13, y=33)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=14, y=36)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=12, y=31)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=15, y=36)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftToXYCoords(x=14, y=33)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=16, y=36)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShiftToXYCoords(x=15, y=33)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	SetSyncActionScript(NPC_0, A0589_EMPTY),
	Pause(3),
	SetSyncActionScript(NPC_1, A0589_EMPTY),
	Pause(3),
	SetSyncActionScript(NPC_2, A0589_EMPTY),
	Pause(3),
	SetSyncActionScript(NPC_3, A0589_EMPTY),
	Pause(3),
	PlaySound(sound=SO064_SPINNING_COPTERS, channel=6),
	SetSyncActionScript(NPC_4, A0589_EMPTY),
	Pause(3),
	SetSyncActionScript(NPC_5, A0589_EMPTY),
	Pause(3),
	SetSyncActionScript(NPC_6, A0589_EMPTY),
	Pause(3),
	SetSyncActionScript(NPC_7, A0589_EMPTY),
	Pause(120),
	SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
	SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
	SetAsyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	DeactivateSoundChannels([0, 1, 2, 3]),
	PlayMusicAtDefaultVolume(M0017_TADPOLEPOND),
	DeactivateSoundChannels([0, 1, 2, 3]),
	ClearBit(UNKNOWN_7093_0),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	ClearBit(TEMP_7043_5),
	ClearBit(TEMP_7043_6),
	ClearBit(TEMP_7043_7),
	Return(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1078_play_sound_126"], identifier="EVENT_1078_jmp_if_var_equals_const_119"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1078_play_sound_128"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1078_play_sound_130"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1078_play_sound_132"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1078_play_sound_134"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1078_play_sound_136"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1078_play_sound_138"]),
	PlaySound(sound=SO136_TOADOFSKY_COMPOSITION_DO, channel=6, identifier="EVENT_1078_play_sound_126"),
	Return(),
	PlaySound(sound=SO137_TOADOFSKY_COMPOSITION_RE, channel=6, identifier="EVENT_1078_play_sound_128"),
	Return(),
	PlaySound(sound=SO138_TOADOFSKY_COMPOSITION_MI, channel=6, identifier="EVENT_1078_play_sound_130"),
	Return(),
	PlaySound(sound=SO139_TOADOFSKY_COMPOSITION_FA, channel=6, identifier="EVENT_1078_play_sound_132"),
	Return(),
	PlaySound(sound=SO140_TOADOFSKY_COMPOSITION_SO, channel=6, identifier="EVENT_1078_play_sound_134"),
	Return(),
	PlaySound(sound=SO141_TOADOFSKY_COMPOSITION_LA, channel=6, identifier="EVENT_1078_play_sound_136"),
	Return(),
	PlaySound(sound=SO142_TOADOFSKY_COMPOSITION_TI, channel=6, identifier="EVENT_1078_play_sound_138"),
	Return(),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_1078_jmp_if_bit_clear_143"], identifier="EVENT_1078_jmp_if_bit_clear_140"),
	SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_1078_jmp_if_bit_clear_146"], identifier="EVENT_1078_jmp_if_bit_clear_143"),
	SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_1078_jmp_if_bit_clear_149"], identifier="EVENT_1078_jmp_if_bit_clear_146"),
	SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_1078_jmp_if_bit_clear_152"], identifier="EVENT_1078_jmp_if_bit_clear_149"),
	SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_1078_jmp_if_bit_clear_155"], identifier="EVENT_1078_jmp_if_bit_clear_152"),
	SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_1078_jmp_if_bit_clear_158"], identifier="EVENT_1078_jmp_if_bit_clear_155"),
	SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_6, ["EVENT_1078_jmp_if_bit_clear_161"], identifier="EVENT_1078_jmp_if_bit_clear_158"),
	SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_1078_ret_164"], identifier="EVENT_1078_jmp_if_bit_clear_161"),
	SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
	Pause(5),
	Return(identifier="EVENT_1078_ret_164")
])
