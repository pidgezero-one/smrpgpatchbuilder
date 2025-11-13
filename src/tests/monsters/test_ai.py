import pytest
from typing import Optional, Type, List
from dataclasses import dataclass

from disassembler_output.spells.spells import CharacterSpell, EnemySpell
from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttack
from smrpgpatchbuilder.datatypes.items.classes import RegularItem
from smrpgpatchbuilder.datatypes.monster_scripts import *
from smrpgpatchbuilder.datatypes.monster_scripts.arguments.types.classes import DoNothing
from smrpgpatchbuilder.datatypes.monster_scripts.commands import *
from smrpgpatchbuilder.datatypes.monster_scripts.types import MonsterScriptBank
from smrpgpatchbuilder.datatypes.monster_scripts.arguments import *
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status
class DUMMYAttack5(EnemyAttack):
    _index = 102

class DUMMYAttack2(EnemyAttack):
    _index = 98

class FangsAttack(EnemyAttack):
    _index = 67


class BigBangSpell(EnemySpell):
    _index = 103

class KnockOutSpell(EnemySpell):
    _index = 95

class DrainSpell(EnemySpell):
    _index = 64


class SuperJumpSpell(CharacterSpell):
    _index = 2

class ThunderboltSpell(CharacterSpell):
    _index = 21

class GenoBeamSpell(CharacterSpell):
    _index = 16

class StarEggItem(RegularItem):
    _item_id: int = 176

class RockCandyItem(RegularItem):
    _item_id: int = 131

class FireBombItem(RegularItem):
    _item_id: int = 113

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
        commands_factory=lambda: [Attack(DUMMYAttack5)],
        expected_bytes=[0x66, 0xFF, 0xFF],
    ),
    Case(
        label="Attack x3",
        commands_factory=lambda: [Attack(DoNothing, DUMMYAttack2, FangsAttack)],
        expected_bytes=[0xE0, 0xFB, 0x62, 0x43, 0xFF, 0xFF],
    ),
    Case(
        label="SetTarget",
        commands_factory=lambda: [SetTarget(MONSTER_2_SET)],
        expected_bytes=[0xE2, 0x14, 0xFF, 0xFF],
    ),
    Case(
        label="RunBattleDialog",
        commands_factory=lambda: [RunBattleDialog(16)],
        expected_bytes=[0xE3, 0x10, 0xFF, 0xFF],
    ),
    Case(
        label="RunBattleEvent",
        commands_factory=lambda: [
            RunBattleEvent(21)
        ],
        expected_bytes=[0xE5, 0x15, 0xFF, 0xFF],
    ),
    Case(
        label="IncreaseVarBy1",
        commands_factory=lambda: [IncreaseVarBy1(0x7EE00F)],
        expected_bytes=[0xE6, 0x00, 0x0F, 0xFF, 0xFF],
    ),
    Case(
        label="DecreaseVarBy1",
        commands_factory=lambda: [DecreaseVarBy1(0x7EE008)],
        expected_bytes=[0xE6, 0x01, 0x08, 0xFF, 0xFF],
    ),
    Case(
        label="SetVarBits",
        commands_factory=lambda: [SetVarBits(0x7EE001, [1, 4, 6])],
        expected_bytes=[0xE7, 0x00, 0x01, 0x52, 0xFF, 0xFF],
    ),
    Case(
        label="ClearVarBits",
        commands_factory=lambda: [ClearVarBits(0x7EE000, [0, 3, 7])],
        expected_bytes=[0xE7, 0x01, 0x00, 0x89, 0xFF, 0xFF],
    ),
    Case(
        label="ClearVar",
        commands_factory=lambda: [ClearVar(0x7EE006)],
        expected_bytes=[0xE8, 0x06, 0xFF, 0xFF],
    ),
    Case(
        label="RemoveTarget",
        commands_factory=lambda: [RemoveTarget(SELF)],
        expected_bytes=[0xEA, 0x00, 0x00, 0x1B, 0xFF, 0xFF],
    ),
    Case(
        label="CallTarget",
        commands_factory=lambda: [CallTarget(MALLOW)],
        expected_bytes=[0xEA, 0x01, 0x00, 0x04, 0xFF, 0xFF],
    ),
    Case(
        label="MakeInvulnerable",
        commands_factory=lambda: [MakeInvulnerable(BOWSER)],
        expected_bytes=[0xEB, 0x00, 0x02, 0xFF, 0xFF],
    ),
    Case(
        label="MakeVulnerable",
        commands_factory=lambda: [MakeVulnerable(SLOT_3)],
        expected_bytes=[0xEB, 0x01, 0x12, 0xFF, 0xFF],
    ),
    Case(
        label="ExitBattle",
        commands_factory=lambda: [ExitBattle()],
        expected_bytes=[0xEC, 0xFF, 0xFF],
    ),
    Case(
        label="Set7EE005ToRandomNumber",
        commands_factory=lambda: [Set7EE005ToRandomNumber(7)],
        expected_bytes=[0xED, 0x07, 0xFF, 0xFF],
    ),
    Case(
        label="CastSpell",
        commands_factory=lambda: [CastSpell(BigBangSpell)],
        expected_bytes=[0xEF, 0x67, 0xFF, 0xFF],
    ),
    Case(
        label="CastSpell x3",
        commands_factory=lambda: [CastSpell(KnockOutSpell, DrainSpell, DoNothing)],
        expected_bytes=[0xF0, 0x5F, 0x40, 0xFB, 0xFF, 0xFF],
    ),
    Case(
        label="RunObjectSequence",
        commands_factory=lambda: [RunObjectSequence(3)],
        expected_bytes=[0xF1, 0x03, 0xFF, 0xFF],
    ),
    Case(
        label="SetUntargetable",
        commands_factory=lambda: [SetUntargetable(MONSTER_6_SET)],
        expected_bytes=[0xF2, 0x00, 0x06, 0xFF, 0xFF],
    ),
    Case(
        label="SetTargetable",
        commands_factory=lambda: [SetTargetable(MONSTER_1_SET)],
        expected_bytes=[0xF2, 0x01, 0x01, 0xFF, 0xFF],
    ),
    Case(
        label="EnableCommand",
        commands_factory=lambda: [
            EnableCommand(commands=[COMMAND_ATTACK, COMMAND_SPECIAL])
        ],
        expected_bytes=[0xF3, 0x00, 0x03, 0xFF, 0xFF],
    ),
    Case(
        label="DisableCommand",
        commands_factory=lambda: [
            DisableCommand(commands=[COMMAND_SPECIAL, COMMAND_ITEM])
        ],
        expected_bytes=[0xF3, 0x01, 0x06, 0xFF, 0xFF],
    ),
    Case(
        label="RemoveAllInventory",
        commands_factory=lambda: [RemoveAllInventory()],
        expected_bytes=[0xF4, 0x00, 0x00, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="RestoreInventory",
        commands_factory=lambda: [RestoreInventory()],
        expected_bytes=[0xF4, 0x00, 0x01, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetedByCommand",
        commands_factory=lambda: [
            IfTargetedByCommand(commands=[COMMAND_ATTACK, COMMAND_SPECIAL])
        ],
        expected_bytes=[0xFC, 0x01, 0x02, 0x03, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetedByCommand should fail if too many commands",
        commands_factory=lambda: [
            IfTargetedByCommand(
                commands=[COMMAND_ATTACK, COMMAND_SPECIAL, COMMAND_ITEM]
            )
        ],
        exception_type=AssertionError,
    ),
    Case(
        label="IfTargetedBySpell",
        commands_factory=lambda: [IfTargetedBySpell([SuperJumpSpell, ThunderboltSpell])],
        expected_bytes=[0xFC, 0x02, 0x02, 0x15, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetedBySpell should fail if too many commands",
        commands_factory=lambda: [
            IfTargetedBySpell([SuperJumpSpell, ThunderboltSpell, GenoBeamSpell])
        ],
        exception_type=AssertionError,
    ),
    Case(
        label="IfTargetedByItem",
        commands_factory=lambda: [IfTargetedByItem([StarEggItem])],
        expected_bytes=[0xFC, 0x03, 0xB0, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetedByItem should fail if too many items",
        commands_factory=lambda: [IfTargetedByItem([StarEggItem, RockCandyItem, FireBombItem])],
        exception_type=AssertionError,
    ),
    Case(
        label="IfTargetedByElement",
        commands_factory=lambda: [IfTargetedByElement([Element.FIRE, Element.THUNDER])],
        expected_bytes=[0xFC, 0x04, 0x60, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetedByElement",
        commands_factory=lambda: [
            IfTargetedByElement(
                [Element.FIRE, Element.THUNDER, Element.JUMP, Element.ICE]
            )
        ],
        expected_bytes=[0xFC, 0x04, 0xF0, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetedByRegularAttack",
        commands_factory=lambda: [IfTargetedByRegularAttack()],
        expected_bytes=[0xFC, 0x05, 0x00, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetHPBelow",
        commands_factory=lambda: [IfTargetHPBelow(SLOT_1, 64)],
        expected_bytes=[0xFC, 0x06, 0x10, 0x04, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetHPBelow should fail if not a multiple of 16",
        commands_factory=lambda: [IfTargetHPBelow(SLOT_1, 20)],
        exception_type=AssertionError,
    ),
    Case(
        label="IfHPBelow",
        commands_factory=lambda: [IfHPBelow(999)],
        expected_bytes=[0xFC, 0x07, 0xE7, 0x03, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetAfflictedBy",
        commands_factory=lambda: [
            IfTargetAfflictedBy(SELF, [Status.MUTE, Status.POISON])
        ],
        expected_bytes=[0xFC, 0x08, 0x1B, 0x05, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetNotAfflictedBy",
        commands_factory=lambda: [
            IfTargetNotAfflictedBy(AT_LEAST_ONE_OPPONENT, [Status.INVINCIBLE])
        ],
        expected_bytes=[0xFC, 0x09, 0x24, 0x80, 0xFF, 0xFF],
    ),
    Case(
        label="IfTurnCounterEquals",
        commands_factory=lambda: [IfTurnCounterEquals(5)],
        expected_bytes=[0xFC, 0x0A, 0x05, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="IfVarLessThan",
        commands_factory=lambda: [IfVarLessThan(0x7EE006, 6)],
        expected_bytes=[0xFC, 0x0C, 0x06, 0x06, 0xFF, 0xFF],
    ),
    Case(
        label="IfVarEqualOrGreaterThan",
        commands_factory=lambda: [
            IfVarEqualOrGreaterThan(0x7EE005, 10)
        ],
        expected_bytes=[0xFC, 0x0D, 0x05, 0x0A, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetAlive",
        commands_factory=lambda: [IfTargetAlive(TOADSTOOL)],
        expected_bytes=[0xFC, 0x10, 0x00, 0x01, 0xFF, 0xFF],
    ),
    Case(
        label="IfTargetKOed",
        commands_factory=lambda: [IfTargetKOed(ALL_ALLIES_EXCLUDING_SELF)],
        expected_bytes=[0xFC, 0x10, 0x01, 0x1C, 0xFF, 0xFF],
    ),
    Case(
        label="IfVarBitsSet",
        commands_factory=lambda: [IfVarBitsSet(0x7EE001, [5, 7])],
        expected_bytes=[0xFC, 0x11, 0x01, 0xA0, 0xFF, 0xFF],
    ),
    Case(
        label="IfVarBitsSet should fail with invalid bits",
        commands_factory=lambda: [IfVarBitsSet(0x7EE001, [9])],
        exception_type=AssertionError,
    ),
    Case(
        label="IfVarBitsClear",
        commands_factory=lambda: [IfVarBitsClear(0x7EE002, [1, 3])],
        expected_bytes=[0xFC, 0x12, 0x02, 0x0A, 0xFF, 0xFF],
    ),
    Case(
        label="IfVarBitsClear should fail with invalid var",
        commands_factory=lambda: [IfVarBitsClear(0x7EE010, [1, 3])],
        exception_type=AssertionError,
    ),
    Case(
        label="IfCurrentlyInFormationID",
        commands_factory=lambda: [IfCurrentlyInFormationID(511)],
        expected_bytes=[0xFC, 0x13, 0xFF, 0x01, 0xFF, 0xFF],
    ),
    Case(
        label="IfLastMonsterStanding",
        commands_factory=lambda: [IfLastMonsterStanding()],
        expected_bytes=[0xFC, 0x14, 0x00, 0x00, 0xFF, 0xFF],
    ),
    Case(
        label="Wait1Turn",
        commands_factory=lambda: [Wait1Turn()],
        expected_bytes=[0xFD, 0xFF, 0xFF],
    ),
    Case(
        label="Wait1TurnandRestartScript",
        commands_factory=lambda: [Wait1TurnandRestartScript()],
        expected_bytes=[0xFE, 0xFF, 0xFF],
    ),
    Case(
        label="StartCounterCommands",
        commands_factory=lambda: [StartCounterCommands()],
        expected_bytes=[0xFF, 0xFF, 0xFF],
    ),
    Case(
        label="UnknownCommand",
        commands_factory=lambda: [UnknownCommand(bytearray([0x82]))],
        expected_bytes=[0x82, 0xFF],
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
        raise ValueError("At least one of exception or expected_bytes needs to be set")
