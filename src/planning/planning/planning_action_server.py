import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from point_bot_interfaces.action import MoveObject

import time
import random

class PlanningActionServer(Node):
    def __init__(self):
        super().__init__("planning_action_server")
        self._action_server = ActionServer(
            self,
            MoveObject,
            'move_object',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        object_pose = goal_handle.request.object
        target_goal = goal_handle.request.goal
        
        self.get_logger().info(f"Moving object from {object_pose} to {target_goal}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully

        # TODO: Properly implement planning!
        time.sleep(10)

        result = MoveObject.Result()
        result.success = True

        if random.random() > 0.5:
            result.success = False

        return result

def main(args=None):
    rclpy.init(args=args)
    planning_action_server = PlanningActionServer()
    rclpy.spin(planning_action_server)

if __name__ == "__main__":
    main()