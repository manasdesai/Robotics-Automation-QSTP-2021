#!/usr/bin/env python
from __future__ import print_function
from std_msgs.msg import *
from geometry_msgs.msg import *

import sys
import rospy
from ros_automation.srv import Ang_vel,Ang_velResponse
def handle_Ang_vel(req):
    resp=Ang_velResponse(0.1/req.radius)
    print(resp)
    return resp
def return_Ang_vel_server():
    rospy.init_node('compute_ang_vel',anonymous=True)
    server=rospy.Service('compute_ang_vel',Ang_vel,handle_Ang_vel)
    print('Returning the angular velocity')
    rospy.spin()
if __name__=='__main__':
    return_Ang_vel_server()
