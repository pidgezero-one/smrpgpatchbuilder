import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts import *
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
from smrpgpatchbuilder.datatypes.dialogs.ids.dialog_ids import *
from smrpgpatchbuilder.datatypes.items.implementations import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
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
    commands: List[UsableEventScriptCommand]
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None


test_cases = [
    #
    # Basic (no GOTOs) command tests
    #
    Case(
        "Loop 10 frames",
        commands=[StartLoopNFrames(10)],
        expected_bytes=[0xD5, 0x0A, 0x00],
    ),
    #
    # Tests with GOTOs
    #
    Case(
        "Basic GOTO",
        commands=[
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_here"),
            Jmp(destinations=["jmp_here"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x03, 0x00],
    ),
    Case(
        "Should fail if GOTO destination doesn't match anything",
        commands=[
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_fails"),
            Jmp(destinations=["jmp_here"]),
        ],
        exception="couldn't find destination jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should fail if GOTO finds multiple matches",
        commands=[
            StopSound(),
            Set7000ToTappedButton(identifier="jmp_here"),
            Jmp(destinations=["jmp_here"]),
            Return(identifier="jmp_here"),
        ],
        exception="duplicate command identifier found: jmp_here",
        exception_type=IdentifierException,
    ),
    Case(
        "Should not fail if GOTO destination uses illegal override format",
        commands=[
            StopSound(),
            Set7000ToTappedButton(),
            Jmp(destinations=["ILLEGAL_JUMP_0001"]),
        ],
        expected_bytes=[0x9B, 0xCB, 0xD2, 0x01, 0x00],
    ),
    #
    # Non-embedded action queue tests
    #
    Case(
        "NEAQ already in desired position",
        commands=[
            StopSound(),
            StopSound(),
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x03, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        expected_bytes=[0x9B, 0x9B, 0x9B, 0xAD, 0x0A, 0x00],
    ),
    Case(
        "NEAQ is too early, inserts dummy commands to make up the difference",
        commands=[
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x05, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        expected_bytes=[0x9B, 0x9B, 0x9B, 0x9B, 0x9B, 0xAD, 0x0A, 0x00],
    ),
    Case(
        "NEAQ should fail if it would be rendered after required offset",
        commands=[
            StopSound(),
            StopSound(),
            NonEmbeddedActionQueue(
                required_offset=0x01, subscript=[A_AddConstToVar(PRIMARY_TEMP_700C, 10)]
            ),
        ],
        exception="too many commands in script 0 before non-embedded action queue",
        exception_type=ScriptBankTooLongException,
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.exception is not None and case.exception_type is not None:
        with pytest.raises(case.exception_type) as exc_info:
            script = EventScript(case.commands)
            bank = EventScriptBank(0x1E0000, 0x1E0002, 0x1EFFFF, [script])
            bank.render()
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        script = EventScript(case.commands)
        expected_bytes = bytearray(case.expected_bytes)
        bank = EventScriptBank(
            0x1E0000, 0x1E0002, 0x1E0002 + len(expected_bytes), [script]
        )
        assert bank.render() == bytearray([0x02, 0x00]) + expected_bytes
    else:
        raise "At least one of exception or expected_bytes needs to be set"
