"""Dialog auto-formatter and validator for SMRPG's dialog box.

The dialog box displays text in a 256x56 pixel area with 3 visible lines per page.
Each character has a pixel width stored in the ROM. When text overflows a line, the
game wraps implicitly -- but implicit wraps don't start with a space, which looks bad.
The formatter inserts explicit \\n breaks where wrapping would occur.
"""

import math
import re
from dataclasses import dataclass

from .utils import COMPRESSION_TABLE

# Font widths at ROM 0x249280, 128 bytes for chars 0x20-0x9F.
# Each value is the RAW pixel width of the character (without the 1px inter-char spacing).
VANILLA_DIALOG_FONT_WIDTHS: tuple[int, ...] = (
    0x04, 0x06, 0x06, 0x06, 0x08, 0x08, 0x04, 0x04,
    0x07, 0x07, 0x06, 0x08, 0x05, 0x05, 0x05, 0x06,
    0x07, 0x05, 0x07, 0x07, 0x07, 0x07, 0x07, 0x07,
    0x07, 0x08, 0x05, 0x05, 0x06, 0x06, 0x08, 0x08,
    0x07, 0x07, 0x06, 0x07, 0x06, 0x07, 0x07, 0x03,
    0x06, 0x07, 0x05, 0x09, 0x06, 0x07, 0x07, 0x08,
    0x06, 0x06, 0x07, 0x07, 0x09, 0x07, 0x06, 0x06,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x05, 0x06,
    0x06, 0x05, 0x05, 0x06, 0x05, 0x03, 0x05, 0x06,
    0x03, 0x07, 0x06, 0x06, 0x06, 0x06, 0x05, 0x06,
    0x05, 0x06, 0x07, 0x08, 0x06, 0x05, 0x06, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x08, 0x08, 0x09, 0x09,
    0x09, 0x09, 0x09, 0x08, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x07, 0x07, 0x08, 0x08, 0x09, 0x09,
    0x09, 0x09, 0x09, 0x08, 0x09, 0x09, 0x09, 0x04,
    0x08, 0x00, 0x00, 0x00,
)

DEFAULT_LEFT_MARGIN = 1
LINE_COUNT = 3
CANVAS_WIDTH = 256

# Widest digit is '0' at width 7, so rendered width = 7 + 1 = 8.
# Variable tokens like [0x7000] are estimated as 2x the widest digit rendered width.
_VARIABLE_TOKEN_WIDTH = 2 * (7 + 1)  # 16px

# Variable-width tokens that estimate as _VARIABLE_TOKEN_WIDTH
_VARIABLE_WIDTH_TOKENS = ["[0x7000]", "[0x7024]", "[0x7000timer]"]

# Tokens that are "long" -- force a line break after them
_LONG_TOKENS = ["[0x70A7]", "[filename]"]

# ALL-CAPS-followed-by-colon pattern: lines starting with this don't get a leading space
_CAPS_COLON_PATTERN = re.compile(r"^[A-Z][A-Z0-9 ,.'!?\-]*:")


@dataclass
class Token:
    text: str
    width_px: int = 0
    is_line_break: bool = False
    is_page_break: bool = False
    is_await: bool = False
    is_end: bool = False
    is_space: bool = False
    is_variable: bool = False
    is_long_variable: bool = False
    is_select: bool = False


def _calculate_char_width(char: str, widths: tuple[int, ...] = VANILLA_DIALOG_FONT_WIDTHS) -> int:
    """Return the rendered pixel width of a character (raw width + 1px spacing).

    Returns 0 for out-of-range chars.
    """
    code = ord(char) - 0x20
    if 0 <= code < len(widths):
        raw = widths[code]
        if raw == 0:
            return 0
        return raw + 1
    return 0


def _build_control_token_list() -> list[str]:
    """Build a sorted list of control token strings from the compression table.

    Sorted longest-first so greedy matching works correctly.
    """
    tokens = []
    # From COMPRESSION_TABLE, extract all bracket-delimited tokens
    for key, _ in COMPRESSION_TABLE:
        if key.startswith("["):
            tokens.append(key)
    # Also add bare \n if not already present
    if "\n" not in tokens:
        tokens.append("\n")
    # Sort longest first for greedy matching
    tokens.sort(key=lambda x: -len(x))
    return tokens


_CONTROL_TOKENS = _build_control_token_list()


def _tokenize(text: str, widths: tuple[int, ...] = VANILLA_DIALOG_FONT_WIDTHS) -> list[Token]:
    """Parse a dialog string into a sequence of tokens."""
    tokens = []
    cursor = 0

    while cursor < len(text):
        # 1. Match [delay_N] via regex
        delay_match = re.match(r"\[delay_\d+\]", text[cursor:])
        if delay_match:
            tokens.append(Token(text=delay_match.group(), width_px=0))
            cursor += len(delay_match.group())
            continue

        # 2. Match control tokens (longest first)
        matched = False
        for ctrl in _CONTROL_TOKENS:
            if text[cursor:cursor + len(ctrl)] == ctrl:
                tok = Token(text=ctrl, width_px=0)
                if ctrl == "[await][page]\n":
                    tok.is_page_break = True
                elif ctrl == "[page]\n":
                    tok.is_page_break = True
                elif ctrl == "[await]\n":
                    tok.is_await = True
                    tok.is_line_break = True
                elif ctrl == "[await]":
                    tok.is_await = True
                elif ctrl == "[await][pause]":
                    tok.is_await = True
                elif ctrl == "[end]":
                    tok.is_end = True
                elif ctrl == "[select]":
                    tok.is_select = True
                elif ctrl == "\n":
                    tok.is_line_break = True
                elif ctrl in _VARIABLE_WIDTH_TOKENS:
                    tok.width_px = _VARIABLE_TOKEN_WIDTH
                    tok.is_variable = True
                elif ctrl in _LONG_TOKENS:
                    tok.is_long_variable = True

                tokens.append(tok)
                cursor += len(ctrl)
                matched = True
                break

        if matched:
            continue

        # 3. Literal character
        ch = text[cursor]
        if ch == " ":
            tokens.append(Token(
                text=" ",
                width_px=_calculate_char_width(" ", widths),
                is_space=True,
            ))
        else:
            tokens.append(Token(
                text=ch,
                width_px=_calculate_char_width(ch, widths),
            ))
        cursor += 1

    return tokens


def _is_control_or_break(tok: Token) -> bool:
    """A token that is a control code (line break, page break, await, end, select, delay, etc.)."""
    return (tok.is_line_break or tok.is_page_break or tok.is_await
            or tok.is_end or tok.is_select or tok.text.startswith("[delay"))


def _group_into_words(tokens: list[Token]) -> list[list[Token]]:
    """Group tokens into 'words' -- sequences of non-space, non-control printable tokens.

    Spaces, control codes, and breaks become single-token groups.
    This mirrors Lazy Shell's AddWords logic.
    """
    words = []
    current_word: list[Token] = []

    for tok in tokens:
        if tok.is_space or _is_control_or_break(tok) or tok.is_long_variable:
            # Flush current word
            if current_word:
                words.append(current_word)
                current_word = []
            # Add this token as its own group
            words.append([tok])
        else:
            current_word.append(tok)

    if current_word:
        words.append(current_word)

    return words


def format_dialog(
    text: str,
    char_widths: tuple[int, ...] | None = None,
    left_margin: int | None = None,
) -> str:
    """Insert explicit \\n line breaks where the game would wrap text.

    Strips any existing bare \\n (keeps [await]\\n, [page]\\n, [await][page]\\n).
    If the text starts with [center], it is stripped, formatting is done, and
    [center] is prepended back.

    Args:
        text: The dialog string to format.
        char_widths: Font width table. Defaults to VANILLA_DIALOG_FONT_WIDTHS.
        left_margin: Left margin in pixels. Defaults to DEFAULT_LEFT_MARGIN.

    Returns:
        The reformatted dialog string with explicit \\n breaks.
    """
    if char_widths is None:
        char_widths = VANILLA_DIALOG_FONT_WIDTHS
    if left_margin is None:
        left_margin = DEFAULT_LEFT_MARGIN

    # Strip [center] prefix if present
    has_center = text.startswith("[center]")
    if has_center:
        text = text[len("[center]"):]

    # Tokenize
    tokens = _tokenize(text, char_widths)

    # Strip bare \n tokens, replacing with space (keep [await]\n, [page]\n, [await][page]\n)
    new_tokens = []
    for t in tokens:
        if t.is_line_break and not t.is_await and not t.is_page_break:
            new_tokens.append(Token(
                text=" ",
                width_px=_calculate_char_width(" ", char_widths),
                is_space=True,
            ))
        else:
            new_tokens.append(t)
    tokens = new_tokens

    # Group into words
    words = _group_into_words(tokens)

    # Simulate rendering
    start_x = left_margin + 1
    right_boundary = CANVAS_WIDTH - left_margin
    x = start_x
    output_parts: list[str] = []
    is_line_start = True

    for word_group in words:
        # Single-token control groups
        if len(word_group) == 1:
            tok = word_group[0]
            if tok.is_page_break:
                output_parts.append(tok.text)
                x = start_x
                is_line_start = True
                continue
            if tok.is_line_break and tok.is_await:
                # [await]\n
                output_parts.append(tok.text)
                x = start_x
                is_line_start = True
                continue
            if tok.is_await or tok.is_end or tok.is_select:
                output_parts.append(tok.text)
                continue
            if tok.text.startswith("[delay"):
                output_parts.append(tok.text)
                continue
            if tok.is_long_variable:
                output_parts.append(tok.text)
                # Force line break after long variable
                output_parts.append("\n")
                x = start_x
                is_line_start = True
                continue
            if tok.is_space:
                if is_line_start:
                    # Don't add space at line start unless it's meaningful
                    pass
                output_parts.append(tok.text)
                x += tok.width_px
                continue

        # Multi-token word: compute width
        word_width = sum(t.width_px for t in word_group)

        # Check if word fits on current line
        if x + word_width >= right_boundary and not is_line_start:
            # Need to wrap
            output_parts.append("\n")
            x = start_x
            is_line_start = True

            # Check if new line should start with a space
            word_text = "".join(t.text for t in word_group)
            if not _CAPS_COLON_PATTERN.match(word_text):
                output_parts.append(" ")
                x += _calculate_char_width(" ", char_widths)

        # Render each token in the word
        for tok in word_group:
            if tok.width_px > 0:
                # Check if single char exceeds line
                if x + tok.width_px >= right_boundary and not is_line_start:
                    output_parts.append("\n")
                    x = start_x
                    is_line_start = True

                output_parts.append(tok.text)
                x += tok.width_px
                is_line_start = False
            elif tok.is_variable:
                output_parts.append(tok.text)
            else:
                output_parts.append(tok.text)

    result = "".join(output_parts)

    if has_center:
        result = "[center]" + result

    return result


def validate_dialog(
    text: str,
    char_widths: tuple[int, ...] | None = None,
    left_margin: int | None = None,
) -> list[str]:
    """Validate a dialog string and return a list of warnings.

    Runs the same simulation as format_dialog but checks for issues like
    more than 3 lines without an [await] or [page] break.

    Args:
        text: The dialog string to validate (should already be formatted).
        char_widths: Font width table. Defaults to VANILLA_DIALOG_FONT_WIDTHS.
        left_margin: Left margin in pixels. Defaults to DEFAULT_LEFT_MARGIN.

    Returns:
        A list of warning strings. Empty list means no issues.
    """
    if char_widths is None:
        char_widths = VANILLA_DIALOG_FONT_WIDTHS
    if left_margin is None:
        left_margin = DEFAULT_LEFT_MARGIN

    # Strip [center] if present
    if text.startswith("[center]"):
        text = text[len("[center]"):]

    warnings = []
    tokens = _tokenize(text, char_widths)

    line = 0

    for tok in tokens:
        if tok.is_page_break:
            line = 0
        elif tok.is_line_break:
            line += 1
            if tok.is_await:
                line = 0
        elif tok.is_await:
            line = 0
        if line >= LINE_COUNT:
            warnings.append(
                "More than 3 line breaks without [await] or [page]"
            )
            break

    return warnings


def center_lines(
    text: str,
    char_widths: tuple[int, ...] | None = None,
    left_margin: int | None = None,
) -> str:
    """Add space padding to center each line of dialog text.

    For each line (split by \\n):
    1. Calculate content width in pixels
    2. Available width = (CANVAS_WIDTH - left_margin) - (left_margin + 1)
    3. Remaining = available - content_width
    4. Left pad = floor((remaining / 2) / space_rendered_width) spaces
    5. Prepend that many spaces to the line

    Args:
        text: The dialog string with \\n line breaks already inserted.
        char_widths: Font width table. Defaults to VANILLA_DIALOG_FONT_WIDTHS.
        left_margin: Left margin in pixels. Defaults to DEFAULT_LEFT_MARGIN.

    Returns:
        The text with space padding for centering.
    """
    if char_widths is None:
        char_widths = VANILLA_DIALOG_FONT_WIDTHS
    if left_margin is None:
        left_margin = DEFAULT_LEFT_MARGIN

    space_width = _calculate_char_width(" ", char_widths)
    available_width = (CANVAS_WIDTH - left_margin) - (left_margin + 1)

    # We need to split on \n while preserving control tokens that contain \n
    # Tokenize to handle this correctly
    tokens = _tokenize(text, char_widths)

    # Split tokens into lines at bare \n boundaries
    lines: list[list[Token]] = [[]]
    for tok in tokens:
        if tok.is_line_break and not tok.is_await:
            # Bare \n -- start new line
            lines.append([])
        elif tok.is_page_break or (tok.is_line_break and tok.is_await):
            # [await]\n, [page]\n, [await][page]\n -- attach to current line, then start new
            lines[-1].append(tok)
            lines.append([])
        else:
            lines[-1].append(tok)

    result_parts = []
    for line_tokens in lines:
        # Calculate pixel width of content on this line
        content_width = sum(t.width_px for t in line_tokens)

        remaining = available_width - content_width
        if remaining > 0 and space_width > 0:
            pad_spaces = math.floor((remaining / 2) / space_width)
        else:
            pad_spaces = 0

        # Build the line text
        line_text = " " * pad_spaces + "".join(t.text for t in line_tokens)
        result_parts.append(line_text)

    # Join lines back with \n (the bare \n tokens were consumed as separators)
    return "\n".join(result_parts)


def format_wish(
    text: str,
    char_widths: tuple[int, ...] | None = None,
    left_margin: int | None = None,
) -> str:
    """Format a wish for vertical centering after line breaks are calculated.

    After calculating line breaks:
    - 1 line -> prepend \\n\\n
    - 2 lines -> prepend \\n
    - 3 lines -> no prefix

    Args:
        text: The dialog string with \\n breaks already inserted.
        char_widths: Font width table. Defaults to VANILLA_DIALOG_FONT_WIDTHS.
        left_margin: Left margin in pixels. Defaults to DEFAULT_LEFT_MARGIN.

    Returns:
        The text with vertical centering \\n prefix.
    """
    if char_widths is None:
        char_widths = VANILLA_DIALOG_FONT_WIDTHS
    if left_margin is None:
        left_margin = DEFAULT_LEFT_MARGIN

    # Count lines by counting bare \n in the formatted text
    # We need to tokenize to distinguish bare \n from [await]\n etc.
    tokens = _tokenize(text, char_widths)
    line_count = 1
    for tok in tokens:
        if tok.is_line_break and not tok.is_await and not tok.is_page_break:
            line_count += 1

    if line_count == 1:
        return "\n\n" + text
    elif line_count == 2:
        return "\n" + text
    else:
        return text


def calculate_text_width(
    text: str,
    char_widths: tuple[int, ...] | None = None,
) -> int:
    """Calculate the pixel width of a single line of text (no line breaks).

    Args:
        text: A single line of text.
        char_widths: Font width table.

    Returns:
        Total pixel width.
    """
    if char_widths is None:
        char_widths = VANILLA_DIALOG_FONT_WIDTHS

    tokens = _tokenize(text, char_widths)
    return sum(t.width_px for t in tokens)
