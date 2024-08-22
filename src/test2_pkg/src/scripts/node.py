#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("[%s] Received: %s", rospy.get_name(), data.data)

def node():
    rospy.init_node('node', anonymous=True)
    topic_name = 'chat'
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    rospy.Subscriber(topic_name, String, callback)
    
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        msg = input("Enter a message: ")
        rospy.loginfo("[%s] Publishing: %s", rospy.get_name(), msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        node()
    except rospy.ROSInterruptException:
        pass
