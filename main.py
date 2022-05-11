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
            return path[idx], idx
        else:
            idx -= 1


def all_equal(paths_list):
    res = groupby(paths_list)
    return next(res, True) and not next(res, False)


def mutate(self):
    mutated_spots = random.sample(range(4), 2)
    mutated = [self[0], self[1], self[2], self[3], self[4], self[5]]
    temp = self[int(mutated_spots[0]+1)]
    mutated[int(mutated_spots[0] + 1)] = self[int(mutated_spots[1] + 1)]
    mutated[int(mutated_spots[1] + 1)] = temp
    return mutated


#creating the original population (amount N)
paths = []
for N in range(10):
    paths.append(city_shuffle())

#main algorithm
generations = 0
pathsN = len(paths)
#convergence process
while not(all_equal(paths)):
    child_counter = 0
    totalChance = 0
    print("Generation " + str(generations) + ": " + str(paths))

    #calculating the cost of each path
    for og_population_idx in range(pathsN):
        print(CostCalculator.path_cost(paths[og_population_idx]))
        totalChance += CostCalculator.path_cost(paths[og_population_idx])
    print(totalChance)

    #picking randomly the new parents
    random_samples = [0]*round(pathsN * 4 / 5)
    for j in range(0, round(pathsN * 4 / 5), 2):
        random_samples[j] = random.uniform(0, totalChance)
        random_samples[j], p1idx = parent_picker(random_samples[j], totalChance, og_population_idx, paths)
        while True:
            random_samples[j + 1] = random.uniform(0, totalChance)
            random_samples[j + 1], p2idx = parent_picker(random_samples[j+1], totalChance, og_population_idx, paths)
            #making sure they are not the same person
            if p1idx != p2idx:
                break
    print("parents:"+str(random_samples))

    #making the new generation
    #adding some old chromosomes to the new generation (20% of the new generation)
    for idx in range(0, round(pathsN * 1 / 5)):
        paths[idx] = paths[random.randint(0, pathsN - 1)]
    #adding the children (80% of the new population)
    for child_idx in range(round(pathsN * 1 / 5), pathsN, 2):
        #adding the children of each "couple"
        paths[child_idx] = "".join(Reproduction.generate_child(random_samples[child_counter], random_samples[child_counter+1]))
        paths[child_idx+1] = "".join(Reproduction.generate_child(random_samples[child_counter+1], random_samples[child_counter]))
        child_counter += 1

    #mutation process
    for mut in range(pathsN):
        chance = random.randint(1, 10)
        if chance == 1:
            print("Pre-Mutation: " + str(paths[mut]))
            paths[mut] = "".join(mutate(paths[mut]))
            print("Mutation: " + str(paths[mut]))


    generations += 1
    print("children:"+str(paths))
