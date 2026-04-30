import cv2
import numpy as np
import mediapipe as mp
import open3d as o3d
from perception.zed_transform import TAG_SIZE, draw_pose_axes
from types import SimpleNamespace

CUBE_TAG_SIZE = 0.02045
TARGET_FRAMES = 5
CUBE_SIZE = 0.025

X_MIN, X_MAX = 0 + TAG_SIZE / 2, 0.38 - TAG_SIZE / 2
Y_MIN, Y_MAX = -0.4 + TAG_SIZE / 2, 0.4 - TAG_SIZE / 2

class PointBot:
    def __init__(self, zed, t_cam, node):
        self.zed = zed
        self.K = zed.camera_intrinsic
        self.hands = mp.solutions.hands.Hands(
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8
        )
        # self.frame_buffer = []   
        self.tags = None    
        self.t_cam_robot = t_cam
        self.h, self.w, self.image, self.depth = None, None, None, None
        self.node = node


        self.prev_landmarks = None
        # self.stable_counter = 0
        self.stable_frames = 64
        self.motion_thresh = 0.001

        self.finger_gesture_table = [
            [1, 1, 1, 1, 1], # Pick From Hand
            [0, 1, 0, 0, 0] # Pick From Table
        ]

        self.finger_props = [
            (2, 3, 4, 0, 0.85),  # Thumb (MCP=2, PIP=3, Tip=4)
            (5, 6, 8, 0, 0.90),  # Index
            (9, 10, 12, 0, 0.90), # Middle
            (13, 14, 16, 0, 0.90),# Ring
            (17, 18, 20, 0, 0.90) # Pinky
        ]

    # Utility Functions
    def zed_to_pcd(self, pcd, img, scale):
        rgb = img[:, :, :3][..., ::-1].reshape(-1, 3) / 255.0
        xyz = pcd[:, :, :3].reshape(-1, 3) * scale

        mask = ~np.isnan(xyz).any(axis=1)
        xyz_clean = xyz[mask]
        rgb_clean = rgb[mask]
        
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz_clean)
        pcd.colors = o3d.utility.Vector3dVector(rgb_clean)

        return pcd
    
    # 2D_3D Projection  
    def proj_2d_3d(self, p):
        if self.h is None or self.depth is None: return None
        tx, ty = int(p.x * self.w), int(p.y * self.h)
        if not (0 <= tx < self.w and 0 <= ty < self.h):
            return None
        
        p_3d_raw = self.depth[ty, tx][:3]
        if np.isfinite(p_3d_raw).all() and np.linalg.norm(p_3d_raw) > 1e-3:
            return p_3d_raw
        
        #Try Depth Sampling if needed
        window_size = 5
        half_w = window_size // 2
        y_min, y_max = max(0, ty - half_w), min(self.h, ty + half_w + 1)
        x_min, x_max = max(0, tx - half_w), min(self.w, tx + half_w + 1)
        roi = self.depth[y_min:y_max, x_min:x_max, :3]
        roi_flat = roi.reshape(-1, 3)
        valid_mask = np.isfinite(roi_flat).all(axis=1)
        valid_points = roi_flat[valid_mask]

        if len(valid_points) == 0:
            return None
        
        p_3d_filtered = np.median(valid_points, axis=0)
        if np.linalg.norm(p_3d_filtered) < 1e-3:
            return None 
        
        return p_3d_filtered
    
    # Project 3D into 2D
    def proj_3d_2d(self, p):
        fx, fy = self.K[0,0], self.K[1,1]
        cx, cy = self.K[0,2], self.K[1,2]
        if p[2] <= 0:
            return None
        x = int((p[0]*fx/p[2]) + cx)
        y = int((p[1]*fy/p[2]) + cy)
        return (x, y)
    
    def valid_pixel(self, p):
        return p is not None and 0 <= p[0] < self.w and 0 <= p[1] < self.h
    
    # Hand Detection
    def detect_gesture(self, landmark_results):
        multi_hand_landmarks = landmark_results.multi_hand_landmarks
        if not multi_hand_landmarks: return [-1]
        
        ANGLE_THRESH = 30

        gestures = []
        for hand_landmarks in multi_hand_landmarks:
            extended = []
            for points in self.finger_props:
                mcp_idx, pip_idx, tip_idx, _, threshold = points
            
                # Checks in 2D
                is_straight = self.is_finger_extended(hand_landmarks.landmark[mcp_idx], hand_landmarks.landmark[pip_idx], hand_landmarks.landmark[tip_idx], ANGLE_THRESH)
                extended.append(is_straight)
            
            print(f"States: {extended}") 
        
        # Just check index finger vs others for now to differentiate pointing vs open hand
        index_extended = extended[1]
        others_extended = sum(extended[2:]) # Middle, Ring, Pinky
        
        # Open Hand: Index is out AND at least 2 of the other 3 fingers are out
        if index_extended and others_extended >= 2:
            return 0 # Open Hand (Pick)
            
        # Pointing: Index is out AND all other 3 fingers are curled
        if index_extended and others_extended == 0:
            return 1 # Pointing
        
        return -1 # Unrecognized/Unstable Gesture
    
    def is_finger_extended(self, mcp, pip, tip, threshold_angle=5):
        v1 = np.array([pip.x - mcp.x, pip.y - mcp.y, pip.z - mcp.z])
        v2 = np.array([tip.x - pip.x, tip.y - pip.y, tip.z - pip.z])
        
        v1_u = v1 / np.linalg.norm(v1)
        v2_u = v2 / np.linalg.norm(v2)
  
        dot_product = np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)
        angle = np.degrees(np.arccos(dot_product))
        
        # If the angle between segments is small, the finger is straight
        return angle < threshold_angle


    # Detect MP hands and ray from current 
    def sample_frame(self, color, depth, lm):
        h, w = self.h, self.w
        tip = lm.landmark[8]
        knuckle = lm.landmark[6]

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
        return p_tip, ray
    
    # Intersections 
    def check_sphere_intersections(self, ray_origin, ray_dir, object_centers, radius=CUBE_SIZE):
        hits = []
        
        for center in object_centers:
            # Dist from object to pointer finger projected on ray
            L = center - ray_origin
            closest_approach = np.dot(L, ray_dir)
            
            # Object behind the hand 
            if closest_approach < 0:
                continue

            # If ray is further than the radius   
            d2 = np.dot(L, L) - closest_approach * closest_approach
            if d2 > radius**2:
                continue
                
            # Find distance along ray to intersection points
            half_cord = np.sqrt(radius**2 - d2)
            
            hit_point = closest_approach - half_cord
            
            hits.append((center, hit_point))
            
        # Sort hits by distance (closest first if we have multiple objects in a row)
        hits.sort(key=lambda x: x[1])
        return hits
    
    def solve(self, frame_data, objects):
        t_robot_cam = np.linalg.inv(self.t_cam_robot)

        print(f"Robot thinks camera is at: {t_robot_cam[:3, 3]}")

        intersect_rob, intersection_cam = None, None

        #t_robot_cam should be camera frame -> robot frame
        # p_tips = np.array([f[0] for f in self.frame_buffer])
        # rays = np.array([f[1] for f in self.frame_buffer])
        # p_tip_cam = np.mean(p_tips, axis=0)
        # ray_cam = np.mean(rays, axis=0)

        p_tip_cam = frame_data[0]
        ray_cam = frame_data[1]
        ray_cam /= np.linalg.norm(ray_cam)

        pointer_rob = (t_robot_cam @ np.append(p_tip_cam, 1))[:3]
        ray_rob = (t_robot_cam[:3, :3] @ ray_cam)
        ray_rob /= np.linalg.norm(ray_rob)

        print("p_tip_z:", pointer_rob[2])
        print("dir_z:", ray_rob[2])

        if abs(ray_rob[2]) < 1e-6:
            return None

         # Check Sphere Intersections!!
        if objects is not None:
            intersected_objects = self.check_sphere_intersections(pointer_rob, ray_rob, objects)
        
            if len(intersected_objects) > 0:
                best_hit = intersected_objects[0][1]
                intersect_rob = pointer_rob + (best_hit * ray_rob)
                print(f"Hit object at: {intersect_rob}")

        if intersect_rob is None:
            plane_normal_rob = np.array([0, 0, 1])
            plane_point_rob = np.array([0, 0, 0])

            dot_line_plane = np.dot(ray_rob, plane_normal_rob)
            if dot_line_plane >= 0:
                print("Warning: Pointing away from table")
                return None
                
            scalar = np.dot((plane_point_rob - pointer_rob), plane_normal_rob) / dot_line_plane
            
            intersect_rob = pointer_rob + scalar * ray_rob

        intersection_cam = (self.t_cam_robot @ np.append(intersect_rob, 1))[:3]

        return p_tip_cam, ray_cam, pointer_rob, ray_rob, intersect_rob, intersection_cam

    # Visualizations and Debuggers
    def draw_active_ray(self, frame, frame_data, end_point):
        if frame_data is None: return frame

        origin_3d, _ = frame_data
        p1_raw = self.proj_3d_2d(origin_3d * 1000.0)
        p2_raw = self.proj_3d_2d(end_point * 1000.0)

        if p1_raw and p2_raw:
            p1 = (
                int(np.clip(p1_raw[0], 0, self.w - 1)),
                int(np.clip(p1_raw[1], 0, self.h - 1)))
            p2 = (int(np.clip(p2_raw[0], 0, self.w - 1)),
                int(np.clip(p2_raw[1], 0, self.h - 1)))

            cv2.line(frame, p1, p2, (255, 0, 255), 3)
            cv2.circle(frame, p1, 5, (0, 0, 255), -1)

        return frame

    def visualize(self, frame, origin_cam, ray_cam=None, intersection_cam=None, enable3d=None):
        # 2D Projection
        origin_cam *= 1000.0
        p0 = self.proj_3d_2d(origin_cam)
        if self.valid_pixel(p0):
            cv2.circle(frame, p0, 5, (255,0,0), -1)

        if ray_cam is not None and intersection_cam is not None : 
            intersection_cam *= 1000.0
            p_int = self.proj_3d_2d(intersection_cam)
            if self.valid_pixel(p0) and self.valid_pixel(p_int):
                cv2.line(frame, p0, p_int, (0, 255, 0), 2)
                cv2.circle(frame, p_int, 5, (0, 0, 255), -1)
            else:
                print("Skipping full ray draw: invalid projection")

        # print(origin_cam, intersection_cam)
        # print(p0, p_int)

        # 3D Visualization
        if enable3d is not None:
            frame_pcd = self.zed_to_pcd(self.depth, self.image, 1000.0)

            points = np.array([origin_cam, intersection_cam])
            lines = [[0,1]]
            line_set = o3d.geometry.LineSet()
            line_set.points = o3d.utility.Vector3dVector(points)
            line_set.lines = o3d.utility.Vector2iVector(lines)
            line_set.colors = o3d.utility.Vector3dVector([[0,1,0]])

            intersect_point = o3d.geometry.TriangleMesh.create_sphere(radius=2.0)
            intersect_point.translate(intersection_cam)
            intersect_point.paint_uniform_color([0, 0, 1]) # Blue dot

            # Coordinate Frame to see the Origin
            coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=20, origin=[0, 0, 0])

            # Launch Viewer
            o3d.visualization.draw_geometries([frame_pcd, line_set, intersect_point, coord_frame])
        return frame
    
    def landmark_motion(self, lm):
        if lm is None or not lm.landmark:
            return float('inf')
        
        check_indices = [5, 8, 17] 
        curr_list = []
        
        for i, idx in enumerate(check_indices):
            p_3d = self.proj_2d_3d(lm.landmark[idx])
            if p_3d is not None:
                curr_list.append(p_3d)
            elif self.prev_landmarks is not None:
                curr_list.append(self.prev_landmarks[i])
            else:
                # Initial frame fallback
                curr_list.append(np.array([0.0, 0.0, 0.0]))

        curr = np.array(curr_list)

        if self.prev_landmarks is None or self.prev_landmarks.shape != curr.shape:
            self.prev_landmarks = curr
            return float('inf')

        diff = np.linalg.norm(curr - self.prev_landmarks, axis=1)
        motion = np.mean(diff)

        self.prev_landmarks = curr
        return motion
    
    def draw_progress_bar(self, frame, progress):
        h, w = frame.shape[:2]
        bar_width = int(w * 0.4)
        bar_height = 30
        x_start = (w - bar_width) // 2
        y_start = h - 50

        cv2.rectangle(frame, (x_start, y_start), (x_start + bar_width, y_start + bar_height), (50, 50, 50), -1)
        cv2.rectangle(frame, (x_start, y_start), (x_start + int(bar_width * progress), y_start + bar_height), (0, 255, 0), -1)
        cv2.rectangle(frame, (x_start, y_start), (x_start + bar_width, y_start + bar_height), (255, 255, 255), 2)

        cv2.putText(frame, f"Stability: {int(progress * 100)}%", (x_start, y_start - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        return frame
    
    def run(self, objects=None):
        cv2.namedWindow("debug", cv2.WINDOW_NORMAL)
        # self.frame_buffer = []


        stable_counter = 0
        check_pose = True
        while check_pose:
            color = self.zed.image
            depth = self.zed.point_cloud

            self.node.get_logger().info(f"Running pointing system loop with depth data: {depth}")

            if color is None:
                continue
            if self.h is None or self.w is None:
                self.h, self.w = color.shape[:2]

            frame = cv2.cvtColor(color, cv2.COLOR_BGRA2BGR)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)

            if results.multi_hand_landmarks:
                lm = results.multi_hand_landmarks[0]
                
                motion = self.landmark_motion(lm)

                if motion < self.motion_thresh:
                    stable_counter += 1
                else:
                    stable_counter = 0

                progress = stable_counter / self.stable_frames
                frame = self.draw_progress_bar(frame, progress)
                sample = self.sample_frame(frame, depth, lm)
                gesture = self.detect_gesture(results)
                    # self.image = color
                    # self.depth = depth

                if sample is not None and gesture == 1:
                    self.node.get_logger().info("Gesture Detected: Pointing")
                    tip_cam, ray_cam, tip_rob, ray_rob, inter_rob, inter_cam = self.solve(sample, objects)

                    inter_rob[0] = np.clip(inter_rob[0], X_MIN, X_MAX)
                    inter_rob[1] = np.clip(inter_rob[1], Y_MIN, Y_MAX)
                 
                    # self.frame_buffer.clear()
                    if stable_counter >= self.stable_frames:
                        frame = self.visualize(frame, tip_cam, ray_cam=ray_cam, intersection_cam=inter_cam)
                        for object_pose in objects:
                            pose = np.eye(4)
                            pose[:3, 3] = object_pose
                            draw_pose_axes(frame, self.K, pose, size=CUBE_SIZE)
                        cv2.imshow("debug", frame)
                        cv2.waitKey(0)
                        check_pose = False
                        return inter_rob, 1, tip_rob, ray_rob
                    else:
                        frame = self.draw_active_ray(frame, sample, inter_cam)
                elif sample is not None and gesture == 0:
                    self.node.get_logger().info("Gesture Detected: Open Hand")
                    if stable_counter >= self.stable_frames:
                        palm_indices = [0, 1, 5, 9, 13, 17]
                        palm = np.array([
                            [lm.landmark[i].x, 
                            lm.landmark[i].y] 
                            for i in palm_indices
                        ])
                        palm = np.mean(palm, axis=0)
                        palm = SimpleNamespace(x=palm[0], y=palm[1])
                        palm_cam = self.proj_2d_3d(palm)
                        palm_rob = (np.linalg.inv(self.t_cam_robot) @ np.append(palm_cam, 1))[:3]
                        # self.frame_buffer.clear()

                        palm_rob[0] = np.clip(palm_rob[0], X_MIN, X_MAX)
                        palm_rob[1] = np.clip(palm_rob[1], Y_MIN, Y_MAX)
                        frame = self.visualize(frame, palm_cam)
                        for object_pose in objects:
                            pose = np.eye(4)
                            pose[:3, 3] = object_pose
                            draw_pose_axes(frame, self.K, pose, size=CUBE_SIZE)
                        cv2.imshow("debug", frame)
                        cv2.waitKey(0)
                        # Returns 0 when picking from hand, 1 when pointing to table
                        check_pose = False
                        return palm_rob, 0, None, None                   
                    

            for object_pose in objects:
                pose = np.eye(4)
                pose[:3, 3] = object_pose
                draw_pose_axes(frame, self.K, pose, size=CUBE_SIZE)

            cv2.imshow("debug", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break