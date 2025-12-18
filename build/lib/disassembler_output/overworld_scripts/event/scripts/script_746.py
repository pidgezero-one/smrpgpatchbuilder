# E0746_MUSHROOM_KINGDOM_INN_2F_DOWNWARD_STAIRS

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
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_746_enter_area_7"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_746_enter_area_3"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_746_enter_area_5"]),
	EnterArea(room_id=R049_MUSHROOM_KINGDOM_BEFORE_CROCO_INN_1F, face_direction=SOUTHWEST, x=4, y=84, z=0, z_add_half_unit=True, run_entrance_event=True, identifier="EVENT_746_enter_area_3"),
	Return(),
	EnterArea(room_id=R485_MUSHROOM_KINGDOM_DURING_MACK_INN_1F, face_direction=SOUTHWEST, x=4, y=84, z=0, z_add_half_unit=True, run_entrance_event=True, identifier="EVENT_746_enter_area_5"),
	Return(),
	EnterArea(room_id=R493_MUSHROOM_KINGDOM_INN_1F, face_direction=SOUTHWEST, x=4, y=84, z=0, z_add_half_unit=True, run_entrance_event=True, identifier="EVENT_746_enter_area_7"),
	Return()
])
