# E0729_SEVERAL_MARRYMORE_ROOM_LOADERS

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
	JmpIfBitClear(UNUSED_705D_1, ["EVENT_256_ret_0"]),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_256_ret_0"]),
	JmpIfBitClear(TEMP_7044_6, ["EVENT_256_ret_0"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=7, y=86),
		A_WalkNortheastPixels(4),
		A_FaceWest()
	]),
	Pause(1, identifier="EVENT_729_pause_4"),
	JmpIfBitClear(TEMP_7044_6, ["EVENT_729_action_queue_7"]),
	Jmp(["EVENT_729_pause_4"]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_WalkNortheastPixels(6),
		A_FaceSoutheast()
	], identifier="EVENT_729_action_queue_7"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	Pause(10, identifier="EVENT_729_pause_9"),
	RunDialog(dialog_id=DI2314_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=3, is_sequence=True, looping=True)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2315_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(1, identifier="EVENT_729_action_queue_19_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_729_action_queue_19_SUBSCRIPT_pause_4"]),
		A_Pause(40),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2316_EMPTY, above_object=NPC_10, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2317_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	RunDialog(dialog_id=DI2188_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_TransferToXYZF(x=7, y=85, z=12, direction=EAST),
		A_FaceNortheast(),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(12),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI2310_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=4, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties(),
		A_PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
		A_Pause(30),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_Pause(30),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	Pause(60),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(2),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2311_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2312_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2313_EMPTY, above_object=NPC_10, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_12, subscript=[
		A_Pause(10),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=1, y=42, z=0, direction=EAST)
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=1, y=42, z=0, direction=EAST)
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouth()
	]),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	RunDialog(dialog_id=DI2303_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	FadeOutMusicToVolume(duration=2, volume=0),
	Pause(60),
	PlayMusicAtDefaultVolume(M0040_NEWPARTNER),
	Pause(24),
	ActionQueueAsync(target=MARIO, subscript=[
		A_StartLoopNTimes(7),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop()
	]),
	SetAsyncActionScript(MARIO, A0510_EMPTY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	PlayMusicAtDefaultVolume(M0002_MUSHROOMKINGDOM),
	CharacterJoinsParty(TOADSTOOL),
	SetBit(SHUFFLE_ONE_FIREWORKS_ENABLED),
	Return()
])
