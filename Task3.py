import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math


def circular_random_walk(step_options=[0, 0.5, 1], size=1000):

    fig, axs = plt.subplots()

    Radius = 5
    Overflow = 0
    direction_options = [0, np.pi/4, np.pi/2, np.pi *
                         (3/4), np.pi, np.pi*(5/4), np.pi*(3/2), np.pi*(7/4)]
    randomWalk_r = np.random.choice(step_options, size)  # Discrete Random Step
    randomWalk_thet = np.random.choice(
        direction_options, size)  # Dsicrete Random Orientation

    randomWalk_thet = np.cumsum(randomWalk_thet)

    randomWalk_x = [0]
    randomWalk_y = [0]

    for i in range(1, size):

        x_coordinate = randomWalk_r[i] * np.cos(randomWalk_thet[i-1])
        y_coordinate = randomWalk_r[i] * np.sin(randomWalk_thet[i-1])

        new_x = randomWalk_x[i-1] + x_coordinate
        new_y = randomWalk_y[i-1] + y_coordinate

        distance_from_origin = math.sqrt((new_x)**2 + (new_y)**2)

        if distance_from_origin >= Radius:
            Overflow = distance_from_origin - Radius
            randomWalk_x.append(randomWalk_x[i-1])
            randomWalk_y.append(randomWalk_y[i-1])
        else:
            print(distance_from_origin, end="\n")
            randomWalk_x.append(new_x)
            randomWalk_y.append(new_y)

    xdata, ydata = [], []
    ln, = plt.plot(xdata, ydata)

    def init():
        Radius = 5.64189584
        axs.set_xlim(-Radius, Radius)
        axs.set_ylim(-Radius, Radius)
        ln.set_data([], [])
        return ln,

    def update(frame):
        xdata.append(randomWalk_x[int(frame)])
        ydata.append(randomWalk_y[int(frame)])
        ln.set_data(xdata, ydata)
        return ln,
    ani = FuncAnimation(fig, update, frames=np.linspace(0, size, size, endpoint=False), interval=20,
                        init_func=init, blit=True, repeat=False)

    plt.polar(2*np.pi, 100)
    plt.show()


circular_random_walk()
