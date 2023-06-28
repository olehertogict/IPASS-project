from Classes.City import City
from Utils import utils
import Algorithms.NearestNeighbour as NearestNeighbour
import Algorithms.Genetic as Genetic
import Algorithms.TwoOpt as TwoOpt
from Application import GUI
from time import time
import csv


def calc_route(file_name: str, algorithm: str, city_list: list[City] = None) -> dict:
    """
    Calculate a route using the TSP from the provided file_name. Calculated using the provided algorithm

    :param file_name: The path to the .tsp from which to get the tsp problem
    :param algorithm: The name of the algorithm to use ('Nearest Neighbour' or 'Evolutionary/Genetic' or '2-Opt')
    :param city_list: Optional argument, a list of cities to calculate the tsp problem from
    :return: A dictionary containg {'problem': the problem name, 'algo': the algorithm used, 'time': the time
    it took to calculate, 'distance': the length of the route found}
    """
    if not city_list:
        cities = utils.get_tsp_problem_from_file(f'TestProblems/{file_name}.tsp')
    else:
        cities = city_list
    algorithms = {'Nearest Neighbour': NearestNeighbour, 'Evolutionary/Genetic': Genetic, '2-Opt': TwoOpt}
    t1 = time()
    tour = algorithms[algorithm].run(cities)
    t2 = time()
    data = {
        'problem': file_name,
        'algo': algorithm,
        'time': t2 - t1,
        'distance': round(tour.calc_distance())
    }
    with open('Results/time_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['problem', 'algo', 'time', 'distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

    utils.create_tour_image(tour)
    return data

def main():
    GUI.runGUI()

if __name__ == "__main__":
    main()
