import cv2
import numpy as np


def nothing(n):
    pass


cam = cv2.VideoCapture(0)

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 480)

cv2.createTrackbar("H_Hue", "trackbars", 7, 255, nothing)
cv2.createTrackbar("L_Hue", "trackbars", 1, 255, nothing)
cv2.createTrackbar("H_Sat", "trackbars", 255, 255, nothing)
cv2.createTrackbar("L_Sat", "trackbars", 155, 255, nothing)
cv2.createTrackbar("H_Val", "trackbars", 255, 255, nothing)
cv2.createTrackbar("L_Val", "trackbars", 98, 255, nothing)

while 1:
    _, img = cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hh = cv2.getTrackbarPos("H_Hue", "trackbars")
    lh = cv2.getTrackbarPos("L_Hue", "trackbars")
    hs = cv2.getTrackbarPos("H_Sat", "trackbars")
    ls = cv2.getTrackbarPos("L_Sat", "trackbars")
    hv = cv2.getTrackbarPos("H_Val", "trackbars")
    lv = cv2.getTrackbarPos("L_Val", "trackbars")

    h_data = np.array([hh, hs, hv])
    l_data = np.array([lh, ls, lv])

    mask = cv2.inRange(hsv, l_data, h_data)
    new = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("img", img)
    cv2.imshow("hsv", hsv)
    cv2.imshow("new", new)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
