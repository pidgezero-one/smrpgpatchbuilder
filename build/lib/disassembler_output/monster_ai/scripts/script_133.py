# 133 - UnnamedEnemyEnemy2

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
	IfCurrentlyInFormationID(402),
	CastSpell(DrainSpell, DrainSpell, MegaDrainSpell),
	Wait1TurnandRestartScript(),
	Attack(Attack2),
	Wait1Turn(),
	Attack(Attack2),
	Wait1Turn(),
	CastSpell(FlameWallSpell),
	Wait1Turn(),
	StartCounterCommands(),
	Wait1TurnandRestartScript()
])