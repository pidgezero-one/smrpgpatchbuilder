# E3214_SHIP_1ST_BOSS

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
	JmpIfBitSet(SHIP_MIDBOSS_COMPLETED, ["EVENT_3214_fade_out_to_black_async_14"]),
	StartBattleAtBattlefield(PACK167_CALAMARI_FIGHT_STATIC, BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	SetBit(SHIP_MIDBOSS_COMPLETED),
	RestoreAllHP(),
	RestoreAllFP(),
	SetBit(DIRECTIONAL_7049_0, identifier="EVENT_3214_set_bit_9"),
	EnableControls([]),
	EnterArea(room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE, face_direction=SOUTH, x=2, y=92, z=8, run_entrance_event=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	Return(),
	FadeOutToBlack(sync=False, identifier="EVENT_3214_fade_out_to_black_async_14"),
	StartBattleAtBattlefield(PACK194_BODYGUARD_PACK_1, BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR),
	Jmp(["EVENT_3214_set_bit_9"])
])
