import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[{
                'channel_type':'serial',
                'serial_port': '/dev/serial/by-path/platform-3f980000.usb-usb-0:1.2:1.0-port0',
                'serial_baudrate':115200,
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'
            }]
        )
    ])