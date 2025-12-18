# E4014_CLONE_RESERVED

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
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=6, y=16),
		A_DecZCoord1Step(),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=5, y=14),
		A_VisibilityOn(),
		A_FaceSoutheast()
	]),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(UNKNOWN_709D_5, ["EVENT_4014_set_action_script_20"]),
	RunDialog(dialog_id=DI2228_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, looping=True),
		A_Pause(10),
		A_PlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=6),
		A_SetSpriteSequence(index=7, is_mold=True, looping=True),
		A_Pause(35),
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI2229_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=4, looping=False, mirror_sprite=True),
		A_PlaySound(sound=SO101_TERRAPIN_ATTACK, channel=6),
		A_Pause(60)
	]),
	RunDialog(dialog_id=DI1242_UNUSED_DEFAULT_FORTUNE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastSteps(3),
		A_FaceEast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkToXYCoords(x=5, y=9),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI0695_WHAT_DID_YOU_FIND, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_709D_5),
	RunDialog(dialog_id=DI0815_JUST_YOU_WAIT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_4014_run_dialog_18"]),
	JmpToEvent(E4015_CLONE_RESERVED),
	Return(),
	RunDialog(dialog_id=DI2236_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_4014_run_dialog_18"),
	Return(),
	SetSyncActionScript(NPC_0, A0200_COIN_SNAKE_TAIL, identifier="EVENT_4014_set_action_script_20"),
	SetSyncActionScript(NPC_1, A0199_COIN_SNAKE_HEAD),
	Return()
])
