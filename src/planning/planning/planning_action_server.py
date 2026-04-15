import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from moveit.planning import MoveItPy

from point_bot_interfaces.action import MoveObject
from xarm_msgs.srv import Call

import copy
import time

# For the planning code to run, in addition to interfacing with the lite6 control drivers,
# xarm_moveit_config lite6_moveit_realmove.launch.py must be launched (currently launched with the Rvis package/launch file)
# Referenced: https://moveit.picknik.ai/main/doc/examples/motion_planning_python_api/motion_planning_python_api_tutorial.html

class PlanningActionServer(Node):
    def __init__(self):
        super().__init__("planning_action_server")
        self._action_server = ActionServer(
            self,
            MoveObject,
            'move_object',
            self.execute_callback)
        
        # Creates moveitpy instance/node
        self.logger = rclpy.logging.get_logger("lite6 planning")
        self.lite6 = MoveItPy(node_name="path_planner")
        self.arm = self.lite6.get_planning_component("lite6")
        self.logger.info("MoveItPy instance created")

        # Create gripper client
        self.open_gripper_client = self.create_client(
            Call, '/ufactory/open_lite6_gripper')
        self.close_gripper_client = self.create_client(
            Call, '/ufactory/close_lite6_gripper')

    def execute_callback(self, goal_handle):
        object_pose = goal_handle.request.object
        target_goal = goal_handle.request.goal
        
        self.get_logger().info(f"Moving object from {object_pose} to {target_goal}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully
        result = MoveObject.Result()
        result.success = False

        # TODO: Properly implement planning!
        result.success = self.grasp_object(object_pose)
        if not result.success:
            return result

        result.success = self.place_object(target_goal)
        if not result.success:
            return result

        return result
    
    def grasp_object(self, object_pose):
        # Opens gripper, plans and moves to position above the object
        self.open_gripper()
        self.arm.set_start_state_to_current_state()
        object_pose_higher = copy.deepcopy(object_pose)
        object_pose_higher.pose.position.z += 0.05
        self.arm.set_goal_state(pose_stamped_msg=object_pose_higher, pose_link="link_eef")
        if not self.plan_and_execute(self.lite6, self.arm, self.logger):
            return False

        # Plans and moves to object and closes gripper
        self.arm.set_start_state_to_current_state()
        self.arm.set_goal_state(pose_stamped_msg=object_pose, pose_link="link_eef")
        if not self.plan_and_execute(self.lite6, self.arm, self.logger):
            return False
        self.close_gripper()

        # Returns true if completed successfully
        return True

    def place_object(self, target_goal):
        # Plans and moves to above goal location
        self.arm.set_start_state_to_current_state()
        target_goal_higher = copy.deepcopy(target_goal)
        target_goal_higher.pose.position.z += 0.10  
        self.arm.set_goal_state(pose_stamped_msg=target_goal_higher, pose_link="link_eef")
        if not self.plan_and_execute(self.lite6, self.arm, self.logger):
            return False
        
        # Plans and moves arm to goal location and opens gripper
        self.arm.set_start_state_to_current_state()
        self.arm.set_goal_state(pose_stamped_msg=target_goal, pose_link="link_eef")
        if not self.plan_and_execute(self.lite6, self.arm, self.logger):
            return False
        self.open_gripper()

        # Moves arm up after placing
        self.arm.set_start_state_to_current_state()     
        self.arm.set_goal_state(pose_stamped_msg=target_goal_higher, pose_link="link_eef")
        if not self.plan_and_execute(self.lite6, self.arm, self.logger):
            return False
        
        # Returns true if completed successfully
        return True

    # Helpers that open and close the gripper by calling the xarm ros2 gripper service
    def open_gripper(self):
        future = self.open_gripper_client.call_async(Call.Request())
        rclpy.spin_until_future_complete(self, future)
        time.sleep(1.0)

    def close_gripper(self):
        future = self.close_gripper_client.call_async(Call.Request())
        rclpy.spin_until_future_complete(self, future)
        time.sleep(1.0)

    # Helper plan and execute function
    def plan_and_execute(
        self,
        robot,
        planning_component,
        logger,
        single_plan_parameters=None,
        multi_plan_parameters=None,
        ):
        """A helper function to plan and execute a motion."""
        # Plan to goal
        logger.info("Planning trajectory")
        if multi_plan_parameters is not None:
                plan_result = planning_component.plan(
                        multi_plan_parameters=multi_plan_parameters
                )
        elif single_plan_parameters is not None:
                plan_result = planning_component.plan(
                        single_plan_parameters=single_plan_parameters
                )
        else:
                plan_result = planning_component.plan()

        # Execute the plan
        if plan_result:
                logger.info("Executing plan")
                robot_trajectory = plan_result.trajectory
                robot.execute(robot_trajectory, controllers=[])
                return True
        else:
                logger.error("Planning failed")
                return False

def main(args=None):
    rclpy.init(args=args)
    planning_action_server = PlanningActionServer()
    rclpy.spin(planning_action_server)

if __name__ == "__main__":
    main()