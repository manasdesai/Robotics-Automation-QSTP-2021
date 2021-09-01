#! /usr/bin/env python
from __future__ import print_function
from sys import version
import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import *
from ros_automation.srv import Ang_vel

class Infinite_shape:

    def __init__(self):
        self.s_1 = rospy.Subscriber('odom', Odometry,self.callback1)
        self.s_2 = rospy.Subscriber('radius', Float64, self.callback2)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.dist = 0
        self.prev_x = 0
        self.prev_y = 0
        self.rad = 1.0
        self.count = 1
        self.velocity = Twist()
        self.first_run = True
    
    def callback1(self, msg):

        if(self.first_run):
            self.prev_x = msg.pose.pose.position.x
            self.prev_y = msg.pose.pose.position.y

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        d_increase = math.sqrt((x - self.prev_x)**2 + (y - self.prev_y)**2)
        self.dist = self.dist + d_increase
         #angular_velocity = ang_vel(msg.data)
        self.velocity.linear.x = 0.1

        self.velocity.angular.z = (inif((self.velocity.linear.x)/(self.rad))).ang_vel*(self.count)/10
        self.pub.publish(self.velocity)

        self.prev_x = msg.pose.pose.position.x
        self.prev_y = msg.pose.pose.position.y

        self.first_run = False
        print(self.dist)

        if(self.dist >= 2*math.pi*self.rad):
            self.count = (-1) * self.count
            self.dist = 0
            self.first_run = True
    
    def callback2(self,msg):
        self.rad = msg.data

if __name__ == '__main__':
    rospy.init_node('infinity')
    rospy.wait_for_service('compute_ang_vel')
    inif = rospy.ServiceProxy('compute_ang_vel', Ang_vel)

    bot = Infinite_shape()
    rospy.spin()
