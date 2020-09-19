import numpy as np
from aep_calculation import *

class WindFarm:
    def __init__(self, numTurbines, locs):
        assert len(locs) == numTurbines
        self.locs = locs
        self.aep = aep_calculation(self.locs)

def getRandInd(grid, numTurbines=50):
    """
    A function to randomly genrate an individual
    Input :
            grid - a list (or any iterable) with the coordinates
            numTurbines - Number of turbines in each individual. Default - 50
    Output :
            A list of coordinates of the turbines
    """
    locs = []
    loc_ind = np.random.choice(len(grid), numTurbines, replace=False)
    for i in range(len(grid)):
        if i in loc_ind:
            locs.append(grid[i])
    
    return WindFarm(numTurbines, list(locs))

def getPopulation(grid, popSize=100):
    """
    A function to get the population of given size
    Input :
            grid - a list (or any iterable) with the coordinates
            popSize - The size of the population required. Default - 100
    Output :
            Population as a list
    """
    population = []
    for i in range(popSize):
        population.append(getRandInd(grid))

    return population
