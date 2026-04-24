import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from point_bot_interfaces.action import Perception
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped

from perception.detect_object_pose import ObjectPoseDetector
from perception.zed_camera import get_zed_camera
from perception.zed_transform import get_transform_camera_robot
from perception.pointing_system import PointBot

import tf_transformations as tf

class PerceptionActionServer(Node):
    def __init__(self):
        super().__init__("perception_action_server")
        self._action_server = ActionServer(
            self,
            Perception,
            'perception',
            self.execute_callback)        


        self.zed = get_zed_camera()
        
        self.pose_detector = ObjectPoseDetector(self.zed.camera_intrinsic)

        self.t_cube_robot = get_transform_camera_robot(self.zed.image, self.zed.camera_intrinsic)

        self.pointing_system = PointBot(self.zed, self.t_cube_robot)

    def execute_callback(self, goal_handle):
        task = goal_handle.request.task

        self.get_logger().info(f"Peforming perception task {task}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully

        intersection, interaction_type, pointer_position, pointer_direction = self.pointing_system.run()
        
        # Define the result message and populate it with the perception results
        result = Perception.Result()
        result.image = Image()
        result.image.header.frame_id = "zed_camera_frame"
        result.image.data = self.zed.image

        result.pose = PoseStamped()
        match task:
            case "detect_object":
                objects = self.pose_detector.detect_cubes(self.zed.image, self.t_cube_robot)
                object_poses = objects

                attention_scores = self.pose_detector.pointing_object_surface_scores(object_poses, pointer_position, pointer_direction)

                selected = self.pose_detector.select_cube(objects, attention_scores)

                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation = tf.quaternion_from_matrix(selected[:3, :3])
                result.pose.pose.position.x = selected[0, 3]
                result.pose.pose.position.y = selected[1, 3]
                result.pose.pose.position.z = selected[2, 3]
                result.success = True

            case "detect_goal":
                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation.w = 0
                result.pose.pose.position.x = intersection[0]
                result.pose.pose.position.y = intersection[1]
                result.pose.pose.position.z = intersection[2]
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