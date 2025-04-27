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
    ),
    Case(
        label="NewSpriteAtCoords",
        commands_factory=lambda: [
            NewSpriteAtCoords(
                sprite_id=SPR0519_DRAIN_EXPLOSION,
                sequence=0,
                priority=3,
                vram_address=0x6200,
                palette_row=8,
                overwrite_vram=True,
                overwrite_palette=True,
                overlap_all_sprites=True,
            ),
        ],
        expected_bytes=[0x00, 0x81, 0x20, 0x07, 0x02, 0x00, 0x38, 0x00, 0x62],
    ),
    Case(
        label="SetAMEM32ToXYZCoords",
        commands_factory=lambda: [
            SetAMEM32ToXYZCoords(
                origin=ABSOLUTE_POSITION,
                x=183,
                y=175,
                z=-48,
                set_x=True,
                set_y=True,
                set_z=True,
            ),
        ],
        expected_bytes=[0x01, 0x07, 0xB7, 0x00, 0xAF, 0x00, 0xD0, 0xFF],
    ),
    Case(
        label="DrawSpriteAtAMEM32Coords",
        commands_factory=lambda: [
            DrawSpriteAtAMEM32Coords(
                sprite_id=SPR0491_SHYPER,
                sequence=3,
                store_to_vram=True,
                store_palette=True,
                overlap_all_sprites=True,
            )
        ],
        expected_bytes=[0x03, 0x81, 0x20, 0xEB, 0x01, 0x03],
    ),
    Case(
        label="PauseScriptUntil",
        commands_factory=lambda: [
            PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
            PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        ],
        expected_bytes=[0x04, 0x10, 0x3C, 0x00, 0x74, 0x00, 0x04],
    ),
    Case(
        label="RemoveObject",
        commands_factory=lambda: [RemoveObject()],
        expected_bytes=[],
    ),
    Case(
        label="ReturnObjectQueue",
        commands_factory=lambda: [ReturnObjectQueue()],
        expected_bytes=[],
    ),
    Case(
        label="MoveObject", commands_factory=lambda: [MoveObject()], expected_bytes=[]
    ),
    Case(label="Jmp", commands_factory=lambda: [Jmp()], expected_bytes=[]),
    Case(
        label="Pause1Frame", commands_factory=lambda: [Pause1Frame()], expected_bytes=[]
    ),
    Case(
        label="SetAMEM40ToXYZCoords",
        commands_factory=lambda: [SetAMEM40ToXYZCoords()],
        expected_bytes=[],
    ),
    Case(
        label="MoveSpriteToCoords",
        commands_factory=lambda: [MoveSpriteToCoords()],
        expected_bytes=[],
    ),
    Case(
        label="ResetTargetMappingMemory",
        commands_factory=lambda: [ResetTargetMappingMemory()],
        expected_bytes=[],
    ),
    Case(
        label="ResetObjectMappingMemory",
        commands_factory=lambda: [ResetObjectMappingMemory()],
        expected_bytes=[],
    ),
    Case(
        label="RunSubroutine",
        commands_factory=lambda: [RunSubroutine()],
        expected_bytes=[],
    ),
    Case(
        label="ReturnSubroutine",
        commands_factory=lambda: [ReturnSubroutine()],
        expected_bytes=[],
    ),
    Case(
        label="VisibilityOn",
        commands_factory=lambda: [VisibilityOn()],
        expected_bytes=[],
    ),
    Case(
        label="VisibilityOff",
        commands_factory=lambda: [VisibilityOff()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitToConst",
        commands_factory=lambda: [SetAMEM8BitToConst()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitToConst",
        commands_factory=lambda: [SetAMEM16BitToConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsConst",
        commands_factory=lambda: [JmpIfAMEM8BitEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsConst",
        commands_factory=lambda: [JmpIfAMEM16BitEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsConst",
        commands_factory=lambda: [JmpIfAMEM8BitNotEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsConst",
        commands_factory=lambda: [JmpIfAMEM16BitNotEqualsConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanConst",
        commands_factory=lambda: [JmpIfAMEM8BitLessThanConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanConst",
        commands_factory=lambda: [JmpIfAMEM16BitLessThanConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanConst",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThanConst()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanConst",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThanConst()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitByConst",
        commands_factory=lambda: [IncAMEM8BitByConst()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitByConst",
        commands_factory=lambda: [IncAMEM16BitByConst()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitByConst",
        commands_factory=lambda: [DecAMEM8BitByConst()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitByConst",
        commands_factory=lambda: [DecAMEM16BitByConst()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitTo7E1x",
        commands_factory=lambda: [SetAMEM8BitTo7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitTo7E1x",
        commands_factory=lambda: [SetAMEM16BitTo7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="Set7E1xToAMEM8Bit",
        commands_factory=lambda: [Set7E1xToAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="Set7E1xToAMEM16Bit",
        commands_factory=lambda: [Set7E1xToAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEquals7E1x",
        commands_factory=lambda: [JmpIfAMEM8BitEquals7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEquals7E1x",
        commands_factory=lambda: [JmpIfAMEM16BitEquals7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEquals7E1x",
        commands_factory=lambda: [JmpIfAMEM8BitNotEquals7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEquals7E1x",
        commands_factory=lambda: [JmpIfAMEM16BitNotEquals7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThan7E1x",
        commands_factory=lambda: [JmpIfAMEM8BitLessThan7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThan7E1x",
        commands_factory=lambda: [JmpIfAMEM16BitLessThan7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThan7E1x",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThan7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThan7E1x",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThan7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitBy7E1x",
        commands_factory=lambda: [IncAMEM8BitBy7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitBy7E1x",
        commands_factory=lambda: [IncAMEM16BitBy7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitBy7E1x",
        commands_factory=lambda: [DecAMEM8BitBy7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitBy7E1x",
        commands_factory=lambda: [DecAMEM16BitBy7E1x()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitTo7F",
        commands_factory=lambda: [SetAMEM8BitTo7F()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitTo7F",
        commands_factory=lambda: [SetAMEM16BitTo7F()],
        expected_bytes=[],
    ),
    Case(
        label="Set7FToAMEM8Bit",
        commands_factory=lambda: [Set7FToAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="Set7FToAMEM16Bit",
        commands_factory=lambda: [Set7FToAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEquals7F",
        commands_factory=lambda: [JmpIfAMEM8BitEquals7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEquals7F",
        commands_factory=lambda: [JmpIfAMEM16BitEquals7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEquals7F",
        commands_factory=lambda: [JmpIfAMEM8BitNotEquals7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEquals7F",
        commands_factory=lambda: [JmpIfAMEM16BitNotEquals7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThan7F",
        commands_factory=lambda: [JmpIfAMEM8BitLessThan7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThan7F",
        commands_factory=lambda: [JmpIfAMEM16BitLessThan7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThan7F",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThan7F()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThan7F",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThan7F()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitBy7F",
        commands_factory=lambda: [IncAMEM8BitBy7F()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitBy7F",
        commands_factory=lambda: [IncAMEM16BitBy7F()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitBy7F",
        commands_factory=lambda: [DecAMEM8BitBy7F()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitBy7F",
        commands_factory=lambda: [DecAMEM16BitBy7F()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitToAMEM",
        commands_factory=lambda: [SetAMEM8BitToAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitToAMEM",
        commands_factory=lambda: [SetAMEM16BitToAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEMToAMEM8Bit",
        commands_factory=lambda: [SetAMEMToAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEMToAMEM16Bit",
        commands_factory=lambda: [SetAMEMToAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsAMEM",
        commands_factory=lambda: [JmpIfAMEM8BitEqualsAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsAMEM",
        commands_factory=lambda: [JmpIfAMEM16BitEqualsAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsAMEM",
        commands_factory=lambda: [JmpIfAMEM8BitNotEqualsAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsAMEM",
        commands_factory=lambda: [JmpIfAMEM16BitNotEqualsAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanAMEM",
        commands_factory=lambda: [JmpIfAMEM8BitLessThanAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanAMEM",
        commands_factory=lambda: [JmpIfAMEM16BitLessThanAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanAMEM",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThanAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanAMEM",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThanAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitByAMEM",
        commands_factory=lambda: [IncAMEM8BitByAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitByAMEM",
        commands_factory=lambda: [IncAMEM16BitByAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitByAMEM",
        commands_factory=lambda: [DecAMEM8BitByAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitByAMEM",
        commands_factory=lambda: [DecAMEM16BitByAMEM()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitToOMEMCurrent",
        commands_factory=lambda: [SetAMEM8BitToOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitToOMEMCurrent",
        commands_factory=lambda: [SetAMEM16BitToOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="SetOMEMCurrentToAMEM8Bit",
        commands_factory=lambda: [SetOMEMCurrentToAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="SetOMEMCurrentToAMEM16Bit",
        commands_factory=lambda: [SetOMEMCurrentToAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM8BitEqualsOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM16BitEqualsOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM8BitNotEqualsOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM16BitNotEqualsOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM8BitLessThanOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM16BitLessThanOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitByOMEMCurrent",
        commands_factory=lambda: [IncAMEM8BitByOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitByOMEMCurrent",
        commands_factory=lambda: [IncAMEM16BitByOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitByOMEMCurrent",
        commands_factory=lambda: [DecAMEM8BitByOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitByOMEMCurrent",
        commands_factory=lambda: [DecAMEM16BitByOMEMCurrent()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitTo7E5x",
        commands_factory=lambda: [SetAMEM8BitTo7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitTo7E5x",
        commands_factory=lambda: [SetAMEM16BitTo7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="Set7E5xToAMEM8Bit",
        commands_factory=lambda: [Set7E5xToAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="Set7E5xToAMEM16Bit",
        commands_factory=lambda: [Set7E5xToAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEquals7E5x",
        commands_factory=lambda: [JmpIfAMEM8BitEquals7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEquals7E5x",
        commands_factory=lambda: [JmpIfAMEM16BitEquals7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEquals7E5x",
        commands_factory=lambda: [JmpIfAMEM8BitNotEquals7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEquals7E5x",
        commands_factory=lambda: [JmpIfAMEM16BitNotEquals7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThan7E5x",
        commands_factory=lambda: [JmpIfAMEM8BitLessThan7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThan7E5x",
        commands_factory=lambda: [JmpIfAMEM16BitLessThan7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThan7E5x",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThan7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThan7E5x",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThan7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitBy7E5x",
        commands_factory=lambda: [IncAMEM8BitBy7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitBy7E5x",
        commands_factory=lambda: [IncAMEM16BitBy7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitBy7E5x",
        commands_factory=lambda: [DecAMEM8BitBy7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitBy7E5x",
        commands_factory=lambda: [DecAMEM16BitBy7E5x()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitToOMEMMain",
        commands_factory=lambda: [SetAMEM8BitToOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitToOMEMMain",
        commands_factory=lambda: [SetAMEM16BitToOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="SetOMEMMainToAMEM8Bit",
        commands_factory=lambda: [SetOMEMMainToAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="SetOMEMMainToAMEM16Bit",
        commands_factory=lambda: [SetOMEMMainToAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsOMEMMain",
        commands_factory=lambda: [JmpIfAMEM8BitEqualsOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsOMEMMain",
        commands_factory=lambda: [JmpIfAMEM16BitEqualsOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsOMEMMain",
        commands_factory=lambda: [JmpIfAMEM8BitNotEqualsOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsOMEMMain",
        commands_factory=lambda: [JmpIfAMEM16BitNotEqualsOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanOMEMMain",
        commands_factory=lambda: [JmpIfAMEM8BitLessThanOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanOMEMMain",
        commands_factory=lambda: [JmpIfAMEM16BitLessThanOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanOMEMMain",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThanOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanOMEMMain",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThanOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitByOMEMMain",
        commands_factory=lambda: [IncAMEM8BitByOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitByOMEMMain",
        commands_factory=lambda: [IncAMEM16BitByOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitByOMEMMain",
        commands_factory=lambda: [DecAMEM8BitByOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitByOMEMMain",
        commands_factory=lambda: [DecAMEM16BitByOMEMMain()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM8BitToUnknownShort",
        commands_factory=lambda: [SetAMEM8BitToUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM16BitToUnknownShort",
        commands_factory=lambda: [SetAMEM16BitToUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsUnknownShort",
        commands_factory=lambda: [JmpIfAMEM8BitEqualsUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsUnknownShort",
        commands_factory=lambda: [JmpIfAMEM16BitEqualsUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsUnknownShort",
        commands_factory=lambda: [JmpIfAMEM8BitNotEqualsUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsUnknownShort",
        commands_factory=lambda: [JmpIfAMEM16BitNotEqualsUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanUnknownShort",
        commands_factory=lambda: [JmpIfAMEM8BitLessThanUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanUnknownShort",
        commands_factory=lambda: [JmpIfAMEM16BitLessThanUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanUnknownShort",
        commands_factory=lambda: [JmpIfAMEM8BitGreaterOrEqualThanUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanUnknownShort",
        commands_factory=lambda: [JmpIfAMEM16BitGreaterOrEqualThanUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8BitByUnknownShort",
        commands_factory=lambda: [IncAMEM8BitByUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM16BitByUnknownShort",
        commands_factory=lambda: [IncAMEM16BitByUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8BitByUnknownShort",
        commands_factory=lambda: [DecAMEM8BitByUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM16BitByUnknownShort",
        commands_factory=lambda: [DecAMEM16BitByUnknownShort()],
        expected_bytes=[],
    ),
    Case(
        label="IncAMEM8Bit", commands_factory=lambda: [IncAMEM8Bit()], expected_bytes=[]
    ),
    Case(
        label="IncAMEM16Bit",
        commands_factory=lambda: [IncAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="DecAMEM8Bit", commands_factory=lambda: [DecAMEM8Bit()], expected_bytes=[]
    ),
    Case(
        label="DecAMEM16Bit",
        commands_factory=lambda: [DecAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="ClearAMEM8Bit",
        commands_factory=lambda: [ClearAMEM8Bit()],
        expected_bytes=[],
    ),
    Case(
        label="ClearAMEM16Bit",
        commands_factory=lambda: [ClearAMEM16Bit()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEMBits", commands_factory=lambda: [SetAMEMBits()], expected_bytes=[]
    ),
    Case(
        label="ClearAMEMBits",
        commands_factory=lambda: [ClearAMEMBits()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEMBitsSet",
        commands_factory=lambda: [JmpIfAMEMBitsSet()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfAMEMBitsClear",
        commands_factory=lambda: [JmpIfAMEMBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="AttackTimerBegins",
        commands_factory=lambda: [AttackTimerBegins()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilAMEMBitsSet",
        commands_factory=lambda: [PauseScriptUntilAMEMBitsSet()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilAMEMBitsClear",
        commands_factory=lambda: [PauseScriptUntilAMEMBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="SpriteSequence",
        commands_factory=lambda: [SpriteSequence()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEM60ToCurrentTarget",
        commands_factory=lambda: [SetAMEM60ToCurrentTarget()],
        expected_bytes=[],
    ),
    Case(
        label="GameOverIfNoAlliesStanding",
        commands_factory=lambda: [GameOverIfNoAlliesStanding()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilSpriteSequenceDone",
        commands_factory=lambda: [PauseScriptUntilSpriteSequenceDone()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfTargetDisabled",
        commands_factory=lambda: [JmpIfTargetDisabled()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfTargetEnabled",
        commands_factory=lambda: [JmpIfTargetEnabled()],
        expected_bytes=[],
    ),
    Case(
        label="SpriteQueue", commands_factory=lambda: [SpriteQueue()], expected_bytes=[]
    ),
    Case(
        label="ReturnSpriteQueue",
        commands_factory=lambda: [ReturnSpriteQueue()],
        expected_bytes=[],
    ),
    Case(
        label="DisplayMessageAtOMEM60As",
        commands_factory=lambda: [DisplayMessageAtOMEM60As()],
        expected_bytes=[],
    ),
    Case(
        label="ObjectQueueAtOffsetAndIndexAtAMEM60",
        commands_factory=lambda: [ObjectQueueAtOffsetAndIndexAtAMEM60()],
        expected_bytes=[],
    ),
    Case(
        label="ObjectQueueAtOffsetAndIndex",
        commands_factory=lambda: [ObjectQueueAtOffsetAndIndex()],
        expected_bytes=[],
    ),
    Case(
        label="SetOMEM60To072C",
        commands_factory=lambda: [SetOMEM60To072C()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEMToRandomByte",
        commands_factory=lambda: [SetAMEMToRandomByte()],
        expected_bytes=[],
    ),
    Case(
        label="SetAMEMToRandomShort",
        commands_factory=lambda: [SetAMEMToRandomShort()],
        expected_bytes=[],
    ),
    Case(
        label="EnableSpritesOnSubscreen",
        commands_factory=lambda: [EnableSpritesOnSubscreen()],
        expected_bytes=[],
    ),
    Case(
        label="DisableSpritesOnSubscreen",
        commands_factory=lambda: [DisableSpritesOnSubscreen()],
        expected_bytes=[],
    ),
    Case(
        label="NewEffectObject",
        commands_factory=lambda: [NewEffectObject()],
        expected_bytes=[],
    ),
    Case(
        label="Pause2Frames",
        commands_factory=lambda: [Pause2Frames()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilBitsClear",
        commands_factory=lambda: [PauseScriptUntilBitsClear()],
        expected_bytes=[],
    ),
    Case(
        label="ClearEffectIndex",
        commands_factory=lambda: [ClearEffectIndex()],
        expected_bytes=[],
    ),
    Case(label="Layer3On", commands_factory=lambda: [Layer3On()], expected_bytes=[]),
    Case(label="Layer3Off", commands_factory=lambda: [Layer3Off()], expected_bytes=[]),
    Case(
        label="DisplayMessage",
        commands_factory=lambda: [DisplayMessage()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilDialogClosed",
        commands_factory=lambda: [PauseScriptUntilDialogClosed()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutObject",
        commands_factory=lambda: [FadeOutObject()],
        expected_bytes=[],
    ),
    Case(
        label="ResetSpriteSequence",
        commands_factory=lambda: [ResetSpriteSequence()],
        expected_bytes=[],
    ),
    Case(
        label="ShineEffect", commands_factory=lambda: [ShineEffect()], expected_bytes=[]
    ),
    Case(
        label="FadeOutEffect",
        commands_factory=lambda: [FadeOutEffect()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutSprite",
        commands_factory=lambda: [FadeOutSprite()],
        expected_bytes=[],
    ),
    Case(
        label="FadeOutScreen",
        commands_factory=lambda: [FadeOutScreen()],
        expected_bytes=[],
    ),
    Case(
        label="FadeInEffect",
        commands_factory=lambda: [FadeInEffect()],
        expected_bytes=[],
    ),
    Case(
        label="FadeInSprite",
        commands_factory=lambda: [FadeInSprite()],
        expected_bytes=[],
    ),
    Case(
        label="FadeInScreen",
        commands_factory=lambda: [FadeInScreen()],
        expected_bytes=[],
    ),
    Case(
        label="ShakeScreen", commands_factory=lambda: [ShakeScreen()], expected_bytes=[]
    ),
    Case(
        label="ShakeSprites",
        commands_factory=lambda: [ShakeSprites()],
        expected_bytes=[],
    ),
    Case(
        label="ShakeScreenAndSprites",
        commands_factory=lambda: [ShakeScreenAndSprites()],
        expected_bytes=[],
    ),
    Case(
        label="StopShakingObject",
        commands_factory=lambda: [StopShakingObject()],
        expected_bytes=[],
    ),
    Case(
        label="ScreenFlashWithDuration",
        commands_factory=lambda: [ScreenFlashWithDuration()],
        expected_bytes=[],
    ),
    Case(
        label="ScreenFlash", commands_factory=lambda: [ScreenFlash()], expected_bytes=[]
    ),
    Case(
        label="InitializeBonusMessageSequence",
        commands_factory=lambda: [InitializeBonusMessageSequence()],
        expected_bytes=[],
    ),
    Case(
        label="DisplayBonusMessage",
        commands_factory=lambda: [DisplayBonusMessage()],
        expected_bytes=[],
    ),
    Case(
        label="PauseScriptUntilBonusMessageComplete",
        commands_factory=lambda: [PauseScriptUntilBonusMessageComplete()],
        expected_bytes=[],
    ),
    Case(
        label="WaveEffect", commands_factory=lambda: [WaveEffect()], expected_bytes=[]
    ),
    Case(
        label="StopWaveEffect",
        commands_factory=lambda: [StopWaveEffect()],
        expected_bytes=[],
    ),
    Case(
        label="ScreenEffect",
        commands_factory=lambda: [ScreenEffect()],
        expected_bytes=[],
    ),
    Case(
        label="JmpIfTimedHitSuccess",
        commands_factory=lambda: [JmpIfTimedHitSuccess()],
        expected_bytes=[],
    ),
    Case(label="PlaySound", commands_factory=lambda: [PlaySound()], expected_bytes=[]),
    Case(
        label="PlayMusicAtCurrentVolume",
        commands_factory=lambda: [PlayMusicAtCurrentVolume()],
        expected_bytes=[],
    ),
    Case(
        label="PlayMusicAtVolume",
        commands_factory=lambda: [PlayMusicAtVolume()],
        expected_bytes=[],
    ),
    Case(
        label="StopCurrentSoundEffect",
        commands_factory=lambda: [StopCurrentSoundEffect()],
        expected_bytes=[],
    ),
    Case(
        label="FadeCurrentMusicToVolume",
        commands_factory=lambda: [FadeCurrentMusicToVolume()],
        expected_bytes=[],
    ),
    Case(label="SetTarget", commands_factory=lambda: [SetTarget()], expected_bytes=[]),
    Case(
        label="AddItemToStandardInventory",
        commands_factory=lambda: [AddItemToStandardInventory()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveItemFromStandardInventory",
        commands_factory=lambda: [RemoveItemFromStandardInventory()],
        expected_bytes=[],
    ),
    Case(
        label="AddItemToKeyItemInventory",
        commands_factory=lambda: [AddItemToKeyItemInventory()],
        expected_bytes=[],
    ),
    Case(
        label="RemoveItemFromKeyItemInventory",
        commands_factory=lambda: [RemoveItemFromKeyItemInventory()],
        expected_bytes=[],
    ),
    Case(label="AddCoins", commands_factory=lambda: [AddCoins()], expected_bytes=[]),
    Case(
        label="AddYoshiCookiesToInventory",
        commands_factory=lambda: [AddYoshiCookiesToInventory()],
        expected_bytes=[],
    ),
    Case(
        label="DoMaskEffect",
        commands_factory=lambda: [DoMaskEffect()],
        expected_bytes=[],
    ),
    Case(
        label="SetMaskCoords",
        commands_factory=lambda: [SetMaskCoords()],
        expected_bytes=[],
    ),
    Case(
        label="SetSequenceSpeed",
        commands_factory=lambda: [SetSequenceSpeed()],
        expected_bytes=[],
    ),
    Case(
        label="StartTrackingAllyButtonInputs",
        commands_factory=lambda: [StartTrackingAllyButtonInputs()],
        expected_bytes=[],
    ),
    Case(
        label="EndTrackingAllyButtonInputs",
        commands_factory=lambda: [EndTrackingAllyButtonInputs()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForOneTieredButtonPress",
        commands_factory=lambda: [TimingForOneTieredButtonPress()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForOneBinaryButtonPress",
        commands_factory=lambda: [TimingForOneBinaryButtonPress()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForMultipleButtonPresses",
        commands_factory=lambda: [TimingForMultipleButtonPresses()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForButtonMashUnknown",
        commands_factory=lambda: [TimingForButtonMashUnknown()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForButtonMashCount",
        commands_factory=lambda: [TimingForButtonMashCount()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForRotationCount",
        commands_factory=lambda: [TimingForRotationCount()],
        expected_bytes=[],
    ),
    Case(
        label="TimingForChargePress",
        commands_factory=lambda: [TimingForChargePress()],
        expected_bytes=[],
    ),
    Case(
        label="SummonMonster",
        commands_factory=lambda: [SummonMonster()],
        expected_bytes=[],
    ),
    Case(
        label="MuteTimingJmp",
        commands_factory=lambda: [MuteTimingJmp()],
        expected_bytes=[],
    ),
    Case(
        label="DisplayCantRunDialog",
        commands_factory=lambda: [DisplayCantRunDialog()],
        expected_bytes=[],
    ),
    Case(
        label="StoreOMEM60ToItemInventory",
        commands_factory=lambda: [StoreOMEM60ToItemInventory()],
        expected_bytes=[],
    ),
    Case(
        label="RunBattleEvent",
        commands_factory=lambda: [RunBattleEvent()],
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
            script = AnimationScript(commands)
            bank = AnimationScriptBank(
                name=case.label,
                pointer_table_start=0x35C000,
                start=0x35C002,
                end=0x35CFFF,
                scripts=[script],
            )
            bank.render()
        if case.exception:
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
