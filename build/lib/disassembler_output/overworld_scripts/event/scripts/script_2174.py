# E2174_KEEP_BOBOMB_BATTLE_ROOM_SUMMON_4TH_BATTLE

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
	JmpIfBitSet(TEMP_7043_4, ["EVENT_2174_ret_26"]),
	SetBit(TEMP_7043_4),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=20, y=30, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=18, y=33, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2174_create_packet_at_npc_coords_7"]),
	SetAsyncActionScript(NPC_0, A1004_KEEP_1ST_BOSS_SUMMON_ANIMATION),
	Pause(60),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_4, destinations=["EVENT_2174_create_packet_at_npc_coords_7"], identifier="EVENT_2174_create_packet_at_npc_coords_7"),
	SetSyncActionScript(NPC_0, A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_FaceSouthwest7D(arg=0x18)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_VisibilityOn(),
		A_Pause(35),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpSteps(2),
		A_SetWalkingSpeed(FAST),
		A_ShiftZDownPixels(6),
		A_ShiftZUpPixels(6),
		A_ShiftZDownPixels(4),
		A_ShiftZUpPixels(4),
		A_ShiftZDownPixels(2),
		A_ShiftZUpPixels(2),
		A_Pause(20)
	]),
	StartBattleAtBattlefield(PACK235_CHESTER_DUPE, BF07_BOWSERS_KEEP),
	JmpIfBitClear(GAME_OVER, ["EVENT_2174_action_queue_17"]),
	RestoreAllHP(),
	RestoreAllFP(),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=17, y=31, z=0, direction=EAST),
		A_VisibilityOff()
	], identifier="EVENT_2174_action_queue_17"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=19, y=35, z=0, direction=EAST),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, mod_id=38),
	ApplySolidityModToLevel(permanent=True, room_id=R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, mod_id=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, mod_id=39),
	ApplySolidityModToLevel(permanent=True, room_id=R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, mod_id=7),
	FadeInFromBlack(sync=False),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_0, destinations=["EVENT_2174_create_packet_at_npc_coords_24"], identifier="EVENT_2174_create_packet_at_npc_coords_24"),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_4, destinations=["EVENT_2174_create_packet_at_npc_coords_24"]),
	Return(identifier="EVENT_2174_ret_26")
])
