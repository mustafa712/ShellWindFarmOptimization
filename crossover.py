import numpy as np
from WindFarm import *
from grid_old import *
from itertools import combinations

MUTATION_RATE = 0.05

def mutate(child):
    """
    Mutates a child generated from crossover.
    We select a random turbine location
    and change it to some other random location from the grid
    """
    g = grid_old()
    m_index = np.random.choice(len(child), 1)[0]
    rand_pt = g[np.random.choice(len(g), 1)[0]]
    while rand_pt in child:
        rand_pt = g[np.random.choice(len(g), 1)[0]]
    child[m_index] = rand_pt
    return child

def crossover(parent1, parent2):
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
    g = grid_old()
    numTurbines = len(parent1.locs)
    child = []
    for loc in g:
        if loc in parent1.locs:
            child.append(loc)
        elif loc in parent2.locs:
            child.append(loc)

    assert len(child) >= numTurbines
    if len(child) > numTurbines:
        inds = list(np.random.choice(len(child), numTurbines, replace=False))
        child = [child[i] for i in range(len(child)) if i in inds]

    r = np.random.random()
    if r <= MUTATION_RATE:
        child = mutate(child)

    return WindFarm(numTurbines, child)


def breed(selected, numChildren=100):
    children = []
    all_pair = list(combinations(selected, 2))
    if len(all_pair) > numChildren:
        ind = list(np.random.choice(len(all_pair), numChildren, replace=False))
        for i in range(len(all_pair)):
            if i in ind:
                p1 = all_pair[i][0]
                p2 = all_pair[i][1]
                children.append(crossover(p1, p2))
    else:
        for parents in all_pair:
            children.append(crossover(parents[0], parents[1]))
    return children
