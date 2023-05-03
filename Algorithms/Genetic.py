from classes.City import City
from classes.Tour import Tour
import random
import tsplib95
import copy

# initalize a given tour with known  answer
problem = tsplib95.load('/Users/oledenhertog/Downloads/bays29.tsp')
problem_dict = problem.as_name_dict()
c = problem_dict.get('display_data')
cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
all_city_names = [name for name in c.keys()]
opt_tour = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,
            17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21, 1]

POPULATION_SIZE = 100

def get_best_tours(population):
    sorted_dict = dict(sorted(population.items(), key=lambda item: item[1], reverse=True))

    top_values = list(sorted_dict.values())[:int(len(sorted_dict) * 0.1)]

    top_dict = {k: v for k, v in sorted_dict.items() if v in top_values}

    return top_dict

def mutate(tour):
    i, j = random.randint(1, len(tour) - 2), random.randint(1, len(tour) - 2)
    while i == j:
        i, j = random.randint(1, len(tour) - 2), random.randint(1, len(tour) - 2)
    copied = copy.copy(tour)
    copied.swap_cities(i, j)
    return copied

population = {}
for _ in range(POPULATION_SIZE):
    random.shuffle(cities)
    tour = Tour(cities)
    population[copy.copy(tour)] = tour.distance


best_tours = get_best_tours(population)
new_population = {}
for i in range(POPULATION_SIZE):
    gen = random.choice(list(get_best_tours(population).keys()))
    mutated = mutate(gen)
    new_population[mutated] = mutated.distance

print(get_best_tours(new_population))
