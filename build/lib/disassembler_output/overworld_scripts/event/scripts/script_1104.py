# E1104_TADPOLE_POND_LOADER

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
	SetBit(UNKNOWN_7065_7),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_WalkSouthwestPixels(1)
	]),
	JmpIfBitClear(KEEP_GATED_BY_STAR_PIECES, ["EVENT_1104_deactivate_sound_channels_13"]),
	JmpIfBitClear(SEA_GATED_BY_STAR_PIECES, ["EVENT_1104_deactivate_sound_channels_5"]),
	JmpIfBitClear(FACTORY_GATED_BY_STAR_PIECES, ["EVENT_1104_play_music_default_volume_8"]),
	DeactivateSoundChannels([], identifier="EVENT_1104_deactivate_sound_channels_5"),
	FadeInFromBlack(sync=False),
	Return(),
	PlayMusicAtDefaultVolume(M0021_SADSONG, identifier="EVENT_1104_play_music_default_volume_8"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ResetProperties(),
		A_TransferToXYZF(x=23, y=26, z=4, direction=EAST),
		A_FaceNorthwest()
	]),
	SetSyncActionScript(NPC_8, A0095_PLAYER_GAME_START),
	FadeInFromBlack(sync=False),
	Return(),
	DeactivateSoundChannels([0, 1, 2, 3], identifier="EVENT_1104_deactivate_sound_channels_13"),
	FadeInFromBlack(sync=False),
	Return()
])
