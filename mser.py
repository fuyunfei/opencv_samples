import cv2
import numpy as np
import matplotlib.pyplot as plt
import colorsys

img = cv2.imread('1_gray.jpg',0)
img = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
img = cv2.blur(img,(5,5))

vis = cv2.imread('1_gray.jpg')
vis = cv2.resize(vis,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

mser = cv2.MSER_create(1,600,20000,0.5,0.1,200,1,0.003,3)
regions = mser.detectRegions(img)
regions[0].sort(lambda x,y: cmp(len(y), len(x)))

for i in xrange(0,len(regions[0])):
	color=np.array(colorsys.hsv_to_rgb(np.random.rand(1),1,np.random.rand(1)*0.4+0.6))*255

	for j in xrange(0,regions[0][i].shape[0]):
		ind=regions[0][i][j]
		vis[ind[1],ind[0]]= np.squeeze(color)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',vis)
cv2.waitKey(0)
cv2.destroyAllWindows()