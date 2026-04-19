import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import PoseStamped
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
        objects = []
        for i in range(3):
            object = PoseStamped()
            object.header.frame_id = "world"
            object.pose.position.x = 0.5 + i * 0.1
            object.pose.position.y = 0.2
            object.pose.position.z = 0.0
            objects.append(object)
        publish_object_markers(self.object_publisher, objects)
        hand1 = PoseStamped()
        hand1.header.frame_id = "world"
        hand1.pose.position.x = 0.35
        hand1.pose.position.y = -0.6
        hand1.pose.position.z = 0.45
        hand2 = PoseStamped()
        hand2.header.frame_id = "world"
        hand2.pose.position.x = 0.65
        hand2.pose.position.y = -0.4
        hand2.pose.position.z = 0.55
        publish_hand_marker(self.hand_publisher, hand1, hand2)
        start = PoseStamped()
        start.header.frame_id = "world"
        start.pose.position.x = 0.5
        start.pose.position.y = -0.5
        start.pose.position.z = 0.5
        end = PoseStamped()
        end.header.frame_id = "world"
        end.pose.position.x = 0.5
        end.pose.position.y = 0.2
        end.pose.position.z = 0.0
        publish_pointing_vector_marker(self.vector_publisher, start, end)
        selected = PoseStamped()
        selected.header.frame_id = "world"
        selected.pose.position.x = 0.5
        selected.pose.position.y = 0.2
        selected.pose.position.z = 0.0
        publish_selected_marker(self.selected_publisher, selected)
        goal = PoseStamped()
        goal.header.frame_id = "world"
        goal.pose.position.x = 0.2
        goal.pose.position.y = 0.4
        goal.pose.position.z = 0.0
        publish_goal_marker(self.goal_publisher, goal)
        publish_text_marker(self.text_publisher)

def main():
    rclpy.init()
    node = TestVisualizer()
    rclpy.spin(node)
    rclpy.shutdown()