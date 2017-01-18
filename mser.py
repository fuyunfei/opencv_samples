import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg
img = cv2.imread('1_gray.jpg',0)
vis = cv2.imread('1_gray.jpg')
mser = cv2.MSER_create()
regions = mser.detectRegions(img)
for i in xrange(0,len(regions[0])):
	color=np.random.randint(155,255,3)
	for j in xrange(0,regions[0][i].shape[0]):
		ind=regions[0][i][j]
		vis[ind[1],ind[0]]=color
#cv2.imshow('img', vis)
#plt.imshow(vis)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.imshow(vis, interpolation='nearest')
plt.show()
