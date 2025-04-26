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
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    Case(
        label="attack timer begins",
        commands_factory=lambda: [
            AttackTimerBegins(identifier="label"),
        ],
        expected_bytes=[
            0x3A,
        ],
    )
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.exception is not None and case.exception_type is not None:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = AnimationScript(commands)
            bank = AnimationScriptBank(
                name=case.label,
                pointer_table_start=0x35C000,
                start=0x35C002,
                end=0x35CFFF,
                scripts=[script],
            )
            bank.render()
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = AnimationScript(commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = AnimationScriptBank(
            name=case.label,
            pointer_table_start=0x35C000,
            start=0x35C002,
            end=0x35C002 + len(expected_bytes),
            scripts=[script],
        )
        assert bank.render() == bytearray([0x02, 0xC0]) + expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
