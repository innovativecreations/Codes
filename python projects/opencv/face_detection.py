import cv2

face_cas = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
# img = cv2.imread("images/myface.jpg")

cam = cv2.VideoCapture(0)
cam.set(10,200)
while cam.isOpened():
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors= 8)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow("img", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
# cv2.waitKey(0)


