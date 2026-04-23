import cv2
import numpy as np
import mediapipe as mp
from utils.zed_camera import ZedCamera
import math
from checkpoint0 import get_transform_camera_robot
from debug import zed_to_pcd
import open3d as o3d

CUBE_TAG_SIZE = 0.02045
TARGET_FRAMES = 5

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

    def detect_hand_pose(lm):
        # angle between pointer and middle finger 
        m1 = (lm.landmark[7].x - lm.landmark[8].x ) / (lm.landmark[7].y - lm.landmark[8].y)
        m2 = (lm.landmark[11].x - lm.landmark[12].x ) / (lm.landmark[11].y - lm.landmark[12].y)

        angle = math.acrtan((m1-m2)/(1 + m1 * m2))

        if angle > math.pi:
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

    def solve(self):

        #t_cam_robot should be camera frame -> robot frame
        p_tips = np.array([f[0] for f in self.frame_buffer])
        rays = np.array([f[1] for f in self.frame_buffer])
        p_tip_cam = np.mean(p_tips, axis=0)
        ray_cam = np.mean(rays, axis=0)
        ray_cam /= np.linalg.norm(ray_cam)

        ## WORKING LOGIC but transforms back and forth alot Comment ot

        # Extend from the tip of the pointer to the table
        pointer_rob = (self.t_cam_robot @ np.append(p_tip_cam, 1))[:3]
        ray_rob = (self.t_cam_robot[:3, :3] @ ray_cam)
        ray_rob /= np.linalg.norm(ray_rob)
        print("p_tip_z:", pointer_rob[2])
        print("dir_z:", ray_rob[2])

        if abs(ray_rob[2]) < 1e-6:
            return None

        plane_normal = np.array([0, -1, 0])
        plane_point = np.array([0, 100, 0])
        dot_line_plane = np.dot(ray_rob, plane_normal)
        scalar = np.dot((plane_point - pointer_rob), plane_normal) / dot_line_plane
        intersect = pointer_rob + scalar * ray_rob
        intersection_cam = (np.linalg.inv(self.t_cam_robot) @ np.append(intersect, 1))[:3]
        return p_tip_cam, ray_cam, intersect, intersection_cam
    
    # TRY UNCOMMENTING AND USING THIS WHEN WE HAVE THE SET UP!!

        # # t_robot_cam should be robot frame -> camera frame
        # t_robot_cam = np.linalg.inv(t_cam_robot)
        # plane_point_cam = t_robot_cam[:3, 3] 
        # plane_normal_cam = t_robot_cam[:3, :3] @ np.array([0, 0, 1])

        # dot= np.dot(ray_cam, plane_normal_cam)
        
        # if abs(dot) < 1e-6:
        #     return None # Ray is parallel to the table
            
        # scalar = np.dot((plane_point_cam - p_tip_cam), plane_normal_cam) / dot
        # intersection_cam = p_tip_cam + scalar * ray_cam
        # intersection_robot = (self.t_cam_robot @ np.append(intersection_cam, 1))[:3]

        # return p_tip_cam, ray_cam, intersection_robot, intersection_cam

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
        frame_pcd = zed_to_pcd(self.depth, self.image)
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

        interesct_marker = o3d.geometry.TriangleMesh.create_sphere(radius=2.0)
        interesct_marker.translate(intersection_cam)
        interesct_marker.paint_uniform_color([0, 0, 1]) # Blue dot

        # Coordinate Frame to see the Origin
        coord_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=20, origin=[0, 0, 0])

        # Launch Viewer
        o3d.visualization.draw_geometries([frame_pcd, line_set, plane_set, interesct_marker, coord_frame])
        return frame
    
    def run(self):
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
                    self.image = color
                    self.depth = depth
                    self.h, self.w, _ = frame.shape
                    # First version usage
                    # tip_cam, ray_cam, tip_rob, ray_rob, inter, inter_cam = self.solve(t_cam_robot)
                    # Second version usage
                    tip_cam, ray_cam, inter_rob, inter_cam = self.solve()
                    frame = self.visualize(frame, tip_cam, ray_cam, inter_cam)
                    cv2.imshow("debug", frame)
                    cv2.waitKey(0)
                    self.frame_buffer.clear()

                    return inter_rob

            cv2.imshow("debug", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def main():
    zed = ZedCamera()
    # t_cam_robot = get_transform_camera_robot(zed.image, zed.camera_intrinsic)
    t_cam_robot = np.eye(4)
    cam = PointBot(zed, t_cam_robot)
    result = cam.run()
    print("Final intersection:", result)


    zed.close()


if __name__ == "__main__":
    main()