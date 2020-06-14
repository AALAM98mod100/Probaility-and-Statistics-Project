from random import random
from random import seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math




def Two_D_random_walk(start_pos_x, start_pos_y, steps):

    fig, axs = plt.subplots()

    Radius = 5.64189584
    Overflow = 0
    step_options = [0, 0.5, 1]

    randomWalk_r = np.random.choice(step_options, size=steps)    #Discrete Random Step
    randomWalk_thet = np.random.uniform(0,2*np.pi, size=steps)   #Continuous Random Orientation


# ##
#     randomWalk_r = [5,3,1]
#     randomWalk_thet = [np.pi/2, np.pi/2, np.pi/3]

# ##  



    randomWalk_thet = np.cumsum(randomWalk_thet)


    randomWalk_x= [start_pos_x]
    randomWalk_y= [start_pos_y]

    for i in range(1, steps):

        x_coordinate = randomWalk_r[i] * np.cos(randomWalk_thet[i])
        y_coordinate = randomWalk_r[i] * np.sin(randomWalk_thet[i])


        new_x = randomWalk_x[i-1] + x_coordinate
        new_y = randomWalk_y[i-1] + y_coordinate
        

        distance_from_origin = math.sqrt((new_x)**2 + (new_y)**2)

        if distance_from_origin >= Radius:
            Overflow = distance_from_origin - Radius

            ###
                # RE-ENTRY LOGIC HERE
            ###


        randomWalk_x.append(new_x)
        randomWalk_y.append(new_y)


    #randomWalk_x = np.cumsum(randomWalk_x)
    #randomWalk_y = np.cumsum(randomWalk_y)



    #plt.plot(randomWalk, nums)


    

    xdata, ydata = [], []
    ln, = plt.plot(xdata,ydata)

    def init():
        #Radius = 5.64189584 when area of circle = 100 unit^2
        axs.set_xlim(-Radius,Radius)
        axs.set_ylim(-Radius,Radius)
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


Two_D_random_walk(0, 0, 1000)