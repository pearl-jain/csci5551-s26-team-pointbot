from geometry_msgs.msg import PoseStamped 
import open3d as o3d
import numpy as np
import cv2
from pupil_apriltags import Detector

CUBE_TAG_FAMILY = 'tag36h11'
CUBE_TAG_ID = 4
CUBE_TAG_SIZE = 0.02045
CUBE_SIZE = 0.025

class ObjectPoseDetector():
    def __init__(self, camera_intrinsic):
        self.camera_intrinsic = camera_intrinsic

        self.detector = Detector(families=CUBE_TAG_FAMILY)

        size = CUBE_TAG_SIZE / 2
        self.square_3d = np.array([
            [-size, -size, 0], [size, -size, 0], [size, size, 0], [-size, size, 0]
        ], dtype=np.float32)
    
    def detect_cube_contours(self, image):
        blurred = cv2.bilateralFilter(image, 9, 75, 75)

        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        # Color range
        mask = cv2.inRange(hsv, np.array([0, 100, 50]), np.array([179, 255, 255]))

        # Remove noise
        # kernel = np.ones((5,5), np.uint8)
        # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Find countours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Select contours
        cube_data = []
        for contour_index, contour in enumerate(contours):
            area = cv2.contourArea(contour)

            if area < 100 or area > 500:
                continue
            
            # Remove rounded corners by approximating contors to a polygon
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approximate_contour = cv2.approxPolyDP(contour, epsilon, True)

            if not cv2.isContourConvex(approximate_contour):
                continue

            # Get a bounding box
            x, y, w, h = cv2.boundingRect(approximate_contour)

            cube_data.append({
                "id": contour_index,
                "contour": approximate_contour,
                "center": (x + w//2, y + h//2),
                "bbox": (x, y, w, h)
            })
        
        return cube_data

    def show_cube_countour(self, cube, image):
        image = image.copy()

        x, y, w, h = cube['bbox']

        cv2.drawContours(image, [cube["contour"]], -1, (0, 0, 255), 1)
        
        cv2.putText(image, f"Cube {cube['id']}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)

        for point in cube["contour"]:
            x, y = point[0]            
            cv2.circle(image, (x, y), 1, (0, 255, 0), -1)
        
        cv2.imshow('Cube Contours', image)
        cv2.waitKey(0)

    def cube_icp_alignment(self, point_cloud):
        mesh_cube = o3d.geometry.TriangleMesh.create_box(
            width=CUBE_SIZE, height=CUBE_SIZE, depth=CUBE_SIZE
        )        

        mesh_cube.translate(-mesh_cube.get_center())
        source = mesh_cube.sample_points_uniformly(number_of_points=2000)

        target = o3d.geometry.PointCloud()
        target.points = o3d.utility.Vector3dVector(point_cloud)

        inital_translation = np.eye(4)
        inital_translation[:3, 3] = target.get_center()

        threshold = 0.01  # Search distance (1cm)
        reg_p2p = o3d.pipelines.registration.registration_icp(
            source, target, threshold, inital_translation,
            o3d.pipelines.registration.TransformationEstimationPointToPoint(),
            o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=50)
        )

        return reg_p2p.transformation

    def detect_april_tag_poses(self, observation, camera_pose):
        # Detect AprilTag Points
        if len(observation.shape) > 2:
            observation = cv2.cvtColor(observation, cv2.COLOR_BGRA2GRAY)

        params = [self.camera_intrinsic[0][0], self.camera_intrinsic[1][1], self.camera_intrinsic[0][2], self.camera_intrinsic[1][2]]
        tags = self.detector.detect(observation, estimate_tag_pose=True, camera_params=params, tag_size=CUBE_TAG_SIZE)

        if not tags:
            print('No tags detected.')
            return None

        cubes = []
        for tag in tags:
            if tag.tag_id != CUBE_TAG_ID:
                continue

            t_cam_cube = np.eye(4)
            t_cam_cube[:3, :3] = tag.pose_R
            t_cam_cube[:3, 3] = tag.pose_t.flatten()

            t_robot_cube = np.linalg.inv(camera_pose) @ t_cam_cube
            t_robot_cube[2, 3] = t_robot_cube[2, 3] - CUBE_SIZE / 2

            cubes.append(t_robot_cube)

        return cubes

    def detect_individual_cube_pose(self, observation, point_cloud):
        cube_data = self.detect_cube_contours(observation)     

        print(f"Detected {len(cube_data)} cubes.")

        for cube in cube_data:
            self.show_cube_countour(cube, observation)
            # points = cube["contour"].astype(np.float32)

            # success, rvec, tvec, inliers = cv2.solvePnPRansac(self.square_3d, points, self.camera_intrinsic, None)

            # print(success, rvec, tvec, inliers)

        object_pose = PoseStamped()

        return object_pose
    
    def closest_cube(self, cubes, pose):
        if not cubes:
            return None, None

        ref_position = pose[:3, 3]
        
        closest_dist = float('inf')
        closest_idx = -1

        for i, cube_pose in enumerate(cubes):
            cube_position = cube_pose[:3, 3]
            
            dist = np.linalg.norm(ref_position - cube_position)
            
            if dist < closest_dist:
                closest_dist = dist
                closest_idx = i

        # Return the pose of the closest cube and its distance
        return cubes[closest_idx], closest_dist


if __name__ == "__main__":
    fovX = 2.1
    w = 1980
    h = 1080
    focal_length = (w / 2) / np.tan(np.deg2rad(fovX / 2))
    K = np.array([
        [focal_length, 0, w / 2],
        [0, focal_length, h / 2],
        [0, 0, 1]
    ])

    detector = ObjectPoseDetector(K)

    image = cv2.imread("image.png")

    detector.detect_individual_cube_pose(image, "")
    print(detector.detect_april_tag_poses(image, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]))