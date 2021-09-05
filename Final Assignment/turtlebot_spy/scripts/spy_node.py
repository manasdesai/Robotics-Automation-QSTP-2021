#!/usr/bin/env python
from os import path
import rospy
import sys
import math
from tf.transformations import euler_from_quaternion
from numpy.core.numeric import roll
from std_msgs.msg import *
from geometry_msgs.msg import Twist,Point,PoseStamped,Pose,Quaternion
from nav_msgs.msg import *

class path():
    def init(self):
        self.sub1=rospy.Subscriber('/thief_pose',PoseStamped,callback)
        self.sub2=rospy.Subscriber('/odom',Odometry,callback2)
        self.pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        self.arr=PoseStamped.poses
        
        self.velocity=Twist()
    

    def callback2(msg):
        orientation_list=[msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w]
        roll,pitch,yaw=euler_from_quaternion(orientation_list)
        self.ang=yaw
        self.x_current=msg.pose.pose.position.x
        self.y_current=msg.pose.pose.position.y

    def callback(msg):
        self.array=msg.poses
        i=0
        while i<len(self.array):
            x_goal=self.array[i].pose.position.x
            y_goal=self.array[i].pose.position.y
            distance=math.sqrt((x_goal-self.x_current),(y_goal-self.y_current))
            theta=math.atan2((y_goal-self.y_current),(x_goal-self.x_current))
            ang_difference=theta-self.ang
            if distance>=0.09 and distance<=1.1:

                if(abs(ang_difference)>0.15):
                    self.velocity.linear.x=0
                    self.velocity.angular.z=0.05*(ang_difference)
                    self.pub.publish(self.velocity)
                else:
                    self.velocity.linear.x=0.06*distance
                    self.velocity.angular.z=0
                    self.pub.publish(self.velocity)
            else:
                i+=1
                
if name=='main':
    rospy.init_node('spy_node')
    rate=rospy.Rate(10)
    move=path()
    rospy.spin()
