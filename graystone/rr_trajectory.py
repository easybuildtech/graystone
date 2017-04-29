from graystone.robotics_toolbox import transl, compound, ctraj
from graystone import  rr_config, fkine, ikine
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as anim
import math
from numpy.linalg import inv

#get base coordinates in {W}
base = rr_config.base

timestep=100;

#compute robot 
def rrTraj(points):
   
    trajectory = list();
    
    #get total number of points provided
    numberOfPoints = len(points) - 4
  
    for i in points:
        #transform {W} points to robot coordinate frame
        
        try:
            T0
        except NameError: 
            T0 = compound(transl(i[0], i[1], 0), inv(transl(base[0], base[1], 0)))
        else:
            T0 = T1

        next
        T1 = transl(i[0], i[1], 0) * inv(transl(base[0], base[1], 0))
    
        cartesianTrajectory =  ctraj(T0, T1, timestep)

        for i in range(timestep):
            t = cartesianTrajectory[i]
            #print t
            [q1, q2] = ikine(t[0,3], t[1,3])
            trajectory.append([q1, q2])
    
    return trajectory
