from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('pointbot_rviz'),
        #                                                       'launch',
        #                                                       'pointbot_rviz_display.launch.py']))
        # ),
        Node(
            package='perception',
            executable='perception_action_server',
            output='screen'
        ),
        Node(
            package='planning',
            executable='planning_action_server',
            output='screen'
        ),
        Node(
            package='control',
            executable='control_tree',
            output='screen'
        )
    ])