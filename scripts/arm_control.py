#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import time

def move_arms():
    rospy.init_node("arm_control", anonymous=True)
    # Publisher cho 2 joints cua arm 
    arm_joint_1_pub = rospy.Publisher("/arm_1_joint_controller/command", Float64, queue_size=10)
    arm_joint_2_pub = rospy.Publisher("/arm_2_joint_controller/command", Float64, queue_size=10)
    time.sleep(1)  
    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():
        #  -0.35 và 0.35 do limit trong urdf -> lower : -0.35 rad; upper: 0.35 rad
        rospy.loginfo("Di chuyen 2 khop ra sau")
        arm_joint_1_pub.publish(-0.35)
        time.sleep(1)
        arm_joint_2_pub.publish(-0.35)
        time.sleep(1)

        rospy.loginfo("Di chuyen 2 khop len phia truoc")
        arm_joint_1_pub.publish(0.35)
        time.sleep(1)
        arm_joint_2_pub.publish(0.35)
        time.sleep(1)

        rate.sleep()

if __name__ == "__main__":
    try:
        move_arms()
    except rospy.ROSInterruptException:
        pass

