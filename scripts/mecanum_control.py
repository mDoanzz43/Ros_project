#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import sys
import tty
import termios

class MecanumKeyboardControl:
    def __init__(self):
        rospy.init_node('mecanum_keyboard_control', anonymous=True)
        self.pub_wheel_fl = rospy.Publisher('/wheel_4_joint_controller/command', Float64, queue_size=10)
        self.pub_wheel_fr = rospy.Publisher('/wheel_2_joint_controller/command', Float64, queue_size=10)
        self.pub_wheel_rl = rospy.Publisher('/wheel_3_joint_controller/command', Float64, queue_size=10)
        self.pub_wheel_rr = rospy.Publisher('/wheel_1_joint_controller/command', Float64, queue_size=10)

        # toc do 
        self.max_speed = 1.0  
        self.max_omega = 1.0  

        # Chieu dai, rong, bk banh xe
        self.Lx = 0.39  
        self.Ly = 0.27  
        self.wheel_radius = 0.13  

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            key = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key

    def run(self):
        rospy.loginfo("Mecanum Robot Keyboard Control: w/x (Tien/Lui), a/d (Xoay quanh truc), s (stop)")
        
        while not rospy.is_shutdown():
            key = self.get_key()
            
            vx, vy, omega = 0.0, 0.0, 0.0
            
            if key == 'w':  # Tien
                vx = -self.max_speed
            elif key == 'x':  # Lui
                vx = self.max_speed
            elif key == 'a':  # Xoay quanh truc tu trai qua phai
                omega = -self.max_omega
            elif key == 'd':  # Xoay quanh truc tu phai qua trai
                omega = self.max_omega
            elif key == 's':  # Stop
                vx, vy, omega = 0.0, 0.0, 0.0
            elif key == '\x03':  
                break

            # Vtoc banh xe dua vao dong hoc thuan
            v_fl = (1 / self.wheel_radius) * (vx - vy - (self.Lx + self.Ly) * omega)
            v_fr = (1 / self.wheel_radius) * (vx + vy + (self.Lx + self.Ly) * omega)
            v_rl = (1 / self.wheel_radius) * (vx + vy - (self.Lx + self.Ly) * omega)
            v_rr = (1 / self.wheel_radius) * (vx - vy + (self.Lx + self.Ly) * omega)

            self.pub_wheel_fl.publish(v_fl)
            self.pub_wheel_fr.publish(v_fr)
            self.pub_wheel_rl.publish(v_rl)
            self.pub_wheel_rr.publish(v_rr)

            rospy.loginfo(f"FL: {v_fl:.2f}, FR: {v_fr:.2f}, RL: {v_rl:.2f}, RR: {v_rr:.2f}")
            rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        controller = MecanumKeyboardControl()
        controller.run()
    except rospy.ROSInterruptException:
        pass

