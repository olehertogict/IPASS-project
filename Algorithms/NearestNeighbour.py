import copy
import tsplib95
from City import City
from Tour import Tour

def get_tsp_problem(file_name: str) -> list[City]:
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    c = problem_dict.get('display_data')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities

def nearest_neighbour_algorithm(tour: Tour, cities: list[City], tours: list[Tour]):
    if not cities:
        print("no remaining possibilities, returning tour")
        print(f"The final tour length is {tour.distance}")
        return tours
    remaining_cities = cities
    distances_from_city = {}
    for city in remaining_cities:
        # TODO - Write magic method for City class so City object is hashable
        distances_from_city[city.name] = tour[-1].distance_to(city)
    min_distance = min(distances_from_city.values())
    closest_city_name = [key for key, value in distances_from_city.items() if value == min_distance][0]
    closest_city = [city for city in cities if city.name == closest_city_name][0]
    tour.add_city(closest_city)
    remaining_cities = [city for city in remaining_cities if city.name != closest_city_name]
    print(f"adding city {closest_city} to tour")
    tours.append(copy.copy(tour))
    return nearest_neighbour_algorithm(tour, remaining_cities, tours)

def run() -> list[Tour]:
    all_cities = get_tsp_problem('/Users/oledenhertog/PycharmProjects/IPASS-project/TestCases/bays29.tsp')
    tour = Tour([all_cities[0]])
    tour_steps = nearest_neighbour_algorithm(tour, all_cities[1:], [])
    return tour_steps

if __name__ == "__main__":
    run()

