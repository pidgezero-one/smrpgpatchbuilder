# 160 - UnnamedEnemyEnemy3

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
	IfVarBitsClear(BV7EE004, [0]),
	SetVarBits(BV7EE004, [0]),
	SetUntargetable(SELF),
	RunBattleDialog(24),
	RunBattleDialog(25),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(3),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	RunBattleDialog(14),
	Wait1TurnandRestartScript(),
	StartCounterCommands()
])