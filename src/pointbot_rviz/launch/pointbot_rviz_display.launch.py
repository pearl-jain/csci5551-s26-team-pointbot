import numpy as np
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from perception.zed_transform import get_transform
from scipy.spatial.transform import Rotation as R

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

	zed_cam = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('zed_wrapper'), 'launch', 'zed_camera.launch.py'])),
		launch_arguments={
			'camera_model': 'zed2i',
			'publish_tf': 'false',
			'publish_map_tf': 'false',
			'base_frame': 'zed_camera_center'
		}.items(),
	)

	transform_camera_world = get_transform()
	transform_world_camera = np.linalg.inv(transform_camera_world)
	x = transform_world_camera[0][3]
	y = transform_world_camera[1][3]
	z = transform_world_camera[2][3]
	r = R.from_matrix(transform_world_camera[:3, :3])
	quat = r.as_quat()

	return LaunchDescription([
		realmove,
		zed_cam,
		Node(
			package='tf2_ros',
			executable='static_transform_publisher',
			arguments=['0', '0', '0', '0', '0', '0', 'world', 'link_base']
		),
		Node(
			package='tf2_ros',
			executable='static_transform_publisher',
			arguments=[str(x), str(y), str(z), str(quat[0]), str(quat[1]), str(quat[2]), str(quat[3]), 'world', 'zed_camera_link']
		)
	])
