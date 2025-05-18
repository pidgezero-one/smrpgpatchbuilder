# Special test file to test proper assembly of subroutines or bankless scripts

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
    expected_size: int
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    Case(
        label="assemble a bankless script",
        commands_factory=lambda: [
            AttackTimerBegins(identifier="start_command"),
            SetAMEM60ToCurrentTarget(),
            GameOverIfNoAlliesStanding(),
            PauseScriptUntilSpriteSequenceDone(),
            Jmp(["start_command"]),
            SetOMEM60To072C(),
            EnableSpritesOnSubscreen(),
        ],
        expected_bytes=[
            0x3A,  # true start of script
            0x45,
            0x46,
            0x4E,
            0x09,
            0x00,  # short, addr = true beginning of script ("start_command")
            0xF0,
            0x69,
            0x70,
        ],
        expected_size=9,
    ),
    Case(
        label="error if bankless script doesn't match expected size",
        commands_factory=lambda: [
            AttackTimerBegins(identifier="start_command"),
            SetAMEM60ToCurrentTarget(),
            GameOverIfNoAlliesStanding(),
            PauseScriptUntilSpriteSequenceDone(),
            Jmp(["start_command"]),
            SetOMEM60To072C(),
            EnableSpritesOnSubscreen(),
        ],
        expected_size=12,
        exception_type=AssertionError,
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.exception or case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = SubroutineOrBanklessScript(
                expected_size=case.expected_size, script=commands
            )
            bank = AnimationScriptBank(
                name=case.label,
                start=0x02F000,
                end=0x02FFFF,
                scripts=[script],
            )
            c = AnimationScriptBankCollection([bank])
            c.render()
        if case.exception:
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = SubroutineOrBanklessScript(
            expected_size=case.expected_size, script=commands
        )
        expected_bytes = bytearray(case.expected_bytes)
        bank = AnimationScriptBank(
            name=case.label,
            start=0x02F000,
            end=0x02F000 + len(expected_bytes),
            scripts=[script],
        )
        c = AnimationScriptBankCollection([bank])
        comp = c.render()
        assert comp[bank.start] == expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
