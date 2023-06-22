from Classes.Tour import Tour
from Classes.City import City
import random
import copy
import Algorithms.NearestNeighbour as NearestNeighbour

def select_parents(population: list[Tour]) -> list[Tour]:
    """
    From a list of Tours select the best 50% and return those parents

    :param population: The population from which to select the best routes
    :return: A list of parents (best routes)
    """
    sorted_population = sorted(population, key=lambda ind: ind.distance)
    # 50% of population will be parents
    num_parents = len(population) // 2
    parents = sorted_population[:num_parents]
    return parents

def mutate(individual: Tour, mutation_chance: float) -> Tour:
    """
    Mutate a route (individual) which a certain chance of mutation

    :param individual: The tour to mutate
    :param mutation_chance: The chance the individual has to be mutated
    :return: The individual that maybe is mutated
    """
    i, j = random.sample(range(len(individual)), 2)
    # use mutation chance
    if random.random() < mutation_chance:
        # Swap the two selected cities (mutate the tour)
        individual.swap_cities(i, j)
    return individual

def crossover(parent1: Tour, parent2: Tour) -> Tour:
    """
    Return a child from 2 parents, using crossover rule

    :param parent1: Parent 1 to create a child with
    :param parent2: Parent 2 to create a child with
    :return: The child generated from the 2 parents
    """
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

def create_children(parents: list[Tour], number_of_children: int) -> list[Tour]:
    """
    Create n (number_of_children) children from the given parents

    :param parents: parents to create children from
    :param number_of_children: amount of children to be created
    :return: the generated children
    """
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

def selection(population: list[Tour], max_population: int) -> list[Tour]:
    """
    Select the n (max_population) fittest individuals from given population

    :param population: The population to select from
    :param max_population: The number of individuals to return
    :return: the n (max_population) fittest individuals
    """
    sorted_population = sorted(population, key=lambda ind: ind.distance)
    return sorted_population[:max_population]

def run(cities: list[City], POPULATION_SIZE: int = 100, MAX_GENERATION: int = 200) -> Tour:
    """
    Run the Genetic algorithm with given cities

    :param cities: a list of cities to calculate 'optimal' route from
    :param POPULATION_SIZE: the amount of individuals that survive each generation
    :param MAX_GENERATION: number of generations to run the algorithm with
    :return: the best tour found
    """
    # generate initial random population
    population = []
    for i in range(POPULATION_SIZE):
        # use nearest neighbour algorithm to initialize first tours
        population.append(NearestNeighbour.run(copy.copy(cities)))
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
    return sorted_population[0]
