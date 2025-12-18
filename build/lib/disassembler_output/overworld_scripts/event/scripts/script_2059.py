# E2059_MONSTROMAMA

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
	JmpIfBitSet(TEMPLE_BOSS_DEFEATED, ["EVENT_2059_run_dialog_84"]),
	JmpIfBitSet(UNKNOWN_MONSTRO_TOWN_7089_1, ["EVENT_2059_jmp_if_bit_set_11"]),
	RunDialog(dialog_id=DI2976_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=15, y=78, height=0),
		A_FaceSoutheast(),
		A_Pause(20),
		A_PlaySound(sound=SO081_STAR, channel=6),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(20)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(15),
		A_FaceNorthwest()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunDialog(dialog_id=DI2975_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_2059_action_queue_15"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(15),
		A_FaceSouthwest()
	]),
	SetBit(UNKNOWN_MONSTRO_TOWN_7089_1),
	Return(),
	JmpIfBitSet(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_2059_run_dialog_14"], identifier="EVENT_2059_jmp_if_bit_set_11"),
	RunDialog(dialog_id=DI2974_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI2973_MONSTROMAMA, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2059_run_dialog_14"),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=15, y=78, height=0),
		A_FaceSoutheast(),
		A_Pause(20),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO056_SHAKE_HEAD, channel=6),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(30),
		A_PlaySound(sound=SO081_STAR, channel=6),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True),
		A_Pause(30),
		A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_Pause(20)
	], identifier="EVENT_2059_action_queue_15"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(15),
		A_FaceNorthwest(),
		A_Pause(30)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunDialog(dialog_id=DI2972_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(45),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(45),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
		A_JumpToHeight(height=48, silent=True),
		A_WalkSoutheastSteps(1),
		A_Pause(30)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunDialog(dialog_id=DI2971_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(15),
		A_FaceSouthwest(),
		A_Pause(40)
	]),
	RunDialog(dialog_id=DI2988_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(15),
		A_FaceSouthwest()
	]),
	Pause(60),
	FadeOutSoundToVolume(duration=0, volume=0),
	PlaySound(sound=SO122_SKY_TROOPAS_APPROACHING, channel=6),
	FadeOutSoundToVolume(duration=5, volume=100),
	Pause(60),
	Pause(60),
	Pause(60),
	Pause(60),
	Pause(60),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(15),
	PlaySound(sound=SO123_CHAIN_RUMBLING_NOISE, channel=6),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferToXYZF(x=13, y=83, z=3, direction=EAST),
		A_WalkSouthwestPixels(8),
		A_WalkSoutheastPixels(8),
		A_FaceNortheast(),
		A_SetWalkingSpeed(FASTER),
		A_VisibilityOn(),
		A_Pause(1, identifier="EVENT_2059_action_queue_37_SUBSCRIPT_pause_7"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_2, destinations=["EVENT_2059_action_queue_37_SUBSCRIPT_pause_7"]),
		A_WalkNortheastSteps(5),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(8),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_SequenceLoopingOn(),
		A_SetBit(TEMP_7043_0)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferToXYZF(x=13, y=83, z=3, direction=EAST),
		A_WalkSouthwestPixels(8),
		A_FaceNortheast(),
		A_SetWalkingSpeed(FASTER),
		A_VisibilityOn(),
		A_Pause(1, identifier="EVENT_2059_action_queue_38_SUBSCRIPT_pause_7"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_3, destinations=["EVENT_2059_action_queue_38_SUBSCRIPT_pause_7"]),
		A_WalkNortheastSteps(4),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(8),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_SequenceLoopingOn(),
		A_SetBit(TEMP_7043_0)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferToXYZF(x=14, y=84, z=3, direction=EAST),
		A_WalkSouthwestPixels(8),
		A_FaceNortheast(),
		A_SetWalkingSpeed(FASTER),
		A_VisibilityOn(),
		A_Pause(1, identifier="EVENT_2059_action_queue_39_SUBSCRIPT_pause_7"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_4, destinations=["EVENT_2059_action_queue_39_SUBSCRIPT_pause_7"]),
		A_WalkNortheastSteps(4),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastPixels(8),
		A_ResetProperties(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_SequenceLoopingOn(),
		A_SetBit(TEMP_7043_0)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(70),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(70),
		A_FaceNortheast()
	]),
	FadeOutSoundToVolume(duration=2, volume=0),
	Pause(5),
	RunDialog(dialog_id=DI3016_DUPLICATE, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3017_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(20),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_PlaySound(sound=SO134_SWIPE, channel=6),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_Pause(20),
		A_PlaySound(sound=SO134_SWIPE, channel=6),
		A_WalkNorthwestSteps(1),
		A_Pause(15),
		A_PlaySound(sound=SO134_SWIPE, channel=6),
		A_WalkNortheastSteps(1),
		A_Pause(15),
		A_PlaySound(sound=SO134_SWIPE, channel=6),
		A_WalkSoutheastSteps(1),
		A_Pause(15)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(FAST),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_Pause(20),
		A_WalkSoutheastSteps(1),
		A_Pause(15),
		A_WalkNortheastSteps(1),
		A_Pause(15),
		A_WalkNorthwestSteps(1),
		A_Pause(15)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FAST),
		A_FaceSouthwest(),
		A_Pause(20),
		A_WalkSouthwestSteps(1),
		A_Pause(15),
		A_Pause(20),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_Pause(35),
		A_PlaySound(sound=SO133_CLOSE_HIT_DOOR, channel=6),
		A_Pause(15)
	]),
	RunDialog(dialog_id=DI3018_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3019_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(5),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties()
	]),
	Pause(5),
	RunDialog(dialog_id=DI3020_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	RunDialog(dialog_id=DI3021_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(FASTER),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=False),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI3022_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI3023_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO124_ENGINE_STARTING, channel=6),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_Pause(45),
		A_SetSequenceSpeed(FASTER),
		A_Pause(45),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_Pause(45),
		A_SetSequenceSpeed(FASTER),
		A_Pause(45),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_Pause(45),
		A_SetSequenceSpeed(FASTER),
		A_Pause(45),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3024_EMPTY, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(TEMP_70AE, 0),
	ClearBit(TEMP_7043_0),
	PlaySound(sound=SO123_CHAIN_RUMBLING_NOISE, channel=6),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8),
		A_ClearBit(TEMP_7043_0),
		A_Pause(1, identifier="EVENT_2059_action_queue_72_SUBSCRIPT_pause_4"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_2, destinations=["EVENT_2059_action_queue_72_SUBSCRIPT_pause_4"]),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_SetWalkingSpeed(FASTER),
		A_SetSequenceSpeed(SLOW),
		A_WalkSouthwestSteps(7),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8),
		A_Pause(1, identifier="EVENT_2059_action_queue_73_SUBSCRIPT_pause_3"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_3, destinations=["EVENT_2059_action_queue_73_SUBSCRIPT_pause_3"]),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_SetWalkingSpeed(FASTER),
		A_SetSequenceSpeed(SLOW),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(8),
		A_Pause(1, identifier="EVENT_2059_action_queue_74_SUBSCRIPT_pause_3"),
		A_CreatePacketAtObjectCoords(packet=P047_BLUE_FIRE_TRAIL, target_npc=NPC_4, destinations=["EVENT_2059_action_queue_74_SUBSCRIPT_pause_3"]),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_SetWalkingSpeed(FASTER),
		A_SetSequenceSpeed(SLOW),
		A_WalkSouthwestSteps(8),
		A_VisibilityOff(),
		A_PlaySound(sound=SO016_OPEN_DOOR, channel=6),
		A_Pause(15),
		A_PlaySound(sound=SO000_SILENCE, channel=6)
	]),
	SetBit(TEMP_7043_0),
	Pause(90),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3025_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	SetBit(TEMPLE_BOSS_DEFEATED),
	SetBit(MAP_BEAN_VALLEY),
	Return(),
	RunDialog(dialog_id=DI3026_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2059_run_dialog_84"),
	Return()
])
