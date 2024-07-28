## Robot Package Template

This is a GitHub template. You can make your own copy by clicking the green "Use this template" button.

It is recommended that you keep the repo/package name the same, but if you do change it, ensure you do a "Find all" using your IDE (or the built-in GitHub IDE by hitting the `.` key) and rename all instances of `articubot_one` to whatever your project's name is.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).


command

#Build robot 

ros2 launch articubot_one launch_sim.launch.py world:=/home/boat1470/finding_robot_ws/src/articubot_one/worlds/completition.world 
 
#tele 1

ros2 run teleop_twist_keyboard teleop_twist_keyboard  --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

#rviz2 

rviz2 -d /home/boat1470/finding_robot_ws/src/articubot_one/config/drive_bot.rviz 

#slam

ros2 launch slam_toolbox online_async_launch.py slam_params_file:=/home/boat1470/finding_robot_ws/src/articubot_one/config/mapper_params_online_sync.yaml use_sim_time:=true



sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*

ros2 run nav2_map_server map_server --ros-args -p yaml_filename:=/home/boat1470/my_map_save.yaml -p use_sim_time:=true

ros2 run nav2_util lifecycle_bringup map_server

ros2 run nav2_amcl amcl -ros-args -p use_sim_time:=true

ros2 run nav2_util lifecycle_bringup amcl

sudo apt install ros-humble-twist-mux


#tele 2

ros2 run twist_mux twist_mux --ros-args --params-file /home/boat1470/finding_robot_ws/src/articubot_one/config/twist_mux.yaml -r cmd_vel_out:=diff_cont/cmd_vel_unstamped

ros2 run teleop_twist_keyboard teleop_twist_keyboard  --ros-args -r /cmd_vel:=/cmd_vel_keyboard

ros2 launch nav2_bringup navigation_launch.py use_sim_time:=true



#lidar

ros2 run rplidar_ros rplidar_composition --ros-args -p channel_type:=serial -p serial_port:=/dev/ttyUSB1 -p serial_baudrate:=115200 -p frame_id:=laser_frame -p angle_compensate:=true -p scan_mode:=Standard





###########################
for nav2

ros2 run teleop_twist_keyboard teleop_twist_keyboard  --ros-args -r /cmd_vel:=cmd_vel_keyboard
ros2 run tf2_tools view_frames.py

ros2 launch nav2_bringup navigation_launch.py params_file:=/home/boat1470/finding_robot_ws/src/articubot_one/config/nav2_params.yaml

ros2 run twist_mux twist_mux --ros-args --params-file /home/boat1470/finding_robot_ws/src/articubot_one/config/twist_mux.yaml -r cmd_vel_out:=/demo/cmd_vel
#################################



In raspberry pi

ros2 run serial_motor_demo driver --ros-args -p serial_port:=/dev/ttyUSB0 -p buad_rate:=57600 -p loop_rate:=30 -p encoder_cpr:=1443

ros2 launch articubot_one launch_robot.launch.py

ros2 launch articubot_one rplidar.launch.py

ros2 service call /stop_motor std_srvs/srv/Empty "{}"
ros2 service call /start_motor std_srvs/srv/Empty "{}"

python3 -m serial.tools.miniterm /dev/ttyUSB0 57600

journalctl -fe



In dev
rviz2 -d /home/boat1470/finding_robot_ws/src/articubot_one/config/real_bot.rviz 

ros2 run teleop_twist_keyboard teleop_twist_keyboard  --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

ros2 node list
