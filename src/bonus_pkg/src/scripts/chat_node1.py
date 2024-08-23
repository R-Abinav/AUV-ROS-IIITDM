#!/usr/bin/env python3

import rospy
from bonus_pkg.msg import node1  
from bonus_pkg.msg import node2   

def callback(msg):
    rospy.loginfo(f"Node1 received: {msg.data2}")

def node1():
    rospy.init_node('node1', anonymous=True)

    pub = rospy.Publisher('chat', node1, queue_size=10)
    rospy.Subscriber('chat', node2, callback)

    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        msg = node1()
        msg.data1 = input("Node 1 is getting input")
        rospy.loginfo("Node1 is sending: " + msg.data1)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        node1()
    except rospy.ROSInterruptException:
        pass
