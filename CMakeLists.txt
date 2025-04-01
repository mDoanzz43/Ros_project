cmake_minimum_required(VERSION 2.8.3)

project(robot_model_final)

# find_package(catkin REQUIRED)

catkin_package()
find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	urdf
)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

catkin_install_python(PROGRAMS
  scripts/arm_control.py  
  scripts/arm_control_keyboard.py
  scripts/mecanum_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)