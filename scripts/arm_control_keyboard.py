
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import sys
import termios
import tty

JOINT_LIMIT = 0.35
STEP = 0.05 

def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def move_arms_keyboard():
    rospy.init_node("arm_control_keyboard", anonymous=True)
    # Publisher cho 2 joints của arm
    arm_joint_1_pub = rospy.Publisher("/arm_1_joint_controller/command", Float64, queue_size=10)
    arm_joint_2_pub = rospy.Publisher("/arm_2_joint_controller/command", Float64, queue_size=10)
    rospy.sleep(1)

    # Bien luu trang thai cua 2 goc
    joint_1_angle = 0.0
    joint_2_angle = 0.0

    print("===== Key control =====")
    print("Nhan a va d de dieu khien Joint 1 ")
    print("Nhan q va e de dieu khien Joint 2 ")
    print("Nhan 's' de shutdown")

    while not rospy.is_shutdown():
        key = get_key()
        if key == 'a':  
            joint_1_angle = max(joint_1_angle - STEP, -JOINT_LIMIT)
            rospy.loginfo(f"Joint 1: {joint_1_angle:.2f}")
            arm_joint_1_pub.publish(joint_1_angle)

        elif key == 'd':  
            joint_1_angle = min(joint_1_angle + STEP, JOINT_LIMIT)
            rospy.loginfo(f"Joint 1: {joint_1_angle:.2f}")
            arm_joint_1_pub.publish(joint_1_angle)

        elif key == 'q':  
            joint_2_angle = max(joint_2_angle - STEP, -JOINT_LIMIT)
            rospy.loginfo(f"Joint 2: {joint_2_angle:.2f}")
            arm_joint_2_pub.publish(joint_2_angle)

        elif key == 'e':  
            joint_2_angle = min(joint_2_angle + STEP, JOINT_LIMIT)
            rospy.loginfo(f"Joint 2: {joint_2_angle:.2f}")
            arm_joint_2_pub.publish(joint_2_angle)

        elif key == 's':  
            print("Shutdown")
            break

        rospy.sleep(0.1)

if __name__ == "__main__":
    try:
        move_arms_keyboard()
    except rospy.ROSInterruptException:
        pass
