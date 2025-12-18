# E3820_FORCED_TOWER_BOSS_1_FIGHT

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
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["EVENT_3584_ret_0"]),
	JmpToSubroutine(["EVENT_3818_disable_trigger_21"]),
	SetVarToConst(TIMER_7022, 8),
	RunBackgroundEventWithPause(event_id=E3075_HEAL_FLASH, timer_var=TIMER_7022, bit_4=True, bit_5=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_Pause(6),
		A_UnknownCommand(bytearray(b'\x99'))
	]),
	Pause(1, identifier="EVENT_3820_pause_5"),
	JmpIfMarioInAir(["EVENT_3820_pause_5"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkToXYCoords(x=5, y=97),
		A_FaceNortheast()
	]),
	PauseActionScript(NPC_3),
	StartAsyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=6, y=96),
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(10),
	RunDialog(dialog_id=DI3754_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=False),
		A_Pause(16),
		A_TransferToXYZF(x=13, y=91, z=0, direction=EAST)
	]),
	JmpToSubroutine(["EVENT_3818_action_queue_34"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkNorthwestSteps(3),
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownSteps(2)
	]),
	SetSyncActionScript(NPC_3, A0978_RANDOMLY_FACE_SOUTHWEST),
	RestoreAllHP(),
	RestoreAllFP(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Jmp(["EVENT_3818_clear_bit_38"])
])
