# E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE

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
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3584_ret_0"]),
	EnableControlsUntilReturn([]),
	SetBit(CHAPEL_ITEM_RETRIEVAL_STARTED),
	PauseActionScript(NPC_3),
	StartSyncEmbeddedActionScript(target=NPC_3, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=21, y=16),
		A_Walk1StepNortheast()
	]),
	Pause(4),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, mod_id=0),
	Pause(12),
	SetBit(TEMP_704C_0),
	EnterArea(room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, face_direction=NORTHEAST, x=9, y=100, z=0, run_entrance_event=True),
	FreezeCamera(),
	ActionQueueSync(target=NPC_15, subscript=[
		A_TransferXYZFPixels(x=252, y=248, z=0, direction=EAST),
		A_Pause(12),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkNortheastPixels(8),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(13),
		A_WalkNortheastPixels(8),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_WalkNortheastSteps(3),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(FASTEST),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=6),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(3),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(1)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_TransferXYZFPixels(x=8, y=4, z=6, direction=EAST),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
		A_Pause(96),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_JumpToHeight(height=112, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(12),
		A_SetSpriteSequence(index=1, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[1])
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(3),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(8),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_JumpToHeight(height=128, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(5),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetPriority(3),
		A_WalkNortheastSteps(8),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=128, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(5)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(24),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(16),
		A_WalkNortheastPixels(16),
		A_WalkSouthwestPixels(16),
		A_WalkNortheastPixels(12),
		A_WalkSouthwestPixels(8),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_Pause(30),
		A_TransferToObjectXY(NPC_16),
		A_TransferXYZFPixels(x=0, y=0, z=8, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=144, silent=True),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\xf6\x80\xfd')),
		A_Pause(60),
		A_BPL262728(),
		A_TransferToXYZF(x=11, y=86, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_Pause(34),
		A_TransferToObjectXY(NPC_16),
		A_TransferXYZFPixels(x=0, y=8, z=12, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=136, silent=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(4)
	]),
	FadeInFromBlack(sync=True),
	Pause(28),
	ReturnFD(),
	Pause(20),
	ReturnFD(),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(48),
		A_TransferToObjectXY(NPC_16),
		A_TransferXYZFPixels(x=0, y=0, z=14, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=240, silent=True),
		A_ShadowOn(),
		A_Pause(30),
		A_FloatingOff()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(48),
		A_TransferToObjectXY(NPC_16),
		A_TransferXYZFPixels(x=0, y=12, z=14, direction=EAST),
		A_SetPriority(3),
		A_JumpToHeight(height=152, silent=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkWestSteps(5),
		A_VisibilityOn()
	]),
	RemoveObjectFromSpecificLevel(NPC_2, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	RemoveObjectFromSpecificLevel(NPC_3, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	RemoveObjectFromSpecificLevel(NPC_4, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	RemoveObjectFromSpecificLevel(NPC_5, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	RemoveObjectFromSpecificLevel(NPC_6, R153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=0, sprite_offset=5, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2078_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI2079_EMPTY, above_object=NPC_16, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(8),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI2080_EMPTY, above_object=NPC_16, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2081_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	UnfreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast(),
		A_WalkNortheastSteps(13),
		A_Pause(20),
		A_WalkNortheastSteps(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(44),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_ShadowOn(),
		A_AddZCoord1Step(),
		A_Pause(20),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNortheastSteps(1)
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNorth(),
		A_FaceNortheast(),
		A_SetSequenceSpeed(SLOW),
		A_FixedFCoordOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_Pause(30),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepEast(),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(10),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x04\x00\xff')),
		A_JumpToHeight(height=104, silent=True),
		A_Pause(10),
		A_FloatingOn(),
		A_Pause(14),
		A_BPL262728(),
		A_Pause(30),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True)
	]),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2082_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2083_EMPTY, above_object=NPC_15, closable=False, sync=False, multiline=True, use_background=True),
	RememberLastObject(),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI2084_EMPTY, above_object=NPC_15, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastPixels(10)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2085_EMPTY, above_object=NPC_15, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(120),
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(10),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2086_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2087_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2088_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2089_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(8),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2090_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	PlaySoundBalance(sound=SO004_JUMP, balance=64),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSouthwest()
	]),
	PlaySoundBalance(sound=SO004_JUMP, balance=64),
	Pause(60),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2091_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Walk1StepNortheast(),
		A_SetSequenceSpeed(FAST)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2092_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2093_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_15, subscript=[
		A_WalkSoutheastPixels(10),
		A_Pause(30),
		A_WalkNorthwestPixels(14),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_Pause(50),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(SLOW),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Walk1StepNorthwest(),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RememberLastObject(),
	Pause(30),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2124_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOn(),
		A_Walk1StepSouthwest(),
		A_FaceNortheast(),
		A_FixedFCoordOff()
	]),
	Pause(30),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_FaceSouthwest()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(30),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(30),
		A_FaceSouthwest(),
		A_FixedFCoordOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(30),
		A_FaceSouthwest(),
		A_FixedFCoordOff()
	]),
	RunDialog(dialog_id=DI2125_EMPTY, above_object=NPC_15, closable=False, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueSync(target=NPC_8, subscript=[
		A_Pause(140),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_15, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_16, subscript=[
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(2)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkToXYCoords(x=20, y=75),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(15),
		A_WalkNorthwestSteps(3),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(10),
		A_WalkToXYCoords(x=20, y=75),
		A_FixedFCoordOff(),
		A_WalkSouthwestSteps(9),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(16),
		A_WalkToXYCoords(x=20, y=75),
		A_WalkSouthwestSteps(3),
		A_WalkNorthwestSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_Pause(60),
		A_SetBit(TEMP_7043_0),
		A_PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
		A_Pause(30),
		A_ClearBit(TEMP_7043_0),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_FaceNortheast()
	]),
	Pause(20),
	RunDialog(dialog_id=DI2126_EMPTY, above_object=NPC_15, closable=True, sync=False, multiline=True, use_background=True),
	Pause(30),
	SetSyncActionScript(SCREEN_FOCUS, A0214_SANCTUARY_CAMERA),
	Pause(60),
	StopAllBackgroundEvents(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_TransferToXYZF(x=15, y=125, z=0, direction=EAST)
	]),
	RememberLastObject(),
	RunDialog(dialog_id=DI2498_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(SCREEN_FOCUS, A0215_SANCTUARY_CAMERA),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(8),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RemoveObjectFromCurrentLevel(NPC_6),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_WalkNorthwestSteps(4),
		A_SetSequenceSpeed(SLOW),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2499_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	SetSyncActionScript(SCREEN_FOCUS, A0215_SANCTUARY_CAMERA),
	Pause(10),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RemoveObjectFromCurrentLevel(NPC_5),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2500_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	RunDialog(dialog_id=DI2501_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=22, y=73, z=6, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=26, direction=NORTHEAST)
	]),
	SetSyncActionScript(NPC_2, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_0, A0376_TURN_RANDOMLY_IN_PLACE),
	RunDialog(dialog_id=DI2502_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI2094_EMPTY, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	PauseActionScript(NPC_2),
	PauseActionScript(NPC_0),
	SetSyncActionScript(NPC_1, A0373_SANCTUARY_HENCHMAN),
	SetSyncActionScript(NPC_0, A0372_SANCTUARY_HENCHMAN),
	SetSyncActionScript(NPC_2, A0374_SANCTUARY_HENCHMAN),
	SlowDownMusicTempoBy(duration=0, change=12),
	SetVarToConst(TEMP_70AE, 8),
	SetVarToConst(TEMP_70AF, 0),
	SetVarToConst(FACTORY_FALL_1, 0),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 0),
	ClearBit(SANCTUARY_LOCKED),
	SetVarToConst(TIMER_701C, 300),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0647_MARRYMORE_SANCTUARY_CANDLE_1, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Return()
])
