# E2347_TOWER_TOP_FLOOR_DUMMY_CHEST

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
	JmpIfBitSet(UNKNOWN_7048_1, ["EVENT_2347_ret_19"]),
	SetBit(UNKNOWN_7048_1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x03\x80\xff')),
		A_Pause(8),
		A_BPL262728(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(48),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%@\x00\x80\xff')),
		A_Pause(8),
		A_BPL262728(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(3),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_VisibilityOn(),
		A_Pause(44),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(16),
		A_VisibilityOff()
	]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_2347_action_queue_6_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_2347_action_queue_6_SUBSCRIPT_pause_5"]),
		A_Jmp(["EVENT_2347_action_queue_6_SUBSCRIPT_pause_0"]),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouth(),
		A_Pause(24, identifier="EVENT_2347_action_queue_6_SUBSCRIPT_pause_5")
	]),
	SetSyncActionScript(NPC_2, A0401_SEQUENCE_LOOPING_OFF),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	SetAsyncActionScript(MARIO, A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST),
	SetVarToConst(ITEM_ID, GoodieBagItem),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RemoveObjectFromSpecificLevel(NPC_2, R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT),
	RemoveObjectFromSpecificLevel(NPC_7, R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT),
	SummonObjectToSpecificLevel(NPC_1, R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT),
	DisableObjectTriggerInSpecificLevel(NPC_1, R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT),
	RunDialog(dialog_id=DI3166_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(GoodieBagItem),
	Inc(HIDDEN_CHEST_COUNTER),
	Return(identifier="EVENT_2347_ret_19")
])
