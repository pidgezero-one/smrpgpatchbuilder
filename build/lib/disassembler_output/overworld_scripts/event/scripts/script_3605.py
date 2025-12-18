# E3605_PIPE_VAULT_PIPE_TO_TRIPLE_CHEST_ROOM

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
	SetBit(TEMP_7044_3),
	SetVarToConst(X_COORD_2, 7),
	SetVarToConst(Y_COORD_2, 50),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
	EnterArea(room_id=R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, face_direction=NORTHEAST, x=0, y=79, z=0, run_entrance_event=True),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x00')),
		A_AddConstToVar(Z_COORD_2, 2304),
		A_UnknownCommand(bytearray(b'\x99')),
		A_JumpToHeight(height=0, silent=True)
	]),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3605_pause_8"),
	JmpIfMarioInAir(["EVENT_3605_pause_8"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3584_ret_0"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_9, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["EVENT_3605_clear_bit_15"]),
	JmpIfObjectTriggerEnabledInSpecificLevel(NPC_10, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["EVENT_3605_clear_bit_15"]),
	Jmp(["EVENT_3584_ret_0"]),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_3605_clear_bit_15"),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	Return()
])
