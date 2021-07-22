#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

def main():
    radius_pub = rospy.Publisher('radius', Float64, queue_size=10)

    rospy.init_node('radius_pub_node', anonymous=True)
    loop_rate = rospy.Rate(5)
    radius = 1.0
    PI = math.pi
    angular_speed = 1.0
    distance = 2*PI*radius

    current_distance = 0

    # while not rospy.is_shutdown():

    # t0 = rospy.Time.now().to_sec() # Start Time
    for i in range(2):
        current_distance = 0        
        t0 = rospy.Time.now().to_sec() # Start Time
        
        while current_distance < distance:
            t1 = rospy.Time.now().to_sec() # Current time
            t = t1 - t0  # Time valuetracker
            current_distance = angular_speed*t*abs(radius) # distance = Radius*angular_speed*time
            msg1 = Float64(radius)
            
            rospy.loginfo("Publishing: ")
            rospy.loginfo(msg1)
            radius_pub.publish(msg1)
        
        radius = -radius

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass