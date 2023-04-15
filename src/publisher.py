#!/usr/bin/env python3
import rospy
from nav_msgs.msg import OccupancyGrid 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import threading
# import cv2
arr1=None
arr2=None
arr3=None

# rate = rospy.Rate(1)
# arr.data=[0 for i in range(160000)]
# print(arr)
# arr.data=np.zeros(400, 400).to_list()

def f(a1, a2, a3):
    rospy.loginfo("agsghsshsgsgfsfstshgsgsfsfs")
    np.save('array1_demo', arr1)
    np.save('array2_demo', arr2)
    np.save('array3_demo', arr3)
    rospy.loginfo(np.unique(a1))


def callback(data):
    global arr1
    arr1=np.array(data.data).reshape(data.info.height, data.info.width)
    f(arr1, arr2, arr3)
    # cmap = colors.ListedColormap(['Blue','red', 'Green'])
    # plt.imshow(arr)
    # plt.show()
    rospy.loginfo(arr1.shape)
    rospy.loginfo("1")

def callback2(data):
    global arr2
    arr2=np.array(data.data).reshape(data.info.height, data.info.width)
    # cmap = colors.ListedColormap(['Blue','red', 'Green'])
    # plt.imshow(arr_map)
    # plt.show()
    rospy.loginfo(arr2.shape)
    rospy.loginfo("2")

def callback3(data):
    global arr3
    arr3=np.array(data.data).reshape(data.info.height, data.info.width)
    # cmap = colors.ListedColormap(['Blue','red', 'Green'])
    # plt.imshow(arr_map)
    # plt.show()
    rospy.loginfo(arr3.shape)
    rospy.loginfo("3")

# def talker():
#     global arr
#     rospy.init_node('talker', anonymous=True)
#     pub = rospy.Publisher("/tb3_0/map", OccupancyGrid, queue_size=10)
#     rate = rospy.Rate(1)       # 10hz
#     while not rospy.is_shutdown():
#         hello_str = "Published"
#         rospy.loginfo(hello_str)
#         pub.publish(arr)
#         rate.sleep()

def listener():
    rospy.init_node('talker', anonymous=True)
    rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback)
    # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
    # rospy.spin()

def listener1():
    rospy.init_node('talker', anonymous=True)
    rospy.Subscriber("/tb3_1/map", OccupancyGrid, callback2)
    # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
    # rospy.spin()

def listener2():
    rospy.init_node('talker', anonymous=True)
    rospy.Subscriber("/tb3_2/map", OccupancyGrid, callback3)
    # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
    # rospy.spin()

if __name__ == '__main__':
    listener()
    listener1()
    listener2()
    rospy.sleep(0.1)
    rospy.spin()