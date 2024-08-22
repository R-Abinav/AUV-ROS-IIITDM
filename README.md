# AUV-ROS-IIITDM
This repo contains all the required files for the hw from the AUV session on ROS. 
Q1 -> (test1_pkg) : It is just a basic script , where we have 2 publishers and 2 subscribers.
Q2 -> (test2_pkg) : It is a script where we have only one node , which is both a publisher and a subscriber ( subscribed to itself ). On running the node using rosrun (run the code on the two different terminals) whatever message we type, we get the response (from the same program).
Q3 -> (bonus_pkg) : Exactly similar to Q2, but we have 2 nodes and the catch is that the subscriber (subscribed to itself) shouldn't display the message from the publisher which is itself.

