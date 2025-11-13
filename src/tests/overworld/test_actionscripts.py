import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import Packet
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.ids import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    ActionScriptBank,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ByteVar,
    IdentifierException,
    InvalidCommandArgumentException,
    ShortVar,
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
            A_SetBit(Flag(0x7043, 5)),
            A_SetBit(Flag(0x7062, 0)),
            A_SetBit(Flag(0x7086, 6)),
        ],
        expected_bytes=[0xA0, 0x1D, 0xA1, 0x10, 0xA2, 0x36],
    ),
    Case(
        "Clear bit",
        commands_factory=lambda: [
            A_ClearBit(Flag(0x7043, 5)),
            A_ClearBit(Flag(0x7062, 0)),
            A_ClearBit(Flag(0x7086, 6)),
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
            A_SetVarToConst(ShortVar(0x700C), 1000),
            A_SetVarToConst(ByteVar(0x70B2), 200),
            A_SetVarToConst(ShortVar(0x7038), 3000),
        ],
        expected_bytes=[0xAC, 0xE8, 0x03, 0xA8, 0x12, 0xC8, 0xB0, 0x1C, 0xB8, 0x0B],
    ),
    Case(
        "Should fail if you try to use the wrong const size for a byte var",
        commands_factory=lambda: [
            A_SetVarToConst(ByteVar(0x70B2), 2000, identifier="aaaa"),
        ],
        exception_type=InvalidCommandArgumentException,
        exception="illegal args for aaaa: 0x70B2: 2000",
    ),
    Case(
        "add const to var",
        commands_factory=lambda: [
            A_AddConstToVar(ShortVar(0x700C), 1000),
            A_AddConstToVar(ByteVar(0x70B2), 200),
            A_AddConstToVar(ShortVar(0x7038), 3000),
        ],
        expected_bytes=[0xAD, 0xE8, 0x03, 0xA9, 0x12, 0xC8, 0xB1, 0x1C, 0xB8, 0x0B],
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
            A_AddConstToVar(ByteVar(0x70AD), 4),
            A_AddConstToVar(ShortVar(0x703E), 10),
            A_AddConstToVar(ShortVar(0x700C), 100),
        ],
        expected_bytes=[0xA9, 0x0D, 0x04, 0xB1, 0x1F, 0x0A, 0x00, 0xAD, 0x64, 0x00],
    ),
    Case(
        label="A_Inc",
        commands_factory=lambda: [
            A_Inc(ShortVar(0x7024)),
            A_Inc(ShortVar(0x700C)),
            A_Inc(ByteVar(0x70CB)),
        ],
        expected_bytes=[0xB2, 0x12, 0xAE, 0xAA, 0x2B],
    ),
    Case(
        label="A_Dec",
        commands_factory=lambda: [
            A_Dec(ShortVar(0x7024)),
            A_Dec(ShortVar(0x700C)),
            A_Dec(ByteVar(0x70CB)),
        ],
        expected_bytes=[0xB3, 0x12, 0xAF, 0xAB, 0x2B],
    ),
    Case(
        label="A_CopyVarToVar",
        commands_factory=lambda: [
            A_CopyVarToVar(ShortVar(0x700C), ByteVar(0x70D0)),
            A_CopyVarToVar(ShortVar(0x700C), ShortVar(0x702E)),
            A_CopyVarToVar(ByteVar(0x70C9), ShortVar(0x700C)),
            A_CopyVarToVar(ShortVar(0x7020), ShortVar(0x700C)),
            A_CopyVarToVar(ShortVar(0x7020), ShortVar(0x702E)),
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
            A_CopyVarToVar(ByteVar(0x70C9), ByteVar(0x70D0), identifier="aaaa"),
        ],
        exception_type=InvalidCommandArgumentException,
        exception="illegal args for aaaa: 0x70C9 0x70D0",
    ),
    Case(
        label="A_CompareVarToConst",
        commands_factory=lambda: [
            A_CompareVarToConst(ShortVar(0x700C), 80),
            A_CompareVarToConst(ShortVar(0x7010), 65535),
        ],
        expected_bytes=[0xC0, 0x50, 0x00, 0xC2, 0x08, 0xFF, 0xFF],
    ),
    Case(
        label="A_Compare700CToVar",
        commands_factory=lambda: [A_Compare700CToVar(ShortVar(0x7036))],
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
        commands_factory=lambda: [A_SetVarToRandom(ShortVar(0x7036), 90)],
        expected_bytes=[0xB7, 0x1B, 0x5A, 0x00],
    ),
    Case(
        label="A_AddVarTo700C",
        commands_factory=lambda: [A_AddVarTo700C(ShortVar(0x7036))],
        expected_bytes=[0xB8, 0x1B],
    ),
    Case(
        label="A_DecVarFrom700C",
        commands_factory=lambda: [A_DecVarFrom700C(ShortVar(0x703E))],
        expected_bytes=[0xB9, 0x1F],
    ),
    Case(
        label="A_SwapVars",
        commands_factory=lambda: [A_SwapVars(ShortVar(0x700A), ShortVar(0x700E))],
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
        commands_factory=lambda: [A_Mem700CAndVar(ShortVar(0x701C))],
        expected_bytes=[0xFD, 0xB3, 0x0E],
    ),
    Case(
        label="A_Mem700COrConst",
        commands_factory=lambda: [A_Mem700COrConst(99)],
        expected_bytes=[0xFD, 0xB1, 0x63, 0x00],
    ),
    Case(
        label="A_Mem700COrVar",
        commands_factory=lambda: [A_Mem700COrVar(ShortVar(0x7028))],
        expected_bytes=[0xFD, 0xB4, 0x14],
    ),
    Case(
        label="A_Mem700CXorConst",
        commands_factory=lambda: [A_Mem700CXorConst(128)],
        expected_bytes=[0xFD, 0xB2, 0x80, 0x00],
    ),
    Case(
        label="A_Mem700CXorVar",
        commands_factory=lambda: [A_Mem700CXorVar(ShortVar(0x7024))],
        expected_bytes=[0xFD, 0xB5, 0x12],
    ),
    Case(
        label="A_VarShiftLeft",
        commands_factory=lambda: [A_VarShiftLeft(ShortVar(0x7010), 113)],
        expected_bytes=[0xFD, 0xB6, 0x08, 0x8F],
    ),
    Case(
        label="A_LoadMemory",
        commands_factory=lambda: [A_LoadMemory(ShortVar(0x7030))],
        expected_bytes=[0xD6, 0x18],
    ),
    Case(
        label="A_SetSpriteSequence",
        commands_factory=lambda: [
            A_SetSpriteSequence(
                sprite_offset=2, index=1, is_mold=True, mirror_sprite=True
            ),
            A_SetSpriteSequence(
                sprite_offset=7, index=15, is_mold=True, is_sequence=True, looping=True
            ),
        ],
        expected_bytes=[0x08, 0x1A, 0x81, 0x08, 0x4F, 0x0F],
    ),
    Case(
        label="A_SetSequenceSpeed",
        commands_factory=lambda: [
            A_SetSequenceSpeed(VERY_FAST),
            A_SetSequenceSpeed(VERY_SLOW),
        ],
        expected_bytes=[0x10, 0x83, 0x10, 0x86],
    ),
    Case(
        label="A_SetWalkingSpeed",
        commands_factory=lambda: [A_SetWalkingSpeed(FAST), A_SetWalkingSpeed(FASTEST)],
        expected_bytes=[0x10, 0x41, 0x10, 0x44],
    ),
    Case(
        label="A_SetAllSpeeds",
        commands_factory=lambda: [A_SetAllSpeeds(NORMAL), A_SetAllSpeeds(FAST)],
        expected_bytes=[0x10, 0xC0, 0x10, 0xC1],
    ),
    Case(
        label="A_MaximizeSequenceSpeed",
        commands_factory=lambda: [A_MaximizeSequenceSpeed()],
        expected_bytes=[0x85],
    ),
    Case(
        label="A_MaximizeSequenceSpeed86",
        commands_factory=lambda: [A_MaximizeSequenceSpeed86()],
        expected_bytes=[0x86],
    ),
    Case(
        label="A_Set700CToCurrentLevel",
        commands_factory=lambda: [A_Set700CToCurrentLevel()],
        expected_bytes=[0xC3],
    ),
    Case(
        label="A_Set700CToPressedButton",
        commands_factory=lambda: [A_Set700CToPressedButton()],
        expected_bytes=[0xCA],
    ),
    Case(
        label="A_BPL262728",
        commands_factory=lambda: [A_BPL262728()],
        expected_bytes=[0x21],
    ),
    Case(
        label="A_BMI262728",
        commands_factory=lambda: [A_BMI262728()],
        expected_bytes=[0x22],
    ),
    Case(
        label="A_BPL2627", commands_factory=lambda: [A_BPL2627()], expected_bytes=[0x2A]
    ),
    Case(
        label="A_SummonObjectToSpecificLevel",
        commands_factory=lambda: [
            A_SummonObjectToSpecificLevel(
                target_npc=NPC_4, level_id=20
            )
        ],
        expected_bytes=[0xF2, 0x14, 0xB0],
    ),
    Case(
        label="A_SummonObjectAt70A8ToCurrentLevel",
        commands_factory=lambda: [A_SummonObjectAt70A8ToCurrentLevel()],
        expected_bytes=[0xF4],
    ),
    Case(
        label="A_RemoveObjectFromSpecificLevel",
        commands_factory=lambda: [
            A_RemoveObjectFromSpecificLevel(
                target_npc=NPC_1, level_id=76
            )
        ],
        expected_bytes=[0xF2, 0x4C, 0x2A],
    ),
    Case(
        label="A_RemoveObjectAt70A8FromCurrentLevel",
        commands_factory=lambda: [A_RemoveObjectAt70A8FromCurrentLevel()],
        expected_bytes=[0xF5],
    ),
    Case(
        label="A_EnableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [
            A_EnableObjectTriggerInSpecificLevel(
                target_npc=NPC_3, level_id=311
            )
        ],
        expected_bytes=[0xF3, 0x37, 0xAF],
    ),
    Case(
        label="A_EnableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [A_EnableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[0xF6],
    ),
    Case(
        label="A_DisableObjectTriggerInSpecificLevel",
        commands_factory=lambda: [
            A_DisableObjectTriggerInSpecificLevel(
                target_npc=NPC_6, level_id=509
            )
        ],
        expected_bytes=[0xF3, 0xFD, 0x35],
    ),
    Case(
        label="A_DisableTriggerOfObjectAt70A8InCurrentLevel",
        commands_factory=lambda: [A_DisableTriggerOfObjectAt70A8InCurrentLevel()],
        expected_bytes=[0xF7],
    ),
    Case(
        label="A_WalkEastSteps",
        commands_factory=lambda: [A_WalkEastSteps(37)],
        expected_bytes=[0x50, 0x25],
    ),
    Case(
        label="A_WalkSoutheastSteps",
        commands_factory=lambda: [A_WalkSoutheastSteps(10)],
        expected_bytes=[0x51, 0x0A],
    ),
    Case(
        label="A_WalkSouthSteps",
        commands_factory=lambda: [A_WalkSouthSteps(100)],
        expected_bytes=[0x52, 0x64],
    ),
    Case(
        label="A_WalkSouthwestSteps",
        commands_factory=lambda: [A_WalkSouthwestSteps(88)],
        expected_bytes=[0x53, 0x58],
    ),
    Case(
        label="A_WalkWestSteps",
        commands_factory=lambda: [A_WalkWestSteps(69)],
        expected_bytes=[0x54, 0x45],
    ),
    Case(
        label="A_WalkNorthwestSteps",
        commands_factory=lambda: [A_WalkNorthwestSteps(8)],
        expected_bytes=[0x55, 0x08],
    ),
    Case(
        label="A_WalkNorthSteps",
        commands_factory=lambda: [A_WalkNorthSteps(255)],
        expected_bytes=[0x56, 0xFF],
    ),
    Case(
        label="A_WalkNortheastSteps",
        commands_factory=lambda: [A_WalkNortheastSteps(13)],
        expected_bytes=[0x57, 0x0D],
    ),
    Case(
        label="A_WalkFDirectionSteps",
        commands_factory=lambda: [A_WalkFDirectionSteps(49)],
        expected_bytes=[0x58, 0x31],
    ),
    Case(
        label="A_ShiftZUpSteps",
        commands_factory=lambda: [A_ShiftZUpSteps(20)],
        expected_bytes=[0x5A, 0x14],
    ),
    Case(
        label="A_ShiftZDownSteps",
        commands_factory=lambda: [A_ShiftZDownSteps(101)],
        expected_bytes=[0x5B, 0x65],
    ),
    Case(
        label="A_WalkEastPixels",
        commands_factory=lambda: [A_WalkEastPixels(3)],
        expected_bytes=[0x60, 0x03],
    ),
    Case(
        label="A_WalkSoutheastPixels",
        commands_factory=lambda: [A_WalkSoutheastPixels(7)],
        expected_bytes=[0x61, 0x07],
    ),
    Case(
        label="A_WalkSouthPixels",
        commands_factory=lambda: [A_WalkSouthPixels(16)],
        expected_bytes=[0x62, 0x10],
    ),
    Case(
        label="A_WalkSouthwestPixels",
        commands_factory=lambda: [A_WalkSouthwestPixels(41)],
        expected_bytes=[0x63, 0x29],
    ),
    Case(
        label="A_WalkWestPixels",
        commands_factory=lambda: [A_WalkWestPixels(74)],
        expected_bytes=[0x64, 0x4A],
    ),
    Case(
        label="A_WalkNorthwestPixels",
        commands_factory=lambda: [A_WalkNorthwestPixels(96)],
        expected_bytes=[0x65, 0x60],
    ),
    Case(
        label="A_WalkNorthPixels",
        commands_factory=lambda: [A_WalkNorthPixels(121)],
        expected_bytes=[0x66, 0x79],
    ),
    Case(
        label="A_WalkNortheastPixels",
        commands_factory=lambda: [A_WalkNortheastPixels(183)],
        expected_bytes=[0x67, 0xB7],
    ),
    Case(
        label="A_WalkFDirectionPixels",
        commands_factory=lambda: [A_WalkFDirectionPixels(231)],
        expected_bytes=[0x68, 0xE7],
    ),
    Case(
        label="A_WalkFDirection16Pixels",
        commands_factory=lambda: [A_WalkFDirection16Pixels()],
        expected_bytes=[0x69],  # nice
    ),
    Case(
        label="A_ShiftZUpPixels",
        commands_factory=lambda: [A_ShiftZUpPixels(187)],
        expected_bytes=[0x6A, 0xBB],
    ),
    Case(
        label="A_ShiftZDownPixels",
        commands_factory=lambda: [A_ShiftZDownPixels(200)],
        expected_bytes=[0x6B, 0xC8],
    ),
    Case(
        label="A_TurnClockwise45DegreesNTimes",
        commands_factory=lambda: [A_TurnClockwise45DegreesNTimes(10)],
        expected_bytes=[0x7B, 0x0A],
    ),
    Case(
        label="A_JumpToHeight",
        commands_factory=lambda: [
            A_JumpToHeight(1000, silent=True),
            A_JumpToHeight(10000, silent=False),
        ],
        expected_bytes=[0x7E, 0xE8, 0x03, 0x7F, 0x10, 0x27],
    ),
    Case(
        label="A_WalkToXYCoords",
        commands_factory=lambda: [A_WalkToXYCoords(3, 5)],
        expected_bytes=[0x80, 0x03, 0x05],
    ),
    Case(
        label="A_WalkXYSteps",
        commands_factory=lambda: [A_WalkXYSteps(10, 9)],
        expected_bytes=[0x81, 0x0A, 0x09],
    ),
    Case(
        label="A_ShiftToXYCoords",
        commands_factory=lambda: [A_ShiftToXYCoords(100, 200)],
        expected_bytes=[0x82, 0x64, 0xC8],
    ),
    Case(
        label="A_ShiftXYSteps",
        commands_factory=lambda: [A_ShiftXYSteps(62, 77)],
        expected_bytes=[0x83, 0x3E, 0x4D],
    ),
    Case(
        label="A_ShiftXYPixels",
        commands_factory=lambda: [A_ShiftXYPixels(90, 88)],
        expected_bytes=[0x84, 0x5A, 0x58],
    ),
    Case(
        label="A_TransferToObjectXY",
        commands_factory=lambda: [A_TransferToObjectXY(NPC_1)],
        expected_bytes=[0x87, 0x15],
    ),
    Case(
        label="A_TransferToObjectXYZ",
        commands_factory=lambda: [A_TransferToObjectXYZ(NPC_8)],
        expected_bytes=[0x95, 0x1C],
    ),
    Case(
        label="A_RunAwayShift",
        commands_factory=lambda: [A_RunAwayShift()],
        expected_bytes=[0x8A],
    ),
    Case(
        label="A_TransferTo70167018",
        commands_factory=lambda: [A_TransferTo70167018()],
        expected_bytes=[0x89],
    ),
    Case(
        label="A_TransferTo70167018701A",
        commands_factory=lambda: [A_TransferTo70167018701A()],
        expected_bytes=[0x99],
    ),
    Case(
        label="A_WalkTo70167018",
        commands_factory=lambda: [A_WalkTo70167018()],
        expected_bytes=[0x88],
    ),
    Case(
        label="A_WalkTo70167018701A",
        commands_factory=lambda: [A_WalkTo70167018701A()],
        expected_bytes=[0x98],
    ),
    Case(
        label="A_BounceToXYWithHeight",
        commands_factory=lambda: [A_BounceToXYWithHeight(x=5, y=20, height=10)],
        expected_bytes=[0x90, 0x05, 0x14, 0x0A],
    ),
    Case(
        label="A_BounceXYStepsWithHeight",
        commands_factory=lambda: [A_BounceXYStepsWithHeight(x=100, y=127, height=40)],
        expected_bytes=[0x91, 0x64, 0x7F, 0x28],
    ),
    Case(
        label="A_TransferToXYZF",
        commands_factory=lambda: [A_TransferToXYZF(x=5, y=9, z=2, direction=NORTHWEST)],
        expected_bytes=[0x92, 0x05, 0x09, 0xA2],
    ),
    Case(
        label="A_TransferXYZFSteps",
        commands_factory=lambda: [
            A_TransferXYZFSteps(x=2, y=3, z=1, direction=NORTHEAST)
        ],
        expected_bytes=[0x93, 0x02, 0x03, 0xE1],
    ),
    Case(
        label="A_TransferXYZFPixels",
        commands_factory=lambda: [A_TransferXYZFPixels(x=7, y=3, z=9, direction=SOUTH)],
        expected_bytes=[0x94, 0x07, 0x03, 0x49],
    ),
    Case(
        label="A_Set700CToObjectCoord",
        commands_factory=lambda: [
            A_Set700CToObjectCoord(target_npc=NPC_6, coord=COORD_X, pixel=True),
            A_Set700CToObjectCoord(target_npc=DUMMY_0X0B, coord=COORD_Y, pixel=True),
            A_Set700CToObjectCoord(
                target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True, bit_7=True
            ),
            A_Set700CToObjectCoord(target_npc=MARIO, isometric=True, coord=COORD_X),
            A_Set700CToObjectCoord(
                target_npc=CHARACTER_IN_SLOT_3, isometric=True, coord=COORD_Y
            ),
            A_Set700CToObjectCoord(target_npc=MEM_70A8, isometric=True, coord=COORD_Z),
        ],
        expected_bytes=[
            0xC4,
            0x1A,
            0xC5,
            0x0B,
            0xC6,
            0x87,
            0xC4,
            0x40,
            0xC5,
            0x4A,
            0xC6,
            0x50,
        ],
    ),
    Case(
        label="A_Set700CToObjectCoord should fail if both types are specified",
        commands_factory=lambda: [
            A_Set700CToObjectCoord(
                target_npc=NPC_6, coord=COORD_X, pixel=True, isometric=True
            )
        ],
        exception_type=AssertionError,
    ),
    Case(
        label="A_PlaySound",
        commands_factory=lambda: [
            A_PlaySound(sound=91, channel=4),
            A_PlaySound(sound=10, channel=6),
        ],
        expected_bytes=[0xFD, 0x9E, 0x5B, 0x9C, 0x0A],
    ),
    Case(
        label="A_PlaySound should fail with invalid channel",
        commands_factory=lambda: [A_PlaySound(sound=9, channel=2)],
        exception_type=AssertionError,
    ),
    Case(
        label="A_PlaySoundBalance",
        commands_factory=lambda: [A_PlaySoundBalance(sound=14, balance=10)],
        expected_bytes=[0x9D, 0x0E, 0x0A],
    ),
    Case(
        label="A_FadeOutSoundToVolume",
        commands_factory=lambda: [A_FadeOutSoundToVolume(duration=10, volume=20)],
        expected_bytes=[0x9E, 0x0A, 0x14],
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
            A_JmpIfBitSet(Flag(0x7043, 5), ["end_here"]),
            A_JmpIfBitSet(Flag(0x7062, 0), ["end_here"]),
            A_JmpIfBitSet(Flag(0x7086, 6), ["end_here"]),
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
        commands_factory=lambda: [
            A_CompareVarToConst(ShortVar(0x7010), 12544),
            A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_18_ret_61"]),
            A_ReturnQueue(identifier="ACTION_18_ret_61"),
        ],
        expected_bytes=[0xC2, 0x08, 0x00, 0x31, 0xEC, 0x09, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfComparisonResultIsLesser",
        commands_factory=lambda: [
            A_CompareVarToConst(ShortVar(0x7010), 12544),
            A_JmpIfComparisonResultIsLesser(["ACTION_18_ret_61"]),
            A_ReturnQueue(identifier="ACTION_18_ret_61"),
        ],
        expected_bytes=[0xC2, 0x08, 0x00, 0x31, 0xED, 0x09, 0x00, 0xFE],
    ),
    Case(
        "Jump if bit clear",
        commands_factory=lambda: [
            A_JmpIfBitClear(Flag(0x7043, 5), ["end_here"]),
            A_JmpIfBitClear(Flag(0x7062, 0), ["end_here"]),
            A_JmpIfBitClear(Flag(0x7086, 6), ["end_here"]),
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
        commands_factory=lambda: [
            A_JmpIfVarEqualsConst(ShortVar(0x700C), 1, ["end_here"]),
            A_JmpIfVarEqualsConst(ByteVar(0x70AF), 1, ["end_here"]),
            A_JmpIfVarEqualsConst(ShortVar(0x7030), 0, ["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[
            0xE2,
            0x01,
            0x00,
            0x12,
            0x00,
            0xE0,
            0x0F,
            0x01,
            0x12,
            0x00,
            0xE4,
            0x18,
            0x00,
            0x00,
            0x12,
            0x00,
            0xFE,
        ],
    ),
    Case(
        label="A_JmpIfVarNotEqualsConst",
        commands_factory=lambda: [
            A_JmpIfVarNotEqualsConst(ShortVar(0x700C), 13, ["end_here"]),
            A_JmpIfVarNotEqualsConst(ShortVar(0x7032), 1, ["end_here"]),
            A_JmpIfVarNotEqualsConst(ByteVar(0x70AE), 21, ["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[
            0xE3,
            0x0D,
            0x00,
            0x12,
            0x00,
            0xE5,
            0x19,
            0x01,
            0x00,
            0x12,
            0x00,
            0xE1,
            0x0E,
            0x15,
            0x12,
            0x00,
            0xFE,
        ],
    ),
    Case(
        label="A_JmpIf700CAllBitsClear",
        commands_factory=lambda: [
            A_JmpIf700CAllBitsClear(bits=[0], destinations=["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xE6, 0x01, 0x00, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIf700CAnyBitsSet",
        commands_factory=lambda: [
            A_JmpIf700CAnyBitsSet(bits=[0, 1], destinations=["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xE7, 0x03, 0x00, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfRandom2of3",
        commands_factory=lambda: [
            A_StopSound(identifier="start_here"),
            A_JmpIfRandom2of3(["end_here", "start_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x9B, 0xE9, 0x08, 0x00, 0x02, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfRandom1of2",
        commands_factory=lambda: [
            A_JmpIfRandom1of2(["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xE8, 0x05, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIs0",
        commands_factory=lambda: [
            A_JmpIfLoadedMemoryIs0(["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xEA, 0x05, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIsAboveOrEqual0",
        commands_factory=lambda: [
            A_JmpIfLoadedMemoryIsAboveOrEqual0(["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xEF, 0x05, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIsBelow0",
        commands_factory=lambda: [
            A_JmpIfLoadedMemoryIsBelow0(["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xEE, 0x05, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfLoadedMemoryIsNot0",
        commands_factory=lambda: [
            A_JmpIfLoadedMemoryIsNot0(["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xEB, 0x05, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfObjectWithinRange",
        commands_factory=lambda: [
            A_JmpIfObjectWithinRange(
                comparing_npc=NPC_0, usually=48, tiles=0, destinations=["end_here"]
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3A, 0x14, 0x30, 0x00, 0x08, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfObjectWithinRangeSameZ",
        commands_factory=lambda: [
            A_JmpIfObjectWithinRangeSameZ(
                comparing_npc=MARIO,
                usually=128,
                tiles=3,
                destinations=["end_here"],
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3B, 0x00, 0x80, 0x03, 0x08, 0x00, 0xFE],
    ),
    Case(
        label="A_CreatePacketAtObjectCoords",
        commands_factory=lambda: [
            A_CreatePacketAtObjectCoords(
                packet=Packet(
                    packet_id=32,
                ),
                target_npc=DUMMY_0X07,
                destinations=["end_here"],
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3E, 0x20, 0x07, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_CreatePacketAt7010",
        commands_factory=lambda: [
            A_CreatePacketAt7010(
                packet=Packet(
                    packet_id=24,
                ), destinations=["end_here"]
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3F, 0x18, 0x06, 0x00, 0xFE],
    ),
    Case(
        label="A_CreatePacketAt7010WithEvent",
        commands_factory=lambda: [
            A_CreatePacketAt7010WithEvent(
                packet=Packet(
                    packet_id=28,
                ),
                event_id=3077,
                destinations=["end_here"],
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xFD, 0x3E, 0x1C, 0x05, 0x0C, 0x09, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfObjectInSpecificLevel",
        commands_factory=lambda: [
            A_JmpIfObjectInSpecificLevel(
                NPC_6, 251, ["end_here"]
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xF8, 0xFB, 0xB4, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfObjectNotInSpecificLevel",
        commands_factory=lambda: [
            A_JmpIfObjectNotInSpecificLevel(
                NPC_2, 43, ["end_here"]
            ),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xF8, 0x2B, 0x2C, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfObjectInAir",
        commands_factory=lambda: [
            A_JmpIfObjectInAir(NPC_3, ["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0xFD, 0x3D, 0x17, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_UnknownJmp3C",
        commands_factory=lambda: [
            A_UnknownJmp3C(0x00, 0x20, ["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3C, 0x00, 0x20, 0x07, 0x00, 0xFE],
    ),
    Case(
        label="A_JmpIfMarioInAir",
        commands_factory=lambda: [
            A_JmpIfMarioInAir(["end_here"]),
            A_ReturnQueue(identifier="end_here"),
        ],
        expected_bytes=[0x3D, 0x05, 0x00, 0xFE],
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
