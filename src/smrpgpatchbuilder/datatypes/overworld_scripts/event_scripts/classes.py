"""Base classes supporting event script assembly."""

from typing import List, Optional, Type, Union
from copy import deepcopy
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.types.classes import (
    UsableActionScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    EventScriptCommandActionScriptContainer,
    UsableEventScriptCommand,
    NonEmbeddedActionQueuePrototype,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    StopSound,
)

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.ids.misc import (
    TOTAL_SCRIPTS,
)
from smrpgpatchbuilder.datatypes.numbers.classes import UInt16


class EventScript(Script[UsableEventScriptCommand]):
    """Base class for a single event script, a list of script command subclasses."""

    _contents: List[UsableEventScriptCommand]

    @property
    def contents(self) -> List[UsableEventScriptCommand]:
        return self._contents

    def append(self, command: UsableEventScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[UsableEventScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: Optional[List[UsableEventScriptCommand]] = None
    ) -> None:
        super().set_contents(script)

    def __init__(self, script: Optional[List[UsableEventScriptCommand]] = None) -> None:
        if script is None:
            ss = []
        else:
            ss = deepcopy(script)
        super().__init__(ss)

    def insert_before_nth_command(
        self, index: int, command: UsableEventScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableEventScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableEventScriptCommand],
        command: UsableEventScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableEventScriptCommand],
        command: UsableEventScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableEventScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableEventScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: UsableEventScriptCommand) -> None:
        super().replace_at_index(index, content)


class EventScriptBank(ScriptBank[EventScript]):
    """base class for a collection of npc action scripts
    that should belong to the same $##xxxx bank (1e, 1f, or 20)."""

    _scripts: List[EventScript]
    _pointer_table_start: int
    _start: int
    _end: int

    @property
    def pointer_table_start(self) -> int:
        """The beginning address for this bank's pointer table."""
        return self._pointer_table_start

    def set_pointer_table_start(self, pointer_table_start: int) -> None:
        """Set the beginning address for this bank's pointer table."""
        self._pointer_table_start = pointer_table_start

    @property
    def start(self) -> int:
        """the beginning address for this bank's scripts content, indexed by the
        pointer table."""
        return self._start

    def set_start(self, start: int) -> None:
        """set the beginning address for this bank's scripts content, indexed by the
        pointer table."""
        self._start = start

    @property
    def end(self) -> int:
        """The address at which this bank's scripts should have finished by."""
        return self._end

    def set_end(self, end: int) -> None:
        """Set the address at which this bank's scripts should have finished by."""
        self._end = end

    @property
    def script_count(self) -> UInt16:
        """The total number of scripts included in this bank."""
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[EventScript]:
        return self._scripts

    def set_contents(self, scripts: Optional[List[EventScript]] = None) -> None:
        if scripts is None:
            scripts = []
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, index: int, script: EventScript) -> None:
        assert 0 <= index < self.script_count
        super().replace_script(index, script)

    def __init__(
        self,
        pointer_table_start: int,
        start: int,
        end: int,
        scripts: Optional[List[EventScript]],
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        super().__init__(scripts)

    def _associate_address(
        self,
        command: Union[UsableEventScriptCommand, UsableActionScriptCommand],
        position: int,
    ) -> int:
        key: str = command.identifier.label
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        if isinstance(command, EventScriptCommandActionScriptContainer):
            position += command.header_size
            action_command: UsableActionScriptCommand
            for action_command in command.subscript.contents:
                position = self._associate_address(action_command, position)
        else:
            position += command.size

        if position > self.end:
            raise ScriptBankTooLongException(
                f"command exceeded max bank size of {self.end:06X}: {key} @ 0x{position:06X}"
            )
        return position

    def render(self) -> bytearray:
        """Return this script set as ROM patch data."""
        position: int = self._start

        script: EventScript
        command: UsableEventScriptCommand

        # build command name and pointer table : address table
        for script_id, script in enumerate(self.scripts):
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            initial_position = position
            c = deepcopy(script.contents)
            for index, command in enumerate(script.contents):
                # if this is a non-embedded action queue, insert dummy commands to fill space before the offset it should be at
                if isinstance(command, NonEmbeddedActionQueuePrototype):
                    relative_offset: int = position - initial_position
                    if relative_offset <= command.required_offset:
                        for _ in range(command.required_offset - relative_offset):
                            c.insert(index, StopSound())
                            position += 1
                    else:
                        raise ScriptBankTooLongException(
                            f"too many commands in script {script_id} before non-embedded action queue"
                        )

                position = self._associate_address(command, position)
            script.set_contents(c)

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)
            commands_with_subscripts = [
                cmd
                for cmd in script.contents
                if isinstance(cmd, EventScriptCommandActionScriptContainer)
            ]
            for command in commands_with_subscripts:
                self._populate_jumps(command.subscript)

        # finalize bytes
        for i, script in enumerate(self.scripts):
            self.script_bytes.extend(script.render())

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"event script output too long: got {final_length} expected {expected_length}"
            )
        buffer: List[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        return self.pointer_bytes + self.script_bytes


class EventScriptController:
    """Contains all event script banks. Allows lookup by identifier in any bank."""

    _banks: List[EventScriptBank]

    @property
    def banks(self) -> List[EventScriptBank]:
        """List of event script banks."""
        return self._banks

    def set_banks(self, banks: List[EventScriptBank]) -> None:
        """Overwrite the list of event script banks."""
        self._banks = banks

    def __init__(self, banks: List[EventScriptBank]):
        assert len(banks) == 3
        assert (
            len(banks[0].scripts) + len(banks[1].scripts) + len(banks[2].scripts)
            == TOTAL_SCRIPTS
        )
        self.set_banks(banks)

    def get_script_by_id(self, script_id: int) -> EventScript:
        """get one script from any bank by absolute id.\n
        It is recommended to use event name constants for this."""
        assert 0 <= script_id < TOTAL_SCRIPTS
        bank_0x1e: EventScriptBank = self.banks[0]
        bank_0x1f: EventScriptBank = self.banks[1]
        bank_0x20: EventScriptBank = self.banks[2]
        range_0x1e = range(0, bank_0x1e.script_count)
        range_0x1f = range(
            bank_0x1e.script_count, bank_0x1e.script_count + bank_0x1f.script_count
        )
        range_0x20 = range(
            bank_0x1e.script_count + bank_0x1f.script_count,
            bank_0x1e.script_count + bank_0x1f.script_count + bank_0x20.script_count,
        )
        if script_id in range_0x1e:
            return bank_0x1e.scripts[script_id]
        if script_id in range_0x1f:
            relative_id: int = script_id - range_0x1f[0]
            return bank_0x1f.scripts[relative_id]
        if script_id in range_0x20:
            relative_id: int = script_id - range_0x20[0]
            return bank_0x20.scripts[relative_id]
        raise IdentifierException(f"could not find script id {id} for some reason")
