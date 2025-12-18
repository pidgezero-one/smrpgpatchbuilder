# E2425_FOREST_MAZE_SECRET_LOADER

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
	SetBit(FOREST_MAZE_SECRET_FOUND),
	ClearBit(DIRECTIONAL_7047_1),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_6"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_7, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_6"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_13, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_6"]),
	Jmp(["EVENT_2425_jmp_if_object_trigger_disabled_9"]),
	DisableObjectTriggerInSpecificLevel(NPC_1, R234_FOREST_MAZE_SECRET, identifier="EVENT_2425_disable_trigger_in_level_6"),
	DisableObjectTriggerInSpecificLevel(NPC_7, R234_FOREST_MAZE_SECRET),
	DisableObjectTriggerInSpecificLevel(NPC_13, R234_FOREST_MAZE_SECRET),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_2, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_13"], identifier="EVENT_2425_jmp_if_object_trigger_disabled_9"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_8, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_13"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_14, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_13"]),
	Jmp(["EVENT_2425_jmp_if_object_trigger_disabled_16"]),
	DisableObjectTriggerInSpecificLevel(NPC_2, R234_FOREST_MAZE_SECRET, identifier="EVENT_2425_disable_trigger_in_level_13"),
	DisableObjectTriggerInSpecificLevel(NPC_8, R234_FOREST_MAZE_SECRET),
	DisableObjectTriggerInSpecificLevel(NPC_14, R234_FOREST_MAZE_SECRET),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_3, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_20"], identifier="EVENT_2425_jmp_if_object_trigger_disabled_16"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_9, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_20"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_15, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_20"]),
	Jmp(["EVENT_2425_jmp_if_object_trigger_disabled_23"]),
	DisableObjectTriggerInSpecificLevel(NPC_3, R234_FOREST_MAZE_SECRET, identifier="EVENT_2425_disable_trigger_in_level_20"),
	DisableObjectTriggerInSpecificLevel(NPC_9, R234_FOREST_MAZE_SECRET),
	DisableObjectTriggerInSpecificLevel(NPC_15, R234_FOREST_MAZE_SECRET),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_27"], identifier="EVENT_2425_jmp_if_object_trigger_disabled_23"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_10, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_27"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_16, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_27"]),
	Jmp(["EVENT_2425_jmp_if_object_trigger_disabled_30"]),
	DisableObjectTriggerInSpecificLevel(NPC_4, R234_FOREST_MAZE_SECRET, identifier="EVENT_2425_disable_trigger_in_level_27"),
	DisableObjectTriggerInSpecificLevel(NPC_10, R234_FOREST_MAZE_SECRET),
	DisableObjectTriggerInSpecificLevel(NPC_16, R234_FOREST_MAZE_SECRET),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_34"], identifier="EVENT_2425_jmp_if_object_trigger_disabled_30"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_11, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_34"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_17, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_34"]),
	Jmp(["EVENT_2425_jmp_if_object_trigger_disabled_37"]),
	DisableObjectTriggerInSpecificLevel(NPC_5, R234_FOREST_MAZE_SECRET, identifier="EVENT_2425_disable_trigger_in_level_34"),
	DisableObjectTriggerInSpecificLevel(NPC_11, R234_FOREST_MAZE_SECRET),
	DisableObjectTriggerInSpecificLevel(NPC_17, R234_FOREST_MAZE_SECRET),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_6, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_41"], identifier="EVENT_2425_jmp_if_object_trigger_disabled_37"),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_12, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_41"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_18, R234_FOREST_MAZE_SECRET, ["EVENT_2425_disable_trigger_in_level_41"]),
	Jmp(["EVENT_2425_jmp_if_bit_set_44"]),
	DisableObjectTriggerInSpecificLevel(NPC_6, R234_FOREST_MAZE_SECRET, identifier="EVENT_2425_disable_trigger_in_level_41"),
	DisableObjectTriggerInSpecificLevel(NPC_12, R234_FOREST_MAZE_SECRET),
	DisableObjectTriggerInSpecificLevel(NPC_18, R234_FOREST_MAZE_SECRET),
	JmpIfBitSet(UNKNOWN_ROSE_TOWN_7060_5, ["EVENT_2425_remove_from_current_level_74"], identifier="EVENT_2425_jmp_if_bit_set_44"),
	JmpIfBitSet(UNKNOWN_ROSE_TOWN_7060_6, ["EVENT_2425_remove_from_current_level_60"]),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromCurrentLevel(NPC_11),
	RemoveObjectFromCurrentLevel(NPC_12),
	RemoveObjectFromCurrentLevel(NPC_13),
	RemoveObjectFromCurrentLevel(NPC_14),
	RemoveObjectFromCurrentLevel(NPC_15),
	RemoveObjectFromCurrentLevel(NPC_16),
	RemoveObjectFromCurrentLevel(NPC_17),
	RemoveObjectFromCurrentLevel(NPC_18),
	Jmp(["EVENT_2425_jmp_87"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_2425_remove_from_current_level_60"),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_13),
	RemoveObjectFromCurrentLevel(NPC_14),
	RemoveObjectFromCurrentLevel(NPC_15),
	RemoveObjectFromCurrentLevel(NPC_16),
	RemoveObjectFromCurrentLevel(NPC_17),
	RemoveObjectFromCurrentLevel(NPC_18),
	Jmp(["EVENT_2425_jmp_87"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_2425_remove_from_current_level_74"),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromCurrentLevel(NPC_11),
	RemoveObjectFromCurrentLevel(NPC_12),
	RemoveObjectFromCurrentLevel(NPC_14),
	Jmp(["EVENT_2418_play_sound_63"], identifier="EVENT_2425_jmp_87")
])
