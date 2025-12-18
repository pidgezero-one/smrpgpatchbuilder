# E2066_DOJO_BOSS_1

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
	JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2066_jmp_if_bit_set_37"]),
	JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["EVENT_2066_run_dialog_35"]),
	RunDialog(dialog_id=DI3033_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2066_run_dialog_33"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=5, y=16),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3035_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	FreezeCamera(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkNortheastSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_PlaySound(sound=SO101_TERRAPIN_ATTACK, channel=6),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_Pause(45)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkSouthwestSteps(1),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=False),
		A_Pause(45)
	]),
	StartBattleAtBattlefield(PACK189_JAGGER_FIGHT_STATIC, BF46_JINXS_DOJO),
	RestoreAllHP(),
	RestoreAllFP(),
	JmpIfBitSet(GAME_OVER, ["EVENT_2066_fade_in_from_black_async_17"]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2066_fade_in_from_black_async_17"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=6, y=8, z=3, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_2066_fade_in_from_black_async_17"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkSouthwestSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(70),
		A_ResetProperties(),
		A_FaceNortheast(),
		A_FixedFCoordOff(),
		A_Pause(30),
		A_SetAllSpeeds(SLOW),
		A_WalkNortheastSteps(1),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(NORMAL)
	]),
	UnfreezeCamera(),
	Pause(30),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2066_run_dialog_31"]),
	JmpIfBitClear(GAME_OVER, ["EVENT_2066_run_dialog_29"]),
	StopMusicFDA2(),
	FadeOutMusicToVolume(duration=0, volume=100),
	PlayMusicAtDefaultVolume(M0051_MONSTROTOWN),
	RunDialog(dialog_id=DI3036_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3037_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2066_run_dialog_29"),
	Jmp(["EVENT_2066_run_dialog_43"]),
	RunDialog(dialog_id=DI2592_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_31"),
	Return(),
	RunDialog(dialog_id=DI3034_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_33"),
	Return(),
	RunDialog(dialog_id=DI3044_DOJO_BOSS_1_AFTER_DEFEAT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_35"),
	Return(),
	JmpIfBitSet(UNKNOWN_709D_6, ["EVENT_2066_run_dialog_43"], identifier="EVENT_2066_jmp_if_bit_set_37"),
	JmpIfBitSet(UNKNOWN_709D_5, ["EVENT_2066_run_dialog_41"]),
	RunDialog(dialog_id=DI3352_DOJO_BOSS_1_FULLY_DEFEATED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0592_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_41"),
	Return(),
	RunDialog(dialog_id=DI3682_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2066_run_dialog_43"),
	Return()
])
