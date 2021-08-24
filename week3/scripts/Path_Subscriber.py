#!/usr/bin/env python3

from os import path

from numpy.core.numeric import roll
import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import *
from std_msgs.msg import *
import sys
import math
from tf.transformations import euler_from_quaternion

class plot :
    def __init__(self):
        
        self.sub1 = rospy.Subscriber( sys.argv[1], Path, self.call1)
        self.sub2 = rospy.Subscriber('odom', Odometry, self.call2)
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        self.kp =1
        self.vel = Twist()
        self.arr = Path.poses
        self.run = True

    def call1(self,msg):
        self.arr = msg.poses
        
        i = 0
        while i< len(self.arr):

            x_g = self.arr[i].pose.position.x
            y_g = self.arr[i].pose.position.y
           
            theta2 = math.atan2((y_g - self.y_in),(x_g - self.x_in))
            distance = math.sqrt((x_g - self.x_in)**2 + (y_g - self.y_in)**2)
            print(distance , x_g, y_g, abs(theta2 - self.ang))
            
            

            if (distance >= 0.05):

                if(abs(theta2 - self.ang) > 0.15):
                    self.vel.linear.x =0
                    self.vel.angular.z = 0.06 * ((theta2 - self.ang))
                    self.pub.publish(self.vel)
                    

                else:
                    self.vel.linear.x = 0.08 * distance
                    self.vel.angular.z = 0.0
                    self.pub.publish(self.vel)

            else:
                
                i += 1
                

    def call2(self,msg):
        orientation_list = [msg.pose.pose.orientation.x , msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w ]
        (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
        self.ang = yaw
        self.x_in = msg.pose.pose.position.x
        self.y_in = msg.pose.pose.position.y


if __name__ == '__main__':
    rospy.init_node("path_subscriber")
    rate = rospy.Rate(5)
    move = plot()
    
    

    rospy.spin()
