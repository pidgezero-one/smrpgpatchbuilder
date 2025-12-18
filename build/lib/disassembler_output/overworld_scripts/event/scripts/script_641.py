# E0641_MARRYMORE_ANTECHAMBER_LOADER_EXTENSION

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
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_TransferXYZFPixels(x=0, y=3, z=0, direction=EAST)
	]),
	JmpIfBitSet(CHAPEL_ITEM_RETRIEVAL_STARTED, ["EVENT_641_apply_solidity_mod_17"]),
	JmpIfBitClear(SANCTUARY_LOCKED, ["EVENT_641_jmp_if_bit_set_6"], identifier="EVENT_641_jmp_if_bit_clear_2"),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_641_jmp_if_bit_set_6"]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=18, y=19, z=0, direction=EAST)
	]),
	SetSyncActionScript(NPC_3, A0031_EMPTY),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_641_run_event_as_subroutine_15"], identifier="EVENT_641_jmp_if_bit_set_6"),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_256_ret_0"]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=18, y=20, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(12),
		A_WalkToXYCoords(x=18, y=19),
		A_FaceSouthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2076_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_3, A0031_EMPTY),
	SetBit(SANCTUARY_LOCKED),
	Return(),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_641_run_event_as_subroutine_15"),
	Return(),
	ApplySolidityModToLevel(permanent=True, room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, mod_id=0, identifier="EVENT_641_apply_solidity_mod_17"),
	Jmp(["EVENT_641_jmp_if_bit_clear_2"])
])
