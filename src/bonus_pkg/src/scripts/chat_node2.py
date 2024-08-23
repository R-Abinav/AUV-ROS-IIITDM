#!/usr/bin/env python3

import rospy
from bonus_pkg.msg import node1  
from bonus_pkg.msg import node2

def callback(msg):
    rospy.loginfo(f"Node2 received: {msg.data1}")

def node1():
    rospy.init_node('node2', anonymous=True)

    pub = rospy.Publisher('chat', node2, queue_size=10)
    rospy.Subscriber('chat', node1, callback)

    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        msg = node2()
        msg.message2 = input("Node 2 getting input")
        rospy.loginfo("Node2 sending: " + msg.data2)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass

		
