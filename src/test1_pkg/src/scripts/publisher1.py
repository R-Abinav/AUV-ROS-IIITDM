#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('t1', String, queue_size=10)
    rospy.init_node('publisher1', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        msg = input("Enter a message for topic t1: ")
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
