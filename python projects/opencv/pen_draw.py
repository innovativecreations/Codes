import cv2
import my_lib
import numpy as np

red_colour_h = np.array([186, 207, 251])
red_colour_l = np.array([0, 101, 137])

lib = my_lib.All()

cam = cv2.VideoCapture(1)

lib.create_trackbars()

while cam.isOpened():
    _, frame = cam.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hh, lh, hs, ls, hv, lv = lib.return_trackbar_data()

    red_h = np.array([hh, hs, hv])
    red_l = np.array([lh, ls, lv])

    mask = cv2.inRange(hsv, red_l, red_h)
    colour = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("colour", colour)

    key = cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()


