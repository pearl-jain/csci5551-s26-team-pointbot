from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    lite6_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([
            FindPackageShare('xarm_moveit_config'), 'launch', 'lite6_moveit_fake.launch.py'
        ])),
        launch_arguments={
            'rviz_config': PathJoinSubstitution([FindPackageShare('pointbot_rviz'), 'rviz', 'pointbot.rviz']),
            'hw_ns': 'ufactory',
            'add_gripper': 'true',
            'dof': '6',
            'robot_type': 'lite',
            'no_gui_ctrl': 'false'
        }.items(),
    )

    test_visualizer = Node(
        package='pointbot_rviz',
        executable='test_visualizer'
    )

    return LaunchDescription([
        lite6_launch,
        test_visualizer,
    ])