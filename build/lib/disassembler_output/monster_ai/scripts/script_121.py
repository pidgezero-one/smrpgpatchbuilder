# 121 - Booster1Enemy

from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import DoNothing
from ...variables.battle_event_names import *
from ...variables.battle_variable_names import *
from ...items.items import *
from ...spells.spells import *
from ...enemies.enemies import *
from ...enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *

script = MonsterScript([
	IfVarBitsClear(BV7EE009, [0]),
	SetVarBits(BV7EE009, [0]),
	RunBattleDialog(68),
	SetUntargetable(MONSTER_1_SET),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript(),
	StartCounterCommands()
])