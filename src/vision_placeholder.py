import cv2
import numpy as np
import mediapipe as mp
from pupil_apriltags import Detector
from xarm.wrapper import XArmAPI
from utils.zed_camera import ZedCamera
import Math
from checkpoint0 import get_transform_camera_robot

CUBE_TAG_SIZE = 0.02045
TARGET_FRAMES = 30

class PointBot:
    def __init__(self, zed):
        self.zed = zed
        self.K = zed.camera_intrinsic
        self.detector = Detector(families="tag36h11")
        self.hands = mp.solutions.hands.Hands(
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8
        )
        self.frame_buffer = []   
        self.tags = None    

    def detect_hand_pose(lm):
        # angle between pointer and middle finger 
        m1 = (lm.landmark[7].x - lm.landmark[8].x ) / (lm.landmark[7].y - lm.landmark[8].y)
        m2 = (lm.landmark[11].x - lm.landmark[12].x ) / (lm.landmark[11].y - lm.landmark[12].y)

        angle = Math.acrtan((m1-m2)/(1 + m1 * m2))

        if angle > Math.pi:
            print("Pick from hand")
        else:
            print("Pick from table")
        return 


    # Detect MP hands and ray from current 
    def sample_frame(self, color, depth, lm):
        h, w = color.shape[:2]
        tip = lm.landmark[8]
        knuckle = lm.landmark[7]

        # Unnormalize mediapipe outputs
        tx, ty = int(tip.x * w), int(tip.y * h)
        kx, ky = int(knuckle.x * w), int(knuckle.y * h)

        if not (0 <= tx < w and 0 <= ty < h):
            return None
        if not (0 <= kx < w and 0 <= ky < h):
            return None

        p_tip = depth[ty, tx][:3]
        p_knuckle = depth[ky, kx][:3]

        if not (np.isfinite(p_tip).all() and np.isfinite(p_knuckle).all()):
            return None
        
        # Calculate ray/dir from knuckle to tip 
        ray = p_tip - p_knuckle
        norm = np.linalg.norm(ray)
        if norm < 1e-6:
            return None

        ray /= norm
        self.frame_buffer.append((p_tip, ray))
        return p_tip, ray

    def solve(self, t_cam_robot):
        #t_cam_robot should be camera frame -> robot frame
        p_tips = np.array([f[0] for f in self.frame_buffer])
        # Calc from sample function
        rays = np.array([f[1] for f in self.frame_buffer])

        p_tip_cam = np.mean(p_tips, axis=0)
        ray_cam = np.mean(rays, axis=0)
        ray_cam /= np.linalg.norm(ray_cam)

        # t_robot_cam should be robot frame -> camera frame
        t_robot_cam = np.linalg.inv(t_cam_robot)

        # Extend from the tip of the pointer to the table
        # CHECK TRANSFORMATION
        origin_rob = (t_cam_robot @ np.append(p_tip_cam, 1))[:3]
        ray_rob = (t_cam_robot[:3, :3] @ ray_cam)
        ray_rob /= np.linalg.norm(ray_rob)
        print("origin_z:", origin_rob[2])
        print("dir_z:", ray_rob[2])

        if abs(ray_rob[2]) < 1e-6:
            return None

        # Find intersection by setting eq = 0 (origin_z + t * dir_z = 0)
        t = -origin_rob[2] / ray_rob[2]
        intersection = origin_rob + t * ray_rob
        intersection_cam = (np.linalg.inv(t_cam_robot) @ np.append(intersection, 1))[:3]

        return p_tip_cam, ray_cam, origin_rob, ray_rob, intersection, intersection_cam
    
    # Project 3D into 2D
    def proj_3d_2d(self, p):
            fx, fy = self.K[0,0], self.K[1,1]
            cx, cy = self.K[0,2], self.K[1,2]
            if p[2] <= 0:
                return None
            x = int((p[0]*fx/p[2]) + cx)
            y = int((p[1]*fy/p[2]) + cy)
            return (x, y)

    def visualize(self, frame, p_tip_cam, ray_cam, intersection_cam):
        h, w = frame.shape[:2]

        def valid_pixel(p):
            return p is not None and 0 <= p[0] < w and 0 <= p[1] < h

        # Project points
        p0 = self.proj_3d_2d(p_tip_cam)
        p1 = self.proj_3d_2d(p_tip_cam + 1.0 * ray_cam) 
        p_int = self.proj_3d_2d(intersection_cam)

        # ---- DRAW FULL RAY TO INTERSECTION (blue) ----
        if valid_pixel(p0) and valid_pixel(p_int):
            cv2.line(frame, p0, p_int, (255, 0, 0), 2)
            cv2.circle(frame, p_int, 8, (0, 0, 255), -1)
        else:
            print("Skipping full ray draw: invalid projection")
            if valid_pixel(p0) and valid_pixel(p1):
                cv2.line(frame, p0, p1, (0, 255, 0), 2)

        return frame

    def run(self, t_cam_robot):

        cv2.namedWindow("debug", cv2.WINDOW_NORMAL)
        while True:
            color = self.zed.image
            depth = self.zed.point_cloud

            if color is None:
                continue

            frame = cv2.cvtColor(color, cv2.COLOR_BGRA2BGR)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)

            if results.multi_hand_landmarks:
                lm = results.multi_hand_landmarks[0]
                sample = self.sample_frame(frame, depth, lm)

                if len(self.frame_buffer) > TARGET_FRAMES:
                    tip_cam, ray_cam, tip_rob, ray_rob, inter, inter_cam = self.solve(t_cam_robot)
                    frame = self.visualize(frame, tip_cam, ray_cam, inter_cam)
                    cv2.imshow("debug", frame)
                    cv2.waitKey(0)
                    self.frame_buffer.clear()

                    return inter

            cv2.imshow("debug", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def main():
    zed = ZedCamera()
    cam = PointBot(zed)
    t_cam_robot = get_transform_camera_robot(zed.image, zed.camera_intrinsic)
    result = cam.run(t_cam_robot)
    print("Final intersection:", result)
    zed.close()


if __name__ == "__main__":
    main()