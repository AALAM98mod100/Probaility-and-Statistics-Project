from random import random
from random import seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation




def One_D_random_walk(start_pos_x, start_pos_y, steps):

    fig, axs = plt.subplots()

    

    # randomWalk_x.append(start_pos_x)
    # randomWalk_y.append(start_pos_y)

    randomWalk_r = np.random.uniform(0,1, size=steps)
    print(randomWalk_r)

    randomWalk_thet = np.random.uniform(0,2*np.pi, size=steps)


    randomWalk_thet = np.cumsum(randomWalk_thet)


    randomWalk_x= [start_pos_x]
    randomWalk_y= [start_pos_y]

    for i in range(steps-1):
        randomWalk_x.append(randomWalk_r[i] * np.cos(randomWalk_thet[i]))
        randomWalk_y.append(randomWalk_r[i] * np.sin(randomWalk_thet[i]))


    randomWalk_x = np.cumsum(randomWalk_x)
    randomWalk_y = np.cumsum(randomWalk_y)

    #Distance_from_start_pos = randomWalk[-1] - randomWalk[0]

    #print("Distance from starting position is {}".format(Distance_from_start_pos))

    #plt.plot(randomWalk, nums)

    #print(randomWalk_x)

    

    xdata, ydata = [], []
    ln, = plt.plot(xdata,ydata)

    def init():
        #Radius = 5.64189584 when area of circle = 100 unit^2
        axs.set_xlim(-5.64189584,+5.64189584)
        axs.set_ylim(-5.64189584,+5.64189584)
        ln.set_data([], [])
        return ln,

    def update(frame):
        xdata.append(randomWalk_x[int(frame)])
        ydata.append(randomWalk_y[int(frame)])
        ln.set_data(xdata, ydata)
        return ln,


    ani = FuncAnimation(fig, update, frames=np.linspace(0, steps, steps, endpoint=False), interval = 20,
                    init_func=init, blit=True, repeat=False)


    plt.polar(2*np.pi, 100)
    plt.show()


One_D_random_walk(0, 0, 1000)