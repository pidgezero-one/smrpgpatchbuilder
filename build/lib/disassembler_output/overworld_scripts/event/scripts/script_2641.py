# E2641_FACTORY_1ST_ROOM_LOADER_AFTER_FIGHT

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
	JmpIfBitSet(INNER_FACTORY_ROOM_1_COMPLETED, ["EVENT_2641_jmp_if_bit_clear_14"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=5, y=20),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepNorth(),
		A_WalkNorthwestPixels(8),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetBit(INNER_FACTORY_ROOM_1_COMPLETED),
	FadeInFromBlack(sync=False),
	Pause(16),
	RunDialog(dialog_id=DI3254_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkNorthwestSteps(5),
		A_FaceSoutheast(),
		A_Pause(16),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3255_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_7),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_WalkToXYCoords(x=10, y=47),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_7, R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD),
	UnfreezeCamera(),
	Return(),
	JmpIfBitClear(TOAD_SHOP_FREEBIE_RECEIVED, ["EVENT_2641_jmp_if_bit_clear_17"], identifier="EVENT_2641_jmp_if_bit_clear_14"),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_WalkSouthwestPixels(8)
	]),
	SetSyncActionScript(NPC_9, A0978_RANDOMLY_FACE_SOUTHWEST),
	JmpIfBitClear(UNUSED_7091_1, ["EVENT_2641_fade_in_from_black_async_19"], identifier="EVENT_2641_jmp_if_bit_clear_17"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_2641_fade_in_from_black_async_19"),
	Return()
])
