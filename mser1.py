#!/usr/bin/env python
import cv2
import numpy as np
import sys
import colorsys

img = cv2.imread('1_gray.jpg',0)
img = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

vis = cv2.imread('1_gray.jpg')
vis = cv2.resize(vis,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

mser = cv2.MSER_create()
regions = mser.detectRegions(img, None)
regions.sort(lambda x,y: cmp(len(y), len(x)))

for i in range(0,len(regions)):
    color=np.array(colorsys.hsv_to_rgb(np.random.rand(1),1,np.random.rand(1)*0.4+0.6))*255
    for j in range(regions[i].shape[0]):
        vis[regions[i][j][1],regions[i][j][0]]=np.squeeze(color)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',vis)
cv2.waitKey(0)
cv2.destroyAllWindows()


