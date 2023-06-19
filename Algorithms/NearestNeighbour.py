import copy
import random

from classes.City import City
from classes.Tour import Tour

def nearest_neighbour_algorithm(tour: Tour, cities: list[City], tours: list[Tour]):
    if not cities:
        print("no remaining possibilities, returning tour")
        tour.add_city(tour[0])
        tours.append(copy.copy(tour))
        print(f"The final tour length is {tour.distance}")
        return tours
    remaining_cities = cities
    distances_from_city = {}
    for city in remaining_cities:
        distances_from_city[city] = tour[-1].distance_to(city)
    # Get minimum distance from current city
    min_distance = min(distances_from_city.values())
    # Get city with minimum distance
    closest_city = [key for key, value in distances_from_city.items() if value == min_distance][0]
    tour.add_city(closest_city)
    # Make list of remaining cities to choose from next iteration
    remaining_cities = [city for city in remaining_cities if city != closest_city]
    # Append a copy of this tour to the list of tours (for animation)
    # tours.append(copy.copy(tour))
    return nearest_neighbour_algorithm(tour, remaining_cities, tours)

def run(cities) -> list[Tour]:
    starting_city = random.choice(cities)
    all_cities = [city for city in cities if city.name != starting_city.name]
    tour = Tour([starting_city])
    tour_steps = nearest_neighbour_algorithm(tour, all_cities, [])
    print('algorithm done calculating')
    return tour_steps[-1]

if __name__ == "__main__":
    run([City('1', (0, 0)), City('2', (1, 1)), City('3', (6, 6))])

