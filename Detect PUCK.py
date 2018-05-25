import cv2
import numpy as np
from grabscreen import grab_screen
import sys

def nothing(x):
    pass

if len(sys.argv) == 1:
    start = grab_screen()#grab whole screen
    x,y,w,h = cv2.selectROI(start)
    x1,y1 = x+w,y+h
    print(x,x1,y,y1)
else:
    x,x1,y,y1 = map(int,sys.argv[1][1:-1].split(","))
    print(x,x1,y,y1)
    if len(sys.argv) == 4:
        colorDetect = False
        values = (sys.argv[2] + "," + sys.argv[3]).replace("(","").replace(")","").split(",")
        print(values)
        values = list(map(int,values))
        print(values)
        lower_red = np.array(values[:3])
        upper_red = np.array(values[3:])
        print(lower_red)
        print(upper_red)

    else:
        colorDetect = True
        cv2.namedWindow("Original")
        cv2.createTrackbar("H","Original",0,255,nothing)
        cv2.createTrackbar("S","Original",0,255,nothing)
        cv2.createTrackbar("V","Original",0,255,nothing)
        cv2.createTrackbar("H1","Original",0,255,nothing)
        cv2.createTrackbar("S1","Original",0,255,nothing)
        cv2.createTrackbar("V1","Original",0,255,nothing)




while 1:
    frame = grab_screen((x,y,x1,y1))
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if colorDetect:
        lower_red = np.array([cv2.getTrackbarPos("H","Original"),
                             cv2.getTrackbarPos("S","Original"),
                             cv2.getTrackbarPos("V","Original")])
        upper_red = np.array([cv2.getTrackbarPos("H1","Original"),
                             cv2.getTrackbarPos("S1","Original"),
                             cv2.getTrackbarPos("V1","Original"),])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    cv2.imshow('Original',frame)
    cv2.imshow('Averaging',smoothed)

    _, puck = cv2.threshold(smoothed, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow('Puck',puck)
    # x, y
    # y, x
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.willAllWindows()
