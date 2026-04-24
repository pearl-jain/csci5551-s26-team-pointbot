from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='perception',
            executable='perception_action_server',
            output='screen'
        ),
        Node(
            package='planning',
            executable='planning_action_server',
            name='path_planner',
            output='screen',
            parameters=[
                robot_description,           # The URDF string
                robot_description_semantic,  # The SRDF string
                robot_description_kinematics,# Kinematics yaml
                {'use_sim_time': False}
            ]
        ),
        Node(
            package='control',
            executable='control_tree',
            output='screen'
        )
    ])