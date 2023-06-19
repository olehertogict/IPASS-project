import random
from classes.City import City
from classes.Tour import Tour
from classes.TspProblem import TspProblem


def two_opt_switch(tour: Tour, i: int, j: int):
    reversed_tour = []
    for k in range(j, i, -1):
        reversed_tour.append(tour[k])
    tour.cities[i+1:j+1] = reversed_tour


def run(cities: list[City]):
    tour = Tour(cities)
    print(tour, tour.calc_distance())
    cur_length = tour.calc_distance2()
    n = len(tour)
    found_improvement = True
    while found_improvement:
        found_improvement = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                length_delta = (
                    - tour[i].distance2(tour[(i + 1) % n])
                    - tour[j].distance2(tour[(j + 1) % n])
                    + tour[i].distance2(tour[j])
                    + tour[(i + 1) % n].distance2(tour[(j + 1) % n])
                )
                if length_delta < 0:
                    two_opt_switch(tour, i, j)
                    cur_length += length_delta
                    found_improvement = True
    tour.add_city(tour[0])
    print(tour, tour.calc_distance())
    return tour

if __name__ == "__main__":
    problem = TspProblem()
    # problem.get_cities_from_user()
