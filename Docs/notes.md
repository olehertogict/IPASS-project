## TSP:
http://www.ams.org/publicoutreach/feature-column/fcarc-tsp

## Nearest neighbour algorithm:
https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm
Paper: "On the Nearest Neighbor Algorithms for the Traveling Salesman Problem"
https://sci-hub.se/10.1007/978-3-319-00951-3_11
https://www.jstor.org/stable/169821?seq=1

## Lin-Kernighan Heuristic:
https://en.wikipedia.org/wiki/Lin%E2%80%93Kernighan_heuristic

## Convex hull heuristic:
geen paper gevonden
https://www.reddit.com/r/compsci/comments/12us2lt/visualizing_the_traveling_salesman_problem_with/

## Christofides Algorithm:
https://en.wikipedia.org/wiki/Christofides_algorithm

## 2-Opt Algorithm:
https://en.wikipedia.org/wiki/2-opt

## Genetic Algorithm:
https://www.researchgate.net/publication/226665831_Genetic_Algorithms_for_the_Travelling_Salesman_Problem_A_Review_of_Representations_and_Operators 
algoritme stappen:
- genereer random populatie
- for i in range(max_generations)
    - selecteer ouders van huidige generatie
    - creëer kinderen van gekozen ouders
    - muteer kinderen
    - voeg kinderen toe aan huidige populatie
    - reduceer huidige populatie tot max populatie grootte
    - herhaal
- selecteer beste individueel uit huidige generatie
Pseudocode:
"""
population = random.population(max_population)
for i in range(max_generations):
    parents = select_parents(population)
    children = create_children(parents, 10 * max_population)
    mutated_children = mutate(children)
    population.append(mutated_children)
    population = reduce_pop(population, max_population)
return best_tour(population)
"""

## TSPLIB, A library containing data for TSP, problems with solutions:
http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/

## Opdrachtomschrijving:
Ik ga een implementatie maken van het 'travelling salesman problem' voor de bezorgservice DHL. De opdracht is als volgt:
gegeven een x aantal adressen, vindt de kortste route die alle adressen precies 1 keer langs gaat en weer eindigt bij
het beginpunt. Dit is een bekend probleem en hier bestaat geen oplossing voor. Wel bestaan er genoeg
algoritmes/heuristieken die de beste oplossing benaderen. Ik ga ±4 algoritmes implementeren en visualiseren
(Nearest neighbour algorithm, Christofides Algorithm, 2-Opt Algorithm, Lin-Kernighan Heuristic).

## Ideeën:
- Christa als opdracht gever. Apotheek, moet medicijnen bezorgen.
- werken met echte adressen/coördinaten. Scherm om adressen in te voeren. Gebruik van OpenCage API om coördinaten op te 
halen
- GUI maken in c++ of GUI in python en route berekenen in c++
- visualizatie in PyGame ipv matplotlib?
- class TspProblem maken
