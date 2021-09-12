import cv2
import numpy as np

img = cv2.imread("/Users/monika/PycharmProjects/openCVTutorial/resources/jessicaAlba.jpeg")
kernal = np.ones((5,5),np.uint)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
imgBlur = cv2.GaussianBlur(imgGray , (7,7),0)
imgCanny = cv2.Canny(img, 150,200)
imgDilation = cv2.dilate(imgCanny , kernal , iterations= 1)
imgErode = cv2.erode(imgDilation , kernal, iterations=1)


cv2.imshow("original img", img)
cv2.imshow("gray image", imgGray)
cv2.imshow("Blur gray image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilated Canny image", imgDilation)
cv2.imshow("Erode Canny image", imgErode)
cv2.waitKey(0)