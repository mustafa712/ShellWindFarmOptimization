import sys
from getPopulation import *
from grid_old import *
from selection import *
from crossover import *

g = grid_old()
if len(sys.argv) == 2:
    pop = getPopulation(g, filename=sys.argv[1])
else:
    pop = getPopulation(g)
numGen = 100
totalPopSize = 100

for i in range(numGen):
    selected = selection(pop, 80)
    children = breed(selected)
    pop = pop + children
    pop.sort(key=lambda x:x.aep, reverse=True)
    pop = pop[:totalPopSize]
    print("Generation ", i, "Max AEP = ", pop[0].aep)

with open("population.txt", "w") as f:
    i = 1
    for ind in pop:
        f.write("Wind Farm " + str(i) + "\t AEP = " + str(ind.aep) + "\n")
        for point in ind.locs:
            f.write(str(point[0]) + "," + str(point[1]) + "\n")
        i += 1
    f.write("END")
