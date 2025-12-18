# E4011_CLONE_RESERVED

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
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=12),
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=13),
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=14),
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=15),
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=16),
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=17),
	ApplyTileModToLevel(use_alternate=False, room_id=R158_STAR_HILL_AREA_02, mod_id=18),
	RemoveObjectFromCurrentLevel(NPC_20),
	RemoveObjectFromCurrentLevel(NPC_21),
	RemoveObjectFromCurrentLevel(NPC_22),
	RemoveObjectFromCurrentLevel(NPC_23),
	RemoveObjectFromCurrentLevel(NPC_24),
	RemoveObjectFromCurrentLevel(NPC_25),
	RemoveObjectFromCurrentLevel(NPC_26),
	Return()
])
