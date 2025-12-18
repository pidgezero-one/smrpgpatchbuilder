# E0455_RESUMMON_PIPE_VAULT_ENEMIES

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
	ClearBit(TEMP_707C_0),
	SummonObjectToSpecificLevel(NPC_0, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_1, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_2, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_3, R123_PIPE_VAULT_AREA_01),
	SummonObjectToSpecificLevel(NPC_1, R127_PIPE_VAULT_AREA_02),
	SummonObjectToSpecificLevel(NPC_2, R127_PIPE_VAULT_AREA_02),
	SummonObjectToSpecificLevel(NPC_3, R127_PIPE_VAULT_AREA_02),
	SummonObjectToSpecificLevel(NPC_0, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_1, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_2, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_3, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES),
	SummonObjectToSpecificLevel(NPC_0, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_1, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_2, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R129_PIPE_VAULT_AREA_05),
	SummonObjectToSpecificLevel(NPC_0, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES),
	SummonObjectToSpecificLevel(NPC_1, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES),
	SummonObjectToSpecificLevel(NPC_12, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS),
	SummonObjectToSpecificLevel(NPC_13, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 33, ["EVENT_455_set_var_to_const_27"]),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 20),
	FadeInFromBlack(sync=False, identifier="EVENT_455_fade_in_from_black_async_23"),
	Return(),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_455_run_event_as_subroutine_25"),
	Return(),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 52, identifier="EVENT_455_set_var_to_const_27"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, ["EVENT_455_jmp_if_bit_set_30"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_455_run_event_as_subroutine_25"], identifier="EVENT_455_jmp_if_bit_set_30"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_455_fade_in_from_black_async_23"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT, ["EVENT_455_fade_in_from_black_async_23"]),
	FadeInFromBlack(sync=False),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT),
	Return()
])
