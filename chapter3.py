import cv2

img = cv2.imread("/Users/monika/PycharmProjects/openCVTutorial/resources/jessicaAlba.jpeg")

print("orig image shape :",img.shape)

imgResized = cv2.resize(img ,(100,75))

imgCropped = img[0:100 ,100:200 ]

print("resized img shape :",imgResized.shape)
print("cropped img shape :",imgCropped.shape)

cv2.imshow("orig img" , img)
cv2.imshow("resized img ", imgResized)
cv2.imshow("cropped img ", imgCropped)
cv2.waitKey(0)
