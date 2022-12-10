import cv2

cap = cv2.VideoCapture(0)


while 1:
    _, frame = cap.read()
    cv2.imshow("Cam", frame)
    if cv2.waitKey(1) == 27:
        break


cap.release()
cv2.destroyAllWindows()