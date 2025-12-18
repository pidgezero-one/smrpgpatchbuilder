# E3297_SEA_SHOP

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
	JmpIfBitSet(SEASIDE_BOSS_AVAILABLE, ["EVENT_3297_run_dialog_3"]),
	RunDialog(dialog_id=DI1680_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3297_store_coin_amount_7000_4"]),
	RunDialog(dialog_id=DI1681_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3297_run_dialog_3"),
	StoreCoinCountTo7000(identifier="EVENT_3297_store_coin_amount_7000_4"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	OpenShop(SH07_SEA_AND_SHIP_SHAMAN),
	FadeInFromBlack(sync=False),
	StoreCoinCountTo7000(),
	Compare7000ToVar(SECONDARY_TEMP_7024),
	JmpIfLoadedMemoryIs0(["EVENT_3297_run_dialog_15"]),
	JmpIfBitSet(SEASIDE_BOSS_AVAILABLE, ["EVENT_3297_run_dialog_15"]),
	SetBit(SEASIDE_BOSS_AVAILABLE),
	RunDialog(dialog_id=DI1683_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	RunDialog(dialog_id=DI1682_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3297_run_dialog_15"),
	Return()
])
