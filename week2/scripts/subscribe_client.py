#!/usr/bin/env python

from __future__ import print_function
import rospy
from ros_automation.srv import Ang_vel
from std_msgs.msg import *
from geometry_msgs.msg import Twist
rospy.init_node('ang_vel',anonymous=True)

rospy.wait_for_service('compute_ang_vel')
print('Waiting for service')
rate=rospy.Rate(10)
ang_vel=rospy.ServiceProxy('compute_ang_vel',Ang_vel)
velocity=Twist()
def callback(msg):
    velocity.linear.x=0.1
    velocity.linear.y=0
    velocity.linear.z=0
    angular_velocity=ang_vel(msg.data)
    velocity.angular.z=angular_velocity.ang_vel
pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)
sub=rospy.Subscriber('radius',Float64,callback)   
while not rospy.is_shutdown():
    pub.publish(velocity)
    rate.sleep()
