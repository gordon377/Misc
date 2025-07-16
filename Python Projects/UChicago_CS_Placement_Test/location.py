class Location:
    """
    A class for representing locations based on their x and y coordinates.
    """
    x: int
    y: int

    def __init__(self, x: int, y: int):
        """
        Construct an instance of Location

        Inputs:
          x: the x coordinate of the location
          y: the y coordinate of the location        
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"