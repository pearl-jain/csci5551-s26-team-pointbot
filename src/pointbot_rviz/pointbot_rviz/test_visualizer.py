import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from .visualization_helpers import publish_object_markers, publish_hand_marker, publish_pointing_vector_marker, publish_selected_marker, publish_goal_marker, publish_text_marker

class TestVisualizer(Node):
    def __init__(self):
        super().__init__('test_visualizer')
        self.object_publisher = self.create_publisher(MarkerArray, '/object_markers', 10)
        self.hand_publisher = self.create_publisher(Marker, '/hand_marker', 10)
        self.vector_publisher = self.create_publisher(Marker, '/pointing_vector', 10)
        self.selected_publisher = self.create_publisher(Marker, '/selected_object', 10)
        self.goal_publisher = self.create_publisher(Marker, '/goal_marker', 10)
        self.text_publisher = self.create_publisher(Marker, '/state_text', 10)
        self.timer = self.create_timer(0.5, self.publish_all)

    def publish_all(self):
        positions = [(0.5 + i * 0.1, 0.2, 0.0) for i in range(3)]
        publish_object_markers(self.object_publisher, positions=positions)
        publish_hand_marker(self.hand_publisher)
        publish_pointing_vector_marker(self.vector_publisher)
        publish_selected_marker(self.selected_publisher)
        publish_goal_marker(self.goal_publisher)
        publish_text_marker(self.text_publisher)

def main():
    rclpy.init()
    node = TestVisualizer()
    rclpy.spin(node)
    rclpy.shutdown()