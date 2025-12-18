# E2272_MOLEVILLE_TREASURE_SHOP

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
	JmpIfBitSet(BELOME_HEAD_1, ["EVENT_2272_run_dialog_4"]),
	RunDialog(dialog_id=DI2902_TREASURE_SELLER_ALL_ITEMS_UNLOCKED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(BELOME_HEAD_1),
	Jmp(["EVENT_2272_jmp_if_bit_set_6"]),
	RunDialog(dialog_id=DI2905_TREASURE_SELLER_3RD_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_4"),
	Jmp(["EVENT_2272_jmp_if_bit_set_6"]),
	JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_2272_jmp_if_bit_clear_62"], identifier="EVENT_2272_jmp_if_bit_set_6"),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_2272_jmp_if_bit_clear_28"]),
	Jmp(["EVENT_2272_jmp_if_bit_clear_9"]),
	JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_12"], identifier="EVENT_2272_jmp_if_bit_clear_9"),
	RunDialog(dialog_id=DI2913_TREASURE_SELLER_TEMPORARILY_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_27"], identifier="EVENT_2272_jmp_if_bit_set_12"),
	RunDialog(dialog_id=DI2911_TREASURE_SELLER_ITEM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_27"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_25"]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_1_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(LuckyJewelItem),
	Jmp(["EVENT_2272_jmp_27"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_25"),
	Jmp(["EVENT_2272_jmp_27"]),
	Jmp(["EVENT_2272_run_dialog_112"], identifier="EVENT_2272_jmp_27"),
	JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_32"], identifier="EVENT_2272_jmp_if_bit_clear_28"),
	JmpIfBitClear(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_32"]),
	RunDialog(dialog_id=DI2913_TREASURE_SELLER_TEMPORARILY_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_47"], identifier="EVENT_2272_jmp_if_bit_set_32"),
	RunDialog(dialog_id=DI2911_TREASURE_SELLER_ITEM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_47"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_45"]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_1_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(LuckyJewelItem),
	Jmp(["EVENT_2272_jmp_if_bit_set_47"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_45"),
	Jmp(["EVENT_2272_jmp_if_bit_set_47"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_run_dialog_112"], identifier="EVENT_2272_jmp_if_bit_set_47"),
	RunDialog(dialog_id=DI2908_TREASURE_SELLER_ITEM_2, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_run_dialog_112"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 200),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_45"]),
	SetVarToConst(PRIMARY_TEMP_7000, 200),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_2_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(MysteryEggItem),
	Jmp(["EVENT_2272_run_dialog_112"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_2272_run_dialog_112"]),
	JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_67"], identifier="EVENT_2272_jmp_if_bit_clear_62"),
	JmpIfBitClear(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_67"]),
	JmpIfBitClear(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2272_jmp_if_bit_set_67"]),
	RunDialog(dialog_id=DI2913_TREASURE_SELLER_TEMPORARILY_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2272_jmp_if_bit_set_82"], identifier="EVENT_2272_jmp_if_bit_set_67"),
	RunDialog(dialog_id=DI2911_TREASURE_SELLER_ITEM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_82"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_80"]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_1_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(LuckyJewelItem),
	Jmp(["EVENT_2272_jmp_if_bit_set_82"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_80"),
	Jmp(["EVENT_2272_jmp_if_bit_set_82"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2272_jmp_if_bit_set_97"], identifier="EVENT_2272_jmp_if_bit_set_82"),
	RunDialog(dialog_id=DI2908_TREASURE_SELLER_ITEM_2, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_jmp_if_bit_set_97"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 200),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_95"]),
	SetVarToConst(PRIMARY_TEMP_7000, 200),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_2_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(MysteryEggItem),
	Jmp(["EVENT_2272_jmp_if_bit_set_97"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_95"),
	Jmp(["EVENT_2272_jmp_if_bit_set_97"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2272_run_dialog_112"], identifier="EVENT_2272_jmp_if_bit_set_97"),
	RunDialog(dialog_id=DI2914_TREASURE_SELLER_ITEM_3, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2272_run_dialog_112"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 300),
	JmpIfComparisonResultIsLesser(["EVENT_2272_run_dialog_110"]),
	SetVarToConst(PRIMARY_TEMP_7000, 300),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_3_PURCHASED),
	PlaySound(sound=SO085_FLOWER, channel=6),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	AddToInventory(FryingPanItem),
	Jmp(["EVENT_2272_run_dialog_112"]),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_110"),
	Jmp(["EVENT_2272_run_dialog_112"]),
	RunDialog(dialog_id=DI2909_TREASURE_SELLER_ALL_IVE_GOT_FOR_NOW, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2272_run_dialog_112"),
	Return()
])
