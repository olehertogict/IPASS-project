from classes.City import City
from classes.Tour import Tour
import random
import tsplib95
import copy
from pprint import pprint

# initalize a given tour with known  answer
# problem = tsplib95.load('/Users/oledenhertog/Downloads/att48.tsp')
# problem_dict = problem.as_name_dict()
# c = problem_dict.get('node_coords')
# cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
# all_city_names = [name for name in c.keys()]
# opt_tour = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,
#             17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21, 1]

def select_parents(population):
    sorted_population = sorted(population, key=lambda ind: ind.distance)
    # 50% of population will be parents
    num_parents = len(population) // 2
    parents = sorted_population[:num_parents]
    return parents

def mutate(individual, mutation_chance):
    i, j = random.sample(range(len(individual)), 2)
    # use mutation chance
    if random.random() < mutation_chance:
        # Swap the two selected cities (mutate the tour)
        individual.swap_cities(i, j)
    return individual

def crossover(parent1, parent2):
    # generate slice of parent1
    i, j = random.sample(range(len(parent1)), 2)
    if i > j:
        i, j = j, i
    child = [0 for _ in range(len(parent1))]
    # append slice of parent1 to child
    for k in range(i, j + 1):
        child[k] = parent1[k]
    # cities from parent2 that are not in child already
    remaining_cities = [city for city in parent2 if city not in child]
    # add remaining cities to child
    for k in range(len(parent1)):
        if child[k] == 0:
            child[k] = remaining_cities.pop(0)
    child = Tour(child)
    return child

def create_children(parents, number_of_children):
    children = []
    for i in range(number_of_children):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = crossover(parent1, parent2)
        child = mutate(child, 0.1)
        children.append(child)

    return children

def selection(population, max_population):
    sorted_population = sorted(population, key=lambda ind: ind.distance)
    return sorted_population[:max_population]

def run(cities, POPULATION_SIZE, MAX_GENERATION):
    # generate initial random population
    population = []
    for i in range(POPULATION_SIZE):
        random.shuffle(cities)
        population.append(Tour(copy.copy(cities)))

    for i in range(MAX_GENERATION):
        print(f'generation: {i}')
        parents = select_parents(population)
        children = create_children(parents, 5 * POPULATION_SIZE)
        population.extend(children)
        population = selection(population, POPULATION_SIZE)

    sorted_population = sorted(population, key=lambda ind: ind.distance)
    pprint(sorted_population[0])
    pprint(sorted_population[0].distance)
    return sorted_population[0]

if __name__ == "__main__":
    run()
