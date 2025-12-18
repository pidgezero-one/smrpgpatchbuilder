# E3826_EMPTY

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
	RunDialog(dialog_id=DI2514_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=2, y=64),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_VisibilityOff(),
		A_TransferToXYZF(x=2, y=64, z=0, direction=EAST),
		A_TransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceNortheast()
	]),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3826_inc_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3826_set_var_to_const_17"]),
	Inc(TEMP_70AE),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=12, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2205_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3729_action_queue_147"]),
	Inc(TEMP_70AE, identifier="EVENT_3826_inc_10"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceSoutheast(),
		A_Pause(2),
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2215_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties(),
		A_Pause(60),
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=26, y=80, z=0, direction=EAST)
	]),
	Pause(60),
	Jmp(["EVENT_3729_remember_last_object_149"]),
	SetVarToConst(TEMP_70AE, 0, identifier="EVENT_3826_set_var_to_const_17"),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_Pause(2),
		A_FaceSoutheast()
	]),
	SetSyncActionScript(NPC_6, A0629_EMPTY),
	Pause(30),
	RunDialog(dialog_id=DI2289_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_3826_action_queue_23_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_3826_action_queue_23_SUBSCRIPT_pause_2"]),
		A_Pause(60),
		A_ResetProperties()
	]),
	Pause(30),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	PauseActionScript(NPC_6),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkNorthwestPixels(4),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=6, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(2),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=4, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartSyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastPixels(2),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(2),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(2),
		A_TransferToXYZF(x=26, y=80, z=0, direction=EAST)
	]),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouth()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
