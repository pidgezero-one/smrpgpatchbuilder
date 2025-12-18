# E0600_MARRYMORE_OCCUPIED_CHAPEL_LOADER

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
	Set0158Bit7Offset(0x015E),
	Set0158Bit7Offset(0x0160),
	Set0158Bit7Offset(0x0162),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_257_fade_in_from_black_async_0"]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_SetPriority(2),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	Return()
])
