import sys
from getPopulation import *
from grid import *
from selection import *
from crossover import *
import matplotlib.pyplot as plt

g = grid(50)
if len(sys.argv) == 2:
    pop = getPopulation(g, filename=sys.argv[1])
else:
    pop = getPopulation(g)

numGen = 100
totalPopSize = 100


for i in range(numGen):
    selected = selection(pop, 80)
    children = breed(selected,g)
    pop = pop + children
    pop.sort(key=lambda x:x.aep, reverse=True)
    pop = pop[:totalPopSize]
    print("Generation ", i, "Max AEP = ", pop[0].aep, "Min AEP = ", pop[-1].aep)

with open("population.txt", "w") as f:
    i = 1
    for ind in pop:
        f.write("Wind Farm " + str(i) + "\t AEP = " + str(ind.aep) + "\n")
        for point in ind.locs:
            f.write(str(point.x) + "," + str(point.y) + "\n")
        i += 1
    f.write("END")


def plot_area(filename = "population.txt", numTurbines=50):
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
                locs.append(Point(x,y))
    coord = population[1].locs
    x=[]
    y=[]
    for i in coord:
        x.append(i.x)
        y.append(i.y)
    plt.scatter(x,y)
    plt.show()
    return population
plot_area()

