import tsplib95
import matplotlib.pyplot as plt
from classes.City import City
from classes.Tour import Tour
import Algorithms.NearestNeighbour as NearestNeighbour
import Algorithms.Genetic as Genetic
import Algorithms.TwoOpt as TwoOpt
import GUI
import api_key
from time import time
import csv

def create_tour_image(tour: Tour):
    all_positions = [c.get_coordinates() for c in tour.cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    # setup plot
    fig = plt.figure()
    plt.axis('off')
    img = plt.imread("maps_image.jpeg")
    plt.imshow(img, extent=[min(x_values)-10, max(x_values)+10, min(y_values)-10, max(y_values)+10])
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

def calc_route(file_name: str, algorithm: str) -> float:
    cities = get_tsp_problem_from_file(f'TestProblems/{file_name}.tsp')
    algorithms = {'Nearest Neighbour': NearestNeighbour, 'Evolutionary/Genetic': Genetic, '2-Opt': TwoOpt}
    t1 = time()
    tour = algorithms[algorithm].run(cities)
    t2 = time()
    print(f'ran in: {t2-t1}')
    data = {
        'problem': file_name,
        'algo': algorithm,
        'time': t2 - t1,
        'distance': round(tour.calc_distance())
    }
    with open('time_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['problem', 'algo', 'time', 'distance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(data)

    create_tour_image(tour)
    return tour.calc_distance()

def main():
    GUI.runGUI()

if __name__ == "__main__":
    main()
