# E3723_NIMBUS_CASTLE_OUTER_CELLAR_GIFT_GUARD

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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 107, ["EVENT_3723_run_dialog_73"]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_3723_run_dialog_19"]),
	JmpIfBitSet(RED_CELLAR_GUARD_ITEM_GRANTED, ["EVENT_3723_run_dialog_71"]),
	SetVarToConst(TEMP_70AE, 16),
	RunDialog(dialog_id=DI3649_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_3723_pause_65"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI3650_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	SetVarToConst(ITEM_ID, CastleKey1Item, identifier="EVENT_3723_set_var_to_const_11"),
	SetVarToConst(PRIMARY_TEMP_7000, 3660),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	SetBit(RED_CELLAR_GUARD_ITEM_GRANTED),
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	RunDialog(dialog_id=DI3652_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3723_run_dialog_19"),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_3723_run_dialog_25"]),
	Inc(TEMP_70AF),
	CopyVarToVar(from_var=TEMP_70AF, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsLesser(["EVENT_3584_ret_0"]),
	RunDialog(dialog_id=DI3653_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3723_run_dialog_25"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=27, y=80),
		A_FaceWest()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSouthwest(),
		A_VisibilityOff(),
		A_TransferToXYZF(x=27, y=80, z=0, direction=EAST),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(4),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	SetSyncActionScript(NPC_8, A0025_EMPTY),
	Pause(10),
	RunDialog(dialog_id=DI3654_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	PauseActionScript(NPC_8),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3655_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_Pause(30),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3656_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3657_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties(),
		A_FaceEast(),
		A_Pause(2),
		A_FaceNortheast(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3658_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3650_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3659_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=26, y=16, z=0, direction=EAST)
	]),
	Pause(10),
	Jmp(["EVENT_3723_set_var_to_const_11"]),
	Pause(10, identifier="EVENT_3723_pause_65"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	RunDialog(dialog_id=DI3651_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_704C_0),
	Return(),
	RunDialog(dialog_id=DI3648_NEED_CASTLE_KEY_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3723_run_dialog_71"),
	Return(),
	RunDialog(dialog_id=DI3761_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3723_run_dialog_73"),
	Return()
])
