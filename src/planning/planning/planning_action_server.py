import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from point_bot_interfaces.action import MoveObject
from xarm.wrapper import XArmAPI # Might need to 'pip install xarm-python-sdk'

import time
import numpy
import tf_transformations

GRIPPER_LENGTH = 0.067 * 1000
SPEED = 500 # Values 0-1000
ACCELERATION = 1000 # Values 0-50000
ROBOT_IP = '192.168.1.xxx' # Hard coded ip, change this based on arm
robot_ip = ROBOT_IP

class PlanningActionServer(Node):
    def __init__(self):
        super().__init__("planning_action_server")
        self._action_server = ActionServer(
            self,
            MoveObject,
            'move_object',
            self.execute_callback)
        
        self.arm = XArmAPI(robot_ip)
        self.arm.connect()
        self.arm.motion_enable(enable=True)
        self.arm.set_tcp_offset([0, 0, GRIPPER_LENGTH, 0, 0, 0])
        self.arm.set_mode(0)
        self.arm.set_state(0)
        self.arm.move_gohome(wait=True)
        time.sleep(0.5)

    def execute_callback(self, goal_handle):
        object_pose = goal_handle.request.object
        target_goal = goal_handle.request.goal
        
        self.get_logger().info(f"Moving object from {object_pose} to {target_goal}")
        goal_handle.succeed() # Tell the client that the goal was handled successfully
        result = MoveObject.Result()

        # TODO: Properly implement planning!
        t_robot_object = self.pose_stamped_to_matrix(object_pose)
        t_robot_goal = self.pose_stamped_to_matrix(target_goal)
        self.grasp_cube(self.arm, t_robot_object)
        self.place_cube(self.arm, t_robot_goal)
        self.arm.move_gohome(wait=True)
        time.sleep(0.5)
        result.success = True
        return result
    
    def grasp_cube(self, arm, cube_pose):
        """
        Execute a pick sequence to grasp a cube at a specified pose.

        Parameters
        ----------
        arm : xarm.wrapper.XArmAPI
            The initialized XArm API object controlling the Lite6 robot.
        cube_pose : numpy.ndarray
            A 4x4 transformation matrix representing the cube's pose in the robot base frame.
            All translational units in this matrix are in meters.
        """
        x = cube_pose[0][3].astype(numpy.float32) * 1000
        y = cube_pose[1][3].astype(numpy.float32) * 1000
        z = cube_pose[2][3].astype(numpy.float32) * 1000
        z_higher = z + 50

        #Find rpy
        R = self.matrix_to_rpy(cube_pose)
        roll = R[0]
        pitch = R[1]
        yaw = R[2]

        # Pick up and Place script
        arm.set_position(x, y, z_higher, roll, pitch, yaw, is_radian=True, wait=True, speed=SPEED, mvacc=ACCELERATION)
        time.sleep(0.01)

        arm.open_lite6_gripper()
        time.sleep(1)
        arm.stop_lite6_gripper()

        arm.set_position(x, y, z, roll, pitch, yaw, is_radian=True, wait=True, speed=SPEED, mvacc=ACCELERATION)
        time.sleep(0.01)

        arm.close_lite6_gripper()
        time.sleep(1)
        arm.stop_lite6_gripper()

        arm.set_position(x, y, z_higher, roll, pitch, yaw, is_radian=True, wait=True, speed=SPEED, mvacc=ACCELERATION)
        time.sleep(0.01)

    def place_cube(self, arm, cube_pose):
        """
        Execute a place sequence to release a cube at a specified pose.

        Parameters
        ----------
        arm : xarm.wrapper.XArmAPI
            The initialized XArm API object controlling the Lite6 robot.
        cube_pose : numpy.ndarray
            A 4x4 transformation matrix representing the target placement pose in the robot base frame.
            All translational units in this matrix are in meters.
        """
        # Initialize where to release the cube
        x = cube_pose[0][3].astype(numpy.float32) * 1000
        y = cube_pose[1][3].astype(numpy.float32) * 1000
        z = cube_pose[2][3].astype(numpy.float32) * 1000
        z_higher = z + 50 #5 cm above cause matrix units in meters coverted to mm

        R = self.matrix_to_rpy(cube_pose)
        roll = R[0]
        pitch = R[1]
        yaw = R[2]

        # Moves arm down to place cube
        arm.set_position(x, y, z, roll, pitch, yaw, is_radian = True, wait = True, speed=SPEED, mvacc=ACCELERATION)

        # Opens the gripper to release the cube
        arm.open_lite6_gripper()
        time.sleep(1)
        arm.stop_lite6_gripper()

        # Moves arm back up to position 15cm above the placed cube
        arm.set_position(x, y, z_higher, roll, pitch, yaw, is_radian = True, wait = True, speed=SPEED, mvacc=ACCELERATION)

    #3x3 rotation matrix to roll pitch yaw
    def matrix_to_rpy(self, matrix):
        r, p, y = tf_transformations.euler_from_matrix(matrix)
        return [r, p, y]
    
    def pose_stamped_to_matrix(self, pose_stamped):
        pos = pose_stamped.pose.position
        ori = pose_stamped.pose.orientation

        translation = [pos.x, pos.y, pos.z]
        quaternion = [ori.x, ori.y, ori.z, ori.w]

        T = tf_transformations.quaternion_matrix(quaternion)
        T[0:3, 3] = translation

        return T

def main(args=None):
    rclpy.init(args=args)
    planning_action_server = PlanningActionServer()
    rclpy.spin(planning_action_server)

if __name__ == "__main__":
    main()