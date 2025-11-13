import pytest
from typing import Optional, Type, List
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *

from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.commands import Enemy
from smrpgpatchbuilder.datatypes.items.classes import RegularItem
from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    ScriptBankTooLongException,
)

from dataclasses import dataclass

class SheepAttackItem(RegularItem):
    _item_id: int = 136

class LambsLureItem(RegularItem):
    _item_id: int = 143

class RareFrogCoinItem(RegularItem):
    _item_name: str = "RareFrogCoin"

    _item_id: int = 128

class YARIDOVICH(Enemy):
    _monster_id: int = 226


@dataclass
class Case:
    label: str
    commands_factory: callable
    expected_bytes: Optional[List[int]] = None
    exception: Optional[str] = None
    exception_type: Optional[Type] = None
    expected_length: Optional[int] = None


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
                sprite_id=519,
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
                sprite_id=491,
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
            PauseScriptUntil(condition=UNKNOWN_PAUSE_4),
        ],
        expected_bytes=[
            0x04,
            0x10,
            0x3C,
            0x00,
            0x74,
            0x00,
            0x04,
            0x04,
            0x04,
            0x00,
            0x00,
        ],
    ),
    Case(
        label="RemoveObject",
        commands_factory=lambda: [RemoveObject()],
        expected_bytes=[0x05],
    ),
    Case(
        label="ReturnObjectQueue",
        commands_factory=lambda: [ReturnObjectQueue()],
        expected_bytes=[0x07],
    ),
    Case(
        label="MoveObject",
        commands_factory=lambda: [
            MoveObject(
                speed=1,
                start_position=256,
                end_position=0,
                apply_to_x=True,
                should_set_speed=True,
            ),
        ],
        expected_bytes=[0x08, 0x84, 0x00, 0x01, 0x00, 0x00, 0x01, 0x00],
    ),
    Case(
        label="Jmp",
        commands_factory=lambda: [
            StopCurrentSoundEffect(identifier="jmp_here"),
            Jmp(["jmp_here"]),
        ],
        expected_bytes=[0xB2, 0x09, 0x02, 0xC0],
    ),
    Case(
        label="Pause1Frame",
        commands_factory=lambda: [Pause1Frame()],
        expected_bytes=[0x0A],
    ),
    Case(
        label="SetAMEM40ToXYZCoords",
        commands_factory=lambda: [
            SetAMEM40ToXYZCoords(
                origin=CASTER_INITIAL_POSITION, x=-22, y=8, z=0, set_y=True, set_z=True
            ),
            SetAMEM40ToXYZCoords(
                origin=ABSOLUTE_POSITION,
                x=184,
                y=128,
                z=0,
                set_x=True,
                set_y=True,
                set_z=True,
            ),
        ],
        expected_bytes=[
            0x0B,
            0x16,
            0xEA,
            0xFF,
            0x08,
            0x00,
            0x00,
            0x00,
            0x0B,
            0x07,
            0xB8,
            0x00,
            0x80,
            0x00,
            0x00,
            0x00,
        ],
    ),
    Case(
        label="MoveSpriteToCoords",
        commands_factory=lambda: [
            MoveSpriteToCoords(shift_type=SHIFT_TYPE_0X00, speed=512, arch_height=0),
            MoveSpriteToCoords(
                shift_type=SHIFT_TYPE_TRANSFER, speed=1024, arch_height=96
            ),
        ],
        expected_bytes=[
            0x0C,
            0x00,
            0x00,
            0x02,
            0x00,
            0x00,
            0x0C,
            0x04,
            0x00,
            0x04,
            0x60,
            0x00,
        ],
    ),
    Case(
        label="ResetTargetMappingMemory",
        commands_factory=lambda: [ResetTargetMappingMemory()],
        expected_bytes=[0x0E],
    ),
    Case(
        label="ResetObjectMappingMemory",
        commands_factory=lambda: [ResetObjectMappingMemory()],
        expected_bytes=[0x0F],
    ),
    Case(
        label="RunSubroutine",
        commands_factory=lambda: [
            RunSubroutine(["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x10, 0x05, 0xC0, 0x11],
    ),
    Case(
        label="VisibilityOn",
        commands_factory=lambda: [VisibilityOn(0x01)],
        expected_bytes=[0x1A, 0x01],
    ),
    Case(
        label="VisibilityOff",
        commands_factory=lambda: [VisibilityOff(0x10)],
        expected_bytes=[0x1B, 0x10],
    ),
    Case(
        label="SetAMEM8BitToConst",
        commands_factory=lambda: [
            SetAMEM8BitToConst(0x68, 1),
        ],
        expected_bytes=[0x20, 0x08, 0x01, 0x00],
    ),
    Case(
        label="SetAMEM16BitToConst",
        commands_factory=lambda: [SetAMEM16BitToConst(0x60, 0)],
        expected_bytes=[0x21, 0x00, 0x00, 0x00],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsConst",
        commands_factory=lambda: [
            JmpIfAMEM8BitEqualsConst(0x60, 4, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x00, 0x04, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsConst",
        commands_factory=lambda: [
            JmpIfAMEM16BitEqualsConst(0x60, 77, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x00, 0x4D, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsConst",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEqualsConst(0x60, 0, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x00, 0x00, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsConst",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEqualsConst(0x62, 6, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x02, 0x06, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanConst",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThanConst(0x68, 3, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x08, 0x03, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanConst",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThanConst(0x62, 6, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x02, 0x06, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanConst",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThanConst(0x60, 31, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x00, 0x1F, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanConst",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThanConst(0x62, 128, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x02, 0x80, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitByConst",
        commands_factory=lambda: [
            IncAMEM8BitByConst(0x67, 2),
        ],
        expected_bytes=[0x2C, 0x07, 0x02, 0x00],
    ),
    Case(
        label="IncAMEM16BitByConst",
        commands_factory=lambda: [
            IncAMEM16BitByConst(0x60, 96),
        ],
        expected_bytes=[0x2D, 0x00, 0x60, 0x00],
    ),
    Case(
        label="DecAMEM8BitByConst",
        commands_factory=lambda: [DecAMEM8BitByConst(0x6B, 2)],
        expected_bytes=[0x2E, 0x0B, 0x02, 0x00],
    ),
    Case(
        label="DecAMEM16BitByConst",
        commands_factory=lambda: [
            DecAMEM16BitByConst(0x60, 64),
        ],
        expected_bytes=[0x2F, 0x00, 0x40, 0x00],
    ),
    Case(
        label="SetAMEM8BitTo7E1x",
        commands_factory=lambda: [
            SetAMEM8BitTo7E1x(0x60, 0x7EFAC3),
        ],
        expected_bytes=[0x20, 0x10, 0xC3, 0xFA],
    ),
    Case(
        label="SetAMEM16BitTo7E1x",
        commands_factory=lambda: [
            SetAMEM16BitTo7E1x(0x60, 0x7EE022),
        ],
        expected_bytes=[0x21, 0x10, 0x22, 0xE0],
    ),
    Case(
        label="Set7E1xToAMEM8Bit",
        commands_factory=lambda: [
            Set7E1xToAMEM8Bit(0x7EE001, 0x60),
        ],
        expected_bytes=[0x22, 0x10, 0x01, 0xE0],
    ),
    Case(
        label="Set7E1xToAMEM16Bit",
        commands_factory=lambda: [
            Set7E1xToAMEM16Bit(0x7EE022, 0x60),
        ],
        expected_bytes=[0x23, 0x10, 0x22, 0xE0],
    ),
    Case(
        label="JmpIfAMEM8BitEquals7E1x",
        commands_factory=lambda: [
            JmpIfAMEM8BitEquals7E1x(0x61, 0x7EE003, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x11, 0x03, 0xE0, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEquals7E1x",
        commands_factory=lambda: [
            JmpIfAMEM16BitEquals7E1x(0x61, 0x7EE005, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x11, 0x05, 0xE0, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEquals7E1x",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEquals7E1x(0x60, 0x7EFA00, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x10, 0x00, 0xFA, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEquals7E1x",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEquals7E1x(0x62, 0x7EFA00, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x12, 0x00, 0xFA, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThan7E1x",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThan7E1x(0x63, 0x7E0F00, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x13, 0x00, 0x0F, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThan7E1x",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThan7E1x(0x61, 0x7EE100, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x11, 0x00, 0xE1, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThan7E1x",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThan7E1x(0x60, 0x7E1000, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x10, 0x00, 0x10, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThan7E1x",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThan7E1x(0x65, 0x7E0200, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[
            0x2B,
            0x15,
            0x00,
            0x02,
            0x08,
            0xC0,
            0x11,
        ],
    ),
    Case(
        label="IncAMEM8BitBy7E1x",
        commands_factory=lambda: [IncAMEM8BitBy7E1x(0x67, 0x7E3100)],
        expected_bytes=[0x2C, 0x17, 0x00, 0x31],
    ),
    Case(
        label="IncAMEM16BitBy7E1x",
        commands_factory=lambda: [IncAMEM16BitBy7E1x(0x66, 0x7E1000)],
        expected_bytes=[0x2D, 0x16, 0x00, 0x10],
    ),
    Case(
        label="DecAMEM8BitBy7E1x",
        commands_factory=lambda: [DecAMEM8BitBy7E1x(0x61, 0x7EA000)],
        expected_bytes=[0x2E, 0x11, 0x00, 0xA0],
    ),
    Case(
        label="DecAMEM16BitBy7E1x",
        commands_factory=lambda: [DecAMEM16BitBy7E1x(0x64, 0x7E0F00)],
        expected_bytes=[0x2F, 0x14, 0x00, 0x0F],
    ),
    Case(
        label="SetAMEM8BitTo7F",
        commands_factory=lambda: [SetAMEM8BitTo7F(0x60, 0x7F2100)],
        expected_bytes=[0x20, 0x20, 0x00, 0x21],
    ),
    Case(
        label="SetAMEM16BitTo7F",
        commands_factory=lambda: [SetAMEM16BitTo7F(0x63, 0x7F0D00)],
        expected_bytes=[0x21, 0x23, 0x00, 0x0D],
    ),
    Case(
        label="Set7FToAMEM8Bit",
        commands_factory=lambda: [Set7FToAMEM8Bit(0x7FE000, 0x62)],
        expected_bytes=[0x22, 0x22, 0x00, 0xE0],
    ),
    Case(
        label="Set7FToAMEM16Bit",
        commands_factory=lambda: [
            Set7FToAMEM16Bit(
                0x7F1C00,
                0x62,
            )
        ],
        expected_bytes=[0x23, 0x22, 0x00, 0x1C],
    ),
    Case(
        label="JmpIfAMEM8BitEquals7F",
        commands_factory=lambda: [
            JmpIfAMEM8BitEquals7F(0x60, 0x7F0BA0, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x20, 0xA0, 0x0B, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEquals7F",
        commands_factory=lambda: [
            JmpIfAMEM16BitEquals7F(0x60, 0x7F0BA0, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x20, 0xA0, 0x0B, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEquals7F",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEquals7F(0x64, 0x7F0E00, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x24, 0x00, 0x0E, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEquals7F",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEquals7F(0x64, 0x7F0E00, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x24, 0x00, 0x0E, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThan7F",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThan7F(0x68, 0x7F1110, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x28, 0x10, 0x11, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThan7F",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThan7F(0x68, 0x7F1110, ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x28, 0x10, 0x11, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThan7F",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThan7F(
                amem=0x6A, address=0x7F7300, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x2A, 0x00, 0x73, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThan7F",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThan7F(
                amem=0x6A, address=0x7F7300, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x2A, 0x00, 0x73, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitBy7F",
        commands_factory=lambda: [IncAMEM8BitBy7F(0x67, 0x7F0BA0)],
        expected_bytes=[0x2C, 0x27, 0xA0, 0x0B],
    ),
    Case(
        label="IncAMEM16BitBy7F",
        commands_factory=lambda: [IncAMEM16BitBy7F(0x67, 0x7F0BA0)],
        expected_bytes=[0x2D, 0x27, 0xA0, 0x0B],
    ),
    Case(
        label="DecAMEM8BitBy7F",
        commands_factory=lambda: [DecAMEM8BitBy7F(0x67, 0x7F0BA0)],
        expected_bytes=[0x2E, 0x27, 0xA0, 0x0B],
    ),
    Case(
        label="DecAMEM16BitBy7F",
        commands_factory=lambda: [DecAMEM16BitBy7F(0x67, 0x7F0BA0)],
        expected_bytes=[0x2F, 0x27, 0xA0, 0x0B],
    ),
    Case(
        label="SetAMEM8BitToAMEM",
        commands_factory=lambda: [
            SetAMEM8BitToAMEM(amem=0x62, source_amem=0x60, upper=0x00),
        ],
        expected_bytes=[0x20, 0x32, 0x00, 0x00],
    ),
    Case(
        label="SetAMEM16BitToAMEM",
        commands_factory=lambda: [
            SetAMEM16BitToAMEM(amem=0x68, source_amem=0x6A, upper=0x30),
        ],
        expected_bytes=[0x21, 0x38, 0x3A, 0x00],
    ),
    Case(
        label="SetAMEMToAMEM8Bit",
        commands_factory=lambda: [
            SetAMEMToAMEM8Bit(dest_amem=0x67, upper=0x40, amem=0x6F),
        ],
        expected_bytes=[0x22, 0x3F, 0x47, 0x00],
    ),
    Case(
        label="SetAMEMToAMEM16Bit",
        commands_factory=lambda: [
            SetAMEMToAMEM16Bit(dest_amem=0x6E, upper=0x00, amem=0x62),
        ],
        expected_bytes=[0x23, 0x32, 0x0E, 0x00],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsAMEM",
        commands_factory=lambda: [
            JmpIfAMEM8BitEqualsAMEM(
                amem=0x68, source_amem=0x69, upper=0x60, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x38, 0x69, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsAMEM",
        commands_factory=lambda: [
            JmpIfAMEM16BitEqualsAMEM(
                amem=0x68, source_amem=0x69, upper=0x60, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x38, 0x69, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsAMEM",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEqualsAMEM(
                amem=0x6E, source_amem=0x6C, upper=0x60, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x3E, 0x6C, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsAMEM",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEqualsAMEM(
                amem=0x6E, source_amem=0x6C, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x3E, 0xC, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanAMEM",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThanAMEM(
                amem=0x68, source_amem=0x6D, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x38, 0x0D, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanAMEM",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThanAMEM(
                amem=0x68, source_amem=0x6D, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x38, 0x0D, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanAMEM",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThanAMEM(
                amem=0x6A,
                source_amem=0x6B,
                upper=0x60,
                destinations=["jmp"],
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x3A, 0x6B, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanAMEM",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThanAMEM(
                amem=0x6A,
                source_amem=0x6B,
                upper=0x60,
                destinations=["jmp"],
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x3A, 0x6B, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitByAMEM",
        commands_factory=lambda: [IncAMEM8BitByAMEM(amem=0x61, source_amem=0x63)],
        expected_bytes=[0x2C, 0x31, 0x03, 0x00],
    ),
    Case(
        label="IncAMEM16BitByAMEM",
        commands_factory=lambda: [IncAMEM16BitByAMEM(amem=0x61, source_amem=0x63)],
        expected_bytes=[0x2D, 0x31, 0x03, 0x00],
    ),
    Case(
        label="DecAMEM8BitByAMEM",
        commands_factory=lambda: [DecAMEM8BitByAMEM(amem=0x61, source_amem=0x63)],
        expected_bytes=[0x2E, 0x31, 0x03, 0x00],
    ),
    Case(
        label="DecAMEM16BitByAMEM",
        commands_factory=lambda: [DecAMEM16BitByAMEM(amem=0x61, source_amem=0x63)],
        expected_bytes=[0x2F, 0x31, 0x03, 0x00],
    ),
    Case(
        label="SetAMEM8BitToOMEMCurrent",
        commands_factory=lambda: [SetAMEM8BitToOMEMCurrent(0x60, 0x6F)],
        expected_bytes=[0x20, 0x40, 0x6F, 0x00],
    ),
    Case(
        label="SetAMEM16BitToOMEMCurrent",
        commands_factory=lambda: [SetAMEM16BitToOMEMCurrent(0x60, 0x6F)],
        expected_bytes=[0x21, 0x40, 0x6F, 0x00],
    ),
    Case(
        label="SetOMEMCurrentToAMEM8Bit",
        commands_factory=lambda: [
            SetOMEMCurrentToAMEM8Bit(omem=0x2D, amem=0x60),
        ],
        expected_bytes=[0x22, 0x40, 0x2D, 0x00],
    ),
    Case(
        label="SetOMEMCurrentToAMEM16Bit",
        commands_factory=lambda: [SetOMEMCurrentToAMEM16Bit(omem=0x51, amem=0x62)],
        expected_bytes=[0x23, 0x42, 0x51, 0x00],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM8BitEqualsOMEMCurrent(amem=0x60, omem=0x5C, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x40, 0x5C, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM16BitEqualsOMEMCurrent(amem=0x60, omem=0x5C, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x40, 0x5C, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEqualsOMEMCurrent(
                amem=0x64, omem=0xE9, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x44, 0xE9, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEqualsOMEMCurrent(
                amem=0x64, omem=0xE9, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x44, 0xE9, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThanOMEMCurrent(
                amem=0x66, omem=0x18, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x46, 0x18, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThanOMEMCurrent(
                amem=0x66, omem=0x18, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x46, 0x18, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThanOMEMCurrent(
                amem=0x67, omem=0x44, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x47, 0x44, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThanOMEMCurrent(
                amem=0x67, omem=0x44, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x47, 0x44, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitByOMEMCurrent",
        commands_factory=lambda: [IncAMEM8BitByOMEMCurrent(amem=0x62, omem=0xF7)],
        expected_bytes=[0x2C, 0x42, 0xF7, 0x00],
    ),
    Case(
        label="IncAMEM16BitByOMEMCurrent",
        commands_factory=lambda: [IncAMEM16BitByOMEMCurrent(amem=0x62, omem=0xF7)],
        expected_bytes=[0x2D, 0x42, 0xF7, 0x00],
    ),
    Case(
        label="DecAMEM8BitByOMEMCurrent",
        commands_factory=lambda: [DecAMEM8BitByOMEMCurrent(amem=0x62, omem=0xF7)],
        expected_bytes=[0x2E, 0x42, 0xF7, 0x00],
    ),
    Case(
        label="DecAMEM16BitByOMEMCurrent",
        commands_factory=lambda: [DecAMEM16BitByOMEMCurrent(amem=0x62, omem=0xF7)],
        expected_bytes=[0x2F, 0x42, 0xF7, 0x00],
    ),
    Case(
        label="SetAMEM8BitTo7E5x",
        commands_factory=lambda: [
            SetAMEM8BitTo7E5x(0x60, 0x7E002C),
        ],
        expected_bytes=[0x20, 0x50, 0x2C, 0x00],
    ),
    Case(
        label="SetAMEM16BitTo7E5x",
        commands_factory=lambda: [
            SetAMEM16BitTo7E5x(0x60, 0x7E002C),
        ],
        expected_bytes=[0x21, 0x50, 0x2C, 0x00],
    ),
    Case(
        label="Set7E5xToAMEM8Bit",
        commands_factory=lambda: [
            Set7E5xToAMEM8Bit(0x7E0000, 0x62),
        ],
        expected_bytes=[0x22, 0x52, 0x00, 0x00],
    ),
    Case(
        label="Set7E5xToAMEM16Bit",
        commands_factory=lambda: [
            Set7E5xToAMEM16Bit(0x7E0070, 0x62),
        ],
        expected_bytes=[0x23, 0x52, 0x70, 0x00],
    ),
    Case(
        label="JmpIfAMEM8BitEquals7E5x",
        commands_factory=lambda: [
            JmpIfAMEM8BitEquals7E5x(amem=0x61, address=0x7EFFF0, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x51, 0xF0, 0xFF, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEquals7E5x",
        commands_factory=lambda: [
            JmpIfAMEM16BitEquals7E5x(amem=0x61, address=0x7EFFF0, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x51, 0xF0, 0xFF, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEquals7E5x",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEquals7E5x(
                amem=0x6A, address=0x7E01B0, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x5A, 0xB0, 0x01, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEquals7E5x",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEquals7E5x(
                amem=0x6A, address=0x7E01B0, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x5A, 0xB0, 0x01, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThan7E5x",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThan7E5x(0x65, 0x7E1A00, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x55, 0x00, 0x1A, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThan7E5x",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThan7E5x(0x65, 0x7E1A00, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x55, 0x00, 0x1A, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThan7E5x",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThan7E5x(0x66, 0x7E0500, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x56, 0x00, 0x05, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThan7E5x",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThan7E5x(0x66, 0x7E0500, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x56, 0x00, 0x05, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitBy7E5x",
        commands_factory=lambda: [IncAMEM8BitBy7E5x(amem=0x63, address=0x7EAA00)],
        expected_bytes=[0x2C, 0x53, 0x00, 0xAA],
    ),
    Case(
        label="IncAMEM16BitBy7E5x",
        commands_factory=lambda: [IncAMEM16BitBy7E5x(amem=0x63, address=0x7EAA00)],
        expected_bytes=[0x2D, 0x53, 0x00, 0xAA],
    ),
    Case(
        label="DecAMEM8BitBy7E5x",
        commands_factory=lambda: [DecAMEM8BitBy7E5x(amem=0x63, address=0x7EAA00)],
        expected_bytes=[0x2E, 0x53, 0x00, 0xAA],
    ),
    Case(
        label="DecAMEM16BitBy7E5x",
        commands_factory=lambda: [DecAMEM16BitBy7E5x(amem=0x63, address=0x7EAA00)],
        expected_bytes=[0x2F, 0x53, 0x00, 0xAA],
    ),
    Case(
        label="SetAMEM8BitToOMEMMain",
        commands_factory=lambda: [
            SetAMEM8BitToOMEMMain(amem=0x6F, omem=0x6F),
        ],
        expected_bytes=[0x20, 0x6F, 0x6F, 0x00],
    ),
    Case(
        label="SetAMEM16BitToOMEMMain",
        commands_factory=lambda: [
            SetAMEM16BitToOMEMMain(amem=0x6F, omem=0x6F),
        ],
        expected_bytes=[0x21, 0x6F, 0x6F, 0x00],
    ),
    Case(
        label="SetOMEMMainToAMEM8Bit",
        commands_factory=lambda: [
            SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ],
        expected_bytes=[0x22, 0x6F, 0x6F, 0x00],
    ),
    Case(
        label="SetOMEMMainToAMEM16Bit",
        commands_factory=lambda: [SetOMEMMainToAMEM16Bit(omem=0x4F, amem=0x62)],
        expected_bytes=[0x23, 0x62, 0x4F, 0x00],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM8BitEqualsOMEMMain(amem=0x61, omem=0x64, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0x61, 0x64, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM16BitEqualsOMEMMain(amem=0x61, omem=0x64, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0x61, 0x64, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEqualsOMEMMain(amem=0x6A, omem=0x8A, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x6A, 0x8A, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEqualsOMEMMain(amem=0x6A, omem=0x8A, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x6A, 0x8A, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThanOMEMMain(amem=0x64, omem=0xB9, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x64, 0xB9, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThanOMEMMain(amem=0x64, omem=0xB9, destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x64, 0xB9, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThanOMEMMain(
                amem=0x62, omem=0x9A, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x62, 0x9A, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanOMEMMain",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThanOMEMMain(
                amem=0x62, omem=0x9A, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x62, 0x9A, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitByOMEMMain",
        commands_factory=lambda: [IncAMEM8BitByOMEMMain(amem=0x6B, omem=0x70)],
        expected_bytes=[0x2C, 0x6B, 0x70, 0x00],
    ),
    Case(
        label="IncAMEM16BitByOMEMMain",
        commands_factory=lambda: [IncAMEM16BitByOMEMMain(amem=0x6B, omem=0x70)],
        expected_bytes=[0x2D, 0x6B, 0x70, 0x00],
    ),
    Case(
        label="DecAMEM8BitByOMEMMain",
        commands_factory=lambda: [DecAMEM8BitByOMEMMain(amem=0x6B, omem=0x70)],
        expected_bytes=[0x2E, 0x6B, 0x70, 0x00],
    ),
    Case(
        label="DecAMEM16BitByOMEMMain",
        commands_factory=lambda: [DecAMEM16BitByOMEMMain(amem=0x6B, omem=0x70)],
        expected_bytes=[0x2F, 0x6B, 0x70, 0x00],
    ),
    Case(
        label="SetAMEM8BitToUnknownShort",
        commands_factory=lambda: [
            SetAMEM8BitToUnknownShort(amem=0x60, type=0xB, value=0x0001),
        ],
        expected_bytes=[0x20, 0xB0, 0x01, 0x00],
    ),
    Case(
        label="SetAMEM16BitToUnknownShort",
        commands_factory=lambda: [
            SetAMEM16BitToUnknownShort(amem=0x62, type=0x9, value=0x0032),
        ],
        expected_bytes=[0x21, 0x92, 0x32, 0x00],
    ),
    Case(
        label="SetUnknownShortToAMEM8Bit",
        commands_factory=lambda: [
            SetUnknownShortToAMEM8Bit(amem=0x61, type=0x8, value=45)
        ],
        expected_bytes=[0x22, 0x81, 0x2D, 0x00],
    ),
    Case(
        label="SetUnknownShortToAMEM16Bit",
        commands_factory=lambda: [
            SetUnknownShortToAMEM16Bit(amem=0x61, type=0x8, value=45)
        ],
        expected_bytes=[0x23, 0x81, 0x2D, 0x00],
    ),
    Case(
        label="JmpIfAMEM8BitEqualsUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM8BitEqualsUnknownShort(
                amem=0x61, type=0xA, value=1000, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x24, 0xA1, 0xE8, 0x03, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitEqualsUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM16BitEqualsUnknownShort(
                amem=0x61, type=0xA, value=1000, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x25, 0xA1, 0xE8, 0x03, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitNotEqualsUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM8BitNotEqualsUnknownShort(
                amem=0x6C, type=0x9, value=1000, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x26, 0x9C, 0xE8, 0x03, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitNotEqualsUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM16BitNotEqualsUnknownShort(
                amem=0x6C, type=0x9, value=1000, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x27, 0x9C, 0xE8, 0x03, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitLessThanUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM8BitLessThanUnknownShort(
                amem=0x63, type=0x7, value=100, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x28, 0x73, 0x64, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitLessThanUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM16BitLessThanUnknownShort(
                amem=0x63, type=0x7, value=100, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x29, 0x73, 0x64, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM8BitGreaterOrEqualThanUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM8BitGreaterOrEqualThanUnknownShort(
                amem=0x61, type=0x9, value=10, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2A, 0x91, 0x0A, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEM16BitGreaterOrEqualThanUnknownShort",
        commands_factory=lambda: [
            JmpIfAMEM16BitGreaterOrEqualThanUnknownShort(
                amem=0x61, type=0x9, value=10, destinations=["jmp"]
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x2B, 0x91, 0x0A, 0x00, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="IncAMEM8BitByUnknownShort",
        commands_factory=lambda: [
            IncAMEM8BitByUnknownShort(amem=0x60, type=0x08, value=256)
        ],
        expected_bytes=[0x2C, 0x80, 0x00, 0x01],
    ),
    Case(
        label="IncAMEM16BitByUnknownShort",
        commands_factory=lambda: [
            IncAMEM16BitByUnknownShort(amem=0x60, type=0x08, value=256)
        ],
        expected_bytes=[0x2D, 0x80, 0x00, 0x01],
    ),
    Case(
        label="DecAMEM8BitByUnknownShort",
        commands_factory=lambda: [
            DecAMEM8BitByUnknownShort(amem=0x60, type=0x08, value=256)
        ],
        expected_bytes=[0x2E, 0x80, 0x00, 0x01],
    ),
    Case(
        label="DecAMEM16BitByUnknownShort",
        commands_factory=lambda: [
            DecAMEM16BitByUnknownShort(amem=0x60, type=0x08, value=256)
        ],
        expected_bytes=[0x2F, 0x80, 0x00, 0x01],
    ),
    Case(
        label="IncAMEM8Bit",
        commands_factory=lambda: [
            IncAMEM8Bit(0x6D),
        ],
        expected_bytes=[0x30, 0x0D],
    ),
    Case(
        label="IncAMEM16Bit",
        commands_factory=lambda: [IncAMEM16Bit(0x62)],
        expected_bytes=[0x31, 0x02],
    ),
    Case(
        label="DecAMEM8Bit",
        commands_factory=lambda: [DecAMEM8Bit(0x62)],
        expected_bytes=[0x32, 0x02],
    ),
    Case(
        label="DecAMEM16Bit",
        commands_factory=lambda: [DecAMEM16Bit(0x62)],
        expected_bytes=[0x33, 0x02],
    ),
    Case(
        label="ClearAMEM8Bit",
        commands_factory=lambda: [ClearAMEM8Bit(0x61)],
        expected_bytes=[0x34, 0x01],
    ),
    Case(
        label="ClearAMEM16Bit",
        commands_factory=lambda: [
            ClearAMEM16Bit(0x60),
        ],
        expected_bytes=[0x35, 0x00],
    ),
    Case(
        label="SetAMEMBits",
        commands_factory=lambda: [SetAMEMBits(0x68, [4])],
        expected_bytes=[0x36, 0x08, 0x10],
    ),
    Case(
        label="ClearAMEMBits",
        commands_factory=lambda: [
            ClearAMEMBits(0x60, [4, 5, 6, 7]),
        ],
        expected_bytes=[0x37, 0x00, 0xF0],
    ),
    Case(
        label="JmpIfAMEMBitsSet",
        commands_factory=lambda: [
            JmpIfAMEMBitsSet(0x60, [7], ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x38, 0x00, 0x80, 0x07, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfAMEMBitsClear",
        commands_factory=lambda: [
            JmpIfAMEMBitsClear(0x68, [3], ["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x39, 0x08, 0x08, 0x07, 0xC0, 0x11],
    ),
    Case(
        label="AttackTimerBegins",
        commands_factory=lambda: [AttackTimerBegins()],
        expected_bytes=[0x3A],
    ),
    Case(
        label="PauseScriptUntilAMEMBitsSet",
        commands_factory=lambda: [
            PauseScriptUntilAMEMBitsSet(0x6C, [0]),
        ],
        expected_bytes=[0x40, 0x0C, 0x01],
    ),
    Case(
        label="PauseScriptUntilAMEMBitsClear",
        commands_factory=lambda: [PauseScriptUntilAMEMBitsClear(0x64, [2, 6])],
        expected_bytes=[0x41, 0x04, 0x44],
    ),
    Case(
        label="SpriteSequence",
        commands_factory=lambda: [
            SpriteSequence(sequence=4),
        ],
        expected_bytes=[0x43, 0x04],
    ),
    Case(
        label="SetAMEM60ToCurrentTarget",
        commands_factory=lambda: [SetAMEM60ToCurrentTarget()],
        expected_bytes=[0x45],
    ),
    Case(
        label="GameOverIfNoAlliesStanding",
        commands_factory=lambda: [GameOverIfNoAlliesStanding()],
        expected_bytes=[0x46],
    ),
    Case(
        label="PauseScriptUntilSpriteSequenceDone",
        commands_factory=lambda: [PauseScriptUntilSpriteSequenceDone()],
        expected_bytes=[0x4E],
    ),
    Case(
        label="JmpIfTargetDisabled",
        commands_factory=lambda: [
            JmpIfTargetDisabled(["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x50, 0x05, 0xC0, 0x11],
    ),
    Case(
        label="JmpIfTargetEnabled",
        commands_factory=lambda: [
            JmpIfTargetEnabled(["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0x51, 0x05, 0xC0, 0x11],
    ),
    Case(
        label="SpriteQueue",
        commands_factory=lambda: [
            UseSpriteQueue(
                field_object=4,
                destinations=["queuestart_0x35C007"],
                character_slot=True,
                bit_5=True,
            ),
            ReturnSpriteQueue(identifier="queuestart_0x35C007"),
        ],
        expected_bytes=[0x5D, 0x28, 0x04, 0x07, 0xC0, 0x5E],
    ),
    Case(
        label="DisplayMessageAtOMEM60As",
        commands_factory=lambda: [
            DisplayMessageAtOMEM60As(SPELL_NAME),
        ],
        expected_bytes=[0x63, 0x01],
    ),
    Case(
        label="UseObjectQueueAtOffsetWithAMEM60Index",
        commands_factory=lambda: [
            DefineObjectQueue(["destination_1"], identifier="objqueue"),
            ReturnObjectQueue(identifier="destination_1"),
            UseObjectQueueAtOffsetWithAMEM60Index(
                destinations=["objqueue"]
            ),
            ReturnSubroutine(),
        ],
        expected_bytes=[0x04, 0xC0, 0x07, 0x64, 0x02, 0xC0, 0x11],
    ),
    Case(
        label="UseObjectQueueAtOffsetWithAMEM60PointerOffset",
        commands_factory=lambda: [
            DefineObjectQueue(["oq_1", "oq_2"], identifier="objqueue"),
            DefineObjectQueue(["destination_1"], identifier="oq_1"),
            DefineObjectQueue(["destination_2"], identifier="oq_2"),
            ReturnObjectQueue(identifier="destination_1"),
            ReturnObjectQueue(identifier="destination_2"),
            UseObjectQueueAtOffsetWithAMEM60PointerOffset(
                index=1, destinations=["objqueue"]
            ),
            ReturnSubroutine(),
        ],
        expected_bytes=[0x06, 0xC0, 0x08, 0xC0, 0x0A, 0xC0, 0x0B, 0xC0, 0x07, 0x07, 0x68, 0x02, 0xC0, 0x01, 0x11],
    ),
    Case(
        label="SetOMEM60To072C",
        commands_factory=lambda: [SetOMEM60To072C()],
        expected_bytes=[0x69],
    ),
    Case(
        label="SetAMEMToRandomByte",
        commands_factory=lambda: [
            SetAMEMToRandomByte(amem=0x68, upper_bound=7),
        ],
        expected_bytes=[0x6A, 0x08, 0x07],
    ),
    Case(
        label="SetAMEMToRandomShort",
        commands_factory=lambda: [SetAMEMToRandomShort(amem=0x60, upper_bound=9)],
        expected_bytes=[0x6B, 0x00, 0x09, 0x00],
    ),
    Case(
        label="EnableSpritesOnSubscreen",
        commands_factory=lambda: [EnableSpritesOnSubscreen()],
        expected_bytes=[0x70],
    ),
    Case(
        label="DisableSpritesOnSubscreen",
        commands_factory=lambda: [DisableSpritesOnSubscreen()],
        expected_bytes=[0x71],
    ),
    Case(
        label="NewEffectObject",
        commands_factory=lambda: [
            NewEffectObject(effect=102, playback_off=True),
        ],
        expected_bytes=[0x72, 0x02, 0x66],
    ),
    Case(
        label="Pause2Frames",
        commands_factory=lambda: [Pause2Frames()],
        expected_bytes=[0x73],
    ),
    Case(
        label="PauseScriptUntilBitsClear",
        commands_factory=lambda: [PauseScriptUntilBitsClear(0x300)],
        expected_bytes=[0x75, 0x00, 0x03],
    ),
    Case(
        label="ClearEffectIndex",
        commands_factory=lambda: [ClearEffectIndex()],
        expected_bytes=[0x76],
    ),
    Case(
        label="Layer3On",
        commands_factory=lambda: [
            Layer3On(property=TRANSPARENCY_OFF, bit_0=True, bpp4=True, invisible=True),
        ],
        expected_bytes=[0x77, 0x0B],
    ),
    Case(
        label="Layer3Off",
        commands_factory=lambda: [
            Layer3Off(property=OVERLAP_ALL, bpp4=True),
        ],
        expected_bytes=[0x78, 0x12],
    ),
    Case(
        label="DisplayMessage",
        commands_factory=lambda: [
            DisplayMessage(ITEM_NAME, 11),
        ],
        expected_bytes=[0x7A, 0x02, 0x0B],
    ),
    Case(
        label="PauseScriptUntilDialogClosed",
        commands_factory=lambda: [PauseScriptUntilDialogClosed()],
        expected_bytes=[0x7B],
    ),
    Case(
        label="FadeOutObject",
        commands_factory=lambda: [
            FadeOutObject(duration=1),
        ],
        expected_bytes=[0x7E, 0x01],
    ),
    Case(
        label="ResetSpriteSequence",
        commands_factory=lambda: [ResetSpriteSequence()],
        expected_bytes=[0x7F],
    ),
    Case(
        label="ShineEffect",
        commands_factory=lambda: [
            ShineEffect(
                colour_count=14,
                starting_colour_index=10,
                glow_duration=3,
                east=True,
            ),
        ],
        expected_bytes=[0x80, 0x00, 0xAE, 0x03],
    ),
    Case(
        label="FadeOutEffect",
        commands_factory=lambda: [
            FadeOutEffect(duration=1),
        ],
        expected_bytes=[0x85, 0x00, 0x01],
    ),
    Case(
        label="FadeOutSprite",
        commands_factory=lambda: [
            FadeOutSprite(duration=2),
        ],
        expected_bytes=[0x85, 0x10, 0x02],
    ),
    Case(
        label="FadeOutScreen",
        commands_factory=lambda: [
            FadeOutScreen(duration=1),
        ],
        expected_bytes=[0x85, 0x20, 0x01],
    ),
    Case(
        label="FadeInEffect",
        commands_factory=lambda: [
            FadeInEffect(duration=2),
        ],
        expected_bytes=[0x85, 0x02, 0x02],
    ),
    Case(
        label="FadeInSprite",
        commands_factory=lambda: [
            FadeInSprite(duration=8),
        ],
        expected_bytes=[0x85, 0x12, 0x08],
    ),
    Case(
        label="FadeInScreen",
        commands_factory=lambda: [FadeInScreen(duration=1)],
        expected_bytes=[0x85, 0x22, 0x01],
    ),
    Case(
        label="ShakeScreen",
        commands_factory=lambda: [
            ShakeScreen(amount=5, speed=200),
        ],
        expected_bytes=[0x86, 0x01, 0x00, 0x00, 0x05, 0xC8, 0x00],
    ),
    Case(
        label="ShakeSprites",
        commands_factory=lambda: [ShakeSprites(amount=2, speed=26)],
        expected_bytes=[0x86, 0x02, 0x00, 0x00, 0x02, 0x1A, 0x00],
    ),
    Case(
        label="ShakeScreenAndSprites",
        commands_factory=lambda: [
            ShakeScreenAndSprites(amount=5, speed=200),
        ],
        expected_bytes=[0x86, 0x04, 0x00, 0x00, 0x05, 0xC8, 0x00],
    ),
    Case(
        label="StopShakingObject",
        commands_factory=lambda: [StopShakingObject()],
        expected_bytes=[0x87],
    ),
    Case(
        label="ScreenFlashWithDuration",
        commands_factory=lambda: [
            ScreenFlashWithDuration(WHITE, 1, 16),
        ],
        expected_bytes=[0x8E, 0x17, 0x01],
    ),
    Case(
        label="ScreenFlash",
        commands_factory=lambda: [
            ScreenFlash(NO_COLOUR, 8),
            ScreenFlash(RED, 0),
        ],
        expected_bytes=[0x8F, 0x08, 0x8F, 0x01],
    ),
    Case(
        label="InitializeBonusMessageSequence",
        commands_factory=lambda: [InitializeBonusMessageSequence()],
        expected_bytes=[0x95],
    ),
    Case(
        label="DisplayBonusMessage",
        commands_factory=lambda: [DisplayBonusMessage(message=BM_LUCKY, x=2, y=-32)],
        expected_bytes=[0x96, 0x00, 0x06, 0x02, 0xE0],
    ),
    Case(
        label="PauseScriptUntilBonusMessageComplete",
        commands_factory=lambda: [PauseScriptUntilBonusMessageComplete()],
        expected_bytes=[0x97],
    ),
    Case(
        label="WaveEffect",
        commands_factory=lambda: [
            WaveEffect(
                layer=WAVE_LAYER_4BPP,
                direction=WAVE_LAYER_HORIZONTAL,
                depth=32,
                intensity=4,
                speed=96,
                byte_1=0x80,
            ),
        ],
        expected_bytes=[0x9C, 0x80, 0x42, 0x20, 0x00, 0x04, 0x00, 0x60, 0x00],
    ),
    Case(
        label="StopWaveEffect",
        commands_factory=lambda: [
            StopWaveEffect(bit_7=True),
        ],
        expected_bytes=[0x9D, 0x82],
    ),
    Case(
        label="ScreenEffect",
        commands_factory=lambda: [ScreenEffect(6)],
        expected_bytes=[0xA3, 0x06],
    ),
    Case(
        label="JmpIfTimedHitSuccess",
        commands_factory=lambda: [
            JmpIfTimedHitSuccess(["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0xA7, 0x05, 0xC0, 0x11],
    ),
    Case(
        label="PlaySound",
        commands_factory=lambda: [
            PlaySound(
                sound=89, identifier="command_0x3505e8"
            ),
        ],
        expected_bytes=[0xAB, 0x59],
    ),
    Case(
        label="PlayMusicAtCurrentVolume",
        commands_factory=lambda: [
            PlayMusicAtCurrentVolume(21),
        ],
        expected_bytes=[0xB0, 0x15],
    ),
    Case(
        label="PlayMusicAtVolume",
        commands_factory=lambda: [
            PlayMusicAtVolume(69, 61456),
        ],
        expected_bytes=[0xB1, 0x45, 0x10, 0xF0],
    ),
    Case(
        label="StopCurrentSoundEffect",
        commands_factory=lambda: [StopCurrentSoundEffect()],
        expected_bytes=[0xB2],
    ),
    Case(
        label="FadeCurrentMusicToVolume",
        commands_factory=lambda: [
            FadeCurrentMusicToVolume(speed=3, volume=1),
        ],
        expected_bytes=[0xB6, 0x03, 0x01],
    ),
    Case(
        label="SetTarget",
        commands_factory=lambda: [SetTarget(MONSTER_1_SET)],
        expected_bytes=[0xBB, 0x13],
    ),
    Case(
        label="AddItemToStandardInventory",
        commands_factory=lambda: [
            AddItemToStandardInventory(SheepAttackItem),
        ],
        expected_bytes=[0xBC, 0x88, 0x00],
    ),
    Case(
        label="RemoveItemFromStandardInventory",
        commands_factory=lambda: [
            RemoveItemFromStandardInventory(LambsLureItem),
        ],
        expected_bytes=[0xBC, 0x71, 0xFF],
    ),
    Case(
        label="AddItemToKeyItemInventory",
        commands_factory=lambda: [
            AddItemToKeyItemInventory(RareFrogCoinItem),
        ],
        expected_bytes=[0xBD, 0x80, 0x00],
    ),
    Case(
        label="RemoveItemFromKeyItemInventory",
        commands_factory=lambda: [RemoveItemFromKeyItemInventory(RareFrogCoinItem)],
        expected_bytes=[0xBD, 0x80, 0xFF],
    ),
    Case(
        label="AddCoins",
        commands_factory=lambda: [AddCoins(5)],
        expected_bytes=[0xBE, 0x05, 0x00],
    ),
    Case(
        label="AddYoshiCookiesToInventory",
        commands_factory=lambda: [AddYoshiCookiesToInventory(10)],
        expected_bytes=[0xBF, 0x0A],
    ),
    Case(
        label="DoMaskEffect",
        commands_factory=lambda: [
            DoMaskEffect(CYLINDER_MASK),
        ],
        expected_bytes=[0xC3, 0x07],
    ),
    Case(
        label="SetMaskCoords",
        commands_factory=lambda: [
            SetMaskCoords(points=[(-48, -64), (-48, 112), (48, -64), (48, 112)]),
        ],
        expected_bytes=[0xC6, 0x08, 0xD0, 0xC0, 0xD0, 0x70, 0x30, 0xC0, 0x30, 0x70],
    ),
    Case(
        label="SetSequenceSpeed",
        commands_factory=lambda: [SetSequenceSpeed(4)],
        expected_bytes=[0xCB, 0x04],
    ),
    Case(
        label="StartTrackingAllyButtonInputs",
        commands_factory=lambda: [StartTrackingAllyButtonInputs()],
        expected_bytes=[0xCC],
    ),
    Case(
        label="EndTrackingAllyButtonInputs",
        commands_factory=lambda: [EndTrackingAllyButtonInputs()],
        expected_bytes=[0xCD],
    ),
    Case(
        label="TimingForOneTieredButtonPress",
        commands_factory=lambda: [
            TimingForOneTieredButtonPress(
                start_accepting_input=0,
                end_accepting_input=30,
                partial_start=26,
                perfect_start=29,
                perfect_end=30,
                destinations=["jmp"],
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0xCE, 0x1E, 0x00, 0x1A, 0x1D, 0x1E, 0x0A, 0xC0, 0x11],
    ),
    Case(
        label="TimingForOneBinaryButtonPress",
        commands_factory=lambda: [
            TimingForOneBinaryButtonPress(
                start_accepting_input=0,
                end_accepting_input=15,
                timed_hit_ends=15,
                destinations=["jmp"],
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0xCF, 0x0F, 0x00, 0x0F, 0x08, 0xC0, 0x11],
    ),
    Case(
        label="TimingForMultipleButtonPresses",
        commands_factory=lambda: [
            TimingForMultipleButtonPresses(
                start_accepting_input=7,
                destinations=["jmp"],
            ),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0xD0, 0x07, 0x06, 0xC0, 0x11],
    ),
    Case(
        label="TimingForButtonMashUnknown",
        commands_factory=lambda: [TimingForButtonMashUnknown()],
        expected_bytes=[0xD1],
    ),
    Case(
        label="TimingForButtonMashCount",
        commands_factory=lambda: [
            TimingForButtonMashCount(max_presses=16),
        ],
        expected_bytes=[0xD2, 0x10],
    ),
    Case(
        label="TimingForRotationCount",
        commands_factory=lambda: [
            TimingForRotationCount(
                start_accepting_input=0, end_accepting_input=120, max_presses=26
            )
        ],
        expected_bytes=[0xD3, 0x78, 0x00, 0x1A],
    ),
    Case(
        label="TimingForChargePress",
        commands_factory=lambda: [
            TimingForChargePress(
                charge_level_1_end=30,
                charge_level_2_end=55,
                charge_level_3_end=80,
                charge_level_4_end=105,
                overcharge_end=130,
            ),
        ],
        expected_bytes=[0xD4, 0x1E, 0x37, 0x50, 0x69, 0x82],
    ),
    Case(
        label="SummonMonster",
        commands_factory=lambda: [
            SummonMonster(monster=YARIDOVICH, position=1, bit_6=True, bit_7=True)
        ],
        expected_bytes=[0xD5, 0xC0, 0xE2, 0x01],
    ),
    Case(
        label="MuteTimingJmp",
        commands_factory=lambda: [
            MuteTimingJmp(destinations=["jmp"]),
            ReturnSubroutine(identifier="jmp"),
        ],
        expected_bytes=[0xD8, 0x05, 0xC0, 0x11],
    ),
    Case(
        label="DisplayCantRunDialog",
        commands_factory=lambda: [DisplayCantRunDialog()],
        expected_bytes=[0xD9],
    ),
    Case(
        label="StoreOMEM60ToItemInventory",
        commands_factory=lambda: [StoreOMEM60ToItemInventory()],
        expected_bytes=[0xE0],
    ),
    Case(
        label="RunBattleEvent",
        commands_factory=lambda: [
            RunBattleEvent(script_id=85, offset=4),
        ],
        expected_bytes=[0xE1, 0x55, 0x00, 0x04],
    ),
    Case(
        # this one doesn't have as many protections as event and action scripts do, just don't fuck it up
        label="UnknownCommand",
        commands_factory=lambda: [UnknownCommand(bytearray(b"\x16"))],
        expected_bytes=[0x16],
    ),
    Case(
        label="should fill in expected length when not long enough",
        commands_factory=lambda: [StoreOMEM60ToItemInventory()],
        expected_bytes=[0xE0, 0x11, 0x11, 0x11],
        expected_length=4
    ),
    Case(
        label="should error if expected size is wrong",
        commands_factory=lambda: [StoreOMEM60ToItemInventory(), StoreOMEM60ToItemInventory()],
        expected_length=1,
        exception="animation script output too long: got 2 expected 1",
        exception_type=ScriptBankTooLongException,
    ),
]


@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    if case.expected_bytes is not None and len(case.expected_bytes) == 0:
        return
    if case.exception or case.exception_type:
        with pytest.raises(case.exception_type) as exc_info:
            commands = case.commands_factory()
            expected_size=1000
            if case.expected_length is not None:
                expected_size=case.expected_length
            script = AnimationScriptBlock(expected_size=expected_size, expected_beginning=0x35C002, script=commands)
            bank = AnimationScriptBank(
                name=case.label,
                scripts=[script],
            )
            bank.render()
        if case.exception:
            assert case.exception in str(exc_info.value)
    elif case.expected_bytes is not None:
        commands = case.commands_factory()
        script = AnimationScript(commands)
        expected_bytes = bytearray(case.expected_bytes)
        expected_size=len(case.expected_bytes)
        if case.expected_length is not None:
            expected_size=case.expected_length
        script = AnimationScriptBlock(expected_size=expected_size, expected_beginning=0x35C002, script=commands)
        bank = AnimationScriptBank(
            name=case.label,
            scripts=[script],
        )
        comp = bank.render()
        assert comp[0][1] == expected_bytes
    else:
        raise ValueError("At least one of exception or expected_bytes needs to be set")
