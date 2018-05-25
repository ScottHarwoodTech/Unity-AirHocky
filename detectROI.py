import cv2

from grabscreen import grab_screen

screen = grab_screen((0,0,1920,1080))

print(cv2.selectROI(screen))
