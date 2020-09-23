from aep_calculation import *

P1 = 56453 ### Prime number for multiplication
P2 = 213557 ## Prime number for modulus

class WindFarm:
    def __init__(self, numTurbines, locs):
        assert len(locs) == numTurbines
        self.locs = locs
        self.aep = aep_calculation(self.locs)
        self.hash = self.evalHash()

    def __hash__(self):
        return self.hash

    def evalHash(self):
        return sum(P1*pt.id_ for pt in self.locs) % P2
