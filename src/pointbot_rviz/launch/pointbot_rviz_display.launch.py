from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from perception.zed_transform import get_transform

import numpy as np
from scipy.spatial.transform import Rotation as R

import math

def generate_launch_description():
	robot_ip = LaunchConfiguration('robot_ip', default='192.168.1.155')
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

	# zed_cam = IncludeLaunchDescription(
	# 	PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('zed_wrapper'), 'launch', 'zed_camera.launch.py'])),
	# 	launch_arguments={
	# 		'camera_model': 'zed2i',
	# 		'publish_tf': 'false',           # Stop ZED from publishing odom -> base
	# 		'publish_map_tf': 'false',       # Stop ZED from publishing map -> odom
	# 		'base_frame': 'zed_camera_center' # Ensure the ZED knows its root
	# 	}.items(),
	# )

	# transform = get_transform()

	# x = transform[0][3]
	# y = transform[1][3]
	# z = transform[2][3]
	# roll = 0
	# pitch = 0
	# yaw = 0

	# if (transform[2][0] != -1 and transform[2][0] != 1):   
	# 	roll = -math.asin(transform[2][0])
	# 	cos_roll = math.cos(roll)
	# 	pitch = math.atan2(transform[2][1] / cos_roll, transform[2][2] / cos_roll)
	# 	yaw = math.atan2(transform[1][0] / cos_roll, transform[0][0] / cos_roll)
	# else:
	# 	if (transform[2][0] == -1):
	# 		roll = math.pi / 2
	# 		yaw = math.atan2(transform[0][1], transform[0][2])
	# 	else:
	# 		roll = -math.pi / 2
	# 		yaw = math.atan2(-transform[0][1], -transform[0][2])

	# r = R.from_matrix(transform[:3, :3])

	# quat = r.as_quat()

	return LaunchDescription([
		realmove,
		# zed_cam
		# static_tf,
		# Node(
		# 	package='tf2_ros',
		# 	executable='static_transform_publisher',
		# 	arguments=[str(x), str(y), str(z), str(roll), str(pitch), str(yaw), 'world', 'zed_camera_link']
		# )
	])