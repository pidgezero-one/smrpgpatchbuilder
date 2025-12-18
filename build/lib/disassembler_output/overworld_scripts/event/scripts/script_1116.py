# E1116_JUICE_BAR

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
	JmpIfBitSet(UNKNOWN_7087_6, ["EVENT_1116_run_dialog_4"]),
	RunDialog(dialog_id=DI2654_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7087_6),
	Jmp(["EVENT_1116_jmp_if_bit_set_5"]),
	RunDialog(dialog_id=DI2655_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1116_run_dialog_4"),
	JmpIfBitSet(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1116_jmp_if_bit_set_26"], identifier="EVENT_1116_jmp_if_bit_set_5"),
	JmpIfBitSet(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1116_jmp_if_bit_set_20"]),
	JmpIfBitSet(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1116_jmp_if_bit_set_14"]),
	JmpIfBitSet(UNKNOWN_7087_3, ["EVENT_1116_open_shop_11"]),
	RunDialog(dialog_id=DI2656_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7087_3),
	OpenShop(SH09_JUICE_BAR_BASE, identifier="EVENT_1116_open_shop_11"),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(UNKNOWN_7087_4, ["EVENT_1116_open_shop_17"], identifier="EVENT_1116_jmp_if_bit_set_14"),
	RunDialog(dialog_id=DI2657_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7087_4),
	OpenShop(SH10_JUICE_BAR_ALTO, identifier="EVENT_1116_open_shop_17"),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(UNKNOWN_7087_5, ["EVENT_1116_open_shop_23"], identifier="EVENT_1116_jmp_if_bit_set_20"),
	RunDialog(dialog_id=DI2658_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7087_5),
	OpenShop(SH11_JUICE_BAR_TENOR, identifier="EVENT_1116_open_shop_23"),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(UNKNOWN_7093_2, ["EVENT_1116_open_shop_29"], identifier="EVENT_1116_jmp_if_bit_set_26"),
	RunDialog(dialog_id=DI2659_EMPTY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(UNKNOWN_7093_2),
	OpenShop(SH12_JUICE_BAR_SOPRANO, identifier="EVENT_1116_open_shop_29"),
	FadeInFromBlack(sync=False),
	Return()
])
