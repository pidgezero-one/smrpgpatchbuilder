# E4015_CLONE_RESERVED

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
	RunDialog(dialog_id=DI2661_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartBattleAtBattlefield(PACK248_AXEM_BLACK_ALONE, BF46_JINXS_DOJO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=5, y=18),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, looping=True)
	]),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(GAME_OVER, ["EVENT_4015_run_dialog_27"]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_4015_run_dialog_25"]),
	RunDialog(dialog_id=DI2672_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetSyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	AddToInventory(BombItem),
	SetVarToConst(ITEM_ID, BombItem),
	RunDialog(dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE, above_object=MEM_70A8, closable=False, sync=True, multiline=False, use_background=False),
	Pause(100),
	CloseDialog(),
	Pause(1, identifier="EVENT_4015_pause_15"),
	JmpIfObjectActionScriptIsRunning(MARIO, ["EVENT_4015_pause_15"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, is_mold=True, looping=True)
	]),
	RunDialog(dialog_id=DI2739_FROGFUCIUS_MINE_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkToXYCoords(x=5, y=14),
		A_FaceSoutheast()
	]),
	SetSyncActionScript(NPC_0, A0200_COIN_SNAKE_TAIL),
	SetSyncActionScript(NPC_1, A0199_COIN_SNAKE_HEAD),
	SetBit(UNKNOWN_709D_6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth()
	]),
	Return(),
	RunDialog(dialog_id=DI2237_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_4015_run_dialog_25"),
	Return(),
	RunDialog(dialog_id=DI2667_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_4015_run_dialog_27"),
	Return()
])
