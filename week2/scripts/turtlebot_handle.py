#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
from week2.srv import velocity, velocityResponse
from geometry_msgs.msg import Twist


class ServiceClient:

    def __init__(self, service, req):
        self.service = service
        self.req = req
        
        rospy.wait_for_service(service)
        try:
            self.get_resp_func = rospy.ServiceProxy(self.service, self.req)
        except rospy.ServiceException as e:
            rospy.logerror("Service not Found")

    def get_resp(self, query):
        self.resp = self.get_resp_func(query)
        return self.resp
    

class TurtlebotHandle:

    def __init__(self):
        self.sub = rospy.Subscriber('/radius', Float64, self.sub_callback)
        self.client = ServiceClient('compute_ang_vel', velocity)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.lin_vel = 1

        rospy.init_node('turtlebot_handle_node')
        rospy.spin()

    def sub_callback(self, radius):
        self.radius = radius.data
        self.ang_vel = self.client.get_resp(self.radius).ang_vel
        twist = Twist()
        twist.linear.x = self.lin_vel
        twist.angular.z = self.ang_vel

        self.pub.publish(twist)

if __name__ == "__main__":
    TurtlebotHandle()