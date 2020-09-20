from aep_calculation import *

class WindFarm:
    def __init__(self, numTurbines, locs):
        assert len(locs) == numTurbines
        self.locs = locs
        self.aep = aep_calculation(self.locs)
