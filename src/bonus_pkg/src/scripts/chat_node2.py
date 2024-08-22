#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
	#check if the message is not from this node
	if data._connection_header['callerid']!=rospy.get_name():
		rospy.loginfo("[%s] Received: %s",rospy.get_name(),data.data)

def node2():
	rospy.init_node('chat_node2',anonymous=True)

	pub=rospy.Publisher('chat_bot',String,queue_size=10)
	rospy.Subscriber('chat_bot',String,callback)

	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		msg=input("[%s] Enter a message:" % rospy.get_name())
		rospy.loginfo("[%s] Publishing: %s:",rospy.get_name(),msg)
		pub.publish(msg)
		rate.sleep()

if __name__=="__main__":
	try:
		node2()
	except rospy.ROSInterruptException:
		pass
		
