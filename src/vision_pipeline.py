import cv2
import numpy as np
import time
import math
import mediapipe as mp
from pupil_apriltags import Detector
from xarm.wrapper import XArmAPI
from utils.zed_camera import ZedCamera
from checkpoint0 import get_transform_camera_robot, ROBOT_IP
from utils.vis_utils import draw_pose_axes

# --- Configuration ---
CUBE_TAG_SIZE = 0.02045
GRIPPER_LENGTH = 0.067 * 1000  # mm
SPEED = 500
ACCELERATION = 1000

# Perception Tuning
TARGET_FRAMES = 50         # Total frames to wait
COLLECTION_WINDOW = 1    # Frames to actually average
SNAP_DISTANCE = 0.12       # 12cm snapping window for AprilTags

class PointBotPerception:
    def __init__(self, zed):
        self.zed = zed
        self.intrinsic = zed.camera_intrinsic
        self.detector = Detector(families='tag36h11')
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
        self.mp_draw = mp.solutions.drawing_utils
        
        self.frame_counter = 0
        self.frame_buffer = []

    def project_3d_to_2d(self, p):
        if p is None or not np.isfinite(p[2]) or p[2] < 0.05: return None
        x = int((p[0] * self.intrinsic[0,0] / p[2]) + self.intrinsic[0,2])
        y = int((p[1] * self.intrinsic[1,1] / p[2]) + self.intrinsic[1,2])
        return (x, y)

    def run_cycle(self, mode, t_cam_robot):
        self.frame_counter = 0
        self.frame_buffer = []
        cv2.namedWindow("PointBot Perception", cv2.WINDOW_NORMAL)

        while True:
            color_img = self.zed.image
            xyz_map = self.zed.point_cloud
            if color_img is None: continue

            # Handle BGRA to BGR
            frame_display = cv2.cvtColor(color_img, cv2.COLOR_BGRA2BGR) if color_img.shape[2] == 4 else color_img.copy()
            
            rgb = cv2.cvtColor(frame_display, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)

            if results.multi_hand_landmarks:
                self.frame_counter += 1
                lm = results.multi_hand_landmarks[0]
                self.mp_draw.draw_landmarks(frame_display, lm, self.mp_hands.HAND_CONNECTIONS)
                
                # Progress Bar
                progress = min(self.frame_counter / TARGET_FRAMES, 1.0)
                color = (0, 255, 0) if mode == "pick" else (255, 200, 0)
                cv2.rectangle(frame_display, (50, 50), (350, 80), (50, 50, 50), -1)
                cv2.rectangle(frame_display, (50, 50), (50 + int(progress * 300), 80), color, -1)
                cv2.putText(frame_display, f"{mode.upper()}: {self.frame_counter}/50", (60, 73), 1, 1, (255,255,255), 2)

                # Capture Window (frames 48, 49, 50)
                if self.frame_counter > (TARGET_FRAMES - COLLECTION_WINDOW):
                    h, w = frame_display.shape[:2]
                    self.h = h
                    self.w = w
                    tx, ty = np.clip(int(lm.landmark[8].x*w), 0, w-1), np.clip(int(lm.landmark[8].y*h), 0, h-1)
                    wx, wy = np.clip(int(lm.landmark[6].x*w), 0, w-1), np.clip(int(lm.landmark[0].y*h), 0, h-1)
                    p_tip, p_wrist = xyz_map[ty, tx][:3], xyz_map[wy, wx][:3]


                    if np.all(np.isfinite(p_tip)) and np.all(np.isfinite(p_wrist)):
                        current_tags = {}
                        if mode == "pick":
                            gray = cv2.cvtColor(frame_display, cv2.COLOR_BGR2GRAY)
                            params = [self.intrinsic[0,0], self.intrinsic[1,1], self.intrinsic[0,2], self.intrinsic[1,2]]
                            tags = self.detector.detect(gray, estimate_tag_pose=True, camera_params=params, tag_size=CUBE_TAG_SIZE)
                            tag_positions = []
                            for tag in tags:
                                # if tag.tag_id != 4:
                                #     continue
                                
                                cube_center = tag.pose_t.flatten()
                                tag_positions.append(cube_center)

                            direction = (p_tip - p_wrist) / np.linalg.norm(p_tip - p_wrist)
                            self.frame_buffer.append((p_tip, direction, tag_positions))
                        direction = (p_tip - p_wrist) / np.linalg.norm(p_tip - p_wrist)
                        self.frame_buffer.append((p_tip, direction))

                if self.frame_counter >= TARGET_FRAMES:
                    if len(self.frame_buffer) > 0:
                        return self.finalize_and_freeze(frame_display, mode, t_cam_robot, p_tip)
                    self.frame_counter = 0 # Reset if no valid 3D points were found

            cv2.imshow("PointBot Perception", frame_display)
            if cv2.waitKey(1) & 0xFF == ord('q'): return None

    def finalize_and_freeze(self, last_frame, mode, t_cam_robot, tip):
        # Average Ray (Camera Frame)
        avg_o_cam = np.mean([f[0] for f in self.frame_buffer], axis=0)
        avg_d_cam = np.mean([f[1] for f in self.frame_buffer], axis=0)
        avg_d_cam /= np.linalg.norm(avg_d_cam)

        # Transform Ray to Robot Frame to find Z=0 intersection
        t_robot_cam = np.linalg.inv(t_cam_robot)
        avg_o_rob = (t_robot_cam @ np.append(avg_o_cam, 1.0))[:3]
        avg_d_rob = (t_robot_cam[:3, :3] @ avg_d_cam)
        
        # t = -o_z / d_z
        t = -avg_o_rob[2] / avg_d_rob[2]
        target_rob = avg_o_rob + t * avg_d_rob

        print(avg_d_rob)
        
        # Target in Cam Frame (for drawing)
        target_cam = (t_cam_robot @ np.append(target_rob, 1.0))[:3]

        # Snap to Tags (Pick Mode Only)
        if mode == "pick":
            # all_ids = set().union(*[f[2].keys() for f in])
            print(target_cam)
            # all_ids = self.b
            positions = self.frame_buffer[0][2]
            if positions:
                min_dist = float('inf')
                target_cube = None
                w,h = self.w, self.h
                print(len(positions))
                for pos in positions:

                    d = np.linalg.norm(pos - target_cam)
                    if d < min_dist:
                        min_dist= d
                        target_cube = pos
                if target_cube is not None:
                    target_cam = target_cube
                    target_rob = (t_robot_cam @ np.append(target_cam, 1.0))[:3]

            for pos in self.frame_buffer[0][2]:
                end = self.project_3d_to_2d(pos)
                cv2.circle(last_frame, end, 20, (0, 255, 0), -1)

            
        # Draw Static View
        p_start = self.project_3d_to_2d(tip)
        p_end = self.project_3d_to_2d(target_cam)

        print(p_start, p_end,)
        if p_start and p_end:
            color = (0, 255, 0) if mode == "pick" else (255, 200, 0)
            cv2.line(last_frame, p_end, p_start, color, 4)
            cv2.circle(last_frame, p_end, 10, (0, 0, 255), -1)
        
        
        cv2.putText(last_frame, "CONFIRM: 'K' | RESET: 'R'", (50, 120), 1, 2, (255,255,255), 2)
        while True:
            cv2.imshow("PointBot Perception", last_frame)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('k'):
                cv2.destroyWindow("PointBot Perception")
                return target_rob, t_robot_cam
            elif key == ord('r'):
                return self.run_cycle(mode, t_cam_robot)
            
    def zed_capture(self):
        instance = self.grab()
        return instance.image(), instance.point_cloud

def main():
    zed = ZedCamera()
    camera_intrinsic = zed.camera_intrinsic
    perception = PointBotPerception(zed)
    
    try:
        t_cam_robot = get_transform_camera_robot(zed.image, zed.camera_intrinsic)
        if t_cam_robot is None: return

        # t_cam_robot = np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])

        # PICK PHASE
        cv_image = zed.image
        # target_place_rob, target_place_cam= perception.run_cycle("pick", t_cam_robot)
        target_pick_rob, target_pick_cam  = perception.run_cycle("place", t_cam_robot)
        if target_pick_rob is not None:

            #grasp_cube(arm, target_pick, is_pick=True)

            draw_pose_axes(cv_image, camera_intrinsic, target_pick_cam,  size=CUBE_TAG_SIZE)
            cv2.namedWindow('Verifying Cube Pose', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Verifying Cube Pose', 1280, 720)
            cv2.imshow('Verifying Cube Pose', cv_image)
            key = cv2.waitKey(0)

            if key == ord('k'):
                cv2.destroyAllWindows()

        #     # PLACE PHASE
        #     target_place_rob, target_place_cam= perception.run_cycle("place", t_cam_robot)
        #     if target_place_rob is not None:
        #         pass
        #         #place_cube(arm, target_place, is_pick=False)
    finally:

        zed.close()

if __name__ == "__main__":
    main()