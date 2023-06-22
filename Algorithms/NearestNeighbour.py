import random
from Classes.City import City
from Classes.Tour import Tour

def nearest_neighbour_algorithm(cities: list[City]):
    """
    Calculate a route using the nearest neighbour algorithm. Start at a random city and choose the next closest
    city until no more cities are available.

    :param cities: A list of cities to calculate the 'optimal' route of
    :return: the tour found by the algorithm
    """
    remaining_cities = cities
    current_city = random.choice(cities)
    tour = Tour([current_city])
    while remaining_cities:
        # current city is the last city in the tour
        current_city = tour[-1]
        distances_from_city = {}
        for city in remaining_cities:
            distances_from_city[city] = current_city.distance2(city)
        closest_city = min(distances_from_city, key=distances_from_city.get)
        tour.add_city(closest_city)
        remaining_cities.remove(closest_city)

    return tour

def run(cities: list[City]) -> Tour:
    """
    run the nearest neighbour algorithm given cities

    :param cities: a list of cities to calculate a route from
    :return: the route found by the algorithm
    """
    tour = nearest_neighbour_algorithm(cities)
    tour.add_city(tour[0])
    return tour


