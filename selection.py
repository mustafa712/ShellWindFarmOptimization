# Select 5% of individuals hest AEP
# For rest, sample from exponential distribution

from getPopulation import *
import numpy as np
from grid_old import *

grid_points = grid_old()
pop = getPopulation(grid_points)
np.random.seed(1)

def distribution(followers,n):
    """
    Function for sampling from the exponential distribution
    Input : 
            followers is the list of elements which are not elite
            n is the number of elements we want to select
    Output:
            gives the elements to be selected from followers (non-elite)
    """
    b = followers[0].aep
    a = followers[-1].aep
    
    rest_list = []
    while(len(rest_list)<n):
        x_index = np.random.choice(len(followers))
        x = followers[x_index-1].aep

        prob = (np.exp((x-b)/(2*(b-a))))/2       
        if prob > np.random.rand():
            rest_list.append(followers[x_index - 1])
    return rest_list


def selection(population, non_elite,elite_percent = 5):
    """
    A function to select the mating individuals from the population
    Input :
            population - from which mating individuals are selected
            elite - percent of elite which are selected. (Default is 5%)
            non_elite - number of followers which you want to pick
    Output :
            Mating pool
    """
    population.sort(key=lambda x:x.aep, reverse =True)
        
    elite = population[:int(elite_percent*len(population)/100)]    
    rest = population[int(elite_percent*len(population)/100):]

    followers = distribution(rest,non_elite)
    return followers+elite

print(len(selection(pop,80)))
