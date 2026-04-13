from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='perception',
            executable='perception_action_server',
        ),
        Node(
            package='planning',
            executable='planning_action_server',
        ),
        Node(
            package='control',
            executable='control_tree',
        )
    ])