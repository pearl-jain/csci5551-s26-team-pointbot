import numpy as np
import time
import threading
import pyzed.sl as sl

class ZedCamera:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """Implement Singleton pattern to prevent multiple camera objects."""
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ZedCamera, cls).__new__(cls)
                cls._instance._initialized = False
            return cls._instance

    def __init__(self, resolution=sl.RESOLUTION.HD2K, fps=30):
        # Prevent re-initialization if the singleton already exists
        if self._initialized:
            return
            
        self._zed = sl.Camera()
        self._init_params = sl.InitParameters()
        self._init_params.camera_resolution = resolution
        self._init_params.camera_fps = fps
        self._init_params.depth_mode = sl.DEPTH_MODE.NEURAL
        self._init_params.coordinate_units = sl.UNIT.METER
        
        self._runtime_parameters = sl.RuntimeParameters()
        
        # Open the camera
        status = self._zed.open(self._init_params)
        if status != sl.ERROR_CODE.SUCCESS:
            raise ConnectionError(f"ZED Open Failed: {status}")

        # Warmup and Auto-exposure
        for _ in range(30):
            if self._zed.grab() == sl.ERROR_CODE.SUCCESS:
                break

        # Get Intrinsics
        calib = self._zed.get_camera_information().camera_configuration.calibration_parameters.left_cam
        self._camera_intrinsic = np.array([
            [calib.fx, 0, calib.cx],
            [0, calib.fy, calib.cy],
            [0, 0, 1]
        ])

        # Threading storage
        self._image_mat = sl.Mat()
        self._measure_xyz = sl.Mat()
        self._image = None
        self._point_cloud = None
        
        self._running = True
        self._data_lock = threading.Lock()
        self._thread = threading.Thread(target=self._update, daemon=True)
        self._thread.start()

        # Wait for first frame
        while self._image is None:
            time.sleep(0.1)
            
        self._initialized = True
        print("ZED Camera initialized and streaming.")

    def _update(self):
        while self._running:
            if self._zed.grab(self._runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                self._zed.retrieve_image(self._image_mat, sl.VIEW.LEFT)
                self._zed.retrieve_measure(self._measure_xyz, sl.MEASURE.XYZ)

                with self._data_lock:
                    self._image = self._image_mat.get_data().copy()
                    self._point_cloud = self._measure_xyz.get_data().copy()
            else:
                time.sleep(0.01)

    @property
    def image(self):
        with self._data_lock:
            return self._image if self._image is not None else None

    @property
    def point_cloud(self):
        with self._data_lock:
            return self._point_cloud if self._point_cloud is not None else None

    @property
    def camera_intrinsic(self):
        return self._camera_intrinsic

    def close(self):
        self._running = False
        if hasattr(self, '_thread'):
            self._thread.join()
        self._zed.close()
        ZedCamera._instance = None # Allow re-opening later if needed