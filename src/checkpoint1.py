import cv2, numpy, time
import math
import time
from pupil_apriltags import Detector
from xarm.wrapper import XArmAPI

from utils.vis_utils import draw_pose_axes
from utils.zed_camera import ZedCamera
from checkpoint0 import get_transform_camera_robot, ROBOT_IP

CUBE_SIZE = 0.025
GRIPPER_LENGTH = 0.067 * 1000
CUBE_TAG_FAMILY = 'tag36h11'
CUBE_TAG_ID = 4
CUBE_TAG_SIZE = 0.02045

SPEED = 500 # Values 0-1000
ACCELERATION = 1000 # Values 0-50000

robot_ip = ROBOT_IP

def grasp_cube(arm, cube_pose, tower_height=CUBE_SIZE):
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
    z_higher = z + GRIPPER_LENGTH

    #Find rpy
    R = matrix_to_rpy(cube_pose)
    theta = R[0]
    phi = R[1]
    psy = R[2]

    # Pick up and Place script
    arm.set_position(x, y, z_higher, phi, theta, psy, is_radian=True, wait=True, speed=SPEED, mvacc=ACCELERATION)
    time.sleep(0.01)

    arm.open_lite6_gripper()
    time.sleep(1)
    arm.stop_lite6_gripper()

    arm.set_position(x, y, z + 0.002, phi, theta, psy, is_radian=True, wait=True, speed=SPEED, mvacc=ACCELERATION)
    time.sleep(0.01)

    arm.close_lite6_gripper()
    time.sleep(1)
    # arm.stop_lite6_gripper()

    arm.set_position(x, y, z + (tower_height * 1000) + GRIPPER_LENGTH, phi, theta, psy, is_radian=True, wait=True, speed=SPEED, mvacc=ACCELERATION)
    time.sleep(0.01)

def place_cube(arm, cube_pose):
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
    z_higher = z + GRIPPER_LENGTH

    R = matrix_to_rpy(cube_pose)
    theta = R[0]
    phi = R[1]
    psy = R[2]

    # Moves arm down to place cube
    arm.set_position(x, y, z, phi, theta, psy, is_radian = True, wait = True, speed=SPEED, mvacc=ACCELERATION)

    # Opens the gripper to release the cube
    arm.open_lite6_gripper()
    time.sleep(1)
    arm.stop_lite6_gripper()

    # Moves arm back up to position above the placed cube
    arm.set_position(x, y, z_higher, phi, theta, psy, is_radian = True, wait = True, speed=SPEED, mvacc=ACCELERATION)
    

#3x3 rotation matrix to roll pitch yaw
def matrix_to_rpy(matrix):
    R = matrix
    theta = 0
    phi = 0
    psy = 0

    if (R[2][0] != -1 and R[2][0] != 1):   
        theta = -math.asin(R[2][0])
        cos_theta = math.cos(theta)
        phi = math.atan2(R[2][1] / cos_theta, R[2][2] / cos_theta)
        psy = math.atan2(R[1][0] / cos_theta, R[0][0] / cos_theta)
    else:
        if (R[2][0] == -1):
            theta = math.pi / 2
            psy = math.atant2(R[0][1], R[0][2])
        else:
            theta = -math.pi / 2
            psy = math.atant2(-R[0][1], -R[0][2])

    return [theta, phi, psy]


def get_transform_cube(observation, camera_intrinsic, camera_pose):
    """
    Calculate the transformation matrix for the cube relative to the robot base frame, 
    as well as relative to the camera frame.

    This function uses visual fiducial detection to find the cube's pose in the camera's view, 
    then transforms that pose into the robot's global coordinate system. 

    Parameters
    ----------
    observation : numpy.ndarray
        The input image from the camera. Can be a color (BGRA/BGR) or grayscale image.
    camera_intrinsic : numpy.ndarray
        The 3x3 intrinsic camera matrix.
    camera_pose : numpy.ndarray
        A 4x4 transformation matrix representing the camera's pose in the robot base frame (t_cam_robot).
        All translations are in meters.

    Returns
    -------
    tuple or None
        If successful, returns a tuple (t_robot_cube, t_cam_cube) where both 
        are 4x4 transformation matrices with translations in meters. 
        If no cube tag is detected, returns None.
    """
    # Initialize AprilTag Detector
    detector = Detector(families='tag36h11')

    # Detect AprilTag Points
    if len(observation.shape) > 2:
        observation = cv2.cvtColor(observation, cv2.COLOR_BGRA2GRAY)
    params = [camera_intrinsic[0][0], camera_intrinsic[1][1], camera_intrinsic[0][2],camera_intrinsic[1][2]]
    tags = detector.detect(observation, estimate_tag_pose=True, camera_params=params, tag_size=CUBE_TAG_SIZE)

    if not tags:
        print('No tags detected.')
        return None

    for tag in tags:
        if tag.tag_id != CUBE_TAG_ID:
            continue

        t_cam_cube = numpy.eye(4)
        t_cam_cube[:3, :3] = tag.pose_R
        t_cam_cube[:3, 3] = tag.pose_t.flatten()

        t_robot_cube = numpy.linalg.inv(camera_pose) @ t_cam_cube

        print(t_robot_cube)

        return t_robot_cube, t_cam_cube

    return None

def main():

    # Initialize ZED Camera
    zed = ZedCamera()
    camera_intrinsic = zed.camera_intrinsic

    # Initialize Lite6 Robot
    arm = XArmAPI(robot_ip)
    arm.connect()
    arm.motion_enable(enable=True)
    arm.set_tcp_offset([0, 0, GRIPPER_LENGTH, 0, 0, 0])
    arm.set_mode(0)
    arm.set_state(0)
    arm.move_gohome(wait=True)
    time.sleep(0.5)

    try:
        # Get Observation
        cv_image = zed.image

        # Get Transformation
        t_cam_robot = get_transform_camera_robot(cv_image, camera_intrinsic)
        if t_cam_robot is None:
            return
        

        t_robot_cube, t_cam_cube = get_transform_cube(cv_image, camera_intrinsic, t_cam_robot)
        if t_robot_cube is None or t_cam_cube is None:
            print('Cube tag not detected.')
            return

        # Visualization
        draw_pose_axes(cv_image, camera_intrinsic, t_cam_cube,  size=CUBE_TAG_SIZE)
        cv2.namedWindow('Verifying Cube Pose', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Verifying Cube Pose', 1280, 720)
        cv2.imshow('Verifying Cube Pose', cv_image)
        key = cv2.waitKey(0)

        if key == ord('k'):
            cv2.destroyAllWindows()

        grasp_cube(arm, t_robot_cube)
        place_cube(arm, t_robot_cube)
    
    finally:
        # Close Lite6 Robot
        arm.move_gohome(wait=True)
        time.sleep(0.5)
        arm.disconnect()

        # Close ZED Camera
        zed.close()

if __name__ == "__main__":

    main()
