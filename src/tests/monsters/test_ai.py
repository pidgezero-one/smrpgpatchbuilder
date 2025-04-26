import pytest
from typing import Optional, Type, List
from dataclasses import dataclass

from smrpgpatchbuilder.datatypes.enemies.implementations import *
from smrpgpatchbuilder.datatypes.items.implementations import *
from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.ids.battle_events import *
from smrpgpatchbuilder.datatypes.monster_scripts.types import MonsterScriptBank

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
    IdentifierException,
    InvalidCommandArgumentException,
    InvalidOpcodeException,
    RenderException,
)


@dataclass
class Case:
    label: str
    commands_factory: callable
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    Case(
        label="Attack",
        commands_factory=lambda: [Attack(PhysicalAttack102)],
        expected_bytes=[0x66],
    ),
    Case(label="Attack x3", commands_factory=lambda: [Attack()], expected_bytes=[]),
    Case(label="SetTarget", commands_factory=lambda: [SetTarget()], expected_bytes=[]),
    Case(
        label="RunBattleDialog",
        commands_factory=lambda: [RunBattleDialog()],
        expected_bytes=[],
    ),
    Case(
        label="RunBattleEvent",
        commands_factory=lambda: [RunBattleEvent()],
        expected_bytes=[],
    ),
    Case(
        label="IncreaseVarBy1",
        commands_factory=lambda: [IncreaseVarBy1()],
        expected_bytes=[],
    ),
    Case(
        label="DecreaseVarBy1",
        commands_factory=lambda: [DecreaseVarBy1()],
        expected_bytes=[],
    ),
    Case(
        label="SetVarBits", commands_factory=lambda: [SetVarBits()], expected_bytes=[]
    ),
    Case(
        label="ClearVarBits",
        commands_factory=lambda: [ClearVarBits()],
        expected_bytes=[],
    ),
    Case(label="ClearVar", commands_factory=lambda: [ClearVar()], expected_bytes=[]),
    Case(
        label="RemoveTarget",
        commands_factory=lambda: [RemoveTarget()],
        expected_bytes=[],
    ),
    Case(
        label="CallTarget", commands_factory=lambda: [CallTarget()], expected_bytes=[]
    ),
    Case(
        label="MakeInvulnerable",
        commands_factory=lambda: [MakeInvulnerable()],
        expected_bytes=[],
    ),
    Case(
        label="MakeVulnerable",
        commands_factory=lambda: [MakeVulnerable()],
        expected_bytes=[],
    ),
    Case(
        label="ExitBattle", commands_factory=lambda: [ExitBattle()], expected_bytes=[]
    ),
    Case(
        label="Set7EE005ToRandomNumber",
        commands_factory=lambda: [Set7EE005ToRandomNumber()],
        expected_bytes=[],
    ),
    Case(label="CastSpell", commands_factory=lambda: [CastSpell()], expected_bytes=[]),
    Case(
        label="DoMonsterBehaviour",
        commands_factory=lambda: [DoMonsterBehaviour()],
        expected_bytes=[],
    ),
    Case(
        label="SetUntargetable",
        commands_factory=lambda: [SetUntargetable()],
        expected_bytes=[],
    ),
    Case(
        label="SetTargetable",
        commands_factory=lambda: [SetTargetable()],
        expected_bytes=[],
    ),
    Case(
        label="EnableCommand",
        commands_factory=lambda: [EnableCommand()],
        expected_bytes=[],
    ),
    Case(
        label="DisableCommand",
        commands_factory=lambda: [DisableCommand()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveAllInventory",
        commands_factory=lambda: [RemoveAllInventory()],
        expected_bytes=[],
    ),
    Case(
        label="RestoreInventory",
        commands_factory=lambda: [RestoreInventory()],
        expected_bytes=[],
    ),
    Case(label="DoNothing", commands_factory=lambda: [DoNothing()], expected_bytes=[]),
    Case(
        label="IfTargetedByCommand",
        commands_factory=lambda: [IfTargetedByCommand()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetedBySpell",
        commands_factory=lambda: [IfTargetedBySpell()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetedByItem",
        commands_factory=lambda: [IfTargetedByItem()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetedByElement",
        commands_factory=lambda: [IfTargetedByElement()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetedByRegularAttack",
        commands_factory=lambda: [IfTargetedByRegularAttack()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetHPBelow",
        commands_factory=lambda: [IfTargetHPBelow()],
        expected_bytes=[],
    ),
    Case(label="IfHPBelow", commands_factory=lambda: [IfHPBelow()], expected_bytes=[]),
    Case(
        label="IfTargetAfflictedBy",
        commands_factory=lambda: [IfTargetAfflictedBy()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetNotAfflictedBy",
        commands_factory=lambda: [IfTargetNotAfflictedBy()],
        expected_bytes=[],
    ),
    Case(
        label="IfTurnCounterEquals",
        commands_factory=lambda: [IfTurnCounterEquals()],
        expected_bytes=[],
    ),
    Case(
        label="IfVarLessThan",
        commands_factory=lambda: [IfVarLessThan()],
        expected_bytes=[],
    ),
    Case(
        label="IfVarEqualOrGreaterThan",
        commands_factory=lambda: [IfVarEqualOrGreaterThan()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetAlive",
        commands_factory=lambda: [IfTargetAlive()],
        expected_bytes=[],
    ),
    Case(
        label="IfTargetKOed",
        commands_factory=lambda: [IfTargetKOed()],
        expected_bytes=[],
    ),
    Case(
        label="IfVarBitsSet",
        commands_factory=lambda: [IfVarBitsSet()],
        expected_bytes=[],
    ),
    Case(
        label="IfVarBitsClear",
        commands_factory=lambda: [IfVarBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="IfCurrentlyInFormationID",
        commands_factory=lambda: [IfCurrentlyInFormationID()],
        expected_bytes=[],
    ),
    Case(
        label="IfLastMonsterStanding",
        commands_factory=lambda: [IfLastMonsterStanding()],
        expected_bytes=[],
    ),
    Case(label="Wait1Turn", commands_factory=lambda: [Wait1Turn()], expected_bytes=[]),
    Case(
        label="Wait1TurnandRestartScript",
        commands_factory=lambda: [Wait1TurnandRestartScript()],
        expected_bytes=[],
    ),
    Case(
        label="StartCounterCommands",
        commands_factory=lambda: [StartCounterCommands()],
        expected_bytes=[],
    ),
    Case(
        label="UnknownCommand",
        commands_factory=lambda: [UnknownCommand()],
        expected_bytes=[],
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.expected_bytes is not None and len(case.expected_bytes) == 0:
        return
    if case.exception or case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = MonsterScript(commands)
            bank = MonsterScriptBank(
                scripts=[script],
                range_1_start=0x393002,
                range_1_end=0x393FFF,
                pointer_table_start=0x393000,
            )
            bank.render()
        if case.exception:
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = MonsterScript(commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = MonsterScriptBank(
            scripts=[script],
            range_1_start=0x393002,
            range_1_end=0x393002 + len(case.expected_bytes),
            pointer_table_start=0x393000,
        )
        output = bank.render()
        assert output[0] == bytearray([0x02, 0x30]) + expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
