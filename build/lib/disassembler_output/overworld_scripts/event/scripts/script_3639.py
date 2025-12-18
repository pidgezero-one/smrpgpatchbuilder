# E3639_EMPTY

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
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3639_jmp_if_bit_set_23"]),
	JmpIfBitSet(GARRO_SEQUENCE_COMPLETED, ["EVENT_3639_run_dialog_21"]),
	JmpIfBitSet(INVISIBLE_ITEMS_SUMMONED, ["EVENT_3639_action_queue_6"]),
	JmpIfBitSet(SHINY_STONE_TRADED, ["EVENT_3640_pause_4"]),
	RunDialog(dialog_id=DI2444_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=5, y=18),
		A_FaceNortheast()
	], identifier="EVENT_3639_action_queue_6"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2439_EMPTY, above_object=NPC_0, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3640_pause_205"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2442_DUPLICATE, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	ClearBit(INVISIBLE_ITEMS_SUMMONED),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepEast(),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2443_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_3640_set_bit_11"]),
	RunDialog(dialog_id=DI3672_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3639_run_dialog_21"),
	Return(),
	JmpIfBitSet(UNKNOWN_7084_2, ["EVENT_3639_run_dialog_43"], identifier="EVENT_3639_jmp_if_bit_set_23"),
	SetBit(UNKNOWN_7084_2),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=4, y=22)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepNortheast(),
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_Pause(8),
		A_TransferToXYZF(x=4, y=22, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestPixels(8),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3783_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI3784_EMPTY, above_object=NPC_9, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI3785_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3786_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(30),
		A_WalkNortheastPixels(12),
		A_TransferToXYZF(x=28, y=85, z=4, direction=EAST)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	RunDialog(dialog_id=DI3787_DODO_MINIGAME_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3639_run_dialog_43"),
	Return()
])
