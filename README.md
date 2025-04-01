# Mô phỏng Mecanum car Robot with arm trên ROS và Rviz

## Giới thiệu 
Mô phỏng và điều khiển Robot mecanum bốn bánh xe có khả năng di chuyển linh hoạt và trên thân xe có một tay máy với hai góc khớp quay. Robot này được tích hợp thêm các cảm biến Camera, Imu, Lidar để thu thập và hiển thị dữ liệu trong môi trường Gazebo và Rviz

## Yêu cầu
- Sử dụng Ros1 với phiên bản hỗ trợ ROS Noetic
- Có Gazebo và Rviz

## Cài đặt

### Bước 1: Tạo workspace và môi trường
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Bước 2: Clone github vào src
```bash
cd src
git clone https://github.com/mDoanzz43/Ros_project.git
```

## Chạy chương trình điều khiển Robot
### Chạy roslaunch để hiển thị robot trong môi trường Rviz và Gazebo
``` bash
roslaunch robot_model_final control.py
```
Kết quả:


### Chạy Node điều khiển tay máy (2 Node)
``` bash
rosrun robot_model_final arm_control.py
```

Hoặc điều khiển tay máy bằng keyboard

``` bash
rosrun robot_model_final arm_control_keyboard.py
```
Nhấn phím "a, d, q, e, s" để điều khiển
### Chạy Node điều khiển xe mecanum
``` bash
rosrun robot_model_final mecanum_control.py
```
Ấn các phím "w,x,a,d,s" để di chuyển xe

## Chạy chuong trình hiển thị giữ liệu
### Hiển thị dữ liệu từ imu
``` bash
rosrun robot_model_final imu.py
```

hoặc

``` bash
rostopic echo /imu
```

### Hiển thị dữ liệu từ Camera
``` bash
rqt_image_view
```

### Hiển thị dữ liệu từ Lidar
``` bash
 rostopic echo /lidar/scan
```
