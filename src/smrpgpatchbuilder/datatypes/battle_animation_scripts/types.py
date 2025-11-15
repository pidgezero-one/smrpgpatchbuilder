"""Base classes supporting battle animation script assembly."""

from typing import List, Optional, Dict, Type, Union, Tuple

from .commands.types.classes import (
    UsableAnimationScriptCommand,
)

from smrpgpatchbuilder.datatypes.numbers.classes import UInt16

from smrpgpatchbuilder.datatypes.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)

from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.types import (
    UsableAnimationScriptCommand,
)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands.commands import (
    ReturnSubroutine,
)


class AnimationScript(Script[UsableAnimationScriptCommand]):
    """Base class for a single animation script, a list of script command subclasses."""

    _contents: List[UsableAnimationScriptCommand] = []

    @property
    def contents(self) -> List[UsableAnimationScriptCommand]:
        return self._contents

    def append(self, command: UsableAnimationScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[UsableAnimationScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: Optional[List[UsableAnimationScriptCommand]] = None
    ) -> None:
        super().set_contents(script)

    def __init__(
        self, script: Optional[List[UsableAnimationScriptCommand]] = None
    ) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableAnimationScriptCommand],
        command: UsableAnimationScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableAnimationScriptCommand],
        command: UsableAnimationScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(
        self, index: int, content: UsableAnimationScriptCommand
    ) -> None:
        super().replace_at_index(index, content)

    def render(self, _: Optional[int] = None) -> bytearray:
        output = bytearray()
        command: UsableAnimationScriptCommand
        for command in self._contents:
            output += command.render()
        return output


class AnimationScriptBlock(AnimationScript):
    """Covers a range of known animation data in the ROM."""
    _expected_size: int = 0
    _expected_beginning: int = 0

    @property
    def expected_size(self) -> int:
        """The length of bytes that this script should ultimately equal when compiled.  
        The base property should not be mutable."""
        return self._expected_size

    @property
    def expected_beginning(self) -> int:
        """The expected beginning address of this script in the ROM.  
        The base property should not be mutable."""
        return self._expected_beginning
    
    @property
    def expected_end(self) -> int:
        """The expected end address of this script in the ROM."""
        return self._expected_beginning + self._expected_size

    def __repr__(self) -> str:
        """Representation showing expected_size (base 10) and expected_beginning (base 16)."""
        return (
            f"<AnimationScriptBlock expected_size={self.expected_size} "
            f"expected_beginning=0x{self.expected_beginning:06X}>"
        )

    def __str__(self) -> str:
        """Same as repr() but used by print()."""
        return self.__repr__()

    def __init__(
        self,
        expected_size: int,
        expected_beginning: int,
        script: Optional[List[UsableAnimationScriptCommand]] = None,
    ) -> None:
        super().__init__(script)
        self._expected_size = expected_size
        self._expected_beginning = expected_beginning

    def render(self, _: Optional[int] = None) -> bytearray:
        output = super().render(_)
        # fill empty bytes
        if len(output) == self.expected_size:
            return output
        if len(output) > self.expected_size:
            print(self)
            raise ScriptBankTooLongException(
                f"animation script output too long: got {len(output)} expected {self.expected_size}"
            )
        buffer: List[UsableAnimationScriptCommand] = [ReturnSubroutine()] * (self.expected_size - len(output))
        self.set_contents(self.contents + buffer)
        output = super().render(_)
        return output


class AnimationScriptBank(ScriptBank[AnimationScript]):
    """Base class for a collection of scripts that belong to the same bank (ie 0x##0000)
    and are separated by IDs."""

    _scripts: List[Union[AnimationScript, AnimationScriptBlock]]
    _name: str

    @property
    def scripts(self) -> List[Union[AnimationScript, AnimationScriptBlock]]:
        return self._scripts

    @property
    def name(self) -> str:
        """An arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set an arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        self._name = name

    def set_contents(self, scripts: Optional[List[AnimationScript]] = None) -> None:
        """Overwrite the entire list of scripts belonging to this bank."""
        if scripts is None:
            scripts = []
        super().set_contents(scripts)

    def get_command_by_name(self, identifier: str) -> UsableAnimationScriptCommand:
        """Return a single command whose unique identifier matches the name provided."""
        for script in self._scripts:
            for command in script.contents:
                if command.identifier.label == identifier:
                    return command
        raise IdentifierException(f"{identifier} not found")

    def replace_command_by_name(
        self, identifier: str, contents: UsableAnimationScriptCommand
    ) -> None:
        """Overwrite a single command whose unique identifier matches the name provided."""
        for script_id, script in enumerate(self._scripts):
            for index, command in enumerate(script.contents):
                if command.identifier.label == identifier:
                    self._scripts[script_id].contents[index] = contents
                    return
        raise IdentifierException(f"{identifier} not found")

    def set_addresses(self, addrs: Dict[str, int]) -> None:
        """This should ONLY be used when the parent ScriptBankCollection is rendering
        all of its constituent banks. Replaces the identifier-address dict."""
        self._addresses = addrs

    def __init__(
        self,
        name: str,
        scripts: Optional[List[AnimationScript]] = None,
    ) -> None:
        self.set_name(name)
        super().__init__(scripts)

    def _associate_address(
        self, command: UsableAnimationScriptCommand, position: int
    ) -> int:
        """Associates an identifier and an address as a key-value pair in the addresses dict."""
        key: str = command.identifier.label
        if key in self.addresses and self.addresses[key] != position:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position
        position += command.size
        return position

    def build_command_address_mapping(self) -> Dict[str, int]:
        """Build and return the command identifier to address mapping.

        This method populates the internal addresses dict and pointer_bytes
        by iterating through all AnimationScriptBlock instances in this bank.

        Returns:
            Dict[str, int]: Mapping of command identifiers to their ROM addresses.
        """
        self.addresses.clear()
        self._pointer_bytes = bytearray()

        scripts: List[AnimationScriptBlock] = [
            s for s in self.scripts if isinstance(s, AnimationScriptBlock)
        ]

        # build command name : address table
        for script in scripts:
            position: int = script.expected_beginning
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script.contents:
                position = self._associate_address(command, position)

        return self.addresses

    def render(self) -> List[Tuple[int, bytearray]]:
        """generate the bytes representing the current state of this bank to be written
        to the ROM."""

        scripts: List[AnimationScriptBlock] = [
            s for s in self.scripts if isinstance(s, AnimationScriptBlock)
        ]

        # build command name : address table
        self.build_command_address_mapping()

        # replace jump placeholders with addresses
        for script in scripts:
            self._populate_jumps(script)

        return [
            (script.expected_beginning, script.render())
            for script in scripts
        ]
