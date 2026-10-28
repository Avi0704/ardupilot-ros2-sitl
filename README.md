# ardupilot-ros2-sitl

ROS 2 nodes for ArduPilot Copter SITL using the native DDS interface.

## Environment
- Ubuntu 22.04, ROS 2 Humble, Gazebo Harmonic
- ArduPilot (Copter SITL with DDS enabled): https://github.com/ArduPilot/ardupilot
- ArduPilot Gazebo plugin: https://github.com/ArduPilot/ardupilot_gazebo

## Packages
- `comeback` (ament_python): includes `altitude_logger`, a node that logs vehicle altitude.

## Setup
`ardupilot_msgs` is not stored in this repo. Link it from your ArduPilot checkout:

```bash
mkdir -p ~/ws/src && cd ~/ws/src
git clone https://github.com/Avi0704/ardupilot-ros2-sitl.git .
ln -s ~/ardupilot/Tools/ros2/ardupilot_msgs src/ardupilot_msgs
cd ~/ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
```

## Run
Start ArduPilot SITL with DDS enabled, then:

```bash
ros2 run comeback altitude_logger
```
