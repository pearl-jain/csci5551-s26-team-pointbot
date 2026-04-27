import numpy as np
import cv2
import torch
import threading
import pyzed.sl as sl
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection

class ZedCamera:
    def __init__(self, resolution=sl.RESOLUTION.HD720, fps=30):
        self._zed = sl.Camera()
        init_params = sl.InitParameters()
        init_params.camera_resolution = resolution
        init_params.camera_fps = fps
        init_params.depth_mode = sl.DEPTH_MODE.NEURAL # High accuracy
        init_params.coordinate_units = sl.UNIT.METER
        
        err = self._zed.open(init_params)
        if err != sl.ERROR_CODE.SUCCESS:
            exit(-1)

        self._runtime_parameters = sl.RuntimeParameters()
        self._image_mat = sl.Mat()
        self._image = None
        self._running = True
        self._lock = threading.Lock()
        
        self._thread = threading.Thread(target=self._update, daemon=True)
        self._thread.start()
        
        while self._image is None:
            import time
            time.sleep(0.1)

    def _update(self):
        while self._running:
            if self._zed.grab(self._runtime_parameters) == sl.ERROR_CODE.SUCCESS:
                self._zed.retrieve_image(self._image_mat, sl.VIEW.LEFT)
                with self._lock:
                    self._image = self._image_mat.get_data().copy()

    def get_surface_data(self, x, y):
        """Uses ZED SDK to find plane normal/center at pixel (x,y)"""
        plane = sl.Plane()
        # find_plane_at_hit is significantly faster than manual RANSAC
        reset = self._zed.find_plane_at_hit(x, y, plane)
        if reset == sl.ERROR_CODE.SUCCESS:
            return {
                "normal": plane.get_normal(),
                "center": plane.get_center(),
                "valid": True
            }
        return {"valid": False}

    @property
    def image(self):
        with self._lock:
            return self._image.copy() if self._image is not None else None

    def close(self):
        self._running = False
        self._thread.join()
        self._zed.close()

class CubeAnalyzer:
    def __init__(self, model_id="IDEA-Research/grounding-dino-tiny"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = AutoProcessor.from_pretrained(model_id)
        self.model = AutoModelForZeroShotObjectDetection.from_pretrained(model_id).to(self.device)

    def detect_cubes(self, image, prompt="cube"):
        # Convert BGR (OpenCV) to RGB
        rgb_img = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
        
        inputs = self.processor(images=rgb_img, text=prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        results = self.processor.post_process_grounded_object_detection(
            outputs, inputs.input_ids, box_threshold=0.35, target_sizes=[image.shape[:2]]
        )[0]
        
        return results

if __name__ == "__main__":
    cam = ZedCamera(resolution=sl.RESOLUTION.HD720, fps=30)
    analyzer = CubeAnalyzer()

    print("Starting Detection... Press 'q' to quit.")

    try:
        while True:
            frame = cam.image
            if frame is None:
                continue

            # 1. Faster Detection
            detections = analyzer.detect_cubes(frame)

            # 2. Extract 3D Orientation via ZED SDK
            for box, score in zip(detections["boxes"], detections["scores"]):
                x1, y1, x2, y2 = box.cpu().numpy().astype(int)
                
                # Calculate center pixel of the detected box
                cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)
                
                # Get Plane data from ZED (Orientation)
                surface = cam.get_surface_data(cx, cy)
                
                # Draw 2D Box
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                if surface["valid"]:
                    n = surface["normal"]
                    c = surface["center"]
                    # Overlay 3D info
                    text = f"Normal: [{n[0]:.2f}, {n[1]:.2f}, {n[2]:.2f}]"
                    dist = np.linalg.norm(c)
                    cv2.putText(frame, text, (x1, y1 - 25), 1, 1, (0, 255, 0), 2)
                    cv2.putText(frame, f"Dist: {dist:.2f}m", (x1, y1 - 10), 1, 1, (255, 255, 0), 1)

            cv2.imshow("Real-Time Cube Detection", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cam.close()
        cv2.destroyAllWindows()