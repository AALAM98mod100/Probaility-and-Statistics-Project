import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from sympy import Point, Line, solve, Eq, symbols, N



def circular_random_walk():

    fig, axs = plt.subplots()

    Radius = 6
    step_addition_A = 0
    step_addition_B = 0

#####
##Choosing initial points

    r_A = np.random.uniform(0,Radius, size = 1)[0]
    r_B = np.random.uniform(0,Radius, size = 1)[0]

    thet_A = np.random.uniform(0, 2*np.pi, size = 1)[0]
    thet_B = np.random.uniform(0, 2*np.pi, size = 1)[0]

    x_A = r_A * np.cos(thet_A)
    y_A = r_A * np.sin(thet_A)

    x_B = r_B * np.cos(thet_B)
    y_B = r_B * np.sin(thet_B)

####


    randomWalk_x_A= [x_A]
    randomWalk_y_A= [y_A]
    

    randomWalk_x_B= [x_B]
    randomWalk_y_B= [y_B]
    

    flag_A_ref = False
    flag_B_ref = False
    steps = 0

    while True:
        angle_A = np.random.uniform(0, 2*np.pi, size = 1)
        angle_B = np.random.uniform(0, 2*np.pi, size = 1)

        distance_A = np.random.uniform(0, 1, size = 1)
        distance_B = np.random.uniform(0, 1, size = 1)

        x_coordinate_A = distance_A[0] * np.cos(angle_A[0])
        y_coordinate_A = distance_A[0] * np.sin(angle_A[0])

        x_coordinate_B = distance_B[0] * np.cos(angle_B[0])
        y_coordinate_B = distance_B[0] * np.sin(angle_B[0])


        new_x_A = randomWalk_x_A[-1] + x_coordinate_A
        new_y_A = randomWalk_y_A[-1] + y_coordinate_A

        new_x_B = randomWalk_x_B[-1] + x_coordinate_B
        new_y_B = randomWalk_y_B[-1] + y_coordinate_B

        
        distance_from_origin_A = math.sqrt((new_x_A)**2 + (new_y_A)**2)
        distance_from_origin_B = math.sqrt((new_x_B)**2 + (new_y_B)**2)

        while distance_from_origin_A >= (Radius):

            new_x_A = round(new_x_A, 20)
            new_y_A = round(new_y_A, 20)

            new_x_A = float('%.3f'%(new_x_A))
            new_y_A = float('%.3f'%(new_y_A))

            old_x_A = round(randomWalk_x_A[-1], 20)
            old_y_A = round(randomWalk_y_A[-1], 20) 

            old_x_A = float('%.3f'%(old_x_A))
            old_y_A = float('%.3f'%(old_y_A))           

            p1, p2 = Point(old_x_A, old_y_A) , Point(new_x_A, new_y_A)

            if p1.equals(p2):
                randomWalk_x_A.append(old_x_A)
                randomWalk_y_A.append(old_y_A)
                
                flag_A_ref = True
                break
                


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
                randomWalk_x_A.append(old_x_A)
                randomWalk_y_A.append(old_y_A)

                flag_A_ref = True
                break
                

            #we know the overflow amount, call that overflowed
            overflowed = p2.distance(circ_point)


            #get the vector from our curr_pos to circpoint, call it incident
            incident = np.array([circ_point[0] - p1[0], circ_point[1] - p1[1]])


            #circpoint to origin vector
            normal = np.array([circ_point[0], circ_point[1]])


            #-find the angle between incident and normal using dot product wali equation, call that theta

            if p1.equals(circ_point):
                randomWalk_x_A.append(old_x_A)
                randomWalk_y_A.append(old_y_A)

                flag_A_ref = True 
                break        


            dot = (circ_point[0]*incident[0]) + (circ_point[1]*incident[1])

            magnitude1 = math.sqrt(circ_point[0]**2 + circ_point[1]**2)
            magnitude2 = math.sqrt(incident[0]**2 + incident[1]**2) 

            ang = dot / (magnitude1 * magnitude2)

            main_ang = math.acos(ang)


            Theta = main_ang

            if p2[0] < 0 and p2[1] > 0:    #second
                if incident[1] >= incident[0]:
                    Theta = float(-Theta)
                else:
                    Theta = float(-Theta)

            elif p2[0] > 0 and p2[1] > 0:   #first
                if incident[1] >= incident[0]:
                    Theta = float(-Theta)
                else:
                    Theta = float(Theta)
            
            elif p2[0] > 0 and p2[1] < 0:
                if incident[1] <= -incident[0]:   #fourth
                    Theta = float(Theta)
                else:
                    Theta = float(-Theta)

            elif p2[0] < 0 and p2[1] < 0:
                if incident[1] <= incident[0]:
                    Theta = float(-Theta)
                else:
                    Theta = float(Theta)

            else:
                Theta = float(Theta)

            

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
            randomWalk_x_A.append(circ_point[0])
            randomWalk_y_A.append(circ_point[1])
            

            distance_from_origin = math.sqrt((final[0])**2 + (final[1])**2)

            if distance_from_origin >= Radius:
                flag_A_ref = True
                break
            else:
                randomWalk_x_A.append(final[0])
                randomWalk_y_A.append(final[1])



            step_addition_A += 1
            flag_A_ref = True
            break

        while distance_from_origin_B >= (Radius):

            new_x_B = round(new_x_B, 20)
            new_y_B = round(new_y_B, 20)

            new_x_B = float('%.3f'%(new_x_B))
            new_y_B = float('%.3f'%(new_y_B))

            old_x_B = round(randomWalk_x_B[-1], 20)
            old_y_B = round(randomWalk_y_B[-1], 20) 

            old_x_B = float('%.3f'%(old_x_B))
            old_y_B = float('%.3f'%(old_y_B))           

            p1, p2 = Point(old_x_B, old_y_B) , Point(new_x_B, new_y_B)

            if p1.equals(p2):
                randomWalk_x_A.append(old_x_B)
                randomWalk_y_A.append(old_y_B)
                
                flag_B_ref = True
                break
                


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
                randomWalk_x_B.append(old_x_B)
                randomWalk_y_B.append(old_y_B)

                flag_B_ref = True
                break
                

            #we know the overflow amount, call that overflowed
            overflowed = p2.distance(circ_point)


            #get the vector from our curr_pos to circpoint, call it incident
            incident = np.array([circ_point[0] - p1[0], circ_point[1] - p1[1]])


            #circpoint to origin vector
            normal = np.array([circ_point[0], circ_point[1]])


            #-find the angle between incident and normal using dot product wali equation, call that theta

            if p1.equals(circ_point):
                randomWalk_x_B.append(old_x_B)
                randomWalk_y_B.append(old_y_B)

                flag_B_ref = True 
                break        


            dot = (circ_point[0]*incident[0]) + (circ_point[1]*incident[1])

            magnitude1 = math.sqrt(circ_point[0]**2 + circ_point[1]**2)
            magnitude2 = math.sqrt(incident[0]**2 + incident[1]**2) 

            ang = dot / (magnitude1 * magnitude2)

            main_ang = math.acos(ang)


            Theta = main_ang

            if p2[0] < 0 and p2[1] > 0:    #second
                if incident[1] >= incident[0]:
                    Theta = float(-Theta)
                else:
                    Theta = float(-Theta)

            elif p2[0] > 0 and p2[1] > 0:   #first
                if incident[1] >= incident[0]:
                    Theta = float(-Theta)
                else:
                    Theta = float(Theta)
            
            elif p2[0] > 0 and p2[1] < 0:
                if incident[1] <= -incident[0]:   #fourth
                    Theta = float(Theta)
                else:
                    Theta = float(-Theta)

            elif p2[0] < 0 and p2[1] < 0:
                if incident[1] <= incident[0]:
                    Theta = float(-Theta)
                else:
                    Theta = float(Theta)

            else:
                Theta = float(Theta)

            

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
            randomWalk_x_B.append(circ_point[0])
            randomWalk_y_B.append(circ_point[1])
            

            distance_from_origin = math.sqrt((final[0])**2 + (final[1])**2)

            if distance_from_origin >= Radius:
                flag_B_ref = True
                break
            else:
                randomWalk_x_B.append(final[0])
                randomWalk_y_B.append(final[1])



            step_addition_B += 1
            flag_B_ref = True
            break



        if flag_A_ref:
            pass
        else:
            randomWalk_x_A.append(new_x_A)
            randomWalk_y_A.append(new_y_A)  

        if flag_B_ref:
            pass
        else:
            randomWalk_x_B.append(new_x_B)
            randomWalk_y_B.append(new_y_B)    
        

        flag_A_ref = False
        flag_B_ref = False

        steps+=1

        curr_A = (randomWalk_x_A[-1], randomWalk_y_A[-1])
        curr_B = (randomWalk_x_B[-1], randomWalk_y_B[-1])

        dist_between_particles = math.sqrt((curr_B[0] - curr_A[0])**2 + (curr_B[1] - curr_A[1])**2)

        if dist_between_particles <= 1:
            return steps
            break



    return steps
    
    #size = size + step_addition


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

    plt.plot(randomWalk_x_A, randomWalk_y_A)
    plt.plot(randomWalk_x_B, randomWalk_y_B)



    plt.show()



simulations = 200
results = []

for i in range(simulations):
    results.append(circular_random_walk)
