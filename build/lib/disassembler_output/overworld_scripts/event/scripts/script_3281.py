# E3281_SHIP_UPPER_HENCHMAN_ROOM_LOADER

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
	JmpIfBitSet(SHIP_PRE_BOSS_BATTLE_2_CLEARED, ["EVENT_3281_run_event_as_subroutine_3"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=13, y=114)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=13, y=116)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3281_run_event_as_subroutine_3"),
	JmpIfBitSet(SHIP_PRE_BOSS_BATTLE_2_CLEARED, ["EVENT_3281_ret_25"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=15, y=121),
		A_SequenceLoopingOn(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI1692_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=15, y=120),
		A_SequenceLoopingOn(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI1693_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	StartBattleAtBattlefield(PACK069_BANDANA_REDS_2, BF04_SUNKEN_SHIP),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3281_run_event_at_return_26"]),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_FixedFCoordOn(),
		A_SequenceLoopingOff(),
		A_Walk1StepNortheast(),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_SequenceLoopingOff(),
		A_Walk1StepSoutheast(),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI1694_FINAL_SHIP_HENCHMEN_DEFEATED, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNortheastSteps(2)
	]),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, mod_id=0),
	SetBit(TEMP_7043_0),
	SetBit(SHIP_PRE_BOSS_BATTLE_2_CLEARED),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Walk1StepNorthwest(),
		A_FaceSoutheast()
	]),
	Return(identifier="EVENT_3281_ret_25"),
	RunEventAtReturn(E3306_SHIP_LOWER_HENCHMAN_ROOM_LOADER_CONTINUED, identifier="EVENT_3281_run_event_at_return_26"),
	Return()
])
