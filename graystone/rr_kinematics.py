import numpy as np
import math
import robotics_toolbox.transform as t
import rr_config

a1 = config_rr.a1
a2 = config_rr.a2

def ikine(x,y,z=0):

    q2 = math.acos((x**2 + y**2 - a1**2 - a2**2)/(2 * a1 * a2));
    q1 = math.atan2(y,x) - math.atan2((a2 * math.sin(q2)), (a1 + a2 * math.cos(q2)));

    return q1, q2


def fkine(q1, q2):

    #q1 = math.radians(q1)
    #q2 = math.radians(q2)
    
    #T = grt.compound([grt.trotx(q1),grt.transl(150,0,0),grt.trotx(q2),grt.transl(117,0,0)]);
    T = t.trotz(q1) * t.transl(150,0,0) * t.trotz(q2) * t.transl(117,0,0);
    
    #T = grt.trotz(q1)* grt.trotz(q2)
    #print T
    
    return T