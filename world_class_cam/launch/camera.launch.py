import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description(): 
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('world_class_cam'),
        'param',
        'all.yaml')
        )
    
    return LaunchDescription(
        [
            DeclareLaunchArgument( 
                'param_dir',
                default_value=param_dir
            ),

            Node(
                package='world_class_cam',
                executable='img_publisher',
                name='img_publisher',
                parameters=[param_dir],
                output='screen'),
        ]
    )
