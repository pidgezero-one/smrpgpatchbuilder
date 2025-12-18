# E2108_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_FIGHT_ROOM_LOADER

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
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSouthPixels(7)
	]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_2108_play_music_default_volume_19"]),
	JmpIfBitSet(UNKNOWN_STATUE_ROOM_7090_1, ["EVENT_2108_play_music_default_volume_7"]),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_6, ["EVENT_2108_play_music_default_volume_7"]),
	PaletteSet(palette_set=111, row=1, bit_3=True),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_5, ["EVENT_2108_play_music_default_volume_11"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNortheastPixels(6),
		A_FaceSouthwest(),
		A_SetPriority(1),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_SetSequenceSpeed(VERY_SLOW)
	]),
	PlayMusicAtDefaultVolume(M0061_VALENTINA, identifier="EVENT_2108_play_music_default_volume_7"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2108_run_event_as_subroutine_17"]),
	FadeInFromBlack(sync=False),
	Return(),
	PlayMusicAtDefaultVolume(M0061_VALENTINA, identifier="EVENT_2108_play_music_default_volume_11"),
	JmpIfBitSet(STATUE_KEEPER_FIGHT_COMPLETED, ["EVENT_2108_jmp_if_bit_set_14"]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=19, y=16),
		A_WalkNortheastPixels(8),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_VisibilityOn()
	]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2108_run_event_as_subroutine_17"], identifier="EVENT_2108_jmp_if_bit_set_14"),
	FadeInFromBlack(sync=False),
	Return(),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE, identifier="EVENT_2108_run_event_as_subroutine_17"),
	Return(),
	PlayMusicAtDefaultVolume(M0050_NIMBUSLAND, identifier="EVENT_2108_play_music_default_volume_19"),
	Jmp(["EVENT_2108_jmp_if_bit_set_14"]),
	Return()
])
