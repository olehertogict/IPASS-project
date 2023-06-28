from Classes.Tour import Tour
from Classes.City import City
import matplotlib.pyplot as plt
import tsplib95


def create_tour_image(tour: Tour) -> None:
    """
    From a given tour, generate an image and save it to 'Images/maps_image.jpeg'

    :param tour: The tour to generate an image from
    :return: None
    """
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
    """
    Get a TSP problem from an .tsp file, the file has to have a 'NODE_COORD_SECTION'

    :param file_name: the path to the .tsp file
    :return: a list of cities
    """
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    # File has to have a 'NODE_COORD_SECTION'
    c = problem_dict.get('node_coords')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities
