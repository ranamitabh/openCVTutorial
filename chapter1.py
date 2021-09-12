import cv2

print("package imported")

#capture images
#
# img = cv2.imread("/Users/monika/PycharmProjects/openCVTutorial/resources/jessicaAlba.jpeg")
#
# cv2.imshow("output" , img)
# cv2.waitKey(0)

#===================================================================================================================
#Capture video

# cap = cv2.VideoCapture("/Users/monika/PycharmProjects/openCVTutorial/resources/twoAndHalfMen.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("output",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#===================================================================================================================
#Capture video from webcam

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4, 480)
# cap.set(10, 500)
#
# while True:
#     success , img= cap.read()
#     cv2.imshow("webcam", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break