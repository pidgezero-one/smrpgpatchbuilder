# E0744_NIMBUS_LAND_LIBERATED_CASTLE_INNER_CELLAR_REWARD

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
	JmpIfBitSet(NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED, ["EVENT_744_run_dialog_53"]),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	RunDialog(dialog_id=DI0052_EMPTY, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=28, y=52),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSouthwest(),
		A_FaceNorth()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=27, y=53, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_Pause(12),
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(12),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_Pause(16),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceSoutheast(),
		A_SetWalkingSpeed(VERY_FAST),
		A_SequenceLoopingOff(),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SequenceLoopingOn()
	]),
	RunDialog(dialog_id=DI0053_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0054_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI0055_EMPTY, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI0056_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI0057_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI0058_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(32),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthwestPixels(6),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(24),
	RunDialog(dialog_id=DI0059_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(30),
		A_ResetProperties(),
		A_FaceNorthwest()
	]),
	Pause(10),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW),
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW),
		A_Pause(60),
		A_FaceSouthwest(),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(30),
	RunDialog(dialog_id=DI0060_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, FlowerJarItem),
	SetVarToConst(PRIMARY_TEMP_7000, 524),
	RunEventAsSubroutine(E3828_GRANT_ITEM_FLOWER_SOUND),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestPixels(6),
		A_TransferToXYZF(x=37, y=66, z=0, direction=EAST)
	]),
	RememberLastObject(),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED),
	ResumeActionScript(NPC_1),
	ResumeActionScript(NPC_2),
	Return(),
	RunDialog(dialog_id=DI0061_NIMBUS_NPC_AFTER_GIVING_YOU_FINAL_CELLAR_PRIZE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_744_run_dialog_53"),
	Return()
])
