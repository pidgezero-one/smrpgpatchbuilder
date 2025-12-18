# E2586_BOOSTER_PASS_APPRENTICE_FIGHT

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
	CopyVarToVar(from_var=APPRENTICE_LOSS_COUNTER, to_var=PRIMARY_TEMP_7000),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetPriority(3)
	]),
	JmpIfBitSet(UNUSED_708D_7, ["EVENT_2586_run_dialog_5"]),
	RunDialog(dialog_id=DI3088_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2586_start_battle_6"]),
	RunDialog(dialog_id=DI3091_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2586_run_dialog_5"),
	StartBattleAtBattlefield(PACK151_APPRENTICE_FIGHT, BF10_MOUNTAINS, identifier="EVENT_2586_start_battle_6"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2586_set_temp_action_script_14"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2586_stop_music_FD9F_17"]),
	FadeInFromBlack(sync=False),
	SetBit(UNUSED_708D_7),
	RunDialog(dialog_id=DI3089_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetAsyncActionScript(NPC_9, A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT),
	Return(),
	SetTempSyncActionScript(NPC_9, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_2586_set_temp_action_script_14"),
	FadeInFromBlack(sync=False),
	Return(),
	StopMusicFD9F(identifier="EVENT_2586_stop_music_FD9F_17"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_FaceSouthwest()
	]),
	ClearBit(UNUSED_708D_7),
	CopyVarToVar(from_var=APPRENTICE_LOSS_COUNTER, to_var=PRIMARY_TEMP_7000),
	FadeInFromBlack(sync=False),
	RunDialog(dialog_id=DI3090_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetAsyncActionScript(NPC_9, A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT),
	Inc(APPRENTICE_LOSS_COUNTER),
	CopyVarToVar(from_var=APPRENTICE_LOSS_COUNTER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2586_summon_to_level_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2586_summon_to_level_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2586_summon_to_level_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2586_summon_to_level_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2586_summon_to_level_43"]),
	Pause(16, identifier="EVENT_2586_pause_31"),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	SummonObjectToSpecificLevel(NPC_0, R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, identifier="EVENT_2586_summon_to_level_35"),
	Jmp(["EVENT_2586_pause_31"]),
	SummonObjectToSpecificLevel(NPC_1, R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, identifier="EVENT_2586_summon_to_level_37"),
	Jmp(["EVENT_2586_pause_31"]),
	SummonObjectToSpecificLevel(NPC_2, R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, identifier="EVENT_2586_summon_to_level_39"),
	Jmp(["EVENT_2586_pause_31"]),
	SummonObjectToSpecificLevel(NPC_3, R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, identifier="EVENT_2586_summon_to_level_41"),
	Jmp(["EVENT_2586_pause_31"]),
	SummonObjectToSpecificLevel(NPC_4, R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, identifier="EVENT_2586_summon_to_level_43"),
	RemoveObjectFromSpecificLevel(NPC_9, R405_BOOSTER_PASS_SECRET),
	Jmp(["EVENT_2586_pause_31"])
])
