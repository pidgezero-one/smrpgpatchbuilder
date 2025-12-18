# E3148_ROSE_WAY_MAIN_ROOM_LOADER

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
	SetBit(TEMP_707C_1),
	SummonObjectToSpecificLevel(NPC_1, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_2, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_3, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SummonObjectToSpecificLevel(NPC_4, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
	SetVarToConst(ROSE_WAY_7038, 0),
	SetVarToConst(ROSE_WAY_703A, 0),
	SetVarToConst(ROSE_WAY_703C, 0),
	SetVarToConst(ROSE_WAY_703E, 0),
	JmpIfObjectNotInSpecificLevel(NPC_7, R079_ROSE_WAY_MAIN_AREA, ["EVENT_3148_jmp_if_object_not_in_level_11"]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	JmpIfObjectNotInSpecificLevel(NPC_8, R079_ROSE_WAY_MAIN_AREA, ["EVENT_3148_jmp_to_event_13"], identifier="EVENT_3148_jmp_if_object_not_in_level_11"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3148_jmp_to_event_13")
])
