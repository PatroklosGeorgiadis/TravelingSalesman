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
trial_path = [city_shuffle(), city_shuffle(), city_shuffle(), city_shuffle()]
totalChance = 0
og_population_idx = 0
print(trial_path)

#calculating the cost of each path
for og_population_idx in range(len(trial_path)):
    print(CostCalculator.path_cost(trial_path[og_population_idx]))
    totalChance += CostCalculator.path_cost(trial_path[og_population_idx])
print(totalChance)

#picking randomly the new parents
random_samples = [0, 0, 0, 0]
for j in range(len(trial_path)):
    random_samples[j] = random.uniform(0, totalChance)
    random_samples[j] = parent_picker(random_samples[j], totalChance, og_population_idx, trial_path)
print(random_samples)

#make new generation
child = random_samples
child[0] = "".join(Reproduction.generate_child(random_samples[0], random_samples[1]))
child[1] = "".join(Reproduction.generate_child(random_samples[1], random_samples[0]))
child[2] = "".join(Reproduction.generate_child(random_samples[2], random_samples[3]))
child[3] = "".join(Reproduction.generate_child(random_samples[3], random_samples[2]))
print(child)


