import pyzed.sl as sl
import cv2
import mediapipe as mp
import numpy as np
import time

class PointBotVision:
    def __init__(self):
        self.zed = sl.Camera()
        init_params = sl.InitParameters()
        init_params.camera_resolution = sl.RESOLUTION.HD720
        init_params.coordinate_units = sl.UNIT.METER 
        init_params.depth_mode = sl.DEPTH_MODE.ULTRA
        
        if self.zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
            print("Failed to open ZED")
            exit()

        # Get calibration parameters for 3D -> 2D projection
        calibration_params = self.zed.get_camera_information().camera_configuration.calibration_parameters
        self.fx = calibration_params.left_cam.fx
        self.fy = calibration_params.left_cam.fy
        self.cx = calibration_params.left_cam.cx
        self.cy = calibration_params.left_cam.cy

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False, 
            max_num_hands=1, 
            min_detection_confidence=0.4
        )
        self.mp_draw = mp.solutions.drawing_utils

        self.last_pos_3d = None
        self.start_time = None
        self.STABILITY_THRESHOLD = 0.05 
        self.HOLD_DURATION = .5

        self.active_ray = None # Stores (origin_3d, direction_3d)

    def get_zed_data(self):
        image = sl.Mat()
        depth = sl.Mat()
        runtime_params = sl.RuntimeParameters()
        
        if self.zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            self.zed.retrieve_image(image, sl.VIEW.LEFT)
            self.zed.retrieve_measure(depth, sl.MEASURE.XYZRGBA)
            return image.get_data(), depth.get_data()
        return None, None

    def calculate_ray(self, tip_3d, knuckle_3d):
        direction = tip_3d - knuckle_3d
        norm = np.linalg.norm(direction)
        if norm == 0: return tip_3d, direction
        unit_direction = direction / norm
        return tip_3d, unit_direction

    def project_3d_to_2d(self, point_3d):
        """Projects a 3D ZED coordinate (x, y, z) to 2D pixel (u, v)"""
        if point_3d is None:
            return None
        if not np.isfinite(point_3d).all():
            return None

        x, y, z = point_3d
        if z <= 0: 
            return None
            
        u = int((x * self.fx / z) + self.cx)
        v = int((y * self.fy / z) + self.cy)
        return (u, v)

    def draw_active_ray(self, frame):
        """Draws the currently stored ray on the frame"""
        if self.active_ray is None:
            return

        origin_3d, direction_3d = self.active_ray
        
        # Create a second point far along the ray (e.g., 5 meters away)
        end_3d = origin_3d + (direction_3d * 1.0)

        p1 = self.project_3d_to_2d(origin_3d)
        p2 = self.project_3d_to_2d(end_3d)

        if p1 and p2:
            cv2.line(frame, p1, p2, (255, 0, 255), 3) # Neon Purple line
            cv2.circle(frame, p1, 5, (0, 0, 255), -1) # Red dot at origin

    def run(self):  
        while True:
            frame_raw, xyz_map = self.get_zed_data()
            if frame_raw is None: continue

            frame = cv2.cvtColor(frame_raw, cv2.COLOR_BGRA2BGR)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)

            # Draw the persistent ray from the last capture
            self.draw_active_ray(frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                
                    h, w, _ = frame.shape
                    # Clamp coordinates to avoid index errors on edge of screen
                    tx = max(0, min(w-1, int(hand_landmarks.landmark[8].x * w)))
                    ty = max(0, min(h-1, int(hand_landmarks.landmark[8].y * h)))
                    kx = max(0, min(w-1, int(hand_landmarks.landmark[5].x * w)))
                    ky = max(0, min(h-1, int(hand_landmarks.landmark[5].y * h)))

                    tip_3d = xyz_map[ty, tx][:3]
                    knuckle_3d = xyz_map[ky, kx][:3]

                    if not np.isnan(tip_3d).any() and not np.isnan(knuckle_3d).any():
                        if self.last_pos_3d is None:
                            self.last_pos_3d = tip_3d
                            self.start_time = time.time()
                        
                        dist = np.linalg.norm(tip_3d - self.last_pos_3d)

                        if dist < self.STABILITY_THRESHOLD:
                            elapsed = time.time() - self.start_time
                            cv2.putText(frame, f"Steady: {round(elapsed, 1)}s", (50, 80), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                                                        
                            if elapsed >= self.HOLD_DURATION:
                                # Update the active ray (This replaces the old one)
                                origin, direction = self.calculate_ray(tip_3d, knuckle_3d)
                                if not np.isnan(origin).any() and not np.isnan(direction).any():
                                    self.active_ray = (origin, direction)
                                print(f"NEW RAY: Origin {origin}, Dir {direction}")
                                self.start_time = time.time() # Reset to allow immediate re-pointing
                        else:
                            self.start_time = time.time()
                            self.last_pos_3d = tip_3d

            cv2.imshow("PointBot Vision", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.zed.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    bot = PointBotVision()
    bot.run()