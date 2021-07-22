#!/usr/bin/env python
import rospy
from std_msgs.msg import String
rospy.init_node('/listener',anonymous=True)
class add():
    def __init__(self):
        self.addition=String()
        self.subs_msg1=rospy.Subscriber('/hello',String,self.callback1)
        self.subs_msg2=rospy.Subscriber('/World',String,self.callback2)
    def callback1(self,msg1):
        self.addition.data=msg1.data
    def callback2(self,msg2):
        self.addition.data=self.addition.data+msg2.data
addition_object=add()
publisher=rospy.Publisher('/helloworld',String,queue_size=10)
rate=rospy.Rate(10)
while not rospy.is_shutdown():
    publisher.publish(addition_object.addition)
    print("Published message is: ",addition_object.addition)
    rate.sleep()



