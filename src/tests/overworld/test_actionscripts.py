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
        "Walk xx steps east",
        commands_factory=lambda: [A_WalkEastSteps(10)],
        expected_bytes=[0x50, 0x0A],
    ),
    Case(
        "A_SequencePlaybackOn",
        commands_factory=lambda: [A_SequencePlaybackOn()],
        expected_bytes=[0x02],
    ),
    Case(
        "A_SequencePlaybackOff",
        commands_factory=lambda: [A_SequencePlaybackOff()],
        expected_bytes=[0x03],
    ),
    Case(
        "A_SequenceLoopingOn",
        commands_factory=lambda: [A_SequenceLoopingOn()],
        expected_bytes=[0x04],
    ),
    Case(
        "A_SequenceLoopingOff",
        commands_factory=lambda: [A_SequenceLoopingOff()],
        expected_bytes=[0x05],
    ),
    Case(
        "A_FixedFCoordOn",
        commands_factory=lambda: [A_FixedFCoordOn()],
        expected_bytes=[0x06],
    ),
    Case(
        "A_FixedFCoordOff",
        commands_factory=lambda: [A_FixedFCoordOff()],
        expected_bytes=[0x07],
    ),
    Case(
        "A_ResetProperties",
        commands_factory=lambda: [A_ResetProperties()],
        expected_bytes=[0x09],
    ),
    Case(
        "A_ShadowOn-On",
        commands_factory=lambda: [A_ShadowOn()],
        expected_bytes=[0xFD, 0x01],
    ),
    Case(
        "A_ShadowOn-Off",
        commands_factory=lambda: [A_ShadowOff()],
        expected_bytes=[0xFD, 0x00],
    ),
    Case(
        "A_FloatingOn",
        commands_factory=lambda: [A_FloatingOn()],
        expected_bytes=[0xFD, 0x02],
    ),
    Case(
        "A_FloatingOff",
        commands_factory=lambda: [A_FloatingOff()],
        expected_bytes=[0xFD, 0x03],
    ),
    Case(
        "A_IncPaletteRowBy",
        commands_factory=lambda: [A_IncPaletteRowBy(14)],
        expected_bytes=[0x0E, 0x0E],
    ),
    Case(
        "A_IncPaletteRowBy_upper",
        commands_factory=lambda: [A_IncPaletteRowBy(14, upper=2)],
        expected_bytes=[0x0E, 0x2E],
    ),
    Case(
        "A_IncPaletteRowBy (1)",
        commands_factory=lambda: [A_IncPaletteRowBy(1)],
        expected_bytes=[0x0F],
    ),
    Case(
        "A_EmbeddedAnimationRoutine-26",
        commands_factory=lambda: [
            A_EmbeddedAnimationRoutine(
                bytearray(
                    b"&\x00\x00\x00\x00\x00\xc0\x00\x7f\x00\x01\x00\x00\x00\xfe\x80"
                )
            ),
        ],
        expected_bytes=[
            0x26,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0xC0,
            0x00,
            0x7F,
            0x00,
            0x01,
            0x00,
            0x00,
            0x00,
            0xFE,
            0x80,
        ],
    ),
    Case(
        "A_EmbeddedAnimationRoutine-27",
        commands_factory=lambda: [
            A_EmbeddedAnimationRoutine(
                bytearray(b"'\x00\x00\x00\x00\x00\xd0\x00_\x00\x01\x00\x00\x00\xfe\x80")
            ),
        ],
        expected_bytes=[
            0x27,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0xD0,
            0x00,
            0x5F,
            0x00,
            0x01,
            0x00,
            0x00,
            0x00,
            0xFE,
            0x80,
        ],
    ),
    Case(
        "A_EmbeddedAnimationRoutine-28",
        commands_factory=lambda: [
            A_EmbeddedAnimationRoutine(
                bytearray(
                    b"(\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x04\x80"
                )
            )
        ],
        expected_bytes=[
            0x28,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x04,
            0x00,
            0x01,
            0x00,
            0x00,
            0x00,
            0x04,
            0x80,
        ],
    ),
    Case(
        "A_EmbeddedAnimationRoutine invalid header",
        commands_factory=lambda: [
            A_EmbeddedAnimationRoutine(
                bytearray(
                    b"\x01\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x04\x80"
                )
            )
        ],
        exception_type=AssertionError,
    ),
    Case(
        "A_EmbeddedAnimationRoutine invalid length",
        commands_factory=lambda: [
            A_EmbeddedAnimationRoutine(bytearray(b"(\x00\x00\x00\x00\x00\x00"))
        ],
        exception_type=AssertionError,
    ),
    Case(
        "A_Walk1StepEast",
        commands_factory=lambda: [A_Walk1StepEast()],
        expected_bytes=[0x40],
    ),
    Case(
        "A_Walk1StepSoutheast",
        commands_factory=lambda: [A_Walk1StepSoutheast()],
        expected_bytes=[0x41],
    ),
    Case(
        "A_Walk1StepSouth",
        commands_factory=lambda: [A_Walk1StepSouth()],
        expected_bytes=[0x42],
    ),
    Case(
        "A_Walk1StepSouthwest",
        commands_factory=lambda: [A_Walk1StepSouthwest()],
        expected_bytes=[0x43],
    ),
    Case(
        "A_Walk1StepWest",
        commands_factory=lambda: [A_Walk1StepWest()],
        expected_bytes=[0x44],
    ),
    Case(
        "A_Walk1StepNorthwest",
        commands_factory=lambda: [A_Walk1StepNorthwest()],
        expected_bytes=[0x45],
    ),
    Case(
        "A_Walk1StepNorth",
        commands_factory=lambda: [A_Walk1StepNorth()],
        expected_bytes=[0x46],
    ),
    Case(
        "A_Walk1StepNortheast",
        commands_factory=lambda: [A_Walk1StepNortheast()],
        expected_bytes=[0x47],
    ),
    Case(
        "A_Walk1StepFDirection",
        commands_factory=lambda: [A_Walk1StepFDirection()],
        expected_bytes=[0x48],
    ),
    Case(
        "A_AddZCoord1Step",
        commands_factory=lambda: [A_AddZCoord1Step()],
        expected_bytes=[0x4A],
    ),
    Case(
        "A_DecZCoord1Step",
        commands_factory=lambda: [A_DecZCoord1Step()],
        expected_bytes=[0x4B],
    ),
    Case(
        "A_WalkF20Steps",
        commands_factory=lambda: [A_WalkF20Steps()],
        expected_bytes=[0x59],
    ),
    Case(
        "A_ShiftZUp20Steps",
        commands_factory=lambda: [A_ShiftZUp20Steps()],
        expected_bytes=[0x5C],
    ),
    Case(
        "A_ShiftZDown20Steps",
        commands_factory=lambda: [A_ShiftZDown20Steps()],
        expected_bytes=[0x5D],
    ),
    Case(
        "A_WalkFDirection16Pixels",
        commands_factory=lambda: [A_WalkFDirection16Pixels()],
        expected_bytes=[0x69],
    ),
    Case(
        "A_FaceEast",
        commands_factory=lambda: [A_FaceEast()],
        expected_bytes=[0x70],
    ),
    Case(
        "A_FaceEast7C",
        commands_factory=lambda: [A_FaceEast7C()],
        expected_bytes=[0x7C],
    ),
    Case(
        "A_FaceSoutheast",
        commands_factory=lambda: [A_FaceSoutheast()],
        expected_bytes=[0x71],
    ),
    Case(
        "A_FaceSouth",
        commands_factory=lambda: [A_FaceSouth()],
        expected_bytes=[0x72],
    ),
    Case(
        "A_FaceSouthwest",
        commands_factory=lambda: [A_FaceSouthwest()],
        expected_bytes=[0x73],
    ),
    Case(
        "A_FaceSouthwest7D",
        commands_factory=lambda: [A_FaceSouthwest7D(1)],
        expected_bytes=[0x7D, 0x01],
    ),
    Case(
        "A_FaceWest",
        commands_factory=lambda: [A_FaceWest()],
        expected_bytes=[0x74],
    ),
    Case(
        "A_FaceNorthwest",
        commands_factory=lambda: [A_FaceNorthwest()],
        expected_bytes=[0x75],
    ),
    Case(
        "A_FaceNorth",
        commands_factory=lambda: [A_FaceNorth()],
        expected_bytes=[0x76],
    ),
    Case(
        "A_FaceNortheast",
        commands_factory=lambda: [A_FaceNortheast()],
        expected_bytes=[0x77],
    ),
    Case(
        "A_FaceMario",
        commands_factory=lambda: [A_FaceMario()],
        expected_bytes=[0x78],
    ),
    Case(
        "A_TurnClockwise45Degrees",
        commands_factory=lambda: [A_TurnClockwise45Degrees()],
        expected_bytes=[0x79],
    ),
    Case(
        "A_TurnRandomDirection",
        commands_factory=lambda: [A_TurnRandomDirection()],
        expected_bytes=[0x7A],
    ),
    Case(
        label="A_AddConstToVar",
        commands_factory=lambda: [
            A_AddConstToVar(UNKNOWN_70AD, 4),
            A_AddConstToVar(ROSE_WAY_703E, 10),
            A_AddConstToVar(PRIMARY_TEMP_700C, 100),
        ],
        expected_bytes=[0xA9, 0x0D, 0x04, 0xB1, 0x1F, 0x0A, 0x00, 0xAD, 0x64, 0x00],
    ),
    Case(
        label="A_Inc",
        commands_factory=lambda: [
            A_Inc(SECONDARY_TEMP_7024),
            A_Inc(PRIMARY_TEMP_700C),
            A_Inc(KEEP_DOOR_LIVES),
        ],
        expected_bytes=[0xB2, 0x12, 0xAE, 0xAA, 0x2B],
    ),
    Case(
        label="A_Dec",
        commands_factory=lambda: [
            A_Dec(SECONDARY_TEMP_7024),
            A_Dec(PRIMARY_TEMP_700C),
            A_Dec(KEEP_DOOR_LIVES),
        ],
        expected_bytes=[0xB3, 0x12, 0xAF, 0xAB, 0x2B],
    ),
    Case(
        label="A_CopyVarToVar",
        commands_factory=lambda: [
            A_CopyVarToVar(PRIMARY_TEMP_700C, UNKNOWN_70D0),
            A_CopyVarToVar(PRIMARY_TEMP_700C, TEMP_702E),
            A_CopyVarToVar(UNKNOWN_70C9, PRIMARY_TEMP_700C),
            A_CopyVarToVar(TIMER_7020, PRIMARY_TEMP_700C),
            A_CopyVarToVar(TIMER_7020, TEMP_702E),
        ],
        expected_bytes=[
            0xB5,
            0x30,
            0xBB,
            0x17,
            0xB4,
            0x29,
            0xBA,
            0x10,
            0xBC,
            0x10,
            0x17,
        ],
    ),
    Case(
        "A_CopyVarToVar should fail when both vars are bytes that aren't 0x700C",
        commands_factory=lambda: [
            A_CopyVarToVar(UNKNOWN_70C9, UNKNOWN_70D0, identifier="aaaa"),
        ],
        exception_type=InvalidCommandArgumentException,
        exception="illegal args for aaaa: 0x70C9 0x70D0",
    ),
    Case(
        label="A_CompareVarToConst",
        commands_factory=lambda: [
            A_CompareVarToConst(PRIMARY_TEMP_700C, 80),
            A_CompareVarToConst(X_COORD_1, 65535),
        ],
        expected_bytes=[0xC0, 0x50, 0x00, 0xC2, 0x08, 0xFF, 0xFF],
    ),
    Case(
        label="A_Compare700CToVar",
        commands_factory=lambda: [A_Compare700CToVar(UNKNOWN_7036)],
        expected_bytes=[0xC1, 0x1B],
    ),
    Case(
        "A_StopSound",
        commands_factory=lambda: [A_StopSound()],
        expected_bytes=[0x9B],
    ),
    Case(
        "A_EndLoop",
        commands_factory=lambda: [A_EndLoop()],
        expected_bytes=[0xD7],
    ),
    Case(
        "A_ReturnQueue",
        commands_factory=lambda: [A_ReturnQueue()],
        expected_bytes=[0xFE],
    ),
    Case(
        "A_ReturnAll",
        commands_factory=lambda: [A_ReturnAll()],
        expected_bytes=[0xFF],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(0)],
        expected_bytes=[0x0D, 0x00],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(1)],
        expected_bytes=[0x0D, 0x01],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(2)],
        expected_bytes=[0x0D, 0x02],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(3)],
        expected_bytes=[0x0D, 0x03],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(4)],
        expected_bytes=[0x0D, 0x04],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(5)],
        expected_bytes=[0x0D, 0x05],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(6)],
        expected_bytes=[0x0D, 0x06],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(7)],
        expected_bytes=[0x0D, 0x07],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(8)],
        expected_bytes=[0x0D, 0x08],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(9)],
        expected_bytes=[0x0D, 0x09],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(10)],
        expected_bytes=[0x0D, 0x0A],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(11)],
        expected_bytes=[0x0D, 0x0B],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(12)],
        expected_bytes=[0x0D, 0x0C],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(13)],
        expected_bytes=[0x0D, 0x0D],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(14)],
        expected_bytes=[0x0D, 0x0E],
    ),
    Case(
        "A_SetPaletteRow",
        commands_factory=lambda: [A_SetPaletteRow(15)],
        expected_bytes=[0x0D, 0x0F],
    ),
    Case(
        "A_IncPaletteRowBy0",
        commands_factory=lambda: [A_IncPaletteRowBy(0)],
        expected_bytes=[0x0E, 0x00],
    ),
    Case(
        "A_IncPaletteRowBy1",
        commands_factory=lambda: [A_IncPaletteRowBy(1)],
        expected_bytes=[0x0F],
    ),
    Case(
        "A_IncPaletteRowBy2",
        commands_factory=lambda: [A_IncPaletteRowBy(rows=2)],
        expected_bytes=[0x0E, 0x02],
    ),
    Case(
        label="A_SetVarToRandom",
        commands_factory=lambda: [A_SetVarToRandom(UNKNOWN_7036, 90)],
        expected_bytes=[0xB7, 0x1B, 0x5A, 0x00],
    ),
    Case(
        label="A_AddVarTo700C",
        commands_factory=lambda: [A_AddVarTo700C(UNKNOWN_7036)],
        expected_bytes=[0xB8, 0x1B],
    ),
    Case(
        label="A_DecVarFrom700C",
        commands_factory=lambda: [A_DecVarFrom700C(ROSE_WAY_703E)],
        expected_bytes=[0xB9, 0x1F],
    ),
    Case(
        label="A_SwapVars",
        commands_factory=lambda: [A_SwapVars(OLD_STAR_PIECE_ID, BATTLE_PACK_ID)],
        expected_bytes=[0xBD, 0x07, 0x05],
    ),
    Case(
        label="A_Move70107015To7016701B",
        commands_factory=lambda: [A_Move70107015To7016701B()],
        expected_bytes=[0xBE],
    ),
    Case(
        label="A_Move7016701BTo70107015",
        commands_factory=lambda: [A_Move7016701BTo70107015()],
        expected_bytes=[0xBF],
    ),
    Case(
        label="A_Mem700CAndConst",
        commands_factory=lambda: [A_Mem700CAndConst(60)],
        expected_bytes=[0xFD, 0xB0, 0x3C, 0x00],
    ),
    Case(
        label="A_Mem700CAndVar",
        commands_factory=lambda: [A_Mem700CAndVar(TIMER_701C)],
        expected_bytes=[0xFD, 0xB3, 0x0E],
    ),
    Case(
        label="A_Mem700COrConst",
        commands_factory=lambda: [A_Mem700COrConst(99)],
        expected_bytes=[0xFD, 0xB1, 0x63, 0x00],
    ),
    Case(
        label="A_Mem700COrVar",
        commands_factory=lambda: [A_Mem700COrVar(TEMP_7028)],
        expected_bytes=[0xFD, 0xB4, 0x14],
    ),
    Case(
        label="A_Mem700CXorConst",
        commands_factory=lambda: [A_Mem700CXorConst(128)],
        expected_bytes=[0xFD, 0xB2, 0x80, 0x00],
    ),
    Case(
        label="A_Mem700CXorVar",
        commands_factory=lambda: [A_Mem700CXorVar(SECONDARY_TEMP_7024)],
        expected_bytes=[0xFD, 0xB5, 0x12],
    ),
    Case(
        label="A_VarShiftLeft",
        commands_factory=lambda: [A_VarShiftLeft(X_COORD_1, 113)],
        expected_bytes=[0xFD, 0xB6, 0x08, 0x8F],
    ),
    Case(
        label="A_LoadMemory",
        commands_factory=lambda: [A_LoadMemory()],
        expected_bytes=[],
    ),
    Case(
        label="A_SetSpriteSequence",
        commands_factory=lambda: [A_SetSpriteSequence()],
        expected_bytes=[],
    ),
    Case(
        label="A_SetSequenceSpeed",
        commands_factory=lambda: [A_SetSequenceSpeed()],
        expected_bytes=[],
    ),
    Case(
        label="A_SetWalkingSpeed",
        commands_factory=lambda: [A_SetWalkingSpeed()],
        expected_bytes=[],
    ),
    Case(
        label="A_SetAllSpeeds",
        commands_factory=lambda: [A_SetAllSpeeds()],
        expected_bytes=[],
    ),
    Case(
        label="A_MaximizeSequenceSpeed",
        commands_factory=lambda: [A_MaximizeSequenceSpeed()],
        expected_bytes=[],
    ),
    Case(
        label="A_MaximizeSequenceSpeed86",
        commands_factory=lambda: [A_MaximizeSequenceSpeed86()],
        expected_bytes=[],
    ),
    Case(
        label="A_Set700CToCurrentLevel",
        commands_factory=lambda: [A_Set700CToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_Set700CToPressedButton",
        commands_factory=lambda: [A_Set700CToPressedButton()],
        expected_bytes=[],
    ),
    Case(
        label="A_BPL262728", commands_factory=lambda: [A_BPL262728()], expected_bytes=[]
    ),
    Case(
        label="A_BMI262728", commands_factory=lambda: [A_BMI262728()], expected_bytes=[]
    ),
    Case(label="A_BPL2627", commands_factory=lambda: [A_BPL2627()], expected_bytes=[]),
    Case(
        label="A_SummonObjectToSpecificLevel",
        commands_factory=lambda: [A_SummonObjectToSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_SummonObjectAt70A8ToCurrentLevel",
        commands_factory=lambda: [A_SummonObjectAt70A8ToCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_RemoveObjectFromSpecificLevel",
        commands_factory=lambda: [A_RemoveObjectFromSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_RemoveObjectAt70A8FromCurrentLevel",
        commands_factory=lambda: [A_RemoveObjectAt70A8FromCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_EnableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [A_EnableObjectTriggerInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_EnableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [A_EnableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_DisableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [A_DisableObjectTriggerInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_DisableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [A_DisableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkSoutheastSteps",
        commands_factory=lambda: [A_WalkSoutheastSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkSouthSteps",
        commands_factory=lambda: [A_WalkSouthSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkSouthwestSteps",
        commands_factory=lambda: [A_WalkSouthwestSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkWestSteps",
        commands_factory=lambda: [A_WalkWestSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkNorthwestSteps",
        commands_factory=lambda: [A_WalkNorthwestSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkNorthSteps",
        commands_factory=lambda: [A_WalkNorthSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkNortheastSteps",
        commands_factory=lambda: [A_WalkNortheastSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkFDirectionSteps",
        commands_factory=lambda: [A_WalkFDirectionSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftZUpSteps",
        commands_factory=lambda: [A_ShiftZUpSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftZDownSteps",
        commands_factory=lambda: [A_ShiftZDownSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkEastPixels",
        commands_factory=lambda: [A_WalkEastPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkSoutheastPixels",
        commands_factory=lambda: [A_WalkSoutheastPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkSouthPixels",
        commands_factory=lambda: [A_WalkSouthPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkSouthwestPixels",
        commands_factory=lambda: [A_WalkSouthwestPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkWestPixels",
        commands_factory=lambda: [A_WalkWestPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkNorthwestPixels",
        commands_factory=lambda: [A_WalkNorthwestPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkNorthPixels",
        commands_factory=lambda: [A_WalkNorthPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkNortheastPixels",
        commands_factory=lambda: [A_WalkNortheastPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkFDirectionPixels",
        commands_factory=lambda: [A_WalkFDirectionPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkFDirection16Pixels",
        commands_factory=lambda: [A_WalkFDirection16Pixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftZUpPixels",
        commands_factory=lambda: [A_ShiftZUpPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftZDownPixels",
        commands_factory=lambda: [A_ShiftZDownPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_TurnClockwise45DegreesNTimes",
        commands_factory=lambda: [A_TurnClockwise45DegreesNTimes()],
        expected_bytes=[],
    ),
    Case(
        label="A_JumpToHeight",
        commands_factory=lambda: [A_JumpToHeight()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkToXYCoords",
        commands_factory=lambda: [A_WalkToXYCoords()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkXYSteps",
        commands_factory=lambda: [A_WalkXYSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftToXYCoords",
        commands_factory=lambda: [A_ShiftToXYCoords()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftXYSteps",
        commands_factory=lambda: [A_ShiftXYSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_ShiftXYPixels",
        commands_factory=lambda: [A_ShiftXYPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferToObjectXY",
        commands_factory=lambda: [A_TransferToObjectXY()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferToObjectXYZ",
        commands_factory=lambda: [A_TransferToObjectXYZ()],
        expected_bytes=[],
    ),
    Case(
        label="A_RunAwayShift",
        commands_factory=lambda: [A_RunAwayShift()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferTo70167018",
        commands_factory=lambda: [A_TransferTo70167018()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferTo70167018701A",
        commands_factory=lambda: [A_TransferTo70167018701A()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkTo70167018",
        commands_factory=lambda: [A_WalkTo70167018()],
        expected_bytes=[],
    ),
    Case(
        label="A_WalkTo70167018701A",
        commands_factory=lambda: [A_WalkTo70167018701A()],
        expected_bytes=[],
    ),
    Case(
        label="A_BounceToXYWithHeight",
        commands_factory=lambda: [A_BounceToXYWithHeight()],
        expected_bytes=[],
    ),
    Case(
        label="A_BounceXYStepsWithHeight",
        commands_factory=lambda: [A_BounceXYStepsWithHeight()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferToXYZF",
        commands_factory=lambda: [A_TransferToXYZF()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferXYZFSteps",
        commands_factory=lambda: [A_TransferXYZFSteps()],
        expected_bytes=[],
    ),
    Case(
        label="A_TransferXYZFPixels",
        commands_factory=lambda: [A_TransferXYZFPixels()],
        expected_bytes=[],
    ),
    Case(
        label="A_Set700CToObjectCoord",
        commands_factory=lambda: [A_Set700CToObjectCoord()],
        expected_bytes=[],
    ),
    Case(
        label="A_PlaySound", commands_factory=lambda: [A_PlaySound()], expected_bytes=[]
    ),
    Case(
        label="A_PlaySoundBalance",
        commands_factory=lambda: [A_PlaySoundBalance()],
        expected_bytes=[],
    ),
    Case(
        label="A_FadeOutSoundToVolume",
        commands_factory=lambda: [A_FadeOutSoundToVolume()],
        expected_bytes=[],
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
        label="A_JmpIfComparisonResultIsGreaterOrEqual",
        commands_factory=lambda: [A_JmpIfComparisonResultIsGreaterOrEqual()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfComparisonResultIsLesser",
        commands_factory=lambda: [A_JmpIfComparisonResultIsLesser()],
        expected_bytes=[],
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
    Case(
        label="A_JmpIfVarEqualsConst",
        commands_factory=lambda: [A_JmpIfVarEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfVarNotEqualsConst",
        commands_factory=lambda: [A_JmpIfVarNotEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIf700CAllBitsClear",
        commands_factory=lambda: [A_JmpIf700CAllBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIf700CAnyBitsSet",
        commands_factory=lambda: [A_JmpIf700CAnyBitsSet()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfRandom2of3",
        commands_factory=lambda: [A_JmpIfRandom2of3()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfRandom1of2",
        commands_factory=lambda: [A_JmpIfRandom1of2()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIs0",
        commands_factory=lambda: [A_JmpIfLoadedMemoryIs0()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIsAboveOrEqual0",
        commands_factory=lambda: [A_JmpIfLoadedMemoryIsAboveOrEqual0()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIsBelow0",
        commands_factory=lambda: [A_JmpIfLoadedMemoryIsBelow0()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIsNot0",
        commands_factory=lambda: [A_JmpIfLoadedMemoryIsNot0()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfObjectWithinRange",
        commands_factory=lambda: [A_JmpIfObjectWithinRange()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfObjectWithinRangeSameZ",
        commands_factory=lambda: [A_JmpIfObjectWithinRangeSameZ()],
        expected_bytes=[],
    ),
    Case(
        label="A_CreatePacketAtObjectCoords",
        commands_factory=lambda: [A_CreatePacketAtObjectCoords()],
        expected_bytes=[],
    ),
    Case(
        label="A_CreatePacketAt7010",
        commands_factory=lambda: [A_CreatePacketAt7010()],
        expected_bytes=[],
    ),
    Case(
        label="A_CreatePacketAt7010WithEvent",
        commands_factory=lambda: [A_CreatePacketAt7010WithEvent()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfObjectInSpecificLevel",
        commands_factory=lambda: [A_JmpIfObjectInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfObjectNotInSpecificLevel",
        commands_factory=lambda: [A_JmpIfObjectNotInSpecificLevel()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfObjectInAir",
        commands_factory=lambda: [A_JmpIfObjectInAir()],
        expected_bytes=[],
    ),
    Case(
        label="A_UnknownJmp3C",
        commands_factory=lambda: [A_UnknownJmp3C()],
        expected_bytes=[],
    ),
    Case(
        label="A_JmpIfMarioInAir",
        commands_factory=lambda: [A_JmpIfMarioInAir()],
        expected_bytes=[],
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
    if case.expected_bytes is not None and len(case.expected_bytes) == 0:
        return
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
