import pytest
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
    EventScriptBank
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from typing import List

from dataclasses import dataclass

@dataclass
class Case:
    label: str
    commands: List[UsableEventScriptCommand]
    expected_bytes: bytearray
              
test_cases = [
    Case("Loop 10 frames", [StartLoopNFrames(10)], bytearray([0xD5, 0x0A, 0x00])),
    Case("Basic GOTO", [
        StopSound(),
        Set7000ToTappedButton(identifier="jmp_here"),
        Jmp(destinations=["jmp_here"])
    ], bytearray([0x9B, 0xCB, 0xD2, 0x03, 0x00])),
    ### This is where I need help writing test cases for every other command!
]

@pytest.mark.parametrize("case", test_cases, ids=lambda case: case.label)
def test_add(case: Case):
    script = EventScript(case.commands)
    bank = EventScriptBank(0x1E0000, 0x1E0002, 0x1E0002+script.length, [script])
    assert bank.render() == bytearray([0x02, 0x00]) + case.expected_bytes