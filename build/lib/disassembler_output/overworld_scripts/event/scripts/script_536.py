# E0536_EMPTY

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
	JmpIfBitSet(UNKNOWN_7061_3, ["EVENT_536_run_event_as_subroutine_15"], identifier="EVENT_536_jmp_if_bit_set_0"),
	SetBit(UNKNOWN_7061_3),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	RunDialog(dialog_id=DI0795_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_536_pause_20"]),
	Pause(10, identifier="EVENT_536_pause_5"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xfd$\x00\x10')),
		A_Mem700CAndConst(0x00C0),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_6"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_8"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_10"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_12"]),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_6"),
		A_Jmp(["EVENT_536_action_queue_6_SUBSCRIPT_pause_13"]),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, identifier="EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_8"),
		A_Jmp(["EVENT_536_action_queue_6_SUBSCRIPT_pause_13"]),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_10"),
		A_Jmp(["EVENT_536_action_queue_6_SUBSCRIPT_pause_13"]),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, identifier="EVENT_536_action_queue_6_SUBSCRIPT_set_sprite_sequence_12"),
		A_Pause(60, identifier="EVENT_536_action_queue_6_SUBSCRIPT_pause_13"),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0798_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(FOREST_MAZE_SECRET_FOUND, ["EVENT_529_action_queue_58"]),
	SetBit(UNKNOWN_ROSE_TOWN_7060_5),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_6),
	ClearBit(UNKNOWN_ROSE_TOWN_7060_7),
	SetBit(UNUSED_7061_0),
	Return(),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_536_run_event_as_subroutine_15"),
	JmpIfBitSet(UNUSED_7061_0, ["EVENT_534_jmp_if_bit_set_0"]),
	RunDialog(dialog_id=DI0805_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_536_pause_20"]),
	Jmp(["EVENT_536_pause_5"]),
	Pause(10, identifier="EVENT_536_pause_20"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0804_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
