import random
from cost_calculator import CostCalculator
from reproduction import Reproduction
from itertools import groupby


def city_shuffle():
    path = "A"
    cities = ["B", "C", "D", "E"]
    random.shuffle(cities)
    i = 0
    while i < len(cities):
        path += cities[i]
        i += 1
    path += "A"
    return path


def parent_picker(self, totalS, idx, path):
    while idx >= 0:
        totalS -= CostCalculator.path_cost(path[idx])
        if totalS <= self:
            return path[idx]
        else:
            idx -= 1


def all_equal(paths_list):
    res = groupby(paths_list)
    return next(res, True) and not next(res, False)


#creating the original population (amount N)
paths = []
for N in range(4):
    paths.append(city_shuffle())

#main algorithm
generations = 0
pathsN = len(paths)
#convergence process
while not(all_equal(paths)):
    totalChance = 0
    print("Generation " + str(generations) + ": " + str(paths))

    #calculating the cost of each path
    for og_population_idx in range(pathsN):
        print(CostCalculator.path_cost(paths[og_population_idx]))
        totalChance += CostCalculator.path_cost(paths[og_population_idx])
    print(totalChance)

    #picking randomly the new parents
    random_samples = [0]*pathsN
    for j in range(pathsN):
        random_samples[j] = random.uniform(0, totalChance)
        random_samples[j] = parent_picker(random_samples[j], totalChance, og_population_idx, paths)
    print(random_samples)

    #making the new generation of children
    for child_idx in range(0, pathsN, 2):
        paths[child_idx] = "".join(Reproduction.generate_child(random_samples[child_idx], random_samples[child_idx+1]))
        paths[child_idx+1] = "".join(Reproduction.generate_child(random_samples[child_idx+1], random_samples[child_idx]))
    generations += 1
