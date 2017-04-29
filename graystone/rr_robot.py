#!/usr/bin/env python
import rospy
from arbotix_python.arbotix import ArbotiX
import serial, time, sys, thread
from ax12 import *
from struct import unpack
import rr_trajectory
from rr_kinematics import fkine
from operator import add

class Robot(ArbotiX):

    def __init__(self, port="/dev/ttyUSB0", baud=115200):
        # start
        ArbotiX.__init__(self, port, baud)

        q1 = self.getPosition(int(1))
        q2 = self.getPosition(int(2))

        if q1 == -1 or q2 == -1:
        	try:
        		raise ValueError("Position not returned, is ArbotiX Driver running?")
        	except ValueError as err:
        		print err.args
        		sys.exit(1)

        tempr1 = self.getTemperature(int(1))
        tempr2 = self.getTemperature(int(2))

        print "q1 temperature=%s position=%s" % (tempr2, q1)
        print "q2 temperature=%s position=%s " % (tempr1, q2)



if __name__ == "__main__":
    try:
        r = Robot()

        while True:

            userInput = input("Please enter [x, y] points:")

            points = fkine(q1, q2)
            points = [points[0,3], points[1,3]]
            print points
            points2 = [200, 200]

            points = map(add, points, points2)

            points.extend(userInput)

            trajectory = rrTraj(points)

        for t in trajectory:
            r.setPosition(int(1), int(t[0]))
            r.setPosition(int(2), int(t[1]))
            time.sleep(.03)

    except KeyboardInterrupt:
        print "\nExiting..."
