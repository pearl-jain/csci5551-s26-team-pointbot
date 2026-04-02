# csci5551-s26-team-pointbot

**Team Members:**

Pearl Jain: jain0377@umn.edu: Vision Perception

Adam Yaj: yaj00002@umn.edu: Coordinator/Integration/Documentation

Alex Wan: wan02096@umn.edu: Planning

Nathan Stangler: stang451@umn.edu: Control + Manipulation

## ROS2 Guide
**Creating a ROS2 Package**
- Make sure the current directory is `src`  
`cd src`

- Create a new Python package  
`ros2 pkg create <package> --build-type ament_python`

- Create a new C++ package  
`ros2 pkg create <package>`

#
**Building ROS2 Packages**
- Build all packages  
`colcon build`

- Build select packages with their dependencies  
`colcon build --packages-up-to <package1> <package2> ...`

- Build select packages  
`colcon build --packages-select <package1> <package2> ...`
#
**Using ROS2 Nodes and Launch Files**
- Make sure you `source` whenever you build  
`source install/setup.bash`

- Running a ROS2 node  
`ros2 run <package> <node>`

- Running a ROS2 launch file  
`ros2 launch <package> <node>`

#
**Other Useful ROS2 Tips**
- Running rqt  
`rqt`

- Looking at active ROS2 topics  
`ros2 topic list`

- Looking at running ROS2 nodes  
`ros2 node list`