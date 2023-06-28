from Classes.City import City
from Utils import utils
import Algorithms.NearestNeighbour as NearestNeighbour
import Algorithms.Genetic as Genetic
import Algorithms.TwoOpt as TwoOpt
from Application import GUI
from time import time
import csv


def calc_route(file_name: str, algorithm: str, city_list: list[City] = None) -> dict:
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
