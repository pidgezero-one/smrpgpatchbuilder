# E3185_PA_MOLE_IN_DEEP_MINES

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
	JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["EVENT_3185_action_queue_18"]),
	JmpIfBitSet(UNUSED_7058_3, ["EVENT_3185_run_dialog_6"]),
	RunDialog(dialog_id=DI1632_PA_MOLE_NEEDS_BOMB, above_object=NPC_0, closable=True, sync=True, multiline=True, use_background=True),
	PauseScriptResumeOnNextDialogPageB(),
	SetBit(UNUSED_7058_3),
	Jmp(["EVENT_3185_action_queue_8"]),
	RunDialog(dialog_id=DI1633_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3185_run_dialog_6"),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_Pause(32),
		A_FaceMario()
	], identifier="EVENT_3185_action_queue_8"),
	UnsyncDialog(),
	CloseDialog(),
	Return(),
	RunDialog(dialog_id=DI1634_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3185_run_dialog_12"),
	SetVarToConst(TEMP_70AE, 20),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1639_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	Pause(120),
	Jmp(["EVENT_3185_action_queue_21"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(72)
	], identifier="EVENT_3185_action_queue_18"),
	JmpIfBitClear(UNUSED_7058_3, ["EVENT_3185_run_dialog_12"]),
	RunDialog(dialog_id=DI1635_EMPTY, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast(),
		A_Walk1StepNortheast(),
		A_SetBit(TEMP_7043_4),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouthwest(),
		A_Pause(20),
		A_WalkSouthwestSteps(2),
		A_Pause(20),
		A_FixedFCoordOff()
	], identifier="EVENT_3185_action_queue_21"),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_WalkToXYCoords(x=8, y=20),
		A_FixedFCoordOff(),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True)
	]),
	JmpIfBitClear(UNUSED_7058_3, ["EVENT_3185_pause_25"]),
	RunDialog(dialog_id=DI1636_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	Pause(220, identifier="EVENT_3185_pause_25"),
	CloseDialog(),
	Pause(20),
	Store02To0248(),
	SetBit(BAMBINO_BOMB_UNKNOWN),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, mod_id=32),
	ApplySolidityModToLevel(permanent=True, room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, mod_id=0),
	Pause(2),
	ClearBit(BAMBINO_BOMB_UNKNOWN),
	Store00To0248(),
	Pause(1, identifier="EVENT_3185_pause_36"),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_3185_pause_36"]),
	Pause(20),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_FaceMario()
	]),
	RunDialog(dialog_id=DI1637_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(2),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(16),
		A_FaceSoutheast(),
		A_Pause(16),
		A_FaceNortheast()
	]),
	SetVarToConst(TEMP_70AE, 20),
	SetSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1684_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1685_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(16),
		A_FaceSouthwest(),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(72),
		A_Pause(20),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=6, y=24),
		A_WalkToXYCoords(x=4, y=20),
		A_WalkSouthwestSteps(2),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_VisibilityOff()
	]),
	SetBit(MINES_BACK_OPENED),
	RemoveOneOfItemFromInventory(BambinoBombItem),
	Return()
])
