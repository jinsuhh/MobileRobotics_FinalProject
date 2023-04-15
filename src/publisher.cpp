#include "ros/ros.h"
#include "nav_msgs/OccupancyGrid.h"

void chatterCallback(const nav_msgs::OccupancyGrid::ConstPtr& msg)
{
       ROS_INFO_STREAM("This is my index: " << msg->data[0]);
}
int main(int argc, char **argv)
{
   ros::init(argc, argv, "listener");
   ros::NodeHandle n;
   ros::Subscriber sub = n.subscribe("/map", 1000, chatterCallback);
   ros::spin();
 
   return 0;
}