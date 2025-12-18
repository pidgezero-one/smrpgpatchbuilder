# E0669_ENTER_UNOCCUPIED_MARRYMORE_SANCTUARY

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
	JmpIfBitSet(UNKNOWN_709E_5, ["EVENT_669_enter_area_6"]),
	JmpIfBitSet(UNKNOWN_709D_2, ["EVENT_669_enter_area_8"]),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_669_ret_5"]),
	JmpIfBitSet(UNUSED_705D_0, ["EVENT_669_enter_area_6"]),
	EnterArea(room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, face_direction=NORTHEAST, x=9, y=98, z=0, run_entrance_event=True),
	Return(identifier="EVENT_669_ret_5"),
	EnterArea(room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, face_direction=NORTHEAST, x=9, y=98, z=0, run_entrance_event=True, identifier="EVENT_669_enter_area_6"),
	Return(),
	EnterArea(room_id=R294_UNMAPPED_HOUSE_ROOM, face_direction=NORTHEAST, x=9, y=98, z=0, run_entrance_event=True, identifier="EVENT_669_enter_area_8"),
	Return()
])
