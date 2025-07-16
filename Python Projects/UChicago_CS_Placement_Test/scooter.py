from location import Location

class Scooter:
    """
    A class for representing scooters and their locations

    Public attribute:
      sid: the scooter's unique identifier
    """
    sid: str
    __location: Location

    def __init__(self, sid: str, x: int, y: int):
        """
        Construct an instance of Scooter

        Inputs:
          sid: a unique identifier for the scooter
          x: the x coordinate of the scooter's location
          y: the y coordinate of the scooter's location        
        """
        self.sid = sid
        self.__location = Location(x, y)

    def distance_between(self, loc: Location) -> int:
        """
        Compute the distance between the scooter and the specified
        location.

        Inputs:
          loc: a location

        Returns: the manhattan distance between the scooter's location
          and the input location.  This value has no units.
        """
        return abs(self.__location.x - loc.x) + abs(self.__location.y - loc.y)

    def __str__(self) -> str:
        return f"{self.sid}: {self.__location}"