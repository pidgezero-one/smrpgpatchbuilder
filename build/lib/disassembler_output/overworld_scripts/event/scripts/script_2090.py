# E2090_MONSTRO_ENTRANCE_LOADER

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
	JmpIfBitClear(UNUSED_7093_3, ["EVENT_2090_action_queue_2"]),
	SetAsyncActionScript(NPC_2, A0690_OPENING_CHEST),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkNorthwestPixels(8),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	], identifier="EVENT_2090_action_queue_2"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkNortheastPixels(6),
		A_FaceSouthwest(),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkNortheastPixels(6),
		A_FaceSouthwest(),
		A_Pause(1)
	]),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(UNUSED_7093_3, ["EVENT_2090_ret_11"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2090_ret_11"]),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT),
	Return(identifier="EVENT_2090_ret_11")
])
