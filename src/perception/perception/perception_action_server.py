import threading
import time
import rclpy
from rclpy.action import ActionServer, CancelResponse
from rclpy.node import Node

from point_bot_interfaces.action import Perception
from sensor_msgs.msg import Image, PointCloud2
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker, MarkerArray

from perception.detect_object_pose import ObjectPoseDetector
from perception.zed_camera import ZedCamera
from perception.zed_transform import get_transform_camera_robot, draw_pose_axes
from perception.pointing_system import PointBot, CUBE_SIZE

from cv_bridge import CvBridge
import cv2
import numpy as np

import tf_transformations

from pointbot_rviz.visualization_helpers import publish_object_markers, publish_pointing_vector_marker, publish_selected_marker, publish_goal_marker

class PerceptionActionServer(Node):
    def __init__(self):
        super().__init__("perception_action_server")
        self._action_server = ActionServer(
            self,
            Perception,
            'perception',
            execute_callback=self.execute_callback,
            cancel_callback=self.handle_cancel)        

        self.zed = ZedCamera()
        
        self.pose_detector = ObjectPoseDetector(self.zed.camera_intrinsic)

        self.t_cube_robot = get_transform_camera_robot(self.zed.image, self.zed.camera_intrinsic)

        self.pointing_system = PointBot(self.zed, self.t_cube_robot, self)

        self.bridge = CvBridge()

        self.object_publisher = self.create_publisher(MarkerArray, '/object_markers', 10)
        self.vector_publisher = self.create_publisher(Marker, '/pointing_vector', 10)
        self.selected_publisher = self.create_publisher(Marker, '/selected_object', 10)
        self.goal_publisher = self.create_publisher(Marker, '/goal_marker', 10)
        self.point_cloud_publisher = self.create_publisher(PointCloud2, '/point_cloud', 10)

        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while True:
            if self.zed.point_cloud is not None:
                point_cloud_msg = self.bridge.cv2_to_imgmsg(self.zed.point_cloud)
                point_cloud_msg.header.frame_id = "world"
                self.point_cloud_publisher.publish(point_cloud_msg)
            else:
                time.sleep(0.01)

    def handle_cancel(self, cancel_request):
        """Handle cancellation requests."""
        self.get_logger().info('Received cancel request')
        # self.pose_detector.cancel()
        return CancelResponse.ACCEPT # Accept the cancellation

    def execute_callback(self, goal_handle):
        task = goal_handle.request.task

        self.get_logger().info(f"Peforming perception task {task}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully

        is_detect_object = (task == "detect_object")

        result = Perception.Result()

        # Define the result message and populate it with the perception results
        raw_image = self.zed.image.copy()
        if raw_image.shape[2] == 4:
            raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGRA2BGR)

        objects = self.pose_detector.detect_cubes(self.zed.image, self.t_cube_robot)

        self.get_logger().info(f"Detected object poses: {len(objects)}")
        
        object_poses = [obj[:3, 3] for obj in objects]

        attention_pose, interaction_type, pointer_position, pointer_direction = self.pointing_system.run(object_poses, is_detect_object)

        self.get_logger().info(f"Attention Pose: {attention_pose}\nInteraction Type: {interaction_type}\nPointer Position: {pointer_position}\nPointer Direction: {pointer_direction}")
        
        if interaction_type == 1: # Pointing
            attention_scores = self.pose_detector.pointing_object_distance_scores(object_poses, pointer_position, pointer_direction)
        else: # Palm
            if is_detect_object:
                result.success = False
                return result
            attention_scores = self.pose_detector.point_object_distance_scores(object_poses, attention_pose)

        if attention_scores is None:
            result.success = False
            return result

        selected = self.pose_detector.select_cube(objects, attention_scores)

        result.image = self.bridge.cv2_to_imgmsg(raw_image, encoding="bgr8")

        result.pose = PoseStamped()
        match task:
            case "detect_object":
                # attention_scores = self.pose_detector.pointing_object_space_scores(object_poses, pointer_position, pointer_direction, 0.02, 0.01)
                self.get_logger().info(f"Selected value: {selected} Type: {type(selected)}")

                q = tf_transformations.quaternion_from_matrix(selected)

                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation.w = q[0]
                result.pose.pose.orientation.x = q[1]
                result.pose.pose.orientation.y = q[2]
                result.pose.pose.orientation.z = q[3]
                result.pose.pose.position.x = selected[0, 3]
                result.pose.pose.position.y = selected[1, 3]
                result.pose.pose.position.z = selected[2, 3]
                result.success = True
                # publish_selected_marker(self.selected_publisher, result.pose)

            case "detect_goal":
                selected_goal = attention_pose + np.array([0, 0, CUBE_SIZE])
    
                if selected is not None:
                    diff = (attention_pose - selected[:3, 3])
                    if np.linalg.norm(diff[:2]) < CUBE_SIZE * 2: # If the attention pose is close to an object, set the goal to be on top of that object instead of the raw attention pose
                        self.get_logger().info(f"Adjusting goal from {attention_pose} to {selected[:3, 3]} based on proximity to detected object.")
                        selected_goal = selected[:3, 3] + np.array([0, 0, CUBE_SIZE])

                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation.w = 1.0
                result.pose.pose.position.x = selected_goal[0]
                result.pose.pose.position.y = selected_goal[1]
                result.pose.pose.position.z = selected_goal[2]
                result.success = True
                
            case _:
                result.success = False

        return result

def main(args=None):
    rclpy.init(args=args)
    perception_action_server = PerceptionActionServer()
    rclpy.spin(perception_action_server)

if __name__ == "__main__":
    main()