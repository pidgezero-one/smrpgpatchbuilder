# E1118_EMPTY

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
	Pause(15, identifier="EVENT_1118_pause_0"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=13, y=61, z=2, direction=EAST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkNorthwestPixels(10),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_VisibilityOn(),
		A_Pause(45),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(15),
		A_VisibilityOff()
	]),
	Pause(30),
	RunDialog(dialog_id=DI2859_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(15),
	PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_0, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_1, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_2, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_3, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_4, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_5, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_0, R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F),
	RemoveObjectFromSpecificLevel(NPC_0, R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP),
	RemoveObjectFromSpecificLevel(NPC_1, R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP),
	RemoveObjectFromSpecificLevel(NPC_0, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	RemoveObjectFromSpecificLevel(NPC_1, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	RemoveObjectFromSpecificLevel(NPC_0, R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST),
	RemoveObjectFromSpecificLevel(NPC_0, R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE),
	RemoveObjectFromSpecificLevel(NPC_1, R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE),
	RemoveObjectFromSpecificLevel(NPC_0, R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST),
	RemoveObjectFromSpecificLevel(NPC_2, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	RemoveObjectFromSpecificLevel(NPC_3, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	SetBit(SEASIDE_BOSS_SET),
	Dec(EXP_STAR_70D5),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastSteps(1),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	Return()
])
