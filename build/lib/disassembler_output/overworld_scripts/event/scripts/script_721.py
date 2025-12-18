# E0721_PEACHS_GRANDMA

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
	JmpIfBitSet(UNKNOWN_7063_4, ["EVENT_721_run_dialog_33"]),
	JmpIfBitSet(UNKNOWN_709C_2, ["EVENT_721_jmp_if_bit_clear_6"]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ResetProperties(),
		A_FaceMario()
	]),
	RunDialog(dialog_id=DI0732_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	Return(),
	JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_721_action_queue_35"], identifier="EVENT_721_jmp_if_bit_clear_6"),
	SetBit(UNKNOWN_7063_4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_WalkToXYCoords(x=4, y=59),
		A_FaceNorth(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOn()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=4, y=59, z=2, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0733_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(2),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_Pause(4),
		A_TransferToXYZF(x=4, y=57, z=2, direction=EAST)
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI2304_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(10),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(60),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI0734_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0888_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(60),
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=16, y=66, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_TransferToXYZF(x=16, y=66, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(10),
		A_FaceSouth()
	]),
	Return(),
	RunDialog(dialog_id=DI0735_BOWSETTE_COSTUME, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_721_run_dialog_33"),
	Return(),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ResetProperties(),
		A_ObjectMemorySetBit(arg_1=0x08, bits=[4]),
		A_FaceMario(),
		A_Pause(2),
		A_VisibilityOff()
	], identifier="EVENT_721_action_queue_35"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(2),
		A_TransferToXYZF(x=4, y=57, z=2, direction=EAST),
		A_FaceMario()
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2305_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_TransferToXYZF(x=12, y=85, z=0, direction=EAST)
	]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_FaceNorthwest(),
		A_Pause(2),
		A_VisibilityOn()
	]),
	RememberLastObject(),
	Return()
])
