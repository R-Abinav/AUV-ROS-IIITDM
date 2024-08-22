#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received message on t2: %s", data.data)

def subscriber():
    rospy.init_node('subscriber2', anonymous=True)
    rospy.Subscriber('t2', String, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber()
