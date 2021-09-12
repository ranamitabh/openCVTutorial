import cv2
import numpy as np

img = cv2.imread("/Users/monika/PycharmProjects/openCVTutorial/resources/3cards.jpeg")

width , height = 250,350
pts1= np.float32([[128,226],[354,161],[207,520],[455,430]])
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img , matrix, (width,height))


cv2.imshow("img", img)
cv2.imshow("Output img", imgOutput)
cv2.waitKey(0)