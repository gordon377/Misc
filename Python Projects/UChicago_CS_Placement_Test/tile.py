class Tile:
    """
    Class for representing the boundaries of a tile.

    Public attributes:
      r0, c0: the upper left corner of the tile. Both r0 and c0
        are greater than or equal to zero

      r1, c1: the lower right corner of the tile. Both r1 and c1 are
        greater than or equal to zero
    """
    r0: int
    c0: int
    r1: int
    c1: int

    def __init__(self, r0: int, c0: int, r1: int, c1: int):
        self.r0 = r0
        self.c0 = c0
        self.r1 = r1
        self.c1 = c1

    def __str__(self) -> str:
        return str(((self.r0, self.c0), (self.r1, self.c1)))

    def __repr__(self) -> str:
        return str(self)