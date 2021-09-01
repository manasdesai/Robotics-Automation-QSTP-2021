#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def circle():
    rospy.init_node('circle',anonymous=True)
    pub=rospy.Publisher('cmd_vel',Twist,queue_size=10)
    move_command=Twist()
    move_command.linear.x=0.1
    move_command.linear.y=0
    move_command.angular.z=0.5
    now=rospy.Time.now()
    while rospy.Time.now() < now+rospy.Duration.from_sec(6):
        pub.publish(move_command)
        rate.sleep()
if __name__=='__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
