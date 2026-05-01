from launch import LaunchDescription
from launch.actions import RegisterEventHandler, EmitEvent
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit
from launch.events import Shutdown

def generate_launch_description():
    rviz2_params = PathJoinSubstitution([FindPackageShare('pointbot_rviz'), 'rviz', 'pointbot.rviz'])
    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz2_params],
        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static'),
        ]
    )
    
    return LaunchDescription([
        RegisterEventHandler(event_handler=OnProcessExit(
            target_action=rviz2_node,
            on_exit=[EmitEvent(event=Shutdown())]
        )),
        rviz2_node
    ])