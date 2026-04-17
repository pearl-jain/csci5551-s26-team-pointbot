from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
	robot_ip = LaunchConfiguration('robot_ip', default='')
	realmove = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('xarm_moveit_config'), 'launch', '_robot_moveit_realmove.launch.py'])),
		launch_arguments={
			'robot_ip': robot_ip,
			'dof': '6',
			'robot_type': 'lite',
			'hw_ns': 'ufactory',
			'no_gui_ctrl': 'false',
			'rviz_config': PathJoinSubstitution([FindPackageShare('pointbot_rviz'), 'rviz', 'pointbot.rviz']),
			'add_gripper': 'true',
		}.items(),
	)

	static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_transform_publisher',
        output='screen',
        arguments=["--x", "0.5461", "--y", "0.0", "--z", "0.437896", "--pitch", "0.7854", "--frame-id", "base_link", "--child-frame-id", "zed_camera_link"],
    )

	return LaunchDescription([
		realmove,
		static_tf
	])