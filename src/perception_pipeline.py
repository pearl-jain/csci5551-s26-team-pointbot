

# Goal is to 1. calibrate the camera
# 2. Detect hand pose (pointing or flat)
# 3. get the pointing intersection + return it to the control system
# 4. Get the objects in the workspace and return that to the control system
# 5. Let the control system decide whihc object

from checkpoint0 import get_transform_camera_robot
from pupil_apriltags import Detector
from utils.zed_camera import ZedCamera
from pointing_system import PointBot
import numpy as np

def main():
    zed = ZedCamera()
    # Real
    t_cam_robot = get_transform_camera_robot(zed.image, zed.camera_intrinsic)
    # Debug without the system
    t_cam_robot = np.eye(4)
    cam = PointBot(zed, t_cam_robot)

    pickup_loc, interaction_type = cam.run()
    zed.close()