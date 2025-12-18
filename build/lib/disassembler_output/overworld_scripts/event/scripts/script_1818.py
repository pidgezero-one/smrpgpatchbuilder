# E1818_LANDS_END_DESERT_MOUSE

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
	JmpIfMarioOnAnObjectOrNot(['EVENT_1818_play_sound_13', 'EVENT_1818_jmp_if_bit_set_1']),
	JmpIfBitSet(DODO_PRESENT_IN_NIMBUS_HALL, ["EVENT_1818_run_dialog_5"], identifier="EVENT_1818_jmp_if_bit_set_1"),
	RunDialog(dialog_id=DI1284_DUPLICATE, above_object=BOWSER, closable=False, sync=False, multiline=True, use_background=False),
	SetBit(DODO_PRESENT_IN_NIMBUS_HALL),
	Jmp(["EVENT_1818_run_dialog_duration_6"]),
	RunDialog(dialog_id=DI1285_EMPTY, above_object=BOWSER, closable=False, sync=False, multiline=True, use_background=False, identifier="EVENT_1818_run_dialog_5"),
	RunDialogForDuration(dialog_id=DI1272_EMPTY, duration=1, sync=False, identifier="EVENT_1818_run_dialog_duration_6"),
	JmpIfDialogOptionBSelected(["EVENT_1818_run_dialog_10"]),
	RunDialog(dialog_id=DI1274_WHIRLPOOL_INSTRUCTIONS, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_1818_action_queue_11"]),
	RunDialog(dialog_id=DI1273_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_1818_run_dialog_10"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetAllSpeeds(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_JumpToHeight(108),
		A_WalkSoutheastSteps(3),
		A_WalkEastSteps(7),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	], identifier="EVENT_1818_action_queue_11"),
	Return(),
	PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6, identifier="EVENT_1818_play_sound_13"),
	RunDialog(dialog_id=DI1275_JUMP_ON_LANDS_END_MOUSE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
