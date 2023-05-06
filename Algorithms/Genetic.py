from classes.Tour import Tour
import random
import copy
from pprint import pprint

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
    # exlude last city, which is same as first city, from tour
    parent1 = parent1[:len(parent1) - 1]
    parent2 = parent2[:len(parent2) - 1]
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
        # add first city, to back of the tour to create circle
        child.add_city(child[0])
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
        population[i].add_city(population[i][0])
    # Go through all generations
    for i in range(MAX_GENERATION):
        print(f'generation: {i}')
        parents = select_parents(population)
        # generate 5 times more children than the population size
        children = create_children(parents, 5 * POPULATION_SIZE)
        population.extend(children)
        # select fittest individuals
        population = selection(population, POPULATION_SIZE)

    sorted_population = sorted(population, key=lambda ind: ind.distance)
    pprint(len(sorted_population[0]))
    pprint(sorted_population[0].distance)
    return sorted_population[0]

if __name__ == "__main__":
    run()
