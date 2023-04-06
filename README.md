# MobileRobotics_FinalProject
## Environment
* Ubuntu 18.04
* ROS-melodic
## ROS Directory
* ttb3_multi_slam
## 1. Requirements
```
$ sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy \
  ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc \
  ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan \
  ros-melodic-rosserial-arduino ros-melodic-rosserial-python \
  ros-melodic-rosserial-server ros-melodic-rosserial-client \
  ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server \
  ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro \
  ros-melodic-compressed-image-transport ros-melodic-rqt* \
  ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers
```
### 1-1. Turtlebot3 packages
```
$ sudo apt-get install ros-melodic-turtlebot3
$ sudo apt-get install ros-melodic-turtlebot3-msgs
```
### 1-2. ROS Gazebo (melodic) packages
```
sudo apt-get install ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control
```
### 1-3. Multirobot Map Merge, Explore-lite, Navigation (move_base) packages
```
$ sudo apt install ros-melodic-multirobot-map-merge ros-melodic-explore-lite ros-melodic-navigation
```
### 1-4. SLAM Gmapping
```
$ git clone https://github.com/ros-perception/slam_gmapping
```
## 2. How to run:
* Terminal1:
```
roslaunch ttb3_multi_slam final_multi_mapping.launch
```
* Terminal2:
```
roslaunch ttb3_multi_slam final_multi_explore.launch 
```
---
## Reference
[Turtlebot3 Simulation Tutorial](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)<br>
[move_base](http://wiki.ros.org/move_base)<br>
[gmapping](http://wiki.ros.org/gmapping)<br>
[explore_lite](http://wiki.ros.org/explore_lite)<br>
[multirobot_map_merge](http://wiki.ros.org/multirobot_map_merge)<br>

