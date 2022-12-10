import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    _, frame = cam.read()

    cv2.imshow("cam", frame)

    key = cv2.waitKey(1)
    if key == 32:
        cv2.imwrite("images/myface.jpg", frame)
    elif key == 27:
        break

