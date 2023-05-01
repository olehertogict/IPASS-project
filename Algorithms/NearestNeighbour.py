import copy
import random

import tsplib95
from classes.City import City
from classes.Tour import Tour

def get_tsp_problem(file_name: str) -> list[City]:
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    c = problem_dict.get('display_data')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities

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
        # TODO - Write magic method for City class so City object is hashable
        distances_from_city[city.name] = tour[-1].distance_to(city)
    # Get minimum distance from current city
    min_distance = min(distances_from_city.values())
    # Get name of city with minimum distance
    closest_city_name = [key for key, value in distances_from_city.items() if value == min_distance][0]
    # Get city object that is closest to current city
    closest_city = [city for city in cities if city.name == closest_city_name][0]
    tour.add_city(closest_city)
    # Make list of remaining cities to choose from next iteration
    remaining_cities = [city for city in remaining_cities if city.name != closest_city_name]
    print(f"adding city {closest_city} to tour")
    # Append a copy of this tour to the list of tours (for animation)
    tours.append(copy.copy(tour))
    return nearest_neighbour_algorithm(tour, remaining_cities, tours)

def run() -> list[Tour]:
    all_cities = get_tsp_problem('/Users/oledenhertog/PycharmProjects/IPASS-project/TestCases/bays29.tsp')
    starting_city = random.choice(all_cities)
    all_cities = [city for city in all_cities if city.name != starting_city.name]
    tour = Tour([starting_city])
    tour_steps = nearest_neighbour_algorithm(tour, all_cities, [])
    return tour_steps

if __name__ == "__main__":
    run()

