from launch import LaunchDescription
from launch_ros.actions import Node

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