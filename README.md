# Mô phỏng Mecanum car Robot with arm trên ROS và Rviz

## Giới thiệu 
Mô phỏng và điều khiển Robot mecanum bốn bánh xe có khả năng di chuyển linh hoạt và trên thân xe có một tay máy với hai góc khớp quay. Robot này được tích hợp thêm các cảm biến Camera, Imu, Lidar để thu thập và hiển thị dữ liệu trong môi trường Gazebo và Rviz

## Yêu cầu
- Sử dụng Ros1 với phiên bản hỗ trợ ROS Noetic
- Có Gazebo và Rviz
- ⚠️ Có thể cần cài đặt gói này nếu không có velocity_controllers/JointVelocityController: sudo apt-get install ros-noetic-ros-control ros-noetic-ros-controllers

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
roslaunch robot_model_final control.launch
```
Kết quả:
![image](https://github.com/user-attachments/assets/0c6bf812-9f3e-440c-89ad-48933ffb2ba2)


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


## Chạy chương trình để theo dõi dữ liệu
### Hiển thị dữ liệu từ imu
``` bash
rosrun robot_model_final imu.py
```
![image](https://github.com/user-attachments/assets/bca98df8-0593-4e78-bca6-b666758eb8de)

Hoặc

``` bash
rostopic echo /imu
```
⚠️ Vào màn hình của cửa sổ rviz -> tick vào topic imu -> Chỉnh hệ số alpha nhỏ xuống để theo dõi trục

### Hiển thị dữ liệu từ Camera
``` bash
rqt_image_view
```
![image](https://github.com/user-attachments/assets/e36abf3f-c1b7-44c3-85ef-0a03050267fc)


### Hiển thị dữ liệu từ Lidar
``` bash
 rostopic echo /lidar/scan
```
![image](https://github.com/user-attachments/assets/295a4a25-c703-47c9-84b7-20bd0258860d)


## Em có nhờ bạn gitclone về để xem có được không nhưng mà bị lỗi không spawn ra gazebo. Nếu anh cũng bị thì anh xem video này hộ em nha anh, em xin lỗi vì sự bất tiện này ạ
https://youtu.be/TWkJFdkjOTs
