import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    # Starts my planning node
    planning_node = Node(
        package='lite_6_planner',
        executable='planner',
        name='planner',
        output='screen',
    )

    return LaunchDescription([
        planning_node,
    ])