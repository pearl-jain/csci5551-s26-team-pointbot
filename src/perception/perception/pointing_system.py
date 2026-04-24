import cv2
import numpy as np
import mediapipe as mp
import open3d as o3d

CUBE_TAG_SIZE = 0.02045
TARGET_FRAMES = 5
CUBE_SIZE = 0.025

class PointBot:
    def __init__(self, zed, t_cam):
        self.zed = zed
        self.K = zed.camera_intrinsic
        self.hands = mp.solutions.hands.Hands(
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8
        )
        self.frame_buffer = []   
        self.tags = None    
        self.t_cam_robot = t_cam
        self.t_cam_robot[:3, 3] *= 1000.0 # Convert from m to mm for consistency with depth units
        self.h, self.w, self.image, self.depth = None, None, None, None

        self.finger_gesture_table = [
            [0, 1, 0, 0, 0], # Pick From Table
            [1, 1, 1, 1, 1], # Pick From Table
        ]

    # 1. Update thresholds to be realistic for 3D Straightness (Ratio of ~1.0)
        self.finger_props = [
            (2, 3, 4, 0, 0.85),  # Thumb (MCP=2, PIP=3, Tip=4)
            (5, 6, 8, 0, 0.90),  # Index
            (9, 10, 12, 0, 0.90), # Middle
            (13, 14, 16, 0, 0.90),# Ring
            (17, 18, 20, 0, 0.90) # Pinky
        ]

    def zed_to_pcd(self, pcd, img):
        rgb = img[:, :, :3][..., ::-1].reshape(-1, 3) / 255.0
        xyz = pcd[:, :, :3].reshape(-1, 3)

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
        
        p_3d = self.depth[ty, tx][:3]
        if not np.isfinite(p_3d).all() or np.linalg.norm(p_3d) < 1e-3:
            return None 
        return p_3d
    

    def detect_gesture(self, landmark_results):
        multi_hand_landmarks = landmark_results.multi_hand_landmarks
        if not multi_hand_landmarks: return [-1]
        
        gestures = []
        for hand_landmarks in multi_hand_landmarks:
            extended = []
            for points in self.finger_props:
                mcp_idx, pip_idx, tip_idx, _, threshold = points
                
                m_3d = self.proj_2d_3d(hand_landmarks.landmark[mcp_idx])
                p_3d = self.proj_2d_3d(hand_landmarks.landmark[pip_idx])
                t_3d = self.proj_2d_3d(hand_landmarks.landmark[tip_idx])
                
                if m_3d is None or p_3d is None or t_3d is None:
                    # If 3D fails, assume the finger isn't extended 
                    extended.append(0)
                    continue
                    
                # Calculate if finger is straight
                finger_len = np.linalg.norm(t_3d - m_3d)
                max_len = np.linalg.norm(p_3d - m_3d) + np.linalg.norm(t_3d - p_3d)
                is_straight = int((finger_len / max_len) > threshold)
                extended.append(is_straight)
            
            print(f"States: {extended}") 
            
            # Match against table
            match_found = False
            for i, target in enumerate(self.finger_gesture_table):
                if extended == target:
                    gestures.append(i)
                    match_found = True
                    break
            
            if not match_found:
                gestures.append(0) # Default to pointing
                
        return gestures


    # Detect MP hands and ray from current 
    def sample_frame(self, color, depth, lm):
        h, w = self.h, self.w
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

    def solve(self):
        t_robot_cam = np.linalg.inv(self.t_cam_robot)

        print(f"Robot thinks camera is at: {t_robot_cam[:3, 3]}")

        #t_robot_cam should be camera frame -> robot frame
        p_tips = np.array([f[0] for f in self.frame_buffer])
        rays = np.array([f[1] for f in self.frame_buffer])
        p_tip_cam = np.mean(p_tips, axis=0)
        ray_cam = np.mean(rays, axis=0)
        ray_cam /= np.linalg.norm(ray_cam)

        pointer_rob = (t_robot_cam @ np.append(p_tip_cam, 1))[:3]
        ray_rob = (t_robot_cam[:3, :3] @ ray_cam)
        ray_rob /= np.linalg.norm(ray_rob)
        print("p_tip_z:", pointer_rob[2])
        print("dir_z:", ray_rob[2])

        if abs(ray_rob[2]) < 1e-6:
            return None

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
    
    def visualize(self, frame, p_tip_cam, ray_cam, intersection_cam):
        h, w = frame.shape[:2]

        # Project points
        p0 = self.proj_3d_2d(p_tip_cam)
        # Can draw to p1 which is a point in the direction where the person is pointing
        p1 = self.proj_3d_2d(p_tip_cam + 100 * ray_cam) 
        # p_int is the point where the pointing ray intersects with our plane
        p_int = self.proj_3d_2d(intersection_cam)

        if self.valid_pixel(p0) and self.valid_pixel(p_int):
            cv2.circle(frame, p0, 5, (255,0,0), -1)
            cv2.line(frame, p0, p_int, (0, 255, 0), 2)
            cv2.circle(frame, p_int, 5, (0, 0, 255), -1)
        else:
            print("Skipping full ray draw: invalid projection")

        point = [0,1,0]
        print(p_tip_cam, intersection_cam)
        print(p0, p_int)

        # 3D Visualization
        frame_pcd = self.zed_to_pcd(self.depth, self.image)
        points = np.array([p_tip_cam, intersection_cam])
        lines = [[0,1]]
        line_set = o3d.geometry.LineSet()
        line_set.points = o3d.utility.Vector3dVector(points)
        line_set.lines = o3d.utility.Vector2iVector(lines)
        line_set.colors = o3d.utility.Vector3dVector([[0,1,0]])


        # Draws Plane with arbitrary y-values for debugging
        side = 100 
        plane_height = 100 # Adjusted by Y
        
        # Define corners of the plane in the X-Z directions
        plane_corners = np.array([
            [-side, plane_height, -side],
            [ side, plane_height, -side],
            [ side, plane_height,  side],
            [-side, plane_height,  side]
        ])
        plane_lines = [[0, 1], [1, 2], [2, 3], [3, 0]]
        plane_set = o3d.geometry.LineSet()
        plane_set.points = o3d.utility.Vector3dVector(plane_corners)
        plane_set.lines = o3d.utility.Vector2iVector(plane_lines)
        plane_set.paint_uniform_color([1, 0, 0]) # Red boundary

        intersect_point = o3d.geometry.TriangleMesh.create_sphere(radius=2.0)
        intersect_point.translate(intersection_cam)
        intersect_point.paint_uniform_color([0, 0, 1]) # Blue dot

        # Coordinate Frame to see the Origin
        coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=20, origin=[0, 0, 0])

        # Launch Viewer
        o3d.visualization.draw_geometries([frame_pcd, line_set, plane_set, intersect_point, coord_frame])
        return frame
    
    def run(self):
        cv2.namedWindow("debug", cv2.WINDOW_NORMAL)

        check_pose = True
        while True:
            color = self.zed.image
            depth = self.zed.point_cloud

            if color is None:
                continue
            if self.h is None or self.w is None:
                self.h, self.w = color.shape[:2]

            frame = cv2.cvtColor(color, cv2.COLOR_BGRA2BGR)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)

            if results.multi_hand_landmarks:
                lm = results.multi_hand_landmarks[0]
                
                sample = self.sample_frame(frame, depth, lm)

                if len(self.frame_buffer) > TARGET_FRAMES:
                    self.image = color
                    self.depth = depth
                
                    if self.detect_gesture(results)[0] == 1:
                        print("Gesture Detected: Pick from Hand")
                        wrist_cam = self.proj_2d_3d(lm.landmark[0])
                        wrist_rob = (self.t_cam_robot @ np.append(wrist_cam, 1))[:3]
                        # Returns 0 when picking from hand, 1 when pointing to table
                        self.frame_buffer.clear()
                        frame = self.visualize(frame, wrist_cam, wrist_cam, wrist_cam)
                        cv2.imshow("debug", frame)
                        cv2.waitKey(0)
                        return wrist_rob, 0, None, None
                    else:
                        print("Gesture Detected: Pointing")

                        # First version usage
                        # tip_cam, ray_cam, tip_rob, ray_rob, inter, inter_cam = self.solve(t_cam_robot)
                        # Second version usage
                        tip_cam, ray_cam, tip_rob, ray_rob, inter_rob, inter_cam = self.solve()
                        frame = self.visualize(frame, tip_cam, ray_cam, inter_cam)
                        cv2.imshow("debug", frame)
                        cv2.waitKey(0)
                        self.frame_buffer.clear()
                        return inter_rob, 1, tip_rob, ray_rob

            cv2.imshow("debug", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
