from location import Location
from scooter import Scooter

class ScooterPool:
    """
    A class for representing a pool of scooters and their current locations.
    """

    _scooters: dict[str, Scooter]

    def __init__(self):
        """
        Construct an instance of ScooterPool
        """
        # TODO: complete this constructor
        self._scooters = {} # dict() also works

    def add_scooter(self, sid: str, x: int, y: int) -> bool:
        """
        Add a scooter to the pool

        Inputs:
          sid: the unique identifier for this scooter
          x: the initial x coordinate for the scooter
          y: the initial y coordinate for the scooter           

        Returns: True, if the scooter ID does not already appear in the pool
          and False, otherwise.
        """
        # TODO: complete this method

        if self._scooters.get(sid) == None:
            self._scooters.update({f"{sid}": Scooter(sid,x,y)})
            return True
        else:
            return False



    def num_scooters_in_range(self, loc: Location, dist: int) -> int:
        """
        Count the number of scooters where the distance
        between the scooter and a specified location (loc) is
        strictly less than dist.

        Inputs:
          loc: the specified location
          dist: the maximum allowed distance from the specified location

        Returns: the number of scooters where the distance between
          the scooter's location and the specified location is
          strictly less than dist.
        """
        # TODO: complete this method
        sum = 0

        for x in self._scooters:
            scooter = self._scooters[x]
            if scooter.distance_between(loc) < dist:
                sum+=1

        return sum

    def __str__(self) -> str:
        # optional method
        return ""