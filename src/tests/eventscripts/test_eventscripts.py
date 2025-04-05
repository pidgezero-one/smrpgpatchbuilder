import pytest
from smrpgpatchbuilder.types.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.types.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.types.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.types.overworld_scripts.event_scripts.commands.types import (
    UsableEventScriptCommand,
)
from typing import List

from dataclasses import dataclass

@dataclass
class Case:
    commands: List[UsableEventScriptCommand]
    expected_bytes: bytearray
              
test_cases = [
    Case([StartLoopNFrames(10)], bytearray([0xD5, 0x00, 0x0A])),
]

@pytest.mark.parametrize("case", test_cases)
def test_add(case: Case):
    script = EventScript(case.commands)
    assert script.render() == case.expected_bytes