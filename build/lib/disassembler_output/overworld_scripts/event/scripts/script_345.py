# E0345_MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_GUARD

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
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_345_run_dialog_23"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_5, ["EVENT_345_run_dialog_4"]),
	RunDialog(dialog_id=DI0715_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0718_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_345_run_dialog_4"),
	JmpIfDialogOptionBSelected(["EVENT_345_pause_15"]),
	Pause(10),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0719_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xfd$\x00\x10')),
		A_Mem700CAndConst(0x00C0),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_345_action_queue_13_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["EVENT_345_action_queue_13_SUBSCRIPT_set_sprite_sequence_6"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["EVENT_345_action_queue_13_SUBSCRIPT_set_sprite_sequence_6"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["EVENT_345_action_queue_13_SUBSCRIPT_set_sprite_sequence_12"]),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_345_action_queue_13_SUBSCRIPT_set_sprite_sequence_6"),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Jmp(["EVENT_345_action_queue_13_SUBSCRIPT_pause_17"]),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_345_action_queue_13_SUBSCRIPT_set_sprite_sequence_12"),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60, identifier="EVENT_345_action_queue_13_SUBSCRIPT_pause_17"),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouth(),
		A_ResetProperties()
	]),
	Return(),
	Pause(10, identifier="EVENT_345_pause_15"),
	RunDialog(dialog_id=DI0720_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Return(),
	RunDialog(dialog_id=DI2320_TOADSTOOL_ROOM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_345_run_dialog_23"),
	Return()
])
