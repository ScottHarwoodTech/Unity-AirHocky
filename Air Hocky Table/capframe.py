import cv2
cap = cv2.VideoCapture(0)
while True:
    rem, frame= cap.read()
    print(frame.shape)
    cv2.imshow("frame",frame)
    cv2.waitKey(1)
