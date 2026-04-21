import numpy as np
import cv2
import mediapipe as mp
import open3d as o3d
from utils.zed_camera import ZedCamera

def zed_to_pcd(pcd, img):

    rgb = img[:, :, :3][..., ::-1].reshape(-1, 3) / 255.0
    xyz = pcd[:, :, :3].reshape(-1, 3)

    mask = ~np.isnan(xyz).any(axis=1)
    xyz_clean = xyz[mask]
    rgb_clean = rgb[mask]
    
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz_clean)
    pcd.colors = o3d.utility.Vector3dVector(rgb_clean)

    return pcd

def mediapipe_landmarks_to_o3d(landmarks, xyz_map, width, height, transform=None, color=[1, 0, 0]):
    points_3d = []
    for lm in landmarks:
        # Un-normalized Mediapipe results
        u = int(lm.x * width)
        v = int(lm.y * height)

        u = np.clip(u, 0, width - 1)
        v = np.clip(v, 0, height - 1)

        X, Y, Z, _ = xyz_map[v, u]
        if not np.isfinite(Z) or Z <= 0:
            continue
        p = np.array([X, Y, Z, 1.0])

        # Zed to o3d transformation
        if transform is not None:
            p = transform @ p

        points_3d.append(p[:3])
    if len(points_3d) == 0:
        return None

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.array(points_3d))
    pcd.paint_uniform_color(color)

    return pcd


def media_on_single_frame(image):
    mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
    results = mp_hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return results

def view(pcd, lm_pcd):
    o3d.visualization.draw_geometries([pcd, lm_pcd])


def mediapipe_visualization():
    zed = ZedCamera()
    while True:
        image = zed.image
        xyz_map = zed.point_cloud

        h, w = image.shape[:2]
        results = media_on_single_frame(image)
        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0].landmark
            lm_pcd = mediapipe_landmarks_to_o3d(landmarks, xyz_map, w, h)
            if lm_pcd is not None:
                pcd = zed_to_pcd(xyz_map, image)
                view(pcd, lm_pcd)
                break


# Cube Detection
def detect_cubes_from_pcd(pcd, plane_thresh=0.01, cluster_eps=0.02, min_points=100):
    plane_model, inliers = pcd.segment_plane(distance_threshold=plane_thresh,ransac_n=3, num_iterations=1000)
    objects = pcd.select_by_index(inliers, invert=True)

    labels = np.array(objects.cluster_dbscan(eps=cluster_eps, min_points=min_points, print_progress=False))

    max_label = labels.max()
    cubes = []

    for i in range(max_label + 1):
        cluster_idx = np.where(labels == i)[0]
        cluster = objects.select_by_index(cluster_idx)

        # Eliminates noise
        if len(cluster.points) < min_points:
            continue
        obb = cluster.get_oriented_bounding_box()

        center = obb.center
        extent = obb.extent      # w,h,d
        R = obb.R                # orientation 

        ratio = np.max(extent) / (np.min(extent) + 1e-6)
        if ratio < 1.5:  # cube-like
            cubes.append({
                "center": center,
                "rotation": R,
                "size": extent,
                "cluster": cluster,
                "obb": obb
            })
    return cubes

def cube_test():
    zed = ZedCamera()

    img = zed.image
    pcd_zed = zed.point_cloud
    pcd = zed_to_pcd(pcd_zed, img)
    cubes = detect_cubes_from_pcd(pcd)

    print(f"Detected {len(cubes)} cube candidates")

    geometries = [pcd]

    for i, cube in enumerate(cubes):

        print(f"\nCube {i}")
        print("Position:", cube["center"])
        print("Size:", cube["size"])
        print("Rotation:\n", cube["rotation"])

        # visualize OBB
        obb = cube["obb"]
        obb.color = (1, 0, 0)
        geometries.append(obb)

    o3d.visualization.draw_geometries(geometries)


if __name__ == "__main__":
    # cube_test()
    mediapipe_visualization()
