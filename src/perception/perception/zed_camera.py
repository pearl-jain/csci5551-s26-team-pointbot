import rclpy
from rclpy.node import Node
from rclpy.executors import SingleThreadedExecutor
from sensor_msgs.msg import Image, CameraInfo, PointCloud2
from cv_bridge import CvBridge

from sensor_msgs_py import point_cloud2

import numpy as np
import threading

class ZedCamera(Node):
    def __init__(self):
        super().__init__("zed_camera_client")
        self.bridge = CvBridge()
        self._image = None
        self._camera_intrinsic = None
        self._pc = None

        # These subscriptions now belong to the PerceptionActionServer node
        self.info_sub = self.create_subscription(
            CameraInfo, '/zed/zed_node/depth/camera_info', self._info_cb, 10)
        self.img_sub = self.create_subscription(
            Image, '/zed/zed_node/rgb/color/rect/image', self._img_cb, 10)
        self.pc_sub = self.create_subscription(
            PointCloud2, '/zed/zed_node/point_cloud/cloud_registered', self._pc_cb, 10)

        # Background Spinning logic
        self._executor = SingleThreadedExecutor()
        self._executor.add_node(self)
        
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run_node, daemon=True)
        self._thread.start()
        
        self._initialized = True
        self.get_logger().info("Standalone ZED Node started in background thread.")

    def _run_node(self):
        """Internal thread to handle ROS 2 callbacks."""
        while rclpy.ok() and not self._stop_event.is_set():
            self._executor.spin_once(timeout_sec=0.1)

    def _info_cb(self, msg):
        self._camera_intrinsic = np.array(msg.k).reshape((3, 3))

    def _img_cb(self, msg):
        self._image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
    
    def _pc_cb(self, msg):
        points = point_cloud2.read_points(msg, skip_nans=False, field_names=("x", "y", "z"))
        self._pc = np.array(list(points))

    @property
    def image(self):
        return self._image

    @property
    def camera_intrinsic(self):
        return self._camera_intrinsic
    
    @property
    def point_cloud(self):
        return self._pc
    
    def shutdown(self):
        self._stop_event.set()
        self._thread.join()
        self.destroy_node()