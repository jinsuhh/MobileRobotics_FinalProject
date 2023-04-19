import rospy
from nav_msgs.msg import OccupancyGrid 
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import threading
import cv2
import sys

class mergemaps_openCV():
    def __init__(self):
        arr1=np.load("array1_demo.npy")
        arr2=np.load("array2_demo.npy")
        arr3=np.load("array3_demo.npy")

        arr1[arr1==0]=255//4
        arr1[arr1==-1]=0
        arr1[arr1==100]=255
        self.arr1=arr1.astype('uint8')
        # cv2.imshow('img',arr3)
        # cv2.waitKey(0)

        arr2[arr2==0]=255//4
        arr2[arr2==-1]=0
        arr2[arr2==100]=255
        self.arr2=arr2.astype('uint8')

        arr3[arr3==0]=255//4
        arr3[arr3==-1]=0
        arr3[arr3==100]=255
        self.arr3=arr3.astype('uint8')

        # Create a feature detector and descriptor
        self.detector = cv2.ORB_create()

        # Find keypoints and descriptors in both maps
        self.keypoints1, self.descriptors1 = self.detector.detectAndCompute(self.arr1, None)
        self.keypoints2, self.descriptors2 = self.detector.detectAndCompute(self.arr2, None)
        self.keypoints3, self.descriptors3 = self.detector.detectAndCompute(self.arr3, None)

        self.all_params=[[self.arr1, self.keypoints1, self.descriptors1],
                          [self.arr2, self.keypoints2, self.descriptors2],
                            [self.arr3, self.keypoints3, self.descriptors3]]

    def match_two_images(self, i, j):  # i, j are 1,2,3
        # Create a matcher
        arr1, kp1, desc1, arr2, kp2, desc2=self.get_all_params(i, j)
        # matcher=cv2.DescriptorMatcher_create('BruteForce')
        # # Find matching keypoints in both maps
        # matches = matcher.knnMatch(desc1, desc2, k=2)
        index_params = dict(algorithm=6,
                            table_number=6,
                            key_size=12,
                            multi_probe_level=2)
        search_params = {}
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(desc1, desc2, k=2)
        goodmatch = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                goodmatch.append([m])
        matches=goodmatch
        if len(matches)>3:
            #Plot
            kp_img1 = cv2.drawKeypoints(arr1, kp1, None, color=(0,255,0), flags=0)
            kp_img2 = cv2.drawKeypoints(arr2, kp2, None, color=(0,255,0), flags=0)
            conc=np.concatenate((kp_img1, kp_img2), axis=1)
            # cv2.imshow('img',conc)
            # cv2.waitKey(0)

            # plot_imgs(kp_img1, kp_img2)
            match_plot = cv2.drawMatchesKnn(arr1, kp1, arr2, kp2, matches[:20], None, flags=2)
            cv2.imshow('plot',match_plot)
            cv2.waitKey(0)

            p1, p2=[], []
            for match in matches:
                p1.append(kp1[match[0].queryIdx].pt)
                p2.append(kp2[match[0].trainIdx].pt)
            p1=np.array(p1)
            p2=np.array(p2)
            print(p1, p2)
            # # Use RANSAC to estimate the transformation that maps arr1 onto arr2
            M, mask = cv2.estimateAffinePartial2D(p1, p2, cv2.RANSAC)
            M[:2, :2]/=np.linalg.det(M[:2, :2])   # Remove scaling
            print(M)
            # Warp array using the estimated transformation
            result = cv2.warpAffine(arr1, M, (arr2.shape[1], arr2.shape[0]))

            # # Merge the two maps
            merged_map = cv2.addWeighted(arr2, 0.5, result, 0.5, 0.0)
            # Wall in both is wall
            merged_map[merged_map>255//2]=255
            merged_map[(np.where((merged_map > 0) & (merged_map <= 255//2)))]=255//4

            merged_map=merged_map.astype('uint8')

            Hori = np.concatenate((arr1, arr2, merged_map), axis=1)
            cv2.imshow('m', Hori)
            cv2.waitKey(0)

            return merged_map
        else:
            return arr1

    def match_next(self, arr2, i):  # i, j are 1,2,3
        # Create a matcher
        arr1, kp1, desc1=self.all_params[i-1]
        kp2, desc2 = self.detector.detectAndCompute(arr2, None)
        # matcher=cv2.DescriptorMatcher_create('BruteForce')
        # # Find matching keypoints in both maps
        # matches = matcher.knnMatch(desc1,desc2, k=2)
        index_params = dict(algorithm=6,
                            table_number=6,
                            key_size=12,
                            multi_probe_level=2)
        search_params = {}
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(desc1, desc2, k=2)

        goodmatch = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                # print(m.distance)
                goodmatch.append([m])
        matches=goodmatch
        if len(matches)>3:
            #Plot
            kp_img1 = cv2.drawKeypoints(arr1, kp1, None, color=(0,255,0), flags=0)
            kp_img2 = cv2.drawKeypoints(arr2, kp2, None, color=(0,255,0), flags=0)
            conc=np.concatenate((kp_img1, kp_img2), axis=1)
            # cv2.imshow('img',conc)
            # cv2.waitKey(0)

            # plot_imgs(kp_img1, kp_img2)
            match_plot = cv2.drawMatchesKnn(arr1, kp1, arr2, kp2, matches[:20], None, flags=2)
            cv2.imshow('plot',match_plot)
            cv2.waitKey(0)

            p1, p2=[], []
            for match in matches:
                p1.append(kp1[match[0].queryIdx].pt)
                p2.append(kp2[match[0].trainIdx].pt)
            p1=np.array(p1)
            p2=np.array(p2)

            # # Use RANSAC to estimate the transformation that maps arr1 onto arr2
            M, mask = cv2.estimateAffinePartial2D(p1, p2, cv2.RANSAC)
            M[:2, :2]/=np.linalg.det(M[:2, :2])   # Remove scaling
            print(M)
            # Warp array using the estimated transformation
            result = cv2.warpAffine(arr1, M, (arr2.shape[1], arr2.shape[0]))

            # # Merge the two maps
            merged_map = cv2.addWeighted(arr2, 0.67, result, 0.33, 0.0)
            # Wall in both is wall
            merged_map[merged_map>255//2]=255
            merged_map[(np.where((merged_map > 0) & (merged_map <= 255//2)))]=255//4

            merged_map=merged_map.astype('uint8')

            Hori = np.concatenate((self.arr1, self.arr2, self.arr3, merged_map), axis=1)
            cv2.imshow('m', Hori)
            cv2.waitKey(0)

            return merged_map
        else:
            return arr2
        
    def form_t(theta, tx, ty):
        return np.array([[np.cos(theta), -np.sin(theta), tx], 
                        [np.sin(theta), np.cos(theta), ty], 
                        [0, 0, 1]])
    
    def get_all_params(self, i, j): # i, j are 1,2,3
        return self.all_params[i-1]+self.all_params[j-1]
    
a=mergemaps_openCV()
merged1=a.match_two_images(1,2)
print(merged1.shape)
merged=a.match_next(merged1, 3)

merged=merged.astype('int32')
merged[merged==0]=-1
merged[(np.where((merged > 0) & (merged <= 255//2)))]=0
merged[merged>255//2]=100



