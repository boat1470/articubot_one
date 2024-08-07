import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='articubot_one' #<--- CHANGE ME

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')


    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )

    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=['/home/boat1470/finding_robot_ws/src/articubot_one/config/ekf.yaml', {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    )

    # Launch them all!
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        robot_localization_node
        # diff_drive_spawner,
        # joint_broad_spawner
    ])


#ros2 run teleop_twist_keyboard teleop_twist_keyboard  --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped

#ros2 launch slam_toolbox online_async_launch.py params_file:=/home/boat1470/finding_robot_ws/src/articubot_one/config/mapper_params_online_sync.yaml use_sim_time:=true

#rviz2 -d /home/boat1470/finding_robot_ws/src/articubot_one/config/drive_bot.rviz