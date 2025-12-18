# E2637_CASINO_GRATE_GUY

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
	SetVarToConst(TEMP_70AE, 20),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_2637_jmp_if_random_above_128_5"]),
	RunDialog(dialog_id=DI3318_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_1),
	Return(),
	JmpIfRandom1of2(["EVENT_2637_run_dialog_8"], identifier="EVENT_2637_jmp_if_random_above_128_5"),
	RunDialog(dialog_id=DI3320_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI3302_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_8"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOff()
	], identifier="EVENT_2637_action_queue_9"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_WalkToXYCoords(x=4, y=16),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3303_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3304_AWAIT_LEFT_OR_RIGHT, above_object=BOWSER, closable=False, sync=True, multiline=True, use_background=False),
	Set7000ToPressedButton(identifier="EVENT_2637_set_7000_to_pressed_button_13"),
	Pause(1),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2637_close_dialog_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2637_close_dialog_29"]),
	Jmp(["EVENT_2637_set_7000_to_pressed_button_13"]),
	CloseDialog(identifier="EVENT_2637_close_dialog_18"),
	RunDialog(dialog_id=DI3305_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfRandom1of2(["EVENT_2637_action_queue_26"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	Jmp(["EVENT_2637_play_sound_40"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	], identifier="EVENT_2637_action_queue_26"),
	UnsyncDialog(),
	Jmp(["EVENT_2637_play_sound_49"]),
	CloseDialog(identifier="EVENT_2637_close_dialog_29"),
	RunDialog(dialog_id=DI3305_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfRandom1of2(["EVENT_2637_action_queue_37"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	Jmp(["EVENT_2637_play_sound_49"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	], identifier="EVENT_2637_action_queue_37"),
	UnsyncDialog(),
	Jmp(["EVENT_2637_play_sound_40"]),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6, identifier="EVENT_2637_play_sound_40"),
	RunDialog(dialog_id=DI3306_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI3310_LOOK_THE_OTHER_WAY_RETRY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_2637_pause_138"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Jmp(["EVENT_2637_action_queue_9"]),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6, identifier="EVENT_2637_play_sound_49"),
	RunDialog(dialog_id=DI3307_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn()
	]),
	JmpIfBitSet(CASINO_PRIZE_WON, ["EVENT_2637_set_var_to_random_56"]),
	Inc(UNKNOWN_70EF),
	JmpIfVarEqualsConst(UNKNOWN_70EF, 100, ["EVENT_2637_run_dialog_132"]),
	SetVarToRandom(PRIMARY_TEMP_7000, 255, identifier="EVENT_2637_set_var_to_random_56"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2637_run_dialog_84"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2637_run_dialog_90"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2637_run_dialog_90"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2637_run_dialog_96"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2637_run_dialog_96"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2637_run_dialog_96"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2637_run_dialog_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2637_run_dialog_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2637_run_dialog_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2637_run_dialog_102"]),
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2637_run_dialog_108"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2637_run_dialog_114"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2637_run_dialog_114"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2637_run_dialog_114"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2637_run_dialog_120"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2637_run_dialog_120"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_2637_run_dialog_120"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2637_run_dialog_126"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_2637_run_dialog_126"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2637_run_dialog_126"]),
	Jmp(["EVENT_2637_run_dialog_108"]),
	RunDialog(dialog_id=DI3310_LOOK_THE_OTHER_WAY_RETRY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_79"),
	JmpIfDialogOptionBSelected(["EVENT_2637_pause_138"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Jmp(["EVENT_2637_action_queue_9"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_84"),
	SetVarToConst(ITEM_ID, RockCandyItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(RockCandyItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_90"),
	SetVarToConst(ITEM_ID, RoyalSyrupItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(RoyalSyrupItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_96"),
	SetVarToConst(ITEM_ID, RedEssenceItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(RedEssenceItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_102"),
	SetVarToConst(ITEM_ID, KerokeroColaItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(KerokeroColaItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_108"),
	SetVarToConst(ITEM_ID, MushroomItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(MushroomItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_114"),
	SetVarToConst(ITEM_ID, WiltShroomItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(WiltShroomItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_120"),
	SetVarToConst(ITEM_ID, RottenMushItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(RottenMushItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3183_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_126"),
	SetVarToConst(ITEM_ID, MoldyMushItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(MoldyMushItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	RunDialog(dialog_id=DI3308_LOOK_THE_OTHER_WAY_PRIZE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2637_run_dialog_132"),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	SetBit(CASINO_PRIZE_WON),
	RunDialog(dialog_id=DI3309_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(StarEggItem),
	Jmp(["EVENT_2637_run_dialog_79"]),
	Pause(10, identifier="EVENT_2637_pause_138"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI2408_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
