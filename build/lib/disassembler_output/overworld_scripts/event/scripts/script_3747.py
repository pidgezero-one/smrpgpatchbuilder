# E3747_NIMBUS_HOT_SPRING_GUARDS

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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 22, ["EVENT_3747_jmp_if_bit_set_6"]),
	JmpIfBitSet(HOT_SPRING_GUARD_POSITION, ["EVENT_3747_run_dialog_40"], identifier="EVENT_3747_jmp_if_bit_set_2"),
	JmpIfBitSet(BUCKET_PRIZE_GRANT_NO_WARP, ["EVENT_3747_run_dialog_11"]),
	RunDialog(dialog_id=DI3675_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(HOT_SPRING_GUARD_POSITION, ["EVENT_3747_run_dialog_40"], identifier="EVENT_3747_jmp_if_bit_set_6"),
	JmpIfBitSet(BUCKET_PRIZE_GRANT_NO_WARP, ["EVENT_3747_run_dialog_11"]),
	JmpIfBitClear(NIMBUS_BOSS_IN_TOWN_SQUARE, ["EVENT_3747_jmp_if_bit_set_2"]),
	RunDialog(dialog_id=DI3676_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3705_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3747_run_dialog_11"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=19, y=54),
		A_WalkNorthwestPixels(4),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=19, y=54, z=0, direction=EAST),
		A_FaceNortheast(),
		A_TransferXYZFPixels(x=254, y=250, z=0, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_WalkNortheastPixels(14),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNorthwest()
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI3706_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3707_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI3708_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_FixedFCoordOff(),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff(),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI3709_HOT_SPRING_GUARD_AFTER_LIBERATION, above_object=NPC_2, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=18, y=82, z=0, direction=EAST)
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(HOT_SPRING_GUARD_POSITION),
	Return(),
	RunDialog(dialog_id=DI3710_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3747_run_dialog_40"),
	Return()
])
