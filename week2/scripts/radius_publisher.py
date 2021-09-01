#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
def radius():
    rospy.init_node('radius_publisher',anonymous=True)
    pub=rospy.Publisher('radius',Float64,queue_size=10)
    rate=rospy.Rate(10)
    radius=Float64()
    
    while not rospy.is_shutdown():
        radius=1.0
        pub.publish(radius)
        rospy.loginfo(radius)
        rate.sleep()

if __name__=='__main__':
    try:
        radius()
    except rospy.ROSInterruptException():
        pass

