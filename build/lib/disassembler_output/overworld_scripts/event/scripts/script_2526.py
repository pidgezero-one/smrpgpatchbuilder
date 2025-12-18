# E2526_STAR_HILL_1ST_ROOM_LOADER

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
	JmpIfBitSet(UNKNOWN_709D_2, ["EVENT_2526_action_queue_2"]),
	RunEventAsSubroutine(E4011_CLONE_RESERVED),
	ActionQueueSync(target=NPC_11, subscript=[
		A_WalkSouthwestPixels(4),
		A_WalkWestPixels(5)
	], identifier="EVENT_2526_action_queue_2"),
	ActionQueueSync(target=NPC_12, subscript=[
		A_WalkSouthwestPixels(4),
		A_WalkWestPixels(6)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_WalkWestPixels(8)
	]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_WalkSoutheastPixels(6)
	]),
	JmpIfBitClear(UNKNOWN_709D_2, ["EVENT_2526_jmp_if_bit_set_8"]),
	RunEventAsSubroutine(E4012_CLONE_RESERVED),
	JmpIfBitSet(UNUSED_708B_6, ["EVENT_2526_fade_in_from_black_async_27"], identifier="EVENT_2526_jmp_if_bit_set_8"),
	SetBit(UNUSED_708B_6),
	FadeInFromBlack(sync=False),
	SummonObjectToCurrentLevel(NPC_16),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3117_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	RunDialog(dialog_id=DI3118_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties()
	]),
	Pause(48),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(64),
		A_SetSpriteSequence(index=27, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3119_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_16),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_2526_fade_in_from_black_async_27"),
	Return()
])
