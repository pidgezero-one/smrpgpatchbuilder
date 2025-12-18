# E2399_ABYSS_ROOM_1_LOADER

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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 55),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=28, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties()
	]),
	SetVarToConst(FACTORY_FALL_1, 219),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkNorthwestPixels(12)
	]),
	JmpIfBitClear(ABYSS_ENTRANCE_DIRECTIONAL_BIT, ["EVENT_2399_jmp_if_bit_set_8"]),
	ClearBit(ABYSS_ENTRANCE_DIRECTIONAL_BIT),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(RELOAD_MUSIC_IN_FACTORY, ["EVENT_2399_fade_in_music_11"], identifier="EVENT_2399_jmp_if_bit_set_8"),
	FadeInMusic(M0065_GATE),
	Jmp(["EVENT_2399_freeze_camera_12"]),
	FadeInMusic(M0067_WEAPONSFACTORY, identifier="EVENT_2399_fade_in_music_11"),
	FreezeCamera(identifier="EVENT_2399_freeze_camera_12"),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=2, y=10)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=4, y=25, z=21, direction=EAST),
		A_WalkSouthPixels(8)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_SetSpriteSequence(index=0, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(1, identifier="EVENT_2399_action_queue_17_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_2399_action_queue_17_SUBSCRIPT_pause_3"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	JmpIfBitSet(RELOAD_MUSIC_IN_FACTORY, ["EVENT_2399_unfreeze_camera_111"]),
	SetBit(RELOAD_MUSIC_IN_FACTORY),
	Pause(24),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_2),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(24),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_Pause(10),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(8),
	RunDialog(dialog_id=DI3128_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_Pause(24),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3129_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetAsyncActionScript(NPC_2, A0854_EMPTY),
	RunDialog(dialog_id=DI3130_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	PlaySound(sound=SO026_LAUGHING_BOWSER, channel=6),
	RunDialog(dialog_id=DI3131_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_1),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(16),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(12),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3132_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_FaceEast(),
		A_Pause(4),
		A_FaceSoutheast(),
		A_Pause(4),
		A_FaceSouth(),
		A_Pause(4),
		A_FaceSouthwest()
	]),
	RunDialog(dialog_id=DI3133_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	RunDialog(dialog_id=DI3134_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(8),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3135_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(48),
		A_FaceNortheast(),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3136_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_ResetProperties()
	]),
	UnsyncDialog(),
	Pause(8),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3137_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=1, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3138_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties()
	]),
	Pause(8),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(16),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(64),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3139_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(NPC_2, A0854_EMPTY),
	RunDialog(dialog_id=DI3140_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3141_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	RunDialog(dialog_id=DI3142_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3142_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(24),
	RunDialog(dialog_id=DI3146_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnsyncDialog(),
	Pause(16),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_ResetProperties()
	]),
	RunDialog(dialog_id=DI3147_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	RunDialog(dialog_id=DI3142_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3148_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(8),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(32),
		A_ResetProperties()
	]),
	UnsyncDialog(),
	Pause(32),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=10, sprite_offset=1, looping=False),
		A_Pause(54),
		A_SetSpriteSequence(index=30, sprite_offset=1, is_mold=True, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3143_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(8),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_Pause(8)
	]),
	RunDialog(dialog_id=DI3144_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNorthwest(),
		A_WalkNorthwestPixels(10),
		A_VisibilityOff()
	]),
	Pause(32),
	RunDialog(dialog_id=DI3149_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	RunDialog(dialog_id=DI3145_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(8),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_WalkSouthwestPixels(4),
		A_VisibilityOff()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(16),
		A_FaceSouth()
	]),
	UnfreezeCamera(identifier="EVENT_2399_unfreeze_camera_111"),
	Return()
])
