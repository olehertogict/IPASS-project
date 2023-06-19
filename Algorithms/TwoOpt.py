from classes.City import City
from classes.Tour import Tour

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
    tour = Tour(cities)
    n = len(tour)
    found_improvement = True
    while found_improvement:
        found_improvement = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                sum_plus = tour[i].distance2(tour[j]) + tour[(i + 1) % n].distance2(tour[(j + 1) % n])
                sum_neg = tour[i].distance2(tour[(i + 1) % n]) + tour[j].distance2(tour[(j + 1) % n])
                if sum_plus - sum_neg < 0:
                    two_opt_switch(tour, i, j)
                    found_improvement = True

    tour.add_city(tour[0])
    return tour


