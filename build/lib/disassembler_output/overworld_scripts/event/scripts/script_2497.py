# E2497_ADDITIONAL_GATING_LOGIC_START_PLAYING

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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2497_ret_14"]),
	SetBit(TEMP_7043_0),
	FreezeAllNPCsUntilReturn(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(24),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSequenceSpeed(NORMAL),
		A_PlaySound(sound=SO101_TERRAPIN_ATTACK, channel=4),
		A_SetSpriteSequence(index=4, looping=False),
		A_Pause(64)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(32),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(24),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, looping=False),
		A_Pause(64)
	]),
	Pause(96),
	StopEmbeddedActionScript(NPC_2),
	StartBattleAtBattlefield(PACK001_BOBOMB_HENCHMEN, BF07_BOWSERS_KEEP),
	JmpIfBitClear(GAME_OVER, ["EVENT_2497_remove_from_current_level_10"]),
	ResetGame(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_2497_remove_from_current_level_10"),
	RemoveObjectFromCurrentLevel(NPC_2),
	UnfreezeAllNPCs(),
	FadeInFromBlack(sync=False),
	Return(identifier="EVENT_2497_ret_14")
])
