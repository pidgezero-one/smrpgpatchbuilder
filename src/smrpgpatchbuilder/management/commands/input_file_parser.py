"""Utility for parsing *_names.input files from the config directory."""

from pathlib import Path
import re
import string
from typing import Dict, List, Tuple, Optional


# Constants for name normalization
NAME_KEEP = {"-", "_"}
RE_SPACES = re.compile(r"[ \-_]+")
RE_LEADING_DIGITS = re.compile(r"^\d+")
RE_HEX = re.compile(r"^[0-9A-Fa-f]+$")
RE_FLAG_DIGIT = re.compile(r"^[0-9]$")


def normalize_label(raw: str) -> str:
    """Normalize a raw label string into a valid Python identifier.

    Args:
        raw: The raw label string to normalize

    Returns:
        A normalized label suitable for use as a Python identifier
    """
    s = RE_LEADING_DIGITS.sub("", raw)
    s = s.upper()
    keep = set(NAME_KEEP)
    trans_table = {ord(ch): None for ch in string.punctuation if ch not in keep}
    s = s.translate(trans_table)
    s = RE_SPACES.sub("_", s)
    s = s.strip("_ ")
    if s and s[0].isdigit():
        s = "_" + s
    return s or "_"


def parse_standard_lines(lines: List[str]) -> List[Tuple[str, str]]:
    """Parse standard input file lines into (name, index) tuples.

    Args:
        lines: Lines from the input file

    Returns:
        List of (normalized_name, index) tuples
    """
    out = []
    for idx, raw in enumerate(lines):
        line = raw.rstrip("\n\r")
        if not line.strip():
            continue
        if line.strip().startswith("#"):
            continue
        name = normalize_label(line)
        out.append((name, str(idx)))
    return out


def parse_variable_names_lines(lines: List[str]) -> List[Tuple[str, str]]:
    """Parse variable_names.input lines into (name, value) tuples.

    Handles special formats for flags and variables:
    - Lines ending with hex and digit: Flag(0xHEX, digit)
    - Lines ending with hex in 0x7000-0x703E: ShortVar(0xHEX)
    - Lines ending with hex in 0x7040-0x71FE: ByteVar(0xHEX)
    - Lines ending with other hex: 0xHEX
    - Lines without hex: 0

    Args:
        lines: Lines from the variable_names.input file

    Returns:
        List of (normalized_name, value_expression) tuples
    """
    out = []
    for raw in lines:
        line = raw.rstrip("\n\r")
        if not line.strip() or line.strip().startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2 and RE_FLAG_DIGIT.match(parts[-1]) and RE_HEX.match(parts[-2]):
            hex_str = parts[-2]
            digit = parts[-1]
            label_raw = " ".join(parts[:-2])
            label = normalize_label(label_raw)
            hex_val = int(hex_str, 16)
            out.append((label, f"Flag(0x{hex_val:04X}, {digit})"))
        elif parts and RE_HEX.match(parts[-1]):
            hex_str = parts[-1]
            label_raw = " ".join(parts[:-1])
            label = normalize_label(label_raw)
            hex_val = int(hex_str, 16)
            if 0x7000 <= hex_val <= 0x703E:
                out.append((label, f"ShortVar(0x{hex_val:04X})"))
            elif 0x7040 <= hex_val <= 0x71FE:
                out.append((label, f"ByteVar(0x{hex_val:04X})"))
            else:
                out.append((label, f"0x{hex_val:04X}"))
        else:
            label = normalize_label(line)
            out.append((label, "0"))
    return out


def find_config_dir(start_path: Optional[Path] = None) -> Optional[Path]:
    """Find the config directory by searching up the directory tree.

    Args:
        start_path: Starting path for the search. If None, uses __file__.

    Returns:
        Path to the config directory, or None if not found
    """
    if start_path is None:
        start_path = Path(__file__)

    for p in start_path.resolve().parents:
        cand = p / "config"
        if cand.is_dir():
            return cand
    return None


def parse_input_files(config_dir: Optional[Path] = None) -> Dict[str, List[Tuple[str, str]]]:
    """Parse all *_names.input files in the config directory.

    Args:
        config_dir: Path to the config directory. If None, will search for it.

    Returns:
        Dictionary mapping file stem (without .input extension) to list of (name, value) tuples

    Raises:
        ValueError: If config directory is not found or contains no input files
    """
    if config_dir is None:
        config_dir = find_config_dir()

    if config_dir is None:
        raise ValueError("Could not find a config directory")

    files = sorted(config_dir.glob("*_names.input"))
    # Also include item_prefixes.input
    prefix_file = config_dir / "item_prefixes.input"
    if prefix_file.exists():
        files.append(prefix_file)

    if not files:
        raise ValueError("No input files found in config directory")

    parsed = {}

    for f in files:
        key = f.stem  # e.g., variable_names, item_prefixes
        content = f.read_text(encoding="utf-8").splitlines()
        if f.name == "variable_names.input" or key == "variable_names":
            parsed[key] = parse_variable_names_lines(content)
        else:
            parsed[key] = parse_standard_lines(content)

    return parsed
