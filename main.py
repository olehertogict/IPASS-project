import tsplib95
import matplotlib.pyplot as plt
import numpy as np
from Cities import City
from Tour import Tour

def test_plotting():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 1, 5, 3])
    plt.scatter(x, y)
    # Connecting points 0, 2, 4
    plt.plot([x[0], x[2], x[4]], [y[0], y[2], y[4]])
    plt.show()
    pass

def test_tsp_reading():
    problem = tsplib95.load('/Users/oledenhertog/Downloads/bays29.tsp')
    problem_dict = problem.as_name_dict()
    c = problem_dict.get('display_data')
    print(problem_dict)
    cities = [City(str(name), (pos[0], pos[1])) for name, pos in c.items()]
    all_positions = [c.get_coordinates() for c in cities]
    x = [i[0] for i in all_positions]
    y = [i[1] for i in all_positions]
    plt.scatter(x, y)
    # plot optimal tour without using tour class
    opt_tour = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,
                17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21]
    plt.plot([x[i-1] for i in opt_tour], [y[i-1] for i in opt_tour])
    plt.show()
    pass

def run():
    # test_plotting()
    test_tsp_reading()
    pass

if __name__ == "__main__":
    run()
