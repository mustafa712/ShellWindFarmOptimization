import numpy as np
from WindFarm import *
from grid import *
from itertools import combinations
import random

MUTATION_RATE = 0.05

def mutate(child,grid):
    """
    Mutates a child generated from crossover.
    We select a random turbine location
    and change it to some other random location from the grid
    """

    m_pt = np.random.choice(child, 1)[0]
    child.remove(m_pt)
    shuff_neigh = list(m_pt.inRange)
    random.shuffle(shuff_neigh)
    for pt in shuff_neigh:
        if pt.check_constraints(child):
            child.append(pt)
            break
    if len(child) < 50:
        child.append(m_pt)
    assert len(child) == 50

    #m_index = np.random.choice(len(child), 1)[0]
    #rand_pt = grid[np.random.choice(len(grid), 1)[0]]
    #while rand_pt in child:
    #    rand_pt = grid[np.random.choice(len(grid), 1)[0]]
    #child[m_index] = rand_pt
    return child

def crossover(parent1, parent2,grid):
    """
    Generates a child given two parents.
    This is the crossover step of genetic algorithm.
    Input :
            parent1 - The first parent
            parent2 - The second parent
            grid - a list (or any iterable) with the coordinates
    Output :
            child from the crossover of parent1 and parent2
    Algorithm :
            We iterate over the locations in the grid
            if a location is available in either of the parents
                then it is added to the child
            after that if the number of turbines is more in child
                then we randomly select the required number
            We randomly mutate a child according to some mutation rate
    """
    assert len(parent1.locs) == len(parent2.locs)
    numTurbines = len(parent1.locs)
    child = list(np.random.choice(parent1.locs, int(numTurbines/2), replace=False))
    for loc in parent2.locs:
        if len(child) == numTurbines:
            break
        if loc.check_constraints(child):
            child.append(loc)

    if len(child) < numTurbines:
        for loc in parent2.locs:
            if len(child) == numTurbines:
                break
            for neigh in loc.inRange:
                if neigh.check_constraints(child):
                    child.append(neigh)
                    break

    if len(child) < numTurbines:
        g = grid()
        random.shuffle(g)
        for loc in g:
            if len(child) == numTurbines:
                break
            if loc.check_constraints(child):
                child.append(loc)
    assert len(child) == numTurbines

    ##child = []
    ##for loc in grid:
    ##    if loc in parent1.locs:
    ##        child.append(loc)
    ##    elif loc in parent2.locs:
    ##        child.append(loc)

    ##assert len(child) >= numTurbines
    ##
    ##random.shuffle(child)
    ##child_50 = []

    ##for i in child:
    ##    if len(child_50) == 50:
    ##        break
    ##    else:
    ##        if(i.check_constraints(child_50)):
    ##            child_50.append(i)


#    if len(child) > numTurbines:
#        inds = list(np.random.choice(len(child), numTurbines, replace=False))
#        child = [child[i] for i in range(len(child)) if i in inds]

    r = np.random.random()
    if r <= MUTATION_RATE:
        child = mutate(child, grid)

    return WindFarm(numTurbines, child)


def breed(selected, grid,numChildren=100):
    children = []
    all_pair = list(combinations(selected, 2))
    if len(all_pair) > numChildren:
        ind = list(np.random.choice(len(all_pair), numChildren, replace=False))
        for i in range(len(all_pair)):
            if i in ind:
                p1 = all_pair[i][0]
                p2 = all_pair[i][1]
                children.append(crossover(p1, p2,grid))
    else:
        for parents in all_pair:
            children.append(crossover(parents[0], parents[1], grid))
    return children
