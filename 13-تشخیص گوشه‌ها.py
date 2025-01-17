import cv2
import numpy as np 
 
img = cv2.imread('p1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
 
corners = cv2.goodFeaturesToTrack(gray, 200, 0.1, 10)
corners = np.int32(corners)
 
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, (0, 255, 255), 1)
 
cv2.imshow('corners', img)
 
cv2.waitKey(0)