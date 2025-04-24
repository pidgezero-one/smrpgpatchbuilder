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
    Case(
        "Overwrite solidity",
        commands_factory=lambda: [
            A_OverwriteSolidity(
                bit_0=True,
                cant_walk_under=True,
                cant_pass_walls=True,
                cant_jump_through=True,
            ),
            A_OverwriteSolidity(
                bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
            ),
            A_OverwriteSolidity(
                bit_0=True,
                cant_pass_npcs=True,
                cant_pass_walls=True,
                bit_7=True,
            ),
            A_OverwriteSolidity(
                bit_4=True,
                cant_walk_under=True,
                cant_walk_through=True,
                cant_jump_through=True,
            ),
        ],
        expected_bytes=[0x0A, 0x0F, 0x0A, 0xF0, 0x0A, 0xA5, 0x0A, 0x5A],
    ),
    Case(
        "Set solidity",
        commands_factory=lambda: [
            A_SetSolidityBits(
                bit_0=True,
                cant_walk_under=True,
                cant_pass_walls=True,
                cant_jump_through=True,
            ),
            A_SetSolidityBits(
                bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
            ),
            A_SetSolidityBits(
                bit_0=True,
                cant_pass_npcs=True,
                cant_pass_walls=True,
                bit_7=True,
            ),
            A_SetSolidityBits(
                bit_4=True,
                cant_walk_under=True,
                cant_walk_through=True,
                cant_jump_through=True,
            ),
        ],
        expected_bytes=[0x0B, 0x0F, 0x0B, 0xF0, 0x0B, 0xA5, 0x0B, 0x5A],
    ),
    Case(
        "Clear solidity",
        commands_factory=lambda: [
            A_ClearSolidityBits(
                bit_0=True,
                cant_walk_under=True,
                cant_pass_walls=True,
                cant_jump_through=True,
            ),
            A_ClearSolidityBits(
                bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
            ),
            A_ClearSolidityBits(
                bit_0=True,
                cant_pass_npcs=True,
                cant_pass_walls=True,
                bit_7=True,
            ),
            A_ClearSolidityBits(
                bit_4=True,
                cant_walk_under=True,
                cant_walk_through=True,
                cant_jump_through=True,
            ),
        ],
        expected_bytes=[0x0C, 0x0F, 0x0C, 0xF0, 0x0C, 0xA5, 0x0C, 0x5A],
    ),
    Case(
        "Set movement bits",
        commands_factory=lambda: [
            A_SetMovementsBits(
                bit_0=True,
                cant_walk_under=True,
                cant_pass_walls=True,
                cant_jump_through=True,
            ),
            A_SetMovementsBits(
                bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
            ),
            A_SetMovementsBits(
                bit_0=True,
                cant_pass_npcs=True,
                cant_pass_walls=True,
                bit_7=True,
            ),
            A_SetMovementsBits(
                bit_4=True,
                cant_walk_under=True,
                cant_walk_through=True,
                cant_jump_through=True,
            ),
        ],
        expected_bytes=[0x15, 0x0F, 0x15, 0xF0, 0x15, 0xA5, 0x15, 0x5A],
    ),
    Case(
        "Set VRAM priority",
        commands_factory=lambda: [
            A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            A_SetVRAMPriority(NORMAL_PRIORITY),
            A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
            A_SetVRAMPriority(PRIORITY_3),
        ],
        expected_bytes=[0x13, 0x00, 0x13, 0x01, 0x13, 0x02, 0x13, 0x03],
    ),
    Case(
        "Set VRAM priority should fail if trying to set it to an invalid layer",
        commands_factory=lambda: [
            A_SetVRAMPriority(VRAMPriority(4)),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Set priority",
        commands_factory=lambda: [
            A_SetPriority(0),
            A_SetPriority(1),
            A_SetPriority(2),
            A_SetPriority(3),
        ],
        expected_bytes=[
            0xFD,
            0x0F,
            0x00,
            0xFD,
            0x0F,
            0x01,
            0xFD,
            0x0F,
            0x02,
            0xFD,
            0x0F,
            0x03,
        ],
    ),
    Case(
        "Set priority should fail if trying to set it to an invalid layer",
        commands_factory=lambda: [
            A_SetPriority(4),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Shadows",
        commands_factory=lambda: [A_ShadowOn(), A_ShadowOff()],
        expected_bytes=[0xFD, 0x01, 0xFD, 0x00],
    ),
    Case(
        "Floating",
        commands_factory=lambda: [A_FloatingOn(), A_FloatingOff()],
        expected_bytes=[0xFD, 0x02, 0xFD, 0x03],
    ),
    Case(
        "Set object memory bits",
        commands_factory=lambda: [
            A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[3]),
            A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[2]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
            A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
            A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 2]),
            A_SetObjectMemoryBits(arg_1=0x0D, bits=[0, 1]),
        ],
        expected_bytes=[
            0x12,
            0x03,
            0x14,
            0x08,
            0x12,
            0x02,
            0x14,
            0x02,
            0x14,
            0x04,
            0x14,
            0x00,
            0x12,
            0x00,
            0x14,
            0x05,
            0x14,
            0x0C,
            0x14,
            0x0B,
            0x14,
            0x07,
            0x11,
            0x03,
        ],
    ),
    Case(
        "Set object memory bits should fail with bad arg",
        commands_factory=lambda: [
            A_SetObjectMemoryBits(arg_1=0x0F, bits=[7]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Set object memory bits should fail with bad bits",
        commands_factory=lambda: [
            A_SetObjectMemoryBits(arg_1=0x0D, bits=[8]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory set bit",
        commands_factory=lambda: [
            A_ObjectMemorySetBit(0x08, [4]),
            A_ObjectMemorySetBit(0x09, [7]),
            A_ObjectMemorySetBit(0x0B, [3]),
            A_ObjectMemorySetBit(0x0C, [3, 4, 5]),
            A_ObjectMemorySetBit(0x0D, [6]),
            A_ObjectMemorySetBit(0x0E, [4]),
            A_ObjectMemorySetBit(0x0E, [5]),
            A_ObjectMemorySetBit(0x12, [5]),
            A_ObjectMemorySetBit(0x30, [4]),
            A_ObjectMemorySetBit(0x3C, [6]),
        ],
        expected_bytes=[
            0xFD,
            0x0A,
            0xFD,
            0x08,
            0xFD,
            0x17,
            0xFD,
            0x14,
            0xFD,
            0x19,
            0xFD,
            0x04,
            0xFD,
            0x06,
            0xFD,
            0x11,
            0xFD,
            0x0D,
            0xFD,
            0x18,
        ],
    ),
    Case(
        "Object memory set bit should fail with bad arg",
        commands_factory=lambda: [
            A_ObjectMemorySetBit(0x01, [4]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory set bit should fail with bad bits",
        commands_factory=lambda: [
            A_ObjectMemorySetBit(0x0E, [7]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory set bit should fail with no bits",
        commands_factory=lambda: [
            A_ObjectMemorySetBit(0x0E, []),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit",
        commands_factory=lambda: [
            A_ObjectMemoryClearBit(0x08, [3, 4]),
            A_ObjectMemoryClearBit(0x09, [7]),
            A_ObjectMemoryClearBit(0x0B, [3]),
            A_ObjectMemoryClearBit(0x0C, [3, 4, 5]),
            A_ObjectMemoryClearBit(0x0E, [4]),
            A_ObjectMemoryClearBit(0x0E, [5]),
            A_ObjectMemoryClearBit(0x30, [4]),
        ],
        expected_bytes=[
            0xFD,
            0x0B,
            0xFD,
            0x09,
            0xFD,
            0x16,
            0xFD,
            0x13,
            0xFD,
            0x05,
            0xFD,
            0x07,
            0xFD,
            0x0C,
        ],
    ),
    Case(
        "Object memory clear bit should fail with bad arg",
        commands_factory=lambda: [
            A_ObjectMemoryClearBit(0x01, [4]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit should fail with bad bits",
        commands_factory=lambda: [
            A_ObjectMemoryClearBit(0x0E, [7]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit should fail with no bits",
        commands_factory=lambda: [
            A_ObjectMemoryClearBit(0x0E, []),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory modify bits",
        commands_factory=lambda: [
            A_ObjectMemoryModifyBits(0x09, [5], [4, 6]),
            A_ObjectMemoryModifyBits(0x0C, [4], [3, 5]),
        ],
        expected_bytes=[
            0xFD,
            0x0E,
            0xFD,
            0x15,
        ],
    ),
    Case(
        "Object memory modify bit should fail with bad arg",
        commands_factory=lambda: [
            A_ObjectMemoryModifyBits(0x01, [4], [5]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit should fail with bad set bits",
        commands_factory=lambda: [
            A_ObjectMemoryModifyBits(0x09, [7], [4, 6]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit should fail with no set bits",
        commands_factory=lambda: [
            A_ObjectMemoryModifyBits(0x09, [], [4, 6]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit should fail with bad clear bits",
        commands_factory=lambda: [
            A_ObjectMemoryModifyBits(0x09, [5], [1]),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Object memory clear bit should fail with no clear bits",
        commands_factory=lambda: [
            A_ObjectMemoryModifyBits(0x09, [5], []),
        ],
        exception_type=AssertionError,
    ),
    Case(
        "Set bit",
        commands_factory=lambda: [
            A_SetBit(TEMP_7043_5),
            A_SetBit(MAP_MENU_UNLOCKED),
            A_SetBit(SEASIDE_SHED_EMPTIED),
        ],
        expected_bytes=[0xA0, 0x1D, 0xA1, 0x10, 0xA2, 0x36],
    ),
    Case(
        "Clear bit",
        commands_factory=lambda: [
            A_ClearBit(TEMP_7043_5),
            A_ClearBit(MAP_MENU_UNLOCKED),
            A_ClearBit(SEASIDE_SHED_EMPTIED),
        ],
        expected_bytes=[0xA4, 0x1D, 0xA5, 0x10, 0xA6, 0x36],
    ),
    Case(
        "704x-700C",
        commands_factory=lambda: [A_SetMem704XAt700CBit(), A_ClearMem704XAt700CBit()],
        expected_bytes=[0xA3, 0xA7],
    ),
    Case(
        "Set var to const",
        commands_factory=lambda: [
            A_SetVarToConst(PRIMARY_TEMP_700C, 1000),
            A_SetVarToConst(WEDDING_GEAR_COUNTER, 200),
            A_SetVarToConst(ROSE_WAY_7038, 3000),
        ],
        expected_bytes=[0xAC, 0xE8, 0x03, 0xA8, 0x12, 0xC8, 0xB0, 0x1C, 0xB8, 0x0B],
    ),
    Case(
        "Should fail if you try to use the wrong const size for a byte var",
        commands_factory=lambda: [
            A_SetVarToConst(WEDDING_GEAR_COUNTER, 2000, identifier="aaaa"),
        ],
        exception_type=InvalidCommandArgumentException,
        exception="illegal args for aaaa: 0x70B2: 2000",
    ),
    Case(
        "add const to var",
        commands_factory=lambda: [
            A_SetVarToConst(PRIMARY_TEMP_700C, 1000),
            A_SetVarToConst(WEDDING_GEAR_COUNTER, 200),
            A_SetVarToConst(ROSE_WAY_7038, 3000),
        ],
        expected_bytes=[0xAC, 0xE8, 0x03, 0xA8, 0x12, 0xC8, 0xB0, 0x1C, 0xB8, 0x0B],
    ),
    Case(
        "blah blah blah",
        commands_factory=lambda: [A_SetVarToConst(PRIMARY_TEMP_700C, 100)],
        expected_bytes=[0xAC, 0x64, 0x00],
    ),
    Case(
        "Z coord +1!",
        commands_factory=lambda: [A_Walk1StepNorthwest()],
        expected_bytes=[0x45],
    ),
    Case(
        "Walk xx steps east",
        commands_factory=lambda: [A_WalkEastSteps(10)],
        expected_bytes=[0x50, 0x0A],
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
    Case(
        "Jump if bit set",
        commands_factory=lambda: [
            A_JmpIfBitSet(TEMP_7043_5, ["end_here"]),
            A_JmpIfBitSet(MAP_MENU_UNLOCKED, ["end_here"]),
            A_JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[
            0xD8,
            0x1D,
            0x0E,
            0x00,
            0xD9,
            0x10,
            0x0E,
            0x00,
            0xDA,
            0x36,
            0x0E,
            0x00,
            0xFE,
        ],
    ),
    Case(
        "Jump if bit clear",
        commands_factory=lambda: [
            A_JmpIfBitClear(TEMP_7043_5, ["end_here"]),
            A_JmpIfBitClear(MAP_MENU_UNLOCKED, ["end_here"]),
            A_JmpIfBitClear(SEASIDE_SHED_EMPTIED, ["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[
            0xDC,
            0x1D,
            0x0E,
            0x00,
            0xDD,
            0x10,
            0x0E,
            0x00,
            0xDE,
            0x36,
            0x0E,
            0x00,
            0xFE,
        ],
    ),
    Case(
        "Jmp if 704x-700C",
        commands_factory=lambda: [
            A_JmpIfMem704XAt700CBitSet(destinations=["end_here"]),
            A_JmpIfMem704XAt700CBitClear(destinations=["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xDB, 0x08, 0x00, 0xDF, 0x08, 0x00, 0xFE],
    ),
    Case(
        "If object A & B < (x,y) steps apart...",
        commands_factory=lambda: [
            A_JmpIfObjectWithinRange(
                comparing_npc=NPC_1, usually=6, tiles=20, destinations=["end_here"]
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3A, 0x15, 0x06, 0x14, 0x08, 0x00, 0xFE],
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
    if case.exception or case.exception_type:
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
        if case.exception:
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
