# E1768_TEMPLE_BOSS

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
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_1768_run_dialog_2"]),
	JmpToEvent(E3002_CLONE_RESERVED),
	RunDialog(dialog_id=DI1231_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1768_run_dialog_2"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(50),
		A_ResetProperties(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, looping=False),
		A_Pause(30),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4),
		A_ShadowOff(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_FixedFCoordOn(),
		A_JumpToHeight(112),
		A_Pause(1, identifier="EVENT_1768_action_queue_3_SUBSCRIPT_pause_13"),
		A_JmpIfObjectInAir(NPC_4, ["EVENT_1768_action_queue_3_SUBSCRIPT_pause_13"])
	]),
	StartBattleAtBattlefield(PACK169_BELOME2_FIGHT_STATIC, BF42_BELOME_TEMPLE),
	SetBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	RemoveObjectFromCurrentLevel(NPC_1),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	SetVarToConst(TEMP_7034, 1),
	Set70107015ToObjectXYZ(target=NPC_0),
	StartLoopNTimes(2),
	Pause(1, identifier="EVENT_1768_pause_17"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1768_pause_17"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	EndLoop(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Return()
])
