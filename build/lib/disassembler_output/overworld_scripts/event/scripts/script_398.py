# E0398_EMPTY

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
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_398_run_dialog_11"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_398_jmp_if_bit_set_13"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_5, ["EVENT_398_jmp_if_bit_set_5"]),
	RunDialog(dialog_id=DI0688_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_398_run_dialog_11"], identifier="EVENT_398_jmp_if_bit_set_5"),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_398_run_dialog_9"]),
	RunDialog(dialog_id=DI0722_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0723_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_398_run_dialog_9"),
	Return(),
	RunDialog(dialog_id=DI0731_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_398_run_dialog_11"),
	Return(),
	JmpIfBitSet(FIREWORKS_HOUSE_ITEM_SOLD, ["EVENT_398_run_dialog_32"], identifier="EVENT_398_jmp_if_bit_set_13"),
	SetBit(FIREWORKS_HOUSE_ITEM_SOLD),
	RunDialog(dialog_id=DI0688_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=3, y=65),
		A_Walk1StepSouthwest(),
		A_FaceNorth()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=3, y=66, z=0, direction=EAST),
		A_WalkNortheastPixels(4),
		A_VisibilityOn(),
		A_WalkNortheastPixels(12),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2323_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2324_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunDialog(dialog_id=DI2325_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2326_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=16, y=66, z=0, direction=EAST)
	]),
	Return(),
	RunDialog(dialog_id=DI2327_MARRYMORE_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_398_run_dialog_32"),
	Return()
])
