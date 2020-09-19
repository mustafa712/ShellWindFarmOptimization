import numpy as np

def crossover(parent1, parent2, grid):
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
    """
    assert len(parent1) == len(parent2)
    numTurbines = len(parent1)
    child = []
    for loc in grid:
        if loc in parent1:
            child.append(loc)
        elif loc in parent2:
            child.append(loc)

    assert len(child) >= numTurbines
    if len(child) > numTurbines:
        child = list(np.random.choice(child, numTurbines, replace=False))
    return child

