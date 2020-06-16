import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from sympy import *



def circular_random_walk(step_options = [0, 0.5, 1], size = 1000):


    fig, axs = plt.subplots()

    Radius = 5.64189584
    Overflow = 0
    direction_options = [0, np.pi/4, np.pi/2, np.pi*(3/4), np.pi, np.pi*(5/4), np.pi*(3/2), np.pi*(7/4)]
    step_addition = 0



    randomWalk_r = np.random.choice(step_options, size)     #Discrete Random Step
    randomWalk_thet = np.random.choice(direction_options, size)   #Dsicrete Random Orientation

###
    #NOT RANDOM, SELF GIVEN DATA FOR TESTING
    # randomWalk_r = [3, 5, 2, 5]
    # randomWalk_thet = [0, np.pi/3, np.pi, np.pi/2]

###



    #randomWalk_thet = np.cumsum(randomWalk_thet)



    randomWalk_x= [0]
    randomWalk_y= [0]

    angle = 0

    counter = 1

    reflected = False

    while counter < (size + 1):
        i = counter

        angle = randomWalk_thet[i-1]

        x_coordinate = randomWalk_r[i-1] * np.cos(angle)
        y_coordinate = randomWalk_r[i-1] * np.sin(angle)


        if reflected == True:

            new_x = randomWalk_x[i-1][1] + x_coordinate
            new_y = randomWalk_y[i-1][1] + y_coordinate
        else:

            new_x = randomWalk_x[i-1] + x_coordinate
            new_y = randomWalk_y[i-1] + y_coordinate

        
        reflected = False
        

        distance_from_origin = math.sqrt((new_x)**2 + (new_y)**2)

        if distance_from_origin >= (Radius):

            new_x = round(new_x, 20)
            new_y = round(new_y, 20)

            new_x = float('%.3f'%(new_x))
            new_y = float('%.3f'%(new_y))

            if type(randomWalk_x[i-1]) == tuple:

                old_x = round(randomWalk_x[i-1][1],20)
                old_y = round(randomWalk_y[i-1][1],20)
                
            else:
                old_x = round(randomWalk_x[i-1], 20)
                old_y = round(randomWalk_y[i-1], 20) 

            old_x = float('%.3f'%(old_x))
            old_y = float('%.3f'%(old_y))           

            p1, p2 = Point(old_x, old_y) , Point(new_x, new_y)

            if p1.equals(p2):
                randomWalk_x.append(old_x)
                randomWalk_y.append(old_y)


                
                counter+=1
                
                continue
                # if type(randomWalk_x[i-2]) == tuple:
                #     p1 = Point(randomWalk_x[i-2][1], randomWalk_y[i-2][1])
                    
                # else:
                #     p1 = Point(randomWalk_x[i-2], randomWalk_y[i-2])


            line = Line(p1, p2)
            a, b, c = line.coefficients


            x, y = symbols('x,y')
            eq1 = Eq((x)**2 + (y)**2 - (Radius)**2, 0, evaluate=False)
            eq2 = Eq((a*x) + (b*y) + c, 0, evaluate=False)



            #print(eq1, eq2)

            sol = solve([eq1, eq2], [x, y])


            #find the point on the circumference where our line will touch, call it circpoint

            try:
                if ((old_x <= sol[0][0] <= new_x) and (old_y <= sol[0][1]  <= new_y)) or ((new_x <= sol[0][0] <= old_x) and (new_y <= sol[0][1] <= old_y)):
                    circ_point = sol[0]

                else:

                    circ_point = sol[1]
            except:
                randomWalk_x.append(old_x)
                randomWalk_y.append(old_y)


                
                counter+=1
                
                continue


            # if new_x < 0:
            #     circ_point = sol[0]
            # else:
            #     circ_point = sol[1]

            #print("circ_point = " , circ_point)

            try:
                circ_point = Point(circ_point[0], circ_point[1])
            except:
                print(line)
                






            #we know the overflow amount, call that overflowed
            overflowed = p2.distance(circ_point)

            #print("overflowed = " , N(overflowed))

            #get the vector from our curr_pos to circpoint, call it incident
            incident = np.array([circ_point[0] - old_x, circ_point[1] - old_y])

            #print("incident = " , incident)

            #circpoint to origin vector
            normal = np.array([-circ_point[0], -circ_point[1]])

            #print("normal = " , normal)

            #-find the angle between incident and normal using dot product wali equation, call that theta
            # if Point(circ_point[0], circ_point[1]).equals(p1):
            #     p1 = Point(p1[0]+0.00000001, p1[1])
            l1 = Line(Point(circ_point[0], circ_point[1]), p1)
            l2 = Line(Point(circ_point[0],circ_point[1]), Point(0,0))


            if (p2[0] > 0 and p2[1] > 0) or (p2[0] < 0 and p2[1] < 0):
                Theta = l1.smallest_angle_between(l2)
                Theta = (np.pi*2) - (N(Theta))
            elif (p2[0] > 0 and p2[1] < 0) or (p2[0] < 0 and p2[1] > 0):
                Theta = l1.angle_between(l2)
                Theta = N(Theta)
            Theta = float(-Theta)

            #print("Theta in radians = " , Theta)

            #-form a 2x2 rotation matrix, uska format dekh lo aram se mile ga
            rotation_matrix = np.array([[np.cos(Theta), -np.sin(Theta)],[np.sin(Theta), np.cos(Theta)]])

            #print("rotation_matrix = " , rotation_matrix)

            #-multiply the rotation matrix by the normal vector to get another 2x1 vector, call it reflected
            reflected = np.dot(normal, rotation_matrix)

            #print("reflected = " , reflected)

            #-find the unit vector in the direction of reflected, call it ref_unit
            ref_unit = reflected / math.sqrt(reflected[0]**2 + reflected[1]**2)


            #print("ref_unit = " , ref_unit)

            #-scalar multiply ref_unit with overflow
            ref_point = ref_unit * overflowed

            #-us vector ke components ko add to circpoint ke coordinates to get the final coordinates
            final = circ_point + ref_point
            #print(round(circ_point[0],2) , round(circ_point[1],2) )
            #print(round(ref_point[0],2) , round(ref_point[1],2) )
            #print(round(final[0],2) , round(final[1],2) )
            

            #print("final = " , final)


            #-add both circ point (optional but will look better) and final coord to the arrays
            randomWalk_x.append((circ_point[0], final[0]))
            randomWalk_y.append((circ_point[1], final[1]))
            
            reflected = True


            # randomWalk_x.append(final[0])
            # randomWalk_y.append(final[1])


            
            counter+=1
            


            step_addition += 1
            continue


            ###
                # RE-ENTRY LOGIC HERE
            ###


        randomWalk_x.append(new_x)
        randomWalk_y.append(new_y)
        counter += 1



    x_DATA = []
    y_DATA = []

    for i in range(len(randomWalk_x)):
        if type(randomWalk_x[i]) == tuple:
            pnt1_x, pnt2_x = randomWalk_x[i]
            pnt1_y, pnt2_y = randomWalk_y[i]

            x_DATA.append(pnt1_x)
            x_DATA.append(pnt2_x)

            y_DATA.append(pnt1_y)
            y_DATA.append(pnt2_y)

        else:
            x_DATA.append(randomWalk_x[i])
            y_DATA.append(randomWalk_y[i])

    
    randomWalk_x = x_DATA
    randomWalk_y = y_DATA



    # for i in range(len(randomWalk_x)):
    #     print(round(randomWalk_x[i], 3), round(randomWalk_y[i], 3))


    size = size + step_addition

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


    ani = FuncAnimation(fig, update, frames=np.linspace(0, size, size+1, endpoint=True), interval = 20,
                    init_func=init, blit=True, repeat=False)



    circle1=plt.Circle((0,0),Radius,color='r', alpha= 0.2, edgecolor='r')
    plt.gcf().gca().add_artist(circle1)
    plt.show()



circular_random_walk()