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

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False, 
            max_num_hands=1, 
            min_detection_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        # 3. Stability Logic Variables
        self.last_pos_3d = None
        self.start_time = None
        self.STABILITY_THRESHOLD = 0.05 # Meters (5cm)
        self.HOLD_DURATION = 2.5 # Seconds

    def get_zed_data(self):
        """Grabs the latest image and depth map from ZED so we can stream"""
        image = sl.Mat()
        depth = sl.Mat()
        runtime_params = sl.RuntimeParameters()
        
        if self.zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            self.zed.retrieve_image(image, sl.VIEW.LEFT)
            self.zed.retrieve_measure(depth, sl.MEASURE.XYZRGBA)
            return image.get_data(), depth.get_data()
        return None, None

    def calculate_ray(self, tip_3d, knuckle_3d):
        """Vector from finger knuckle to tip."""
        direction = tip_3d - knuckle_3d
        unit_direction = direction / np.linalg.norm(direction)
        return tip_3d, unit_direction

    def run(self):        
        while True:
            frame, xyz_map = self.get_zed_data()
            if frame is None: continue

            # BGRA --> RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
            results = self.hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    # Get Pixel Coordinates for Index Tip (8) and Knuckle (5)
                    h, w, _ = frame.shape
                    tip_pixel = (int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h))
                    knuckle_pixel = (int(hand_landmarks.landmark[5].x * w), int(hand_landmarks.landmark[5].y * h))

                    # Actual 3D coordinates from ZED XYZ map
                    tip_3d = xyz_map[tip_pixel[1], tip_pixel[0]][:3]
                    knuckle_3d = xyz_map[knuckle_pixel[1], knuckle_pixel[0]][:3]

                    # Check for Stability (Ignore NaN values from depth map)
                    if not np.isnan(tip_3d).any():
                        if self.last_pos_3d is None:
                            self.last_pos_3d = tip_3d
                            self.start_time = time.time()
                        
                        dist = np.linalg.norm(tip_3d - self.last_pos_3d)

                        if dist < self.STABILITY_THRESHOLD:
                            elapsed = time.time() - self.start_time
                            # Visual feedback: Progress bar
                            cv2.putText(frame, f"Holding: {round(elapsed, 1)}s", (50, 50), 
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            
                            if elapsed >= self.HOLD_DURATION:
                                origin, direction = self.calculate_ray(tip_3d, knuckle_3d)
                                print(f"RAY CAPTURED! Origin: {origin}, Dir: {direction}")
                                # --- TRIGGER ROBOT ACTION HERE ---
                                self.start_time = time.time() # Reset
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