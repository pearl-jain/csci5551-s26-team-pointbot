from geometry_msgs.msg import PoseStamped 
import open3d as o3d
import numpy as np
import cv2
from perception.zed_camera import ZedCamera

from pupil_apriltags import Detector

CUBE_TAG_FAMILY = 'tag36h11'
CUBE_TAG_ID = 4
CUBE_TAG_SIZE = 0.02045
CUBE_SIZE = 0.025

class ObjectDectector():
    def __init__(self, camera_intrinsic):
        self.intrinsic = camera_intrinsic

        self.april_detector = Detector(families=CUBE_TAG_FAMILY)

        size = CUBE_TAG_SIZE / 2
        self.square_3d = np.array([
            [-size, -size, 0], [size, -size, 0], [size, size, 0], [-size, size, 0]
        ], dtype=np.float32)

    def detect_april_tag_poses(self, observation, camera_pose):
        # Detect AprilTag Points
        if len(observation.shape) > 2:
            observation = cv2.cvtColor(observation, cv2.COLOR_BGRA2GRAY)

        params = [self.camera_intrinsic[0][0], self.camera_intrinsic[1][1], self.camera_intrinsic[0][2], self.camera_intrinsic[1][2]]
        tags = self.april_detector.detect(observation, estimate_tag_pose=True, camera_params=params, tag_size=CUBE_TAG_SIZE)

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
    
    def detect_cube_poses(self, observation, point_cloud):
        cube_data = self.detect_cube_contours(observation)     
    
        cubes = []
        for cube in cube_data:
            cube_point_cloud = self.get_masked_pc(point_cloud, cube['contour'])
            
            t_matrix = self.object_detector.cube_icp_alignment(cube_point_cloud)
            
            cubes.append(t_matrix)

        return cubes

class ObjectPoseDetector():
    def __init__(self, camera_intrinsic):
        self.camera_intrinsic = camera_intrinsic

        self.object_detector = ObjectDectector(camera_intrinsic)
    
    def line_plane_intersect(self, line_point, line_direction, plane_point, plane_normal):
        dot_line_plane = np.dot(line_direction, plane_normal)

        if (abs(dot_line_plane) < 1e-6):
            return None
        
        scalar = np.dot((plane_point - line_point), plane_normal) / dot_line_plane
        return line_point + scalar * np.array(line_direction)

    def gaussian(self, x, x0, sigma_x, amplitude=1.0):
        exponent = -((x-x0)**2 / (2 * sigma_x**2))
        return amplitude * np.exp(exponent)

    def gaussian_2d(self, x, y, x0, y0, sigma_x, sigma_y, amplitude=1.0):
        exponent = -((x - x0)**2 / (2 * sigma_x**2) + (y - y0)**2 / (2 * sigma_y**2))
        return amplitude * np.exp(exponent)

    def pointing_object_space_scores(self, object_points, pointing_position, pointing_direction, pointing_uncertainty=0.02, uncertainty_growth=0.01):
        if (len(object_points) == 0):
            return None
        
        pointing_vector = pointing_direction / np.linalg.norm(pointing_direction)

        scores = []
        for point in object_points:
            relative_position = point - pointing_position
            distance = np.dot(relative_position, pointing_vector)
            if distance < 0:
                scores.append(0.0)
                continue

            perpendicular_distance = np.linalg.norm(relative_position - distance * pointing_vector)

            attention_score = self.gaussian(perpendicular_distance, 0, pointing_uncertainty + distance * uncertainty_growth)
            scores.append(attention_score)

        return scores


    def pointing_object_surface_scores(self, object_points, pointing_position, pointing_direction, pointing_uncertainty=0.1, uncertainty_growth=0.01):
        intersection_point = self.line_plane_intersect(pointing_position, pointing_direction, np.array([0, 0, 0]), np.array([0, 0, 1]))

        if (len(object_points) == 0) or (intersection_point is None):
            return None
        
        normalized_pointing_direction = pointing_direction / np.linalg.norm(pointing_direction)
        pointing_vector_2d = pointing_direction[:2] / np.linalg.norm(pointing_direction[:2])

        rotation_matrix = np.array([
            [pointing_vector_2d[0], pointing_vector_2d[1]],
            [-pointing_vector_2d[1], pointing_vector_2d[0]]
        ])

        angle_scalar = max(abs(normalized_pointing_direction[2]), 0.0001)

        distance = np.linalg.norm(intersection_point - pointing_position)
        distance_uncertainty = pointing_uncertainty + distance * uncertainty_growth
        direction_uncertanty = distance_uncertainty / angle_scalar

        scores = []
        for object_point in object_points:
            relative_position = object_point[:2] - intersection_point[:2]
            aligned_position = rotation_matrix @ relative_position

            attention_score = self.gaussian_2d(aligned_position[0], aligned_position[1], 0, 0, direction_uncertanty, distance_uncertainty)
            scores.append(attention_score)

        return scores

    def detect_cubes(self, observation, camera_pose):
        cube_poses = self.object_detector.detect_april_tag_poses(observation, camera_pose)

        return cube_poses
    
    def select_cube(self, cubes, attention_scores):
        if not cubes or not attention_scores:
            return None
        
        # TODO: Make this interact with the user

        return cubes[np.argmax(attention_scores)]

if __name__ == "__main__":
    zed = ZedCamera()

    detector = ObjectPoseDetector(zed.camera_intrinsic)

    cubes = [[-25, -32, 1], [30, -30, 1], [30, -20, 1]]

    attention_scores = detector.pointing_object_space_scores([[-25, -32, 1], [30, -30, 1], [30, -20, 1]], np.array([10, 10, 10]), np.array([0.2, -0.5, -0.1]))

    print(cubes)
    print(detector.pointing_object_surface_scores(cubes, np.array([10, 10, 10]), np.array([0.2, -0.5, -0.1])))
    print(detector.pointing_object_space_scores(cubes, np.array([10, 10, 10]), np.array([0.2, -0.5, -0.1])))

    print(detector.select_cube(cubes, attention_scores))

    # image = cv2.imread("image.png")

    # detector.detect_individual_cube_pose(image, "")
    # print(detector.detect_april_tag_poses(image, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1]]))
