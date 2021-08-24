#!/usr/bin/env python3

from os import path
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import *
from std_msgs.msg import *
import sys
import math
from tf.transformations import euler_from_quaternion

class plot :
    def __init__(self):
        self.sub1 = rospy.Subscriber('path1', Path, self.call1)
        self.sub2 = rospy.Subscriber('odom', Odometry , self.call2)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.kp =1
        self.vel= Twist()
        self.arr = Path.poses
        self.ang =0.0

    def call1(self, msg):
        self.arr = msg.poses
        x_2 = self.arr[1].pose.position.x
        y_2 = self.arr[1].pose.position.y
        x_1 = self.arr[0].pose.position.x
        y_1 = self.arr[0].pose.position.y
        theta_2 = math.atan2((y_2 - y_1),(x_2 - x_1))
        print(theta_2)

        distance = math.sqrt((x_2 - self.x_in)**2 + (y_2 - self.y_in)**2)
        
        #if(distance <= 3):
        self.vel.angular.z = self.kp * (abs(theta_2 - self.ang))
        self.vel.linear.x = 0.2
        self.pub.publish(self.vel)
        print(distance)

        if(distance > 0.0 and distance < 0.05):
            self.vel.linear.x = 0
            self.vel.angular.z = 0
            self.pub.publish(self.vel)

        

    def call2(self,msg):
        orientation_list = [msg.pose.pose.orientation.x , msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w ]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.x_in = msg.pose.pose.position.x 
        self.y_in = msg.pose.pose.position.y

if __name__ == '__main__':
    rospy.init_node("path_subscriber")
    rate = rospy.Rate(5)

    
    move =  plot()

    rospy.spin()
