import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# cv2.imshow("metrix" , img)

cv2.line(img,(0,0), (img.shape[1],img.shape[0]),((255,255,0)),3)
# cv2.line(img,(0,0), (200,100),((255,255,0)),3)
# cv2.rectangle(img, (0,0),(200,150),(255,0,255),31)
cv2.rectangle(img, (0,0),(200,150),(255,0,255),cv2.FILLED)
cv2.circle(img, (300,100),30,(0,255,255),10)
cv2.putText(img, "Amitabh", (350,200), cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0,255,255),2)

cv2.imshow("img ", img)
cv2.waitKey(0)