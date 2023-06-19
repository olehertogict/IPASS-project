import tsplib95
import matplotlib.pyplot as plt
from classes.City import City
from classes.Tour import Tour
import Algorithms.NearestNeighbour as NearestNeighbour
import Algorithms.Genetic as Genetic
import Algorithms.TwoOpt as TwoOpt
import api_key

def create_tour_image(tour: Tour):
    all_positions = [c.get_coordinates() for c in tour.cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    # setup plot
    fig = plt.figure()
    plt.axis('off')
    plt.scatter(x_values, y_values)
    plt.plot([c.x for c in tour], [c.y for c in tour], color='blue')
    plt.savefig('animation.jpeg')

def get_tsp_problem_from_file(file_name: str) -> list[City]:
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    # File has to have a 'NODE_COORD_SECTION'
    c = problem_dict.get('node_coords')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities

def run(file_name: str, algorithm: str) -> float:
    cities = get_tsp_problem_from_file(file_name)
    algortihms = {'Nearest Neighbour': NearestNeighbour, 'Evolutionary/Genetic': Genetic, '2-Opt': TwoOpt}
    tour = algortihms[algorithm].run(cities)
    create_tour_image(tour)
    return tour.calc_distance()

