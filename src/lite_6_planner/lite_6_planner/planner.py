import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from moveit.planning import MoveItPy

#https://moveit.picknik.ai/main/doc/examples/motion_planning_python_api/motion_planning_python_api_tutorial.html

class planner(Node):
    def __init__(self):
        super().__init__('planner')
        self.logger = rclpy.logging.get_logger("lite6 planning")
        self.lite6 = MoveItPy(node_name="planner")
        self.arm = self.lite6.get_planning_component("arm")
        self.logger.info("MoveItPy instance created")

        # Subscribes to /goal topic
        self.goal_subscriber = self.create_subscription(PoseStamped, '/goal', self.plan_and_execute_callback, 1)

    def plan_and_execute_callback(self, msg : PoseStamped):
        self.arm.set_goal_state(pose_stamped_msg=msg, pose_link="link_eef")
        self.plan_and_execute(self.lite6, self.arm, self.logger)

    # Helper plan and execute function
    def plan_and_execute(
        robot,
        planning_component,
        logger,
        single_plan_parameters=None,
        multi_plan_parameters=None,
        ):
        """A helper function to plan and execute a motion."""
        # plan to goal
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

        # execute the plan
        if plan_result:
                logger.info("Executing plan")
                robot_trajectory = plan_result.trajectory
                robot.execute(robot_trajectory, controllers=[])
        else:
                logger.error("Planning failed")

    # Deletes node
    def cleanup(self):
        self.get_logger().info("Goal Node Shutting Down")
        self.destroy_node()

# Spins up node from main entry point, deletes node on keyboard interrupt
def main(args=None):
    rclpy.init(args=args)
    try:
        rclpy.spin(planner)
    except KeyboardInterrupt:
        pass
    
    planner.cleanup()
    
    if rclpy.ok():
        rclpy.shutdown()

if __name__ == '__main__':
        main()