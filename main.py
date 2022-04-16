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

trial_path = city_shuffle()
print(trial_path)
print(CostCalculator.path_cost(trial_path))
