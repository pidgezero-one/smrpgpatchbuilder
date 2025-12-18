# E3743_NIMBUS_CASTLE_RIGHT_SHAMAN_HALLWAY_LIBERATED_NPC

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
	ApplyTileModToLevel(use_alternate=True, room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, mod_id=0),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, mod_id=1),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, mod_id=2),
	Pause(1),
	ApplyTileModToLevel(use_alternate=True, room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, mod_id=3),
	Pause(1),
	ApplySolidityModToLevel(permanent=True, room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, mod_id=0),
	PaletteSet(palette_set=111, row=1, bit_0=True, bit_1=True, bit_3=True),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShadowOn(),
		A_TransferXYZFPixels(x=0, y=2, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPaletteRow(row=11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferXYZFPixels(x=1, y=252, z=0, direction=EAST),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
		A_ShadowOn()
	]),
	RememberLastObject(),
	ApplySolidityModToLevel(permanent=True, room_id=R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, mod_id=1),
	Pause(1),
	PaletteSet(palette_set=109, row=1, bit_2=True, bit_3=True),
	Pause(1),
	PaletteSet(palette_set=108, row=1, bit_0=True, bit_2=True, bit_3=True),
	PaletteSet(palette_set=169, row=1, bit_1=True, bit_2=True, bit_3=True),
	PaletteSet(palette_set=170, row=1, bit_0=True, bit_1=True, bit_2=True, bit_3=True),
	FadeInFromBlack(sync=False),
	Return()
])
