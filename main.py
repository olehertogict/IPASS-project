import matplotlib.pyplot as plt
import numpy as np

def test_plotting():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 1, 5, 3])
    plt.scatter(x, y)
    # Connecting points 0, 2, 4
    plt.plot([x[0], x[2], x[4]], [y[0], y[2], y[4]])
    plt.show()

def run():
    test_plotting()
    pass

if __name__ == "__main__":
    run()
