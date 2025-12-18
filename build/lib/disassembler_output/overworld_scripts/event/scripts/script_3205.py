# E3205_EMPTY

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
	JmpIfBitClear(UNUSED_7056_4, ["EVENT_3205_ret_27"]),
	JmpIfBitSet(UNUSED_7057_3, ["EVENT_3205_ret_27"]),
	EnterArea(room_id=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, face_direction=SOUTHWEST, x=27, y=86, z=0),
	RemoveObjectFromCurrentLevel(MARIO),
	JmpIfObjectNotInSpecificLevel(NPC_6, R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, ["EVENT_3205_run_event_as_subroutine_7"]),
	PauseActionScript(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_6),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3205_run_event_as_subroutine_7"),
	Set70107015ToObjectXYZ(target=MARIO),
	StartLoopNTimes(7),
	CreatePacketAt7010(packet=P024_REGULAR_SOUND_EXPLOSION, destinations=["EVENT_3205_pause_13"]),
	AddConstToVar(Z_COORD_1, 32),
	Pause(4),
	Pause(4, identifier="EVENT_3205_pause_13"),
	EndLoop(),
	ApplyTileModToLevel(use_alternate=True, room_id=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, mod_id=32),
	ApplySolidityModToLevel(permanent=True, room_id=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, mod_id=0),
	SetBit(UNUSED_7057_3),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_TransferToXYZF(x=26, y=87, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SequencePlaybackOn(),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=24, y=96),
		A_WalkToXYCoords(x=22, y=100),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_TransferToXYZF(x=26, y=87, z=0, direction=EAST),
		A_Pause(40),
		A_VisibilityOn(),
		A_SequencePlaybackOn(),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=24, y=96),
		A_WalkToXYCoords(x=22, y=100),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_TransferToXYZF(x=26, y=87, z=0, direction=EAST),
		A_Pause(70),
		A_VisibilityOn(),
		A_SequencePlaybackOn(),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=24, y=96),
		A_WalkToXYCoords(x=22, y=100),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_TransferToXYZF(x=26, y=87, z=0, direction=EAST),
		A_Pause(90),
		A_VisibilityOn(),
		A_SequencePlaybackOn(),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=24, y=96),
		A_WalkToXYCoords(x=22, y=100),
		A_VisibilityOff()
	]),
	SummonObjectToCurrentLevel(MARIO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Walk1StepSouthwest(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetVarToConst(MINES_MIDBOSS_POSITION, 19),
	JmpIfObjectNotInSpecificLevel(NPC_6, R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, ["EVENT_3205_ret_27"]),
	SetSyncActionScript(NPC_6, A0726_MINES_FIREBALLS),
	Return(identifier="EVENT_3205_ret_27")
])
