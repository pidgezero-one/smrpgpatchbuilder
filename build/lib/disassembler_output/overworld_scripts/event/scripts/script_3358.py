# E3358_KEEP_BALL_SOLITAIRE_LOADER

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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShiftXYPixels(x=250, y=253),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(9)
	]),
	SetVarToConst(ROSE_WAY_703E, 15),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=DI1912_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3358_set_bit_9"]),
	RunDialog(dialog_id=DI1913_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_7, identifier="EVENT_3358_set_bit_9"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, looping=False),
		A_Pause(38)
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ReturnAll()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthwestSteps(9)
	]),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	Return()
])
