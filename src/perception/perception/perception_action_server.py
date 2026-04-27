import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from point_bot_interfaces.action import Perception
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped

from perception.detect_object_pose import ObjectPoseDetector
from perception.zed_camera import ZedCamera
from perception.zed_transform import get_transform_camera_robot
from perception.pointing_system import PointBot, CUBE_SIZE

from cv_bridge import CvBridge
import cv2

import tf_transformations

class PerceptionActionServer(Node):
    def __init__(self):
        super().__init__("perception_action_server")
        self._action_server = ActionServer(
            self,
            Perception,
            'perception',
            self.execute_callback)        

        self.zed = ZedCamera()
        
        self.pose_detector = ObjectPoseDetector(self.zed.camera_intrinsic)

        self.t_cube_robot = get_transform_camera_robot(self.zed.image, self.zed.camera_intrinsic)

        self.pointing_system = PointBot(self.zed, self.t_cube_robot)

        self.bridge = CvBridge()

    def execute_callback(self, goal_handle):
        task = goal_handle.request.task

        self.get_logger().info(f"Peforming perception task {task}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully

        # Define the result message and populate it with the perception results
        raw_image = self.zed.image.copy()
        if raw_image.shape[2] == 4:
            raw_image = cv2.cvtColor(raw_image, cv2.COLOR_BGRA2BGR)

        result = Perception.Result()
        result.image = self.bridge.cv2_to_imgmsg(raw_image, encoding="bgr8")

        result.pose = PoseStamped()
        match task:
            case "detect_object":
                objects = self.pose_detector.detect_cubes(self.zed.image, self.t_cube_robot)

                self.get_logger().info(f"Detected object poses:\n{objects}")
                
                object_poses = [obj[:3, 3] for obj in objects]

                attention_pose, interaction_type, pointer_position, pointer_direction = self.pointing_system.run(object_poses)

                self.get_logger().info(f"Attention Pose: {attention_pose}\nInteraction Type: {interaction_type}\nPointer Position: {pointer_position}\nPointer Direction: {pointer_direction}")
                
                attention_scores = self.pose_detector.pointing_object_space_scores(object_poses, pointer_position, pointer_direction, 0.02, 0.01)

                selected = self.pose_detector.select_cube(objects, attention_scores)

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

            case "detect_goal":
                attention_pose, interaction_type, pointer_position, pointer_direction = self.pointing_system.run()
                self.get_logger().info(f"Attention Pose: {attention_pose}\nInteraction Type: {interaction_type}\nPointer Position: {pointer_position}\nPointer Direction: {pointer_direction}")

                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation.w = 1.0
                result.pose.pose.position.x = attention_pose[0]
                result.pose.pose.position.y = attention_pose[1]
                result.pose.pose.position.z = attention_pose[2] + CUBE_SIZE
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