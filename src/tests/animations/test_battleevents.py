# Special test file to test proper assembly of BattleAnimationScript

import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from smrpgpatchbuilder.datatypes.enemies.implementations import *
from smrpgpatchbuilder.datatypes.items.implementations import *

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
    IdentifierException,
    InvalidCommandArgumentException,
    InvalidOpcodeException,
    RenderException,
)

from dataclasses import dataclass


@dataclass
class Case:
    label: str
    commands_factory: callable
    headers: Optional[List[str]] = None
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    Case(
        label="assemble a battle event with headers",
        commands_factory=lambda: [
            AttackTimerBegins(identifier="start_command"),
            SetAMEM60ToCurrentTarget(),
            GameOverIfNoAlliesStanding(),
            PauseScriptUntilSpriteSequenceDone(),
            Jmp(["start_command"]),
            SetOMEM60To072C(identifier="header1_name"),
            EnableSpritesOnSubscreen(identifier="header2_name"),
        ],
        expected_bytes=[
            0x08,  # header short 1: pointer to true beginning of script (offset 0x08)
            0xC0,
            0x0F,  # header short 2: pointer to header1_name (offset 0x0F)
            0xC0,
            0x10,  # header short 3: pointer to header2_name (offset 0x10)
            0xC0,
            0x3A,  # true start of script
            0x45,
            0x46,
            0x4E,
            0x09,
            0x08,  # short, addr = true beginning of script ("start_command")
            0xC0,
            0x69,
            0x70,
        ],
        headers=["header1_name", "header2_name"],
    ),
    Case(
        label="assemble a battle event with no headers",
        commands_factory=lambda: [
            AttackTimerBegins(identifier="start_command"),
            SetAMEM60ToCurrentTarget(),
            GameOverIfNoAlliesStanding(),
            PauseScriptUntilSpriteSequenceDone(),
            Jmp(["start_command"]),
            SetOMEM60To072C(identifier="header1_name"),
            EnableSpritesOnSubscreen(identifier="header2_name"),
        ],
        expected_bytes=[
            0x04,  # header short 1: pointer to true beginning of script (offset 0x04)
            0xC0,
            0x3A,  # true start of script
            0x45,
            0x46,
            0x4E,
            0x09,
            0x04,  # short, addr = true beginning of script ("start_command")
            0xC0,
            0x69,
            0x70,
        ],
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.exception or case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = BattleAnimationScript(header=case.headers, script=commands)
            bank = AnimationScriptBank(
                name=case.label,
                pointer_table_start=0x3AC000,
                start=0x3AC002,
                end=0x3ACFFF,
                scripts=[script],
            )
            c = AnimationScriptBankCollection([bank])
            c.render()
        if case.exception:
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = BattleAnimationScript(header=case.headers, script=commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = AnimationScriptBank(
            name=case.label,
            pointer_table_start=0x3AC000,
            start=0x3AC002,
            end=0x3AC002 + len(expected_bytes),
            scripts=[script],
        )
        c = AnimationScriptBankCollection([bank])
        comp = c.render()
        assert comp[bank.start] == bytearray([0x02, 0xC0]) + expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
