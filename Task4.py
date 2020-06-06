from random import random
from random import seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




def One_D_random_walk(start_pos, steps):

    fig, axs = plt.subplots()

    randomWalk = []

    randomWalk.append(start_pos)


    for i in range(1,steps):

        outcome = np.random.uniform(0.0, 1.0, size=1)

        new_val = randomWalk[i-1] + outcome[0]

        randomWalk.append(new_val)


    nums = []
    for j in range(0,steps):
        nums.append(j)

    
    Distance_from_start_pos = randomWalk[-1] - 0

    print("Distance from starting position is {}".format(Distance_from_start_pos))


    xdata, ydata = [], []
    ln, = plt.plot(xdata,ydata)

    def init():
        axs.set_xlim(start_pos - 10, randomWalk[-1] + 10)
        axs.set_ylim(0, steps)
        ln.set_data([], [])
        return ln,

    def update(frame):
        xdata.append(randomWalk[int(frame)])
        ydata.append(int(frame))
        ln.set_data(xdata, ydata)
        return ln,


    ani = FuncAnimation(fig, update, frames=np.linspace(0, len(randomWalk)-1, num=len(randomWalk)), interval = 10,
                    init_func=init, blit=True, repeat=False)


    plt.show()


#One_D_random_walk(0, 100)