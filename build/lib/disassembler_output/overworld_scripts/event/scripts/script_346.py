# E0346_TOADSTOOLS_ROOM_ITEM

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
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_346_jmp_if_bit_set_18"]),
	JmpIfBitSet(SIGNAL_RING_STAR_PIECE_5, ["EVENT_256_ret_0"], identifier="EVENT_346_jmp_if_bit_set_1"),
	SetBit(SIGNAL_RING_STAR_PIECE_5),
	RunDialog(dialog_id=DI0716_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_346_run_dialog_29"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(1, identifier="EVENT_346_action_queue_5_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_346_action_queue_5_SUBSCRIPT_pause_3"]),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI0717_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	PauseActionScript(NPC_0),
	StartAsyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(FAST),
		A_BounceToXYWithHeight(x=5, y=65, height=0),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(bit_0=True),
		A_WalkNortheastSteps(5),
		A_SetSequenceSpeed(SLOW)
	]),
	RunDialog(dialog_id=DI0721_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, MushroomItem),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(MushroomItem),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(bit_0=True)
	]),
	SetSyncActionScript(NPC_0, A0128_WALK_RANDOM_DIRECTIONS),
	Return(),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_346_run_dialog_21"], identifier="EVENT_346_jmp_if_bit_set_18"),
	JmpIfBitClear(UNUSED_705D_1, ["EVENT_346_run_dialog_21"]),
	Jmp(["EVENT_346_jmp_if_bit_set_1"]),
	RunDialog(dialog_id=DI2321_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_346_run_dialog_21"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_BounceToXYWithHeight(x=8, y=60, height=2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=8, y=60, z=2, direction=EAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(4),
		A_VisibilityOn(),
		A_WalkNortheastPixels(12),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2322_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(30),
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=16, y=66, z=0, direction=EAST)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	RunDialog(dialog_id=DI2381_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_346_run_dialog_29"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(1, identifier="EVENT_346_action_queue_30_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_346_action_queue_30_SUBSCRIPT_pause_3"]),
		A_Pause(10),
		A_SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2382_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
