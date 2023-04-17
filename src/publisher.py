#!/usr/bin/env python3
import rospy
from nav_msgs.msg import OccupancyGrid 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import threading

class local2global():
    def __init__(self):
        self.arr1=None
        self.arr2=None
        self.arr3=None
        self.arr=OccupancyGrid()

    def f(self, a1, a2, a3):
        rospy.loginfo("inside function")
        np.save('array1_demo', self.arr1)
        np.save('array2_demo', self.arr2)
        np.save('array3_demo', self.arr3)
        rospy.loginfo(np.unique(a1))


    def callback(self, data):
        rospy.loginfo("Header1")
        rospy.loginfo(data.header)
        rospy.loginfo("Info1")
        rospy.loginfo(data.info)
        self.arr1=np.array(data.data).reshape(data.info.height, data.info.width)
        # f(arr1, arr2, arr3)
        # cmap = colors.ListedColormap(['Blue','red', 'Green'])
        # plt.imshow(arr)
        # plt.show()
        # rospy.loginfo(arr1.shape)
        # rospy.loginfo("1")

    def callback2(self, data):
        rospy.loginfo("Header2")
        rospy.loginfo(data.header)
        rospy.loginfo("Info2")
        rospy.loginfo(data.info)
        self.arr2=np.array(data.data).reshape(data.info.height, data.info.width)
        # cmap = colors.ListedColormap(['Blue','red', 'Green'])
        # plt.imshow(arr_map)
        # plt.show()
        # rospy.loginfo(arr2.shape)
        # rospy.loginfo("2")

    def callback3(self, data):
        rospy.loginfo("Header3")
        rospy.loginfo(data.header)
        rospy.loginfo("Info3")
        rospy.loginfo(data.info)
        self.arr3=np.array(data.data).reshape(data.info.height, data.info.width)
        # cmap = colors.ListedColormap(['Blue','red', 'Green'])
        # plt.imshow(arr_map)
        # plt.show()
        # rospy.loginfo(arr2.shape)
        # rospy.loginfo("2")

    def callbackG(self, data):
        self.arr=data
        self.arr.header.frame_id="tb3_0/map"
        self.arr.info.origin.position.x=-10.0
        self.arr.info.origin.position.y=-10.0
        rospy.loginfo("HeaderGlobal")
        rospy.loginfo(data.header)
        rospy.loginfo("InfoGlobal")
        rospy.loginfo(data.info)
        self.arrG=np.array(data.data).reshape(data.info.height, data.info.width)
        # cmap = colors.ListedColormap(['Blue','red', 'Green'])
        # plt.imshow(arr_map)
        # plt.show()
        # rospy.loginfo(arr3.shape)
        # rospy.loginfo("3")

    def talker(self):
        # arr.origin.position.x-=0.4
        # arr.origin.position.y-=0.4
        rospy.init_node('listener', anonymous=True)
        pub = rospy.Publisher("/tb3_0/map", OccupancyGrid, queue_size=10)
        rate = rospy.Rate(1)       # 10hz
        while not rospy.is_shutdown():
            hello_str = "Published"
            rospy.loginfo(hello_str)
            rospy.loginfo(self.arr.info)
            pub.publish(self.arr)
            rate.sleep()

    def listener(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/tb3_0/map", OccupancyGrid, self.callback)
        # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
        # rospy.spin()

    def listener1(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/tb3_1/map", OccupancyGrid, self.callback2)
        # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
        # rospy.spin()

    def listener2(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/tb3_0/map", OccupancyGrid, self.callback3)
        # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
        # rospy.spin()

    def listenerG(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/map", OccupancyGrid, self.callbackG)
        # rospy.Subscriber("/tb3_0/map", OccupancyGrid, callback2)
        # rospy.spin()

if __name__ == '__main__':
    loc2glob=local2global()
    loc2glob.listener()
    loc2glob.listener1()
    loc2glob.listener2()
    loc2glob.listenerG()
    loc2glob.talker()
    rospy.sleep(1)
    rospy.spin()