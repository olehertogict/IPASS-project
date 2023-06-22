from Classes.City import City
from Classes.Tour import Tour

def two_opt_switch(tour: Tour, i: int, j: int) -> None:
    """
    reverse order of the cities between the indices

    :param tour: the tour where the cities will be switched
    :param i: starting index
    :param j: ending index
    """
    reversed_tour = []
    for k in range(j, i, -1):
        reversed_tour.append(tour[k])
    tour.cities[i+1:j+1] = reversed_tour

def run(cities: list[City]) -> Tour:
    """
    Calculate the optimal route using the 2-opt algorithm.

    :param cities: a list of cities for which to calculate a route for
    :return: The best route found by the 2-opt algorithm
    """
    tour = Tour(cities)
    n = len(tour)
    found_improvement = True
    while found_improvement:
        found_improvement = False
        # iterate over pairs of cities
        for i in range(n - 1):
            for j in range(i + 1, n):
                # current distance of i to j + (i+1)%n to (j+1)%n
                cur_dist = tour[i].distance2(tour[j]) + tour[(i + 1) % n].distance2(tour[(j + 1) % n])
                # potential improvement i to (i+1)%n + j to (j+1)%n (the switch of cities)
                potential_improvement = tour[i].distance2(tour[(i + 1) % n]) + tour[j].distance2(tour[(j + 1) % n])
                # if there is an improvement found to the switch
                if cur_dist - potential_improvement < 0:
                    two_opt_switch(tour, i, j)
                    found_improvement = True

    tour.add_city(tour[0])
    return tour


