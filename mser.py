#!/usr/bin/env python
import cv2
import numpy as np
import matplotlib.pyplot as plt
import colorsys

img = cv2.imread('../rosemailing/pic/9.jpg',0)
#img = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#img = cv2.bilateralFilter(img,7,150,150)
#img = cv2.blur(img,(5,5))

vis = cv2.imread('../rosemailing/pic/9.jpg',1)
#vis = cv2.resize(vis,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
mser = cv2.MSER_create(5,30,30000,0.25,0.2,200,1,0.003,9)
#mser = cv2.MSER_create()

regions = mser.detectRegions(img)
#regions[0].sort(lambda x,y: cmp(len(y), len(x)))
print len(regions[0])

for i in xrange(0,len(regions[0])):
	color=np.array(colorsys.hsv_to_rgb(np.random.rand(1),1,np.random.rand(1)*0.3+0.7))*255

	for j in xrange(0,regions[0][i].shape[0]):
		ind=regions[0][i][j]
		vis[ind[1],ind[0]]= np.squeeze(color)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.namedWindow('vis', cv2.WINDOW_NORMAL)

cv2.imshow('vis',vis)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
