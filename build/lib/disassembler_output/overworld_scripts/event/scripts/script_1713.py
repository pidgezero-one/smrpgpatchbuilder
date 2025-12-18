# E1713_BANDITS_WAY_3_LOADER

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
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_5),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	JmpIfBitClear(BANDITS_WAY_CUTSCENE_3_VIEWED, ["EVENT_1713_jmp_if_bit_clear_6"]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return(),
	JmpIfBitClear(UNKNOWN_7077_7, ["EVENT_1713_fade_in_from_black_sync_10"], identifier="EVENT_1713_jmp_if_bit_clear_6"),
	SetSyncActionScript(NPC_8, A0162_BOSS_IN_BANDITS_WAY_3),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return(),
	FadeInFromBlack(sync=True, identifier="EVENT_1713_fade_in_from_black_sync_10"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_Pause(8),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI1058_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_8, A0162_BOSS_IN_BANDITS_WAY_3),
	Return()
])
