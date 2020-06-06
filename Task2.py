from random import random
import math
from random import seed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



#Assumption:

# - It takes 1 second of time, for each of the person to take 1 step on the grid!


def One_D_random_walk_Match(start_pos_A, start_pos_B, prob_left_A, prob_left_B, prob_not_moving_A = 0, prob_not_moving_B = 0):

    fig, axs = plt.subplots()

    prob_right_A = 1 - prob_left_A - prob_not_moving_A
    prob_right_B = 1 - prob_left_B - prob_not_moving_B

    randomWalk_A = []
    randomWalk_B = []

    if start_pos_A == start_pos_B:
        print("The time taken for both people to meet on the path is 0 seconds")
        return

    randomWalk_A.append(start_pos_A)
    randomWalk_B.append(start_pos_B)

    move_step_A, probabilities_A = [-1, 0 , 1], [prob_left_A, prob_not_moving_A, prob_right_A]
    move_step_B, probabilities_B = [-1, 0 , 1], [prob_left_B, prob_not_moving_B, prob_right_B]

    steps = 0

    counter = 1

    while counter < math.inf:

        outcome_A = np.random.choice(move_step_A, size=1, p=probabilities_A)
        outcome_B = np.random.choice(move_step_B, size=1, p=probabilities_B)

        new_val_A = randomWalk_A[counter-1] + outcome_A[0]
        new_val_B = randomWalk_B[counter-1] + outcome_B[0]

        randomWalk_A.append(new_val_A)
        randomWalk_B.append(new_val_B)

        steps += 1

        if new_val_A == new_val_B:
            break

        counter += 1


    nums = []
    for i in range(steps+1):
        nums.append(i)

    
    print("The time taken for both people to meet on the path is {} seconds".format(steps))

    #plt.plot(randomWalk_A, nums)
    #plt.plot(randomWalk_B, nums)


    x_Adata, y_Adata, x_Bdata, y_Bdata = [], [], [], []
    ln, = plt.plot(x_Adata,y_Adata)
    ln2, = plt.plot(x_Bdata,y_Bdata)


    def init():
        if (min(randomWalk_A) > max(randomWalk_B)):
            axs.set_xlim(min(randomWalk_B), max(randomWalk_A))
        else:
            axs.set_xlim(min(randomWalk_A), max(randomWalk_B))


        axs.set_ylim(0, len(nums)+10)
        ln.set_data([], [])
        ln2.set_data([], [])
        return ln, ln2,

    def update(frame):
        x_Adata.append(randomWalk_A[int(frame)])
        y_Adata.append(int(frame))
        x_Bdata.append(randomWalk_B[int(frame)])
        y_Bdata.append(int(frame))
        ln.set_data(x_Adata, y_Adata)
        ln2.set_data(x_Bdata, y_Bdata)
        return ln, ln2,


    ani = FuncAnimation(fig, update, frames=np.linspace(0, len(randomWalk_A)-1, num=len(randomWalk_A)), interval = 1,
                    init_func=init, blit=True, repeat=False)

    plt.show()


#One_D_random_walk_Match(-5, 5, 0.5, 0.5)