import tsplib95
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from classes.City import City
from classes.Tour import Tour
from classes.TspProblem import TspProblem
import Algorithms.NearestNeighbour as nn
import Algorithms.Genetic as genetic
import Algorithms.TwoOpt as TwoOpt
import copy
import api_key
import random


def animate_tour(tours: list[Tour]):
    if len(tours) == 1:
        tour = tours[0].cities
        new_tours = []
        for i in range(len(tours[0])):
            new_tours.append(Tour(copy.copy(tour[:i + 1])))
        tours = new_tours
    all_positions = [c.get_coordinates() for c in tours[-1].cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    # setup plot
    fig = plt.figure()
    plt.axis('off')
    plt.scatter(x_values, y_values)
    plt.plot([c.x for c in tours[-1]], [c.y for c in tours[-1]], color='blue')
    plt.savefig('animation.jpeg')

    # def update(frame):
    #     lines = plt.plot([c.x for c in tours[frame]], [c.y for c in tours[frame]], color='blue')
    #     return lines
    #
    # interval = int(10000 / len(tours))  # every gif/animation should take 10 seconds
    # print('start animating')
    # anim = FuncAnimation(fig, update, frames=len(tours), interval=interval)
    # print('start saving')
    # writervideo = animation.FFMpegWriter()
    # anim.save(r"animation.gif", writer=writervideo)
    # print('done saving')
    # plt.close()

def get_tsp_problem_from_file(file_name: str) -> list[City]:
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    # File has to have a 'NODE_COORD_SECTION'
    c = problem_dict.get('node_coords')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities

def run(file_name: str, algorithm: str) -> float:
    cities = get_tsp_problem_from_file(file_name)
    algortihms = {'Nearest Neighbour': nn, 'Evolutionary/Genetic': genetic, '2-Opt': TwoOpt}
    tours = [algortihms[algorithm].run(cities)]
    animate_tour(tours)
    return tours[-1].distance


if __name__ == "__main__":
    problem = TspProblem()
    problem.get_tsp_problem_from_file('TspProblems/att48.tsp')
    TwoOpt.run(problem.cities)
