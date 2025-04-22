import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.battlefields import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.packets import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.variables import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.types.classes import (
    UsableActionScriptCommand,
)
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
    #
    # Basic (no defined GOTOs) command tests
    #
    Case(
        "Jump to script",
        commands_factory=lambda: [A_JmpToScript(1000)],
        expected_bytes=[0xD0, 0xE8, 0x03],
    ),
    Case(
        "Loop",
        commands_factory=lambda: [A_StartLoopNTimes(100), A_EndLoop()],
        expected_bytes=[0xD4, 0x64, 0xD7],
    ),
    Case(
        "Pausing (max)",
        commands_factory=lambda: [A_Pause(256), A_Pause(65536)],
        expected_bytes=[0xF0, 0xFF, 0xF1, 0xFF, 0xFF],
    ),
    Case(
        "Pausing (min)",
        commands_factory=lambda: [A_Pause(1), A_Pause(0x101)],
        expected_bytes=[0xF0, 0x00, 0xF1, 0x00, 0x01],
    ),
    Case(
        "Jump to start",
        commands_factory=lambda: [
            A_StopSound(),
            A_JmpToStartOfThisScript(),
            A_JmpToStartOfThisScriptFA(),
        ],
        expected_bytes=[0x9B, 0xF9, 0xFA],
    ),
    Case(
        "Visibility & prop reset",
        commands_factory=lambda: [
            A_VisibilityOn(),
            A_VisibilityOff(),
            A_ResetProperties(),
        ],
        expected_bytes=[0x00, 0x01, 0x09],
    ),
    #
    # Tests with defined GOTOs
    #
    Case(
        "Basic GOTO",
        commands_factory=lambda: [
            A_StopSound(),
            A_Set700CToTappedButton(identifier="jmp_here"),
            A_Jmp(destinations=["jmp_here"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x03, 0x00],
    ),
    Case(
        "Should fail if GOTO destination doesn't match anything",
        commands_factory=lambda: [
            A_StopSound(),
            A_Set700CToTappedButton(identifier="jmp_fails"),
            A_Jmp(destinations=["jmp_here"]),
        ],
        exception="couldn't find destination jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should fail if GOTO finds multiple matches",
        commands_factory=lambda: [
            A_StopSound(),
            A_Set700CToTappedButton(identifier="jmp_here"),
            A_Jmp(destinations=["jmp_here"]),
            A_ReturnQueue(identifier="jmp_here"),
        ],
        exception="duplicate command identifier found: jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Jump to subroutine",
        commands_factory=lambda: [
            A_StopSound(),
            A_JmpToSubroutine(destinations=["jmp_here"]),
            A_ReturnQueue(),
            A_Set700CToTappedButton(identifier="jmp_here"),
            A_ReturnAll(),
        ],
        expected_bytes=[0x9B, 0xD3, 0x07, 0x00, 0xFE, 0xCB, 0xFF],
    ),
    #
    # Unknown command tests
    #
    Case(
        "Valid unknown command",
        commands_factory=lambda: [
            A_UnknownCommand(bytearray([0x24, 0xAB, 0xCD, 0xFE, 0x69])),
        ],
        expected_bytes=[0x24, 0xAB, 0xCD, 0xFE, 0x69],
    ),
    Case(
        "Unknown command with wrong length should fail",
        commands_factory=lambda: [A_UnknownCommand(bytearray([0x24, 0xAB, 0xCD]))],
        exception="opcode 0x24 expects 5 total bytes (inclusive), got 3 bytes instead",
        exception_type=InvalidCommandArgumentException,
    ),
    Case(
        "Unknown command using an assigned opcode should fail",
        commands_factory=lambda: [A_UnknownCommand(bytearray([0x01, 0x02, 0x03]))],
        exception="do not use A_UnknownCommand for opcode 0x01, there is already a class for it",
        exception_type=InvalidCommandArgumentException,
    ),
    Case(
        "Valid unknown command (FD)",
        commands_factory=lambda: [
            A_UnknownCommand(bytearray([0xFD, 0xFF])),
        ],
        expected_bytes=[0xFD, 0xFF],
    ),
    Case(
        "Unknown command with wrong length should fail (FD)",
        commands_factory=lambda: [A_UnknownCommand(bytearray([0xFD, 0xFF, 0x01]))],
        exception="opcode 0xFD 0xFF expects 2 total bytes (inclusive), got 3 bytes instead",
        exception_type=InvalidCommandArgumentException,
    ),
    Case(
        "Unknown command using an assigned opcode should fail (FD)",
        commands_factory=lambda: [A_UnknownCommand(bytearray([0xFD, 0xB0, 0x01]))],
        exception="do not use A_UnknownCommand for opcode 0xFD 0xB0, there is already a class for it",
        exception_type=InvalidCommandArgumentException,
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.exception and case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            script = ActionScript(commands)
            bank = ActionScriptBank(
                pointer_table_start=0x210000,
                start=0x210002,
                end=0x21FFFF,
                scripts=[script],
                count=1,
            )
            bank.render()

        assert case.exception in str(exc_info.value)

    elif case.expected_bytes:
        commands = case.commands_factory()
        script = ActionScript(commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = ActionScriptBank(
            pointer_table_start=0x210000,
            start=0x210002,
            end=0x210002 + len(expected_bytes),
            scripts=[script],
            count=1,
        )
        assert bank.render() == bytearray([0x02, 0x00]) + expected_bytes

    else:
        raise ValueError("At least one of exception or expected_bytes must be set.")
