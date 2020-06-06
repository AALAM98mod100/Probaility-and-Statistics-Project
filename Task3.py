import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def circular_random_walk(direction_low = None, direction_high= None, step_options = [0, 0.5, 1], size = 1000):


    fig, axs = plt.subplots(subplot_kw=dict(polar=True))

    direction_options = [0, np.pi/4, np.pi/2, np.pi*(3/4), np.pi, np.pi*(5/4), np.pi*(3/2), np.pi*(7/4)]

    randomWalk = np.random.choice(step_options, size)
    randomWalk = np.cumsum(randomWalk)

    if direction_low != None and direction_high != None:
        randomDirections = np.random.randint(direction_low, direction_high + 1, size)
        randomDirections = np.cumsum(randomDirections)
    else:
        randomDirections = np.random.choice(direction_options, size)
        randomDirections = np.cumsum(randomDirections)

    randomDirections_radians = np.rad2deg(randomDirections)

    #plt.plot(randomDirections_radians, randomWalk)

    # print(randomDirections_radians)
    # print(randomWalk)


    xdata, ydata = [], []
    ln, = plt.plot(xdata,ydata)


    def init():
        axs.set_xlim(0, 2* np.pi)
        axs.set_ylim(0, 100)
        ln.set_data([], [])
        return ln,

    def update(frame):
        xdata.append(randomDirections_radians[int(frame)])
        ydata.append(randomWalk[int(frame)])
        ln.set_data(xdata, ydata)
        return ln,

    ani = FuncAnimation(fig, update, frames=np.linspace(0, size - 1, size-1), interval = 20,
                    init_func=init, blit=True)


    plt.show()



circular_random_walk()