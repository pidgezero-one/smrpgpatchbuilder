class PaletteRow(int):
    """Base class representing a palette row index (0-15)."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 15
        return super(PaletteRow, cls).__new__(cls, num)
