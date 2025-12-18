# E0642_MARRYMORE_ANTECHAMBER_ENTRANCE_REVERSE

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
	JmpIfBitSet(SANCTUARY_LOCKED, ["EVENT_642_pause_action_script_3"]),
	EnterArea(room_id=R152_MARRYMORE_CHAPEL_MAIN_HALL, face_direction=SOUTHWEST, x=6, y=27, z=3, z_add_half_unit=True, run_entrance_event=True),
	Return(),
	PauseActionScript(NPC_3, identifier="EVENT_642_pause_action_script_3"),
	StartAsyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2296_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=18, y=20),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkToXYCoords(x=18, y=19),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI2297_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_WalkSouthwestPixels(8),
		A_TransferToXYZF(x=21, y=42, z=0, direction=EAST)
	]),
	Pause(20),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	ClearBit(SANCTUARY_LOCKED),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_1),
	Return()
])
