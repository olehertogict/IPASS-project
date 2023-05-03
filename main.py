import tsplib95
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from classes.City import City
from classes.Tour import Tour
import Algorithms.NearestNeighbour as nn
matplotlib.use("Agg")
matplotlib.rcParams["animation.writer"] = "pillow"

def animate_tour(tours: list[Tour]):
    all_positions = [c.get_coordinates() for c in tours[-1].cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    # setup plot
    fig = plt.figure()
    plt.axis('off')
    plt.scatter(x_values, y_values)

    def update(frame):
        lines = plt.plot([c.x for c in tours[frame]], [c.y for c in tours[frame]], color='blue')
        return lines

    interval = int(10000 / len(tours))  # every gif/animation should take 10 seconds
    anim = FuncAnimation(fig, update, frames=len(tours), interval=interval)
    video = anim.save('animation.gif', writer='ffmpeg')
    plt.close()

def get_tsp_problem_from_file(file_name: str) -> list[City]:
    problem = tsplib95.load(file_name)
    problem_dict = problem.as_name_dict()
    # File has to have a 'NODE_COORD_SECTION'
    c = problem_dict.get('node_coords')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    return cities

def run(file_name: str) -> float:
    cities = get_tsp_problem_from_file(file_name)
    tours = nn.run(cities)
    print(f'the algorithm took {len(tours)} steps')
    animate_tour(tours)
    return tours[-1].distance

if __name__ == "__main__":
    run('TestProblems/berlin52.tsp')
