from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

from perception.zed_transform import get_transform
from scipy.spatial.transform import Rotation as R

def generate_launch_description():

    zed_cam = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('zed_wrapper'), 'launch', 'zed_camera.launch.py'])),
		launch_arguments={
			'camera_model': 'zed2i',
			'publish_tf': 'false',           # Stop ZED from publishing odom -> base
			'publish_map_tf': 'false',       # Stop ZED from publishing map -> odom
			'base_frame': 'zed_camera_center' # Ensure the ZED knows its root
    	}.items(),
    )

    return LaunchDescription([
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('pointbot_rviz'),
        #                                                       'launch',
        #                                                       'pointbot_rviz_display.launch.py']))
        # ),
        zed_cam,
        Node(
            package='perception',
            executable='perception_action_server',
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0', '0', '0', '0', '0', '0', 'world', 'link_base']
        ),
        # Node(
        #     package='tf2_ros',
        #     executable='static_transform_publisher',
        #     arguments=[str(x), str(y), str(z), str(quat[0]), str(quat[1]), str(quat[2]), str(quat[3]), 'world', 'zed_camera_link']
        # ),
    ])