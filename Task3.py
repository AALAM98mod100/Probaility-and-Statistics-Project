import numpy as np
import matplotlib.pyplot as plt



def circular_random_walk(direction_low, direction_high, step_options, size = 100):


    fig, axs = plt.subplots(subplot_kw=dict(polar=True))

    randomWalk = np.random.choice(step_options, size)
    randomDirections = np.random.randint(direction_low, direction_high + 1, size)

    randomWalk_radians = np.rad2deg(randomWalk)

    plt.plot(randomDirections, randomWalk_radians)

    plt.show()



circular_random_walk(0, 2 * np.pi, [0, 0.5, 1] )