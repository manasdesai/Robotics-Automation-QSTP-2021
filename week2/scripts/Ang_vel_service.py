#!/usr/bin/env python

import rospy
from week2.srv import velocity, velocityResponse


def handle_rad_req(req):
    return velocityResponse(1/req.radius)


def return_rad():
    rospy.init_node('ang_vel_service_node')
    s = rospy.Service('compute_ang_vel', velocity, handle_rad_req)
    rospy.loginfo('Available for computing Angular Velocity')
    rospy.spin()

if __name__ == "__main__":
    return_rad()