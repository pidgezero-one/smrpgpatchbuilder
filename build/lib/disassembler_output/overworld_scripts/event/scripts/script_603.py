# E0603_MARRYMORE_BELLHOP_LOBBY_WHILE_GUEST

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
	JmpIfBitSet(TEMP_704C_0, ["EVENT_603_run_dialog_42"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_603_run_dialog_6"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_603_run_dialog_44"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_321_inc_0"]),
	RunDialog(dialog_id=DI0979_INACTIVE_BELLHOP, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0992_GOOD_MORNING_FROM_BELLHOP, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_6"),
	JmpIfDialogOptionBSelected(["EVENT_603_pause_35"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI0994_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(TEMP_7042_7, ["EVENT_603_run_dialog_17"]),
	RunDialog(dialog_id=DI0996_DROP_BY_AGAIN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_1),
	SetSyncActionScript(NPC_5, A0322_MARRYMORE_INNKEEPER_OVERSTAY_MAKES_YOU_WORK),
	Return(),
	RunDialog(dialog_id=DI0995_BELLHOP_GIFT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_17"),
	Pause(10),
	JmpIfRandom2of3(['EVENT_603_set_var_to_const_24', 'EVENT_603_set_var_to_const_28']),
	SetVarToConst(ITEM_ID, MidMushroomItem),
	JmpToSubroutine(["EVENT_603_play_sound_32"]),
	AddToInventory(MidMushroomItem),
	Jmp(["EVENT_603_set_bit_39"]),
	SetVarToConst(ITEM_ID, MaxMushroomItem, identifier="EVENT_603_set_var_to_const_24"),
	JmpToSubroutine(["EVENT_603_play_sound_32"]),
	AddToInventory(MaxMushroomItem),
	Jmp(["EVENT_603_set_bit_39"]),
	SetVarToConst(ITEM_ID, PickMeUpItem, identifier="EVENT_603_set_var_to_const_28"),
	JmpToSubroutine(["EVENT_603_play_sound_32"]),
	AddToInventory(PickMeUpItem),
	Jmp(["EVENT_603_set_bit_39"]),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_603_play_sound_32"),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Return(),
	Pause(10, identifier="EVENT_603_pause_35"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	RunDialog(dialog_id=DI0993_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_1, identifier="EVENT_603_set_bit_39"),
	SetSyncActionScript(NPC_5, A0322_MARRYMORE_INNKEEPER_OVERSTAY_MAKES_YOU_WORK),
	Return(),
	RunDialog(dialog_id=DI1006_BELLHOP_WHILE_PLAYER_EMPLOYED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_42"),
	Return(),
	RunDialog(dialog_id=DI0969_MAKE_YOURSELF_AT_HOME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_603_run_dialog_44"),
	Return()
])
