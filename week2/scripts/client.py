#!/usr/bin/env python
from __future__ import print_function

import rospy
from week2.srv import *
import numpy as np
import matplotlib.pyplot as plt
def return_poses(x: float,y: float,theta: float,v: float,w: float):
    rospy.wait_for_service('return_poses')
    try:
        return_poses=rospy.ServiceProxy('return_poses',ReturnPoses)
        resp=return_poses(x,y,theta,v,w)
        x_points=resp.x_poses
        y_points=resp.y_poses





    
    

       
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.figure()
        plt.title("Unicycle Model")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(x_points, y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()

    except rospy.ServiceException as e:

        print("Service Not found")
def main():
    return_poses(0,0,0,1,0.5)
    
    
    






if __name__=='__main__':
    main()    
