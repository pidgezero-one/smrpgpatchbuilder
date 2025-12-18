# E0513_EMPTY

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
	Pause(60),
	EnterArea(room_id=R099_ROSE_TOWN_GENO_AWAKENS_IN_INN_1F, face_direction=SOUTH, x=4, y=17, z=0),
	StopMusic(),
	SummonObjectToCurrentLevel(NPC_3),
	ActionQueueSync(target=NPC_3, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOff(),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_TransferToXYZF(x=8, y=18, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SequenceLoopingOn(),
		A_TransferToXYZF(x=8, y=9, z=0, direction=EAST),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=7, y=17, z=0, direction=EAST)
	]),
	JmpToEvent(E3776_EMPTY)
])
