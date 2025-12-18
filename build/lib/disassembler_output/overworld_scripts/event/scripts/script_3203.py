# E3203_EMPTY

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
	JmpIfBitClear(UNUSED_7056_4, ["EVENT_3203_ret_33"]),
	JmpIfBitSet(UNUSED_7057_2, ["EVENT_3203_ret_33"]),
	SetBit(TEMP_7043_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceMario(),
		A_JumpToHeight(72),
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceMario()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=4, y=24),
		A_VisibilityOn(),
		A_FaceMario(),
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceMario()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=1, y=4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceWest()
	]),
	RunDialog(dialog_id=DI1643_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_3203_action_queue_10_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_4, ["EVENT_3203_action_queue_10_SUBSCRIPT_pause_0"]),
		A_Pause(80),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(32),
		A_ResetProperties(),
		A_FaceSouthwest7D(arg=0x14)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SequenceLoopingOn(),
		A_SetSpriteSequence(index=4, looping=False),
		A_Pause(64),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_Pause(30),
		A_SetBit(TEMP_7043_4),
		A_FixedFCoordOn(),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest7D(arg=0x14)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSouthwest7D(arg=0x14)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceSouthwest7D(arg=0x14)
	]),
	Pause(360),
	Store02To0248(),
	SetBit(BAMBINO_BOMB_UNKNOWN),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, mod_id=32),
	ApplySolidityModToLevel(permanent=True, room_id=R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, mod_id=0),
	Pause(2),
	ClearBit(BAMBINO_BOMB_UNKNOWN),
	Store00To0248(),
	Pause(1, identifier="EVENT_3203_pause_24"),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_3203_pause_24"]),
	SetBit(UNUSED_7057_2),
	Pause(20),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(72),
		A_Pause(40),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkNorthwestSteps(4),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(60),
		A_SetAllSpeeds(VERY_FAST),
		A_JumpToHeight(32),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_BounceToXYWithHeight(x=3, y=19, height=0),
		A_BounceToXYWithHeight(x=3, y=18, height=0),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(90),
		A_SetAllSpeeds(VERY_FAST),
		A_JumpToHeight(32),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_BounceToXYWithHeight(x=3, y=19, height=0),
		A_BounceToXYWithHeight(x=3, y=18, height=0),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(100),
		A_SetAllSpeeds(VERY_FAST),
		A_JumpToHeight(32),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_BounceToXYWithHeight(x=3, y=19, height=0),
		A_BounceToXYWithHeight(x=3, y=18, height=0),
		A_VisibilityOff()
	]),
	ClearBit(TEMP_7043_0),
	Return(identifier="EVENT_3203_ret_33")
])
