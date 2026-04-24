

# Goal is to 1. calibrate the camera
# 2. Detect hand pose (pointing or flat)
# 3. get the pointing intersection + return it to the control system
# 4. Get the objects in the workspace and return that to the control system
# 5. Let the control system decide whihc object

from checkpoint0 import get_transform_camera_robot
from pupil_apriltags import Detector
from utils.zed_camera import ZedCamera
from perception.perception.pointing_system import PointBot
import numpy as np
from utils.vis_utils import draw_pose_axes

def main():
    zed = ZedCamera()
    # Real
    t_cam_robot = get_transform_camera_robot(zed.image, zed.camera_intrinsic)
    # Debug without the system
    # t_cam_robot = np.eye(4)
    cam = PointBot(zed, t_cam_robot)

    # p_tip_cam, ray_cam, intersect, intersection_cam = cam.solve()

    # cam.visualize(p_tip_cam, ray_cam, intersect, intersection_cam)

    # Returned in robot frame
    pickup_loc, interaction_type = cam.run()

    print(f"Pickup Location in Robot Frame: {pickup_loc}, Interaction Type: {interaction_type}")

    #cue logic with apriltags for now, will replace with object detection later
    # draw_pose_axes(zed.image, zed.camera_intrinsic, pickup_loc)
    zed.close()

if __name__ == "__main__":
    main()