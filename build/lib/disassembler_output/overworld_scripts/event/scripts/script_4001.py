# E4001_CLONE_RESERVED

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
	AddToInventory(BaneBombItem),
	AddToInventory(ShinyStoneItem),
	AddToInventory(MuteBombItem),
	CharacterJoinsParty(GENO),
	CharacterJoinsParty(BOWSER),
	EquipItemToCharacter(PantsItem, BOWSER),
	EquipItemToCharacter(SpareItem, GENO),
	StartBattleAtBattlefield(PACK250_AXEM_YELLOW_ALONE, BF42_BELOME_TEMPLE),
	EnterArea(room_id=R006_MARRYMORE_INN_2F, face_direction=NORTHEAST, x=15, y=48, z=2, run_entrance_event=True),
	FadeInFromBlack(sync=False),
	Return(),
	JmpToEvent(E4000_CLONE_RESERVED),
	SetBit(UNKNOWN_709D_2),
	Set7000To7FMemVar(0xFFA0),
	Inc(PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1023_DEBUG_MENU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True)
])
