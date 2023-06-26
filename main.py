import tsplib95
import matplotlib.pyplot as plt
from Classes.City import City
from Classes.Tour import Tour
import Algorithms.NearestNeighbour as NearestNeighbour
import Algorithms.Genetic as Genetic
import Algorithms.TwoOpt as TwoOpt
from Application import GUI
from time import time
import csv

def create_tour_image(tour: Tour) -> None:
    all_positions = [c.get_coordinates() for c in tour.cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    fig = plt.figure(figsize=(10, 8))
    plt.axis('off')
    img = plt.imread("Images/maps_image.jpeg")
    plt.imshow(img, extent=[min(x_values)-10, max(x_values)+10, min(y_values)-10, max(y_values)+10])
    plt.scatter(x_values, y_values, color='red')
    plt.plot([c.x for c in tour], [c.y for c in tour], color='blue')
    plt.xlim(min(x_values) - 10, max(x_values) + 10)
    plt.ylim(min(y_values) - 10, max(y_values) + 10)
    plt.savefig('Images/animation.jpeg', bbox_inches='tight')

def get_tsp_problem_from_file(file_name: str) -> list[City]:
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    # File has to have a 'NODE_COORD_SECTION'
    c = problem_dict.get('node_coords')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities

def calc_route(file_name: str, algorithm: str, city_list: list[City] = None) -> dict:
    if not city_list:
        cities = get_tsp_problem_from_file(f'TestProblems/{file_name}.tsp')
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
    with open('Data/time_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['problem', 'algo', 'time', 'distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

    create_tour_image(tour)
    return data

def main():
    GUI.runGUI()

if __name__ == "__main__":
    main()
