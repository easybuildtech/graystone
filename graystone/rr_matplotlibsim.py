from graystone.robotics_toolbox import transl, compound, ctraj
from graystone import  rr_config, fkine, ikine
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as anim
import math
from numpy.linalg import inv

#compute robot 
def rTraj(points):
   
    trajectory = list();
    
    base = rr_config.base
    
    numberOfPoints = len(points) - 4

    timestep=100;

    for i in points:
        #transform W points to robot coordinate frame
        
        try:
            T0
        except NameError: 
            T0 = transl(i[0], i[1], 0) * inv(transl(base[0], base[1], 0))
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



base = rr_config.base

fig,ax = plt.subplots()

p1 = [200, 80];
p2 = [300, 20]; 
p3 = [380, 320]; 
p4 = [20, 380]; 
p5 = [380, 380];

points = [p1, p2, p3, p4, p5]

plt.plot(p1[0], p1[1], 'ro')
plt.plot(p2[0], p2[1], 'ro')
plt.plot(p3[0], p3[1], 'ro')
plt.plot(p4[0], p4[1], 'ro')
plt.plot(p5[0], p5[1], 'ro')

plt.axis([0, 400, 0, 400])

#plot robot base
rect = patches.Rectangle((150,150),100,100,linewidth=1,edgecolor='r',facecolor='none')
ax.add_patch(rect)


traj = rTraj(points)
maxI = len(traj)
def simData():
   
    i = 0

    while i < maxI:
        yield traj[i]
        i = i + 1
#print traj
def simPoints(simData):
    #print i[0], i[1]
    point = fkine(simData[0], simData[1]);
    point = point + transl(base[0], base[1], 0);
   # print transl(base[0],base[1],0)
   # print point
    x = point[0,3];
    y = point[1,3];
    #print point
    #print x, y
    return plt.plot(x, y,'g^');

print len(traj)

a = anim.FuncAnimation(fig, simPoints, simData, blit=False, interval=10, repeat = False)
plt.show()
#fig.clear()
