# E1111_FROGFUCIUS

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
	JmpIfMarioInAir(["EVENT_1111_jmp_if_bit_set_4"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	Pause(1),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1111_jmp_if_mario_in_air_26"]),
	JmpIfBitSet(FACTORY_GATED_BY_STAR_PIECES, ["EVENT_1111_jmp_if_bit_set_29"], identifier="EVENT_1111_jmp_if_bit_set_4"),
	RunDialog(dialog_id=DI2723_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(UNKNOWN_7083_4, ["EVENT_1111_pause_action_script_8"]),
	Return(),
	PauseActionScript(NPC_8, identifier="EVENT_1111_pause_action_script_8"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SequencePlaybackOn(),
		A_ResetProperties(),
		A_FaceMario(),
		A_Pause(40)
	]),
	PlayMusicAtDefaultVolume(M0017_TADPOLEPOND),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_FloatingOff(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(50),
		A_FloatingOn(),
		A_SequenceLoopingOff(),
		A_FixedFCoordOff()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2709_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(TEMP_70A9, 28),
	SetSyncActionScript(MARIO, A0515_MARIO_DURING_SONGS),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=25, y=29, height=4),
		A_FaceNortheast(),
		A_Pause(30),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(SLOW),
		A_Pause(45),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=23, y=26, height=4),
		A_FaceMario()
	]),
	PauseActionScript(MARIO),
	RunDialog(dialog_id=DI2711_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_FixedFCoordOff(),
		A_BounceToXYWithHeight(x=24, y=29, height=4),
		A_FixedFCoordOff(),
		A_Pause(1),
		A_FaceSouthwest(),
		A_Pause(1),
		A_FixedFCoordOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSouth(),
		A_Pause(40),
		A_PlaySound(sound=SO085_FLOWER, channel=6),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(80),
		A_ResetProperties()
	]),
	SetSyncActionScript(NPC_8, A0144_FROGFUCIUS),
	AddToInventory(FroggieStickItem),
	SetBit(FACTORY_GATED_BY_STAR_PIECES),
	RemoveOneOfItemFromInventory(CricketPieItem),
	Return(),
	JmpIfMarioInAir(["EVENT_1111_jmp_if_bit_set_29"], identifier="EVENT_1111_jmp_if_mario_in_air_26"),
	RunDialog(dialog_id=DI2712_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(UNKNOWN_709A_2, ["EVENT_1111_store_item_amount_7000_31"], identifier="EVENT_1111_jmp_if_bit_set_29"),
	JmpIfBitSet(SHINY_STONE_TRADED, ["EVENT_1111_action_queue_70"]),
	StoreItemAmountTo7000(CricketJamItem, identifier="EVENT_1111_store_item_amount_7000_31"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1111_run_dialog_93"]),
	JmpIfBitSet(UNKNOWN_709D_2, ["EVENT_1111_jmp_to_event_110"]),
	JmpIfBitSet(UNKNOWN_709A_3, ["EVENT_1111_run_dialog_91"]),
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_1111_run_dialog_89"]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_1111_run_dialog_87"]),
	JmpIfBitSet(SHINY_STONE_TRADED, ["EVENT_1111_run_dialog_85"]),
	JmpIfBitSet(TEMPLE_BOSS_DEFEATED, ["EVENT_1111_run_dialog_68"]),
	JmpIfBitSet(CASINO_WARP_ENABLED, ["EVENT_1111_run_dialog_66"]),
	JmpIfBitSet(SHIP_LIBERATED, ["EVENT_1111_run_dialog_62"]),
	JmpIfBitSet(UNUSED_7054_7, ["EVENT_1111_run_dialog_64"]),
	JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_1111_run_dialog_62"]),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_1111_run_dialog_58"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_1111_run_dialog_56"]),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7089_2, ["EVENT_1111_run_dialog_54"]),
	JmpIfBitSet(MINECART_CLEARED, ["EVENT_1111_run_dialog_52"]),
	JmpIfBitSet(FOREST_LIBERATED, ["EVENT_1111_run_dialog_50"]),
	RunDialog(dialog_id=DI2710_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2735_FROGFUCIUS_MELODY_BAY_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_50"),
	Return(),
	RunDialog(dialog_id=DI2740_FROGFUCIUS_TOWER_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_52"),
	Return(),
	RunDialog(dialog_id=DI3381_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_54"),
	Return(),
	RunDialog(dialog_id=DI3382_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_56"),
	Return(),
	RunDialog(dialog_id=DI3383_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_58"),
	SetBit(UNUSED_7091_6),
	SetBit(MAP_DIRECTIONAL_MARRYMORE_STAR_HILL),
	Return(),
	RunDialog(dialog_id=DI3388_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_62"),
	Return(),
	RunDialog(dialog_id=DI3389_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_64"),
	Return(),
	RunDialog(dialog_id=DI3390_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_66"),
	Return(),
	RunDialog(dialog_id=DI3391_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_68"),
	Return(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_BounceToXYWithHeight(x=23, y=29, height=4),
		A_FaceSoutheast()
	], identifier="EVENT_1111_action_queue_70"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceNorthwest()
	]),
	Pause(25),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=23, y=29, z=4, direction=EAST),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkNortheastPixels(4),
		A_VisibilityOn(),
		A_WalkNortheastPixels(10)
	]),
	Pause(40),
	RunDialog(dialog_id=DI3396_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI3397_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(15),
	RunDialog(dialog_id=DI3398_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_WalkSouthwestPixels(14),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetBit(UNKNOWN_709A_2),
	Return(),
	RunDialog(dialog_id=DI3399_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_85"),
	Return(),
	RunDialog(dialog_id=DI3400_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_87"),
	Return(),
	RunDialog(dialog_id=DI3401_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_89"),
	Return(),
	RunDialog(dialog_id=DI3402_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_91"),
	Return(),
	RunDialog(dialog_id=DI3384_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_93"),
	JmpIfDialogOptionBSelected(["EVENT_1111_run_dialog_108"]),
	Pause(15),
	RunDialog(dialog_id=DI3386_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartLoopNTimes(9),
	Pause(45),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	EndLoop(),
	SetVarToConst(PRIMARY_TEMP_7000, 10),
	AddFrogCoins(PRIMARY_TEMP_7000),
	RemoveOneOfItemFromInventory(CricketJamItem),
	Pause(60),
	RunDialog(dialog_id=DI3387_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_709A_0),
	Return(),
	RunDialog(dialog_id=DI3385_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_run_dialog_108"),
	Return(),
	JmpToEvent(E3013_CLONE_RESERVED, identifier="EVENT_1111_jmp_to_event_110")
])
