from geometry_msgs.msg import PoseStamped 
# import open3d as o3d
import numpy as np
import cv2
from pupil_apriltags import Detector

import math

class ObjectPoseDetector():
    def __init__(self, camera_intrinsic):
        self.camera_intrinsic = camera_intrinsic

        self.cube_model_points = np.array([
            (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
            (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 1, 1)
        ], dtype=np.float32)

        self.cube_model_points = self.cube_model_points * 25 # mm
    
    def detect_cube_contours(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        image = cv2.bilateralFilter(image, 9, 75, 75)

        # Color range
        lower = np.array([0, 100, 0])
        upper = np.array([179, 255, 255])

        # Mask out colors
        mask = cv2.inRange(hsv, lower, upper)

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

    def detect_april_tag_poses(self, image):
        pass

    def detect_individual_cube_pose(self, image, point_cloud):
        cube_data = self.detect_cube_contours(image)     

        print(f"Detected {len(cube_data)} cubes.")

        for cube in cube_data:
            self.show_cube_countour(cube, image)
            points = cube["contour"].astype(np.float32)

            # success, rvec, tvec, inliers = cv2.solvePnPRansac(self.cube_model_points, points, self.camera_intrinsic, None)

            # print(success, rvec, tvec, inliers)

        object_pose = PoseStamped()

        return object_pose

    def detect_pose(self):
        pass

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