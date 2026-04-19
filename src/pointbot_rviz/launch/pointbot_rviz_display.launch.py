from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from perception.zed_transform import get_transform
import math

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

	transform = get_transform()
	x = transform[0][3]
	y = transform[1][3]
	z = transform[2][3]
	roll = 0
	pitch = 0
	yaw = 0

	if (transform[2][0] != -1 and transform[2][0] != 1):   
		roll = -math.asin(transform[2][0])
		cos_roll = math.cos(roll)
		pitch = math.atan2(transform[2][1] / cos_roll, transform[2][2] / cos_roll)
		yaw = math.atan2(transform[1][0] / cos_roll, transform[0][0] / cos_roll)
	else:
		if (transform[2][0] == -1):
			roll = math.pi / 2
			yaw = math.atant2(transform[0][1], transform[0][2])
		else:
			roll = -math.pi / 2
			yaw = math.atant2(-transform[0][1], -transform[0][2])

	static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_transform_publisher',
        output='screen',
        arguments=["--x", x, "--y", y, "--z", z, "--roll", roll, "--pitch", pitch, "--yaw", yaw, "--frame-id", "base_link", "--child-frame-id", "zed_camera_link"],
    )

	return LaunchDescription([
		realmove,
		static_tf
	])