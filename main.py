from cost_calculator import CostCalculator
import random


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


#creating the original population (N = 4)
trial_path = [city_shuffle(), city_shuffle(), city_shuffle(), city_shuffle()]
totalChance = 0
print(trial_path)

#calculating the cost of each path
for og_population_idx in range(len(trial_path)):
    print(CostCalculator.path_cost(trial_path[og_population_idx]))
    totalChance += CostCalculator.path_cost(trial_path[og_population_idx])
print(totalChance)

#picking randomly the new parents
for j in range(len(trial_path)):
    totalS = totalChance
    random_sample = random.uniform(0, totalS)
    print(str(random_sample))
    while og_population_idx >= 0:
        totalS -= CostCalculator.path_cost(trial_path[og_population_idx])
        if totalS <= random_sample:
            break
        else:
            og_population_idx -= 1
    print("yes " + str(og_population_idx))
    og_population_idx = 3
