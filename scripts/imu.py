#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu

def imu_callback(msg):
    rospy.loginfo(f"Orientation: x={msg.orientation.x}, y={msg.orientation.y}, z={msg.orientation.z}, w={msg.orientation.w}")
    rospy.loginfo(f"Angular Velocity: x={msg.angular_velocity.x}, y={msg.angular_velocity.y}, z={msg.angular_velocity.z}")
    rospy.loginfo(f"Linear Acceleration: x={msg.linear_acceleration.x}, y={msg.linear_acceleration.y}, z={msg.linear_acceleration.z}")

def imu_listener():
    rospy.init_node('imu_listener', anonymous=True)
    rospy.Subscriber('/imu', Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    imu_listener()
