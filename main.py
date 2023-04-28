import tsplib95
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PySimpleGUI as sg
import numpy as np
from Cities import City
from Tour import Tour

def update(frame):
    pass

def animate_complete_tour(tour: Tour):
    all_positions = [c.get_coordinates() for c in tour.cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    tour_animation = Tour([])

    for i in range(len(tour)):
        tour_animation.add_city(tour[i])
        plt.scatter(x_values, y_values)
        plt.plot([c.x for c in tour_animation], [c.y for c in tour_animation])
        plt.pause(0.1)

    plt.show()

def test_tsp_reading():
    problem = tsplib95.load('/Users/oledenhertog/Downloads/bays29.tsp')
    problem_dict = problem.as_name_dict()
    c = problem_dict.get('display_data')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    all_positions = [c.get_coordinates() for c in cities]
    x = [i[0] for i in all_positions]
    y = [i[1] for i in all_positions]

    plt.scatter(x, y)

    # Add labels to points
    for i, (x_val, y_val) in enumerate(zip(x, y)):
        plt.annotate(str(i + 1), (x_val, y_val), xytext=(5, 5), textcoords='offset points')

    # plot optimal tour without using tour class
    opt_tour = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,
                17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21, 1]
    test_tour = []

    t1 = Tour([cities[i - 1] for i in opt_tour])
    t1.show()
    plt.gca().set_xticklabels([])
    plt.gca().set_xticks([])
    plt.gca().set_yticklabels([])
    plt.gca().set_yticks([])
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    for i in range(len(opt_tour)):
        test_tour.append(opt_tour[i])
        plt.plot([x[i - 1] for i in test_tour], [y[i - 1] for i in test_tour])
        plt.pause(0.1)

    plt.show()
    pass

def run():
    # test_plotting()
    # test_tsp_reading()
    problem = tsplib95.load('/Users/oledenhertog/Downloads/bays29.tsp')
    problem_dict = problem.as_name_dict()
    c = problem_dict.get('display_data')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    opt_tour = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,
                17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21, 1]
    tour = Tour([cities[i-1] for i in opt_tour])
    animate_complete_tour(tour)
    pass

if __name__ == "__main__":
    run()
