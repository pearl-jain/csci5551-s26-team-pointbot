from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA

COLORS = {"red": ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0), "green": ColorRGBA(r=0.0, g=1.0, b=0.0, a=1.0), "blue": ColorRGBA(r=0.0, g=0.0, b=1.0, a=1.0)}

def publish_object_markers(publisher, positions=[(0.0, 0.0, 0.0)], color="red"):
    objects = MarkerArray()
    for i, position in enumerate(positions):
        m = Marker()
        m.header.frame_id = "world"
        m.id = i
        m.type = Marker.CUBE
        m.action = Marker.ADD
        m.pose.position.x = position[0]
        m.pose.position.y = position[1]
        m.pose.position.z = position[2]
        m.scale.x, m.scale.y, m.scale.z = 0.025, 0.025, 0.025
        m.color = COLORS.get(color)
        objects.markers.append(m)
    publisher.publish(objects)

def publish_hand_marker(publisher, corner1=(0.35, -0.6, 0.45), corner2=(0.65, -0.4, 0.55)):
    x1, y1, z1 = corner1
    x2, y2, z2 = corner2
    xmin, xmax = (x1, x2) if x1 <= x2 else (x2, x1)
    ymin, ymax = (y1, y2) if y1 <= y2 else (y2, y1)
    zmin, zmax = (z1, z2) if z1 <= z2 else (z2, z1)
    p1 = Point(x=xmin, y=ymin, z=zmin)
    p2 = Point(x=xmax, y=ymin, z=zmin)
    p3 = Point(x=xmin, y=ymax, z=zmin)
    p4 = Point(x=xmax, y=ymax, z=zmin)
    p5 = Point(x=xmin, y=ymin, z=zmax)
    p6 = Point(x=xmax, y=ymin, z=zmax)
    p7 = Point(x=xmin, y=ymax, z=zmax)
    p8 = Point(x=xmax, y=ymax, z=zmax)
    edges = [
        (p1, p2), (p2, p4), (p4, p3), (p3, p1),
        (p5, p6), (p6, p8), (p8, p7), (p7, p5),
        (p1, p5), (p2, p6), (p3, p7), (p4, p8),
    ]
    m = Marker()
    m.header.frame_id = "world"
    m.id = 100
    m.type = Marker.LINE_LIST
    m.action = Marker.ADD
    m.scale.x = 0.01
    m.color = ColorRGBA(r=1.0, g=0.0, b=0.0, a=1.0)
    for a, b in edges:
        m.points.append(a)
        m.points.append(b)
    publisher.publish(m)

def publish_pointing_vector_marker(publisher, start=(0.5, -0.5, 0.5), end=(0.5, 0.2, 0.0)):
    m = Marker()
    m.header.frame_id = "world"
    m.id = 200
    m.type = Marker.LINE_STRIP
    m.action = Marker.ADD
    m.scale.x = 0.01
    m.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
    m.points = [Point(x=start[0], y=start[1], z=start[2]), Point(x=end[0], y=end[1], z=end[2])]
    publisher.publish(m)

def publish_selected_marker(publisher, position=(0.5, 0.2, 0.0)):
    m = Marker()
    m.header.frame_id = "world"
    m.id = 300
    m.type = Marker.CUBE
    m.action = Marker.ADD
    m.pose.position.x = position[0]
    m.pose.position.y = position[1]
    m.pose.position.z = position[2]
    m.scale.x, m.scale.y, m.scale.z = 0.026, 0.026, 0.026
    m.color = ColorRGBA(r=1.0, g=0.7, b=0.3, a=1.0)
    publisher.publish(m)

def publish_goal_marker(publisher, position=(0.2, 0.4, 0.0)):
    m = Marker()
    m.header.frame_id = "world"
    m.id = 400
    m.type = Marker.CUBE
    m.action = Marker.ADD
    m.pose.position.x = position[0]
    m.pose.position.y = position[1]
    m.pose.position.z = position[2]
    m.scale.x, m.scale.y, m.scale.z = 0.025, 0.025, 0.025
    m.color = ColorRGBA(r=0.0, g=0.0, b=0.0, a=0.5)
    publisher.publish(m)

def publish_text_marker(publisher, state="None"):
    m = Marker()
    m.header.frame_id = "world"
    m.id = 500
    m.type = Marker.TEXT_VIEW_FACING
    m.action = Marker.ADD
    m.pose.position.x = 0.0
    m.pose.position.y = 0.0
    m.pose.position.z = 0.5
    m.scale.z = 0.05
    m.color = ColorRGBA(r=1.0, g=1.0, b=1.0, a=1.0)
    m.text = f"State: {state}"
    publisher.publish(m)