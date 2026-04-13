import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from point_bot_interfaces.action import Perception
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped

import time
import random

class PerceptionActionServer(Node):
    def __init__(self):
        super().__init__("perception_action_server")
        self._action_server = ActionServer(
            self,
            Perception,
            'perception',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info("Executing perception...")

        task = goal_handle.request.task

        if random.random() > 0.5:
            task = "weeee!"

        self.get_logger().info(f"Peforming perception task {task}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully

        time.sleep(5)
        
        result = Perception.Result()
        result.image = Image()

        result.pose = PoseStamped()
        match task:
            case "detect_object":
                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation.w = 1.0
                result.pose.pose.position.x = 0.28
                result.pose.pose.position.y = -0.2
                result.pose.pose.position.z = 0.5
                result.success = True

            case "detect_goal":
                result.pose.header.frame_id = "panda_link0"
                result.pose.pose.orientation.w = 0.5
                result.pose.pose.position.x = 1.0
                result.pose.pose.position.y = -0.2
                result.pose.pose.position.z = 0.1
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