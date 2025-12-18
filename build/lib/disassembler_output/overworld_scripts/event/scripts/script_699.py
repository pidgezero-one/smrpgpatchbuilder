# E0699_EMPTY

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
	JmpIfBitSet(UNUSED_705D_1, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_6),
	RunDialog(dialog_id=DI2185_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_699_action_queue_5_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_699_action_queue_5_SUBSCRIPT_pause_0"]),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_BounceToXYWithHeight(x=13, y=65, height=8),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=13, y=65, z=8, direction=EAST),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_TransferXYZFPixels(x=4, y=254, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkNortheastPixels(12),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	Pause(10),
	RunDialog(dialog_id=DI2186_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2187_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_699_close_dialog_18"]),
	CloseDialog(),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(40),
		A_ResetProperties(),
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=21, y=117, z=0, direction=EAST)
	]),
	Jmp(["EVENT_699_pause_155"]),
	CloseDialog(identifier="EVENT_699_close_dialog_18"),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2188_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_Pause(10),
		A_TransferToXYZF(x=13, y=65, z=8, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_TransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(12),
		A_FaceSoutheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2189_EMPTY, above_object=NPC_14, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(8),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_DecZCoord1Step(),
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI2190_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_699_pause_49"]),
	Pause(10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(40),
	RunDialog(dialog_id=DI2146_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=21, y=117, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_ResetProperties(),
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=22, y=117, z=0, direction=EAST)
	]),
	Jmp(["EVENT_699_pause_155"]),
	Pause(10, identifier="EVENT_699_pause_49"),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2191_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_Pause(20),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_Pause(10),
		A_TransferToXYZF(x=13, y=65, z=8, direction=EAST),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkSouthwestPixels(12),
		A_FaceNortheast()
	]),
	Pause(10),
	RunDialog(dialog_id=DI2192_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_699_close_dialog_86"]),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ResetProperties()
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(40),
	RunDialog(dialog_id=DI2146_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(30),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=21, y=117, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ResetProperties(),
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=22, y=117, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_ResetProperties(),
		A_WalkNortheastPixels(12),
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	Jmp(["EVENT_699_pause_155"]),
	CloseDialog(identifier="EVENT_699_close_dialog_86"),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	RunDialog(dialog_id=DI2147_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_Pause(80),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=64, silent=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
		A_Pause(60),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_JumpToHeight(height=64, silent=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ResetProperties(),
		A_Pause(80),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=64, silent=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ResetProperties(),
		A_Pause(20),
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSpriteSequence(index=7, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=64, silent=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(10),
		A_TransferToXYZF(x=13, y=65, z=8, direction=EAST),
		A_SetAllSpeeds(SLOW),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(10),
		A_FaceNorthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpPixels(8),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(8),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_DecZCoord1Step(),
		A_Pause(60),
		A_SetWalkingSpeed(NORMAL),
		A_ResetProperties()
	]),
	Pause(80),
	SetSyncActionScript(SCREEN_FOCUS, A0658_PIPE_VAULT_THWOMP_ROOM_SHAKE_CAMERA),
	PlaySound(sound=SO021_RUMBLING, channel=6),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI2148_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_699_pause_138"]),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ResetProperties()
	]),
	RememberLastObject(),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(30),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=15, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_Pause(20),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	Pause(40),
	RunDialog(dialog_id=DI2146_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10, identifier="EVENT_699_pause_131"),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties(),
		A_WalkSouthwestPixels(12),
		A_TransferToXYZF(x=21, y=117, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_ResetProperties(),
		A_WalkSoutheastPixels(12),
		A_TransferToXYZF(x=22, y=117, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_ResetProperties(),
		A_WalkNortheastPixels(12),
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_ResetProperties(),
		A_WalkNorthwestPixels(10),
		A_TransferToXYZF(x=24, y=117, z=0, direction=EAST)
	]),
	Jmp(["EVENT_699_pause_155"]),
	Pause(10, identifier="EVENT_699_pause_138"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(59),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(59),
		A_WalkNorthwestPixels(2),
		A_WalkSoutheastPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(59),
		A_WalkSouthwestPixels(2),
		A_WalkNortheastPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_StartLoopNTimes(59),
		A_WalkSoutheastPixels(2),
		A_WalkNorthwestPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(SLOW)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(15),
		A_FaceNorthwest(),
		A_Pause(15),
		A_FaceSouthwest(),
		A_Pause(15),
		A_FaceSoutheast(),
		A_Pause(15),
		A_FaceNortheast()
	]),
	RememberLastObject(),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2145_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_699_pause_131"]),
	Pause(20, identifier="EVENT_699_pause_155"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
