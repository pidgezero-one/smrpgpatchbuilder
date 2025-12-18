# E3830_MUSHROOM_KINGDOM_SHOP_CELLAR_NPC

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
	JmpIfBitSet(BUCKET_WARP_ENABLED, ["EVENT_3830_run_dialog_12"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_3830_run_dialog_14"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3830_run_dialog_6"]),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3830_action_queue_5"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=16, y=42),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=15, y=43),
		A_JmpIfBitClear(TEMP_7043_1, ["EVENT_3830_action_queue_5_SUBSCRIPT_face_northwest_5"]),
		A_FaceNortheast(),
		A_Jmp(["EVENT_3830_run_dialog_6"]),
		A_FaceNorthwest(identifier="EVENT_3830_action_queue_5_SUBSCRIPT_face_northwest_5")
	], identifier="EVENT_3830_action_queue_5"),
	RunDialog(dialog_id=DI3745_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3830_run_dialog_6"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceNorthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ClearBit(TEMP_7043_1),
	SetBit(TEMP_7043_2),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	RunDialog(dialog_id=DI3748_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3830_run_dialog_12"),
	Return(),
	RunDialog(dialog_id=DI3746_RARE_FROG_COIN_HINT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3830_run_dialog_14"),
	Return()
])
