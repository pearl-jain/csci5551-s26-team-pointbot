import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from point_bot_interfaces.action import MoveObject

import time

class PlanningActionServer(Node):
    def __init__(self):
        super().__init__("planning_action_server")
        self._action_server = ActionServer(
            self,
            MoveObject,
            'move_object',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info("Executing action...")

        object_pose = goal_handle.request.object
        target_goal = goal_handle.request.goal
        
        self.get_logger().info(f"Moving object from {object_pose} to {target_goal}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully

        time.sleep(10)

        result = MoveObject.Result()
        result.success = True

        return result

def main(args=None):
    rclpy.init(args=args)
    planning_action_server = PlanningActionServer()
    rclpy.spin(planning_action_server)

if __name__ == "__main__":
    main()