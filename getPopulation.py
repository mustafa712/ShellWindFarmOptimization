import numpy as np
from WindFarm import *

def getPopFromFile(filename, numTurbines=50):
    population = []
    locs = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Wind Farm" in line:
                if len(locs) > 0:
                    population.append(WindFarm(numTurbines, locs))
                locs = []
            elif "END" in line:
                population.append(WindFarm(numTurbines, locs))
            else:
                line = line[:-1].split(",")
                x, y = float(line[0]), float(line[1])
                locs.append((x,y))
    return population

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

def getPopulation(grid, popSize=100, filename=None):
    """
    A function to get the population of given size
    Input :
            grid - a list (or any iterable) with the coordinates
            popSize - The size of the population required. Default - 100
    Output :
            Population as a list
    """
    if filename is not None:
        return getPopFromFile(filename)
    population = []
    for i in range(popSize):
        population.append(getRandInd(grid,50))

    return population
