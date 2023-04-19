# MobileRobotics_FinalProject
This is ROB530 Team 11 Final project on Real-time multi-agent Simultaneous Localization and Mapping (SLAM) and map fusion. This project implements the multi-agent SLAM in simulation using Turtlebot3s and different Turtlebot world environments.
## Environment
* Ubuntu 18.04
* ROS-melodic
## ROS Directory
* ttb3_multi_slam
## 1. ROS Requirements
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
sudo apt install ros-melodic-multirobot-map-merge ros-melodic-explore-lite ros-melodic-navigation
```
### 1-4. SLAM Gmapping
```
$ git clone https://github.com/ros-perception/slam_gmapping
```
## 2. Installation
```
$ mkdir -p ~/catkin_ws/src
$ git clone {THIS_REPO}
$ cd ~/catkin_ws && catkin_make
```
## 3. How to run:
* Everytime you open a new terminal you have to source!
```
$ ~/catkin_ws source devel/setup.bash
```
* TURTLEBOT3_MODEL options: burger, waffle, waffle_pi (pick your model)
```
export TURTLEBOT3_MODEL=burger 
```
* Good to echo this in your ~/.bashrc, as you don't have to keep calling this when opening new terminal
```
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
```
* Terminal1: Set up mapping and robot environment
```
roslaunch ttb3_multi_slam final_multi_mapping.launch
```
* Terminal2: Robot should start moving after this command. Sit back and let them explore the map for you.
```
roslaunch ttb3_multi_slam final_multi_explore.launch 
```
---

## 4. Acknowledgments:
* Special thanks to Professor Maani Ghaffari Jadidi and the Mobile Robotics Graduate Student Instructors for helping guide our project and providing support in completing the project.
```
---

## 5. References:
[Turtlebot3 Simulation Tutorial](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/)<br>
[move_base](http://wiki.ros.org/move_base)<br>
[gmapping](http://wiki.ros.org/gmapping)<br>
[explore_lite](http://wiki.ros.org/explore_lite)<br>
[multirobot_map_merge](http://wiki.ros.org/multirobot_map_merge)<br>

