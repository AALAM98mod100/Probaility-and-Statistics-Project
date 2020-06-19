import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from sympy import Point, Line, solve, Eq, symbols, N
import csv



def circular_random_walk(step_options = [0, 0.5, 1], size = 100000):


    fig, axs = plt.subplots()
    plt.xlabel("Position - x")
    plt.ylabel("Position - y")

    Radius = 100
    direction_options = [0, np.pi/4, np.pi/2, np.pi*(3/4), np.pi, np.pi*(5/4), np.pi*(3/2), np.pi*(7/4)]
    step_addition = 0


    randomWalk_x= [0]
    randomWalk_y= [0]


    counter = 1


    while counter < (size + 1):

        angle = np.random.choice(direction_options, size = 1)
        distance = np.random.choice(step_options, size = 1)

        x_coordinate = distance[0] * np.cos(angle[0])
        y_coordinate = distance[0] * np.sin(angle[0])



        new_x = randomWalk_x[-1] + x_coordinate
        new_y = randomWalk_y[-1] + y_coordinate

        
        

        distance_from_origin = ((new_x)**2 + (new_y)**2)**(0.5)

        if distance_from_origin >= (Radius):


            new_x = ('%.3f'%(new_x))
            new_y = ('%.3f'%(new_y))

            old_x = randomWalk_x[-1]
            old_y = randomWalk_y[-1] 

            old_x = ('%.3f'%(old_x))
            old_y = ('%.3f'%(old_y))           

            p1, p2 = Point(old_x, old_y) , Point(new_x, new_y)

            if p1.equals(p2):
                randomWalk_x.append(old_x)
                randomWalk_y.append(old_y)

                counter+=1
                
                continue
                


            line = Line(p1, p2)
            a, b, c = line.coefficients


            x, y = symbols('x,y')
            eq1 = Eq((x)**2 + (y)**2 - (Radius)**2, 0, evaluate=False)
            eq2 = Eq((a*x) + (b*y) + c, 0, evaluate=False)


            sol = solve([eq1, eq2], [x, y])


            #find the point on the circumference where our line will touch, call it circpoint
            try:
                sol1 = Point(sol[0][0], sol[0][1])
                sol2 = Point(sol[1][0], sol[1][1])                

                dist_sol1 = p1.distance(sol1)
                dist_sol2 = p1.distance(sol2)

                if dist_sol1 > dist_sol2:
                    circ_point = sol[1]
                elif dist_sol1 < dist_sol2:
                    circ_point = sol[0]
                else:
                    d1 = sol1.distance(p2)
                    d2 = sol2.distance(p2)

                    if d1 < d2:
                        circ_point = sol[0]
                    else:
                        circ_point = sol[1]

                    

                circ_point = Point(circ_point[0], circ_point[1])
            except:
                randomWalk_x.append(old_x)
                randomWalk_y.append(old_y)


                
                counter+=1
                continue
                

            #we know the overflow amount, call that overflowed
            overflowed = p2.distance(circ_point)


            #get the vector from our curr_pos to circpoint, call it incident
            incident = np.array([circ_point[0] - p1[0], circ_point[1] - p1[1]])


            #circpoint to origin vector
            normal = np.array([circ_point[0], circ_point[1]])


            #-find the angle between incident and normal using dot product wali equation, call that theta

            if p1.equals(circ_point):
                randomWalk_x.append(old_x)
                randomWalk_y.append(old_y)


                
                counter+=1
                
                continue            


            dot = (circ_point[0]*incident[0]) + (circ_point[1]*incident[1])

            magnitude1 = (circ_point[0]**2 + circ_point[1]**2)**(0.5)
            magnitude2 = (incident[0]**2 + incident[1]**2)**(0.5)

            ang = dot / (magnitude1 * magnitude2)

            main_ang = math.acos(ang)


            Theta = main_ang

            if p2[0] < 0 and p2[1] > 0:    #second
                Theta = -Theta

            elif p2[0] > 0 and p2[1] > 0:   #first
                if incident[1] >= incident[0]:
                    Theta = (-Theta)
                else:
                    Theta = (Theta)
            
            elif p2[0] > 0 and p2[1] < 0:
                if incident[1] > -incident[0]:   #fourth
                    Theta = (-Theta)

            elif p2[0] < 0 and p2[1] < 0:
                if incident[1] <= incident[0]:
                    Theta = (-Theta)
                


            

            #-form a 2x2 rotation matrix, uska format dekh lo aram se mile ga
            rotation_matrix = np.array([[np.cos(Theta), -np.sin(Theta)],[np.sin(Theta), np.cos(Theta)]])


            #-multiply the rotation matrix by the normal vector to get another 2x1 vector, call it reflected
            reflected = np.dot(rotation_matrix, normal)

            reflected *= -1


            #-find the unit vector in the direction of reflected, call it ref_unit
            ref_unit = reflected / math.sqrt(reflected[0]**2 + reflected[1]**2)


            #-scalar multiply ref_unit with overflow
            ref_point = ref_unit * overflowed

            #-us vector ke components ko add to circpoint ke coordinates to get the final coordinates
            final = circ_point + ref_point
            

            #-add both circ point (optional but will look better) and final coord to the arrays
            randomWalk_x.append(circ_point[0])
            randomWalk_y.append(circ_point[1])
            

            distance_from_origin = math.sqrt((final[0])**2 + (final[1])**2)

            counter+=1
            if distance_from_origin >= Radius:
                continue
            else:
                randomWalk_x.append(final[0])
                randomWalk_y.append(final[1])



            step_addition += 1
            continue


        randomWalk_x.append(new_x)
        randomWalk_y.append(new_y)
        counter += 1

        if counter % 1000 == 0:
            print(counter)




    distance_from_origin = math.sqrt((randomWalk_x[-1])**2 + (randomWalk_y[-1])**2)


    ### Keep uncommented to see plot
    #return distance_from_origin


    size = size + step_addition

#########################################################
#UNCOMMENT FOR ANIMATION

    # xdata, ydata = [], []
    # ln, = plt.plot(xdata,ydata)

    # def init():
    #     #Radius = 5.64189584 when area of circle = 100 unit^2
    #     axs.set_xlim(-Radius,Radius)
    #     axs.set_ylim(-Radius,Radius)
    #     ln.set_data([], [])
    #     return ln,

    # def update(frame):
    #     xdata.append(randomWalk_x[int(frame)])
    #     ydata.append(randomWalk_y[int(frame)])
    #     ln.set_data(xdata, ydata)
    #     return ln,


    # ani = FuncAnimation(fig, update, frames=np.linspace(0, size, size+1, endpoint=True), interval = 20,
    #                 init_func=init, blit=True, repeat=False)


#ANIMATION CODE
########################################################


    circle1=plt.Circle((0,0),Radius,color='r', alpha= 0.2)
    plt.gcf().gca().add_artist(circle1)

    plt.plot(randomWalk_x, randomWalk_y)

    plt.show()





circular_random_walk()