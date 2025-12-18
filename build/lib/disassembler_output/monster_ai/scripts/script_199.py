# 199 - BELOMEEnemy

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
	RunBattleDialog(21),
	SetTarget(MALLOW),
	Attack(Attack1),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfHPBelow(300),
	IfVarBitsClear(BV7EE004, [1]),
	SetVarBits(BV7EE004, [1]),
	RunBattleDialog(22),
	SetTarget(MARIO),
	Attack(ScrowFunkAttack),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(3),
	IfVarBitsClear(BV7EE000, [0]),
	IfTargetNotAfflictedBy(MALLOW, [Status.SCARECROW]),
	IfTargetNotAfflictedBy(MALLOW, [Status.SLEEP]),
	IfTargetAlive(MARIO),
	IfTargetAlive(MALLOW),
	SetTarget(MALLOW),
	RunBattleEvent(BE0002_BELOME_SWALLOWS_MALLOW),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE000, [0]),
	SetTarget(MARIO),
	Attack(Attack1),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(BV7EE004, [1]),
	Attack(Attack1, ScrowFunkAttack, SleepSauceAttack),
	Wait1TurnandRestartScript(),
	Attack(Attack1, Attack1, SleepSauceAttack),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsSet(BV7EE000, [0]),
	RunBattleEvent(BE0006_BELOME_SPITS_OUT_MALLOW),
	RunBattleDialog(23),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	RunBattleDialog(23),
	RunObjectSequence(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IfVarBitsSet(BV7EE000, [0]),
	IfVarEqualOrGreaterThan(BV7EE001, 2),
	ClearVarBits(BV7EE000, [0]),
	ClearVar(BV7EE005_ATTACK_PHASE_COUNTER),
	RunBattleEvent(BE0006_BELOME_SPITS_OUT_MALLOW),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	IncreaseVarBy1(BV7EE001),
	IncreaseVarBy1(BV7EE001),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IncreaseVarBy1(BV7EE001),
	Wait1TurnandRestartScript()
])