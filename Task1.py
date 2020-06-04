from random import random
from random import seed
import numpy as np
import matplotlib.pyplot as plt



def One_D_random_walk(start_pos, steps, prob_left, prob_not_moving = 0):

    prob_right = 1 - prob_left - prob_not_moving

    randomWalk = []

    randomWalk.append(start_pos)

    move_step, probabilities = [-1, 0 , 1], [prob_left, prob_not_moving, prob_right]


    for i in range(1,steps):

        outcome = np.random.choice(move_step, size=1, p=probabilities)

        new_val = randomWalk[i-1] + outcome[0]

        randomWalk.append(new_val)


    nums = []
    for j in range(0,steps):
        nums.append(j)

    

    plt.plot(randomWalk, nums)
    plt.show()


#One_D_random_walk(0, 1000, .5)