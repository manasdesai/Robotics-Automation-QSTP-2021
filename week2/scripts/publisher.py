#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub=rospy.Publisher('hello',String,queue_size=10)
    rospy.init_node('publish',anonymous=True)
    
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish('hello')
        publishstring='Hello is being published'
        rospy.loginfo(publishstring)
        rate.sleep()
if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass            
