import tsplib95
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Cities import City
from Tour import Tour
matplotlib.use("Agg")
matplotlib.rcParams["animation.writer"] = "pillow"

def animate_tour(tours: list[Tour]):
    all_positions = [c.get_coordinates() for c in tours[-1].cities]
    x_values, y_values = [i[0] for i in all_positions], [i[1] for i in all_positions]
    # setup plot
    fig = plt.figure()
    plt.axis('off')
    plt.scatter(x_values, y_values)

    def animate(frame):
        lines = plt.plot([c.x for c in tours[frame]], [c.y for c in tours[frame]], color='blue')
        return lines

    anim = FuncAnimation(fig, animate, frames=len(tours), interval=150)
    video = anim.save('animation.gif', writer='ffmpeg')
    plt.close()

def run():
    # initalize a given tour with known  answer
    problem = tsplib95.load('/Users/oledenhertog/Downloads/bays29.tsp')
    problem_dict = problem.as_name_dict()
    c = problem_dict.get('display_data')
    cities = [City(str(name), tuple(pos)) for name, pos in c.items()]
    opt_tour = [1, 28, 6, 12, 9, 5, 26, 29, 3, 2, 20, 10, 4, 15, 18,
                17, 14, 22, 11, 19, 25, 7, 23, 27, 8, 24, 16, 13, 21, 1]
    tours = [Tour([cities[j-1] for j in opt_tour[:i+1]]) for i in range(len(opt_tour))]
    animate_tour(tours)
    pass

if __name__ == "__main__":
    run()
