import random
from cost_calculator import CostCalculator
from reproduction import Reproduction

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


'''
totalS (totalChance)
random_sample
og_population_idx
path
'''


def parent_picker(self, totalS, idx, path):
    while idx >= 0:
        totalS -= CostCalculator.path_cost(path[idx])
        if totalS <= self:
            return path[idx]
        else:
            idx -= 1


#creating the original population (N = 4)
paths = [city_shuffle(), city_shuffle(), city_shuffle(), city_shuffle()]
generations = 0
while not(paths[0] == paths[1] == paths[2] == paths[3]):
    totalChance = 0
    print("Generation " + str(generations) + ": " + str(paths))

    #calculating the cost of each path
    for og_population_idx in range(len(paths)):
        print(CostCalculator.path_cost(paths[og_population_idx]))
        totalChance += CostCalculator.path_cost(paths[og_population_idx])
    print(totalChance)

    #picking randomly the new parents
    random_samples = [0, 0, 0, 0]
    for j in range(len(paths)):
        random_samples[j] = random.uniform(0, totalChance)
        random_samples[j] = parent_picker(random_samples[j], totalChance, og_population_idx, paths)
    print(random_samples)

    #make new generation
    paths[0] = "".join(Reproduction.generate_child(random_samples[0], random_samples[1]))
    paths[1] = "".join(Reproduction.generate_child(random_samples[1], random_samples[0]))
    paths[2] = "".join(Reproduction.generate_child(random_samples[2], random_samples[3]))
    paths[3] = "".join(Reproduction.generate_child(random_samples[3], random_samples[2]))
    generations += 1
