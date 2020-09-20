import numpy as np
from WindFarm import *
from grid import *
from itertools import combinations

MUTATION_RATE = 0.05

def mutate(child):
    """
    Mutates a child generated from crossover.
    We select a random turbine location
    and change it to some other random location from the grid
    """
    g = grid()
    m_index = np.random.choice(len(child), 1)
    rand_pt = g[np.random.choice(len(g), 1)]
    while rand_pt in child:
        rand_pt = g[np.random.choice(len(g), 1)]
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
    assert len(parent1.locs) == len(parent2.lcos)
    g = grid()
    numTurbines = len(parent1)
    child = []
    for loc in g:
        if loc in parent1.locs:
            child.append(loc)
        elif loc in parent2.locs:
            child.append(loc)

    assert len(child) >= numTurbines
    if len(child) > numTurbines:
        child = list(np.random.choice(child, numTurbines, replace=False))

    r = np.random.random()
    if r <= MUTATION_RATE:
        child = mutate(child)

    return WindFarm(numTurbines, child)


def breed(selected, numChildren=100):
    all_pair = list(combinations(selected, 2))
    if len(all_pair) > numChildren:
        ind = list(np.random.choice(len(all_pair), numChildren, replace=False))
        for i in range(len(all_pair)):
            if i in ind:
                p1 = all_pair[0]
                p2 = all_pair[1]
                crossover(p1, p2)
    else:
        for parents in all_pair:
            crossover(parents[0], parents[1])
