import cv2


class All:
    def __init__(self):
        pass

    def nothing(n ,a):
        pass

    def create_trackbars(self):
        cv2.namedWindow("trackbars")
        cv2.resizeWindow("trackbars", 640, 480)
        cv2.createTrackbar("H_Hue", "trackbars", 255, 255, self.nothing)
        cv2.createTrackbar("L_Hue", "trackbars", 0, 255, self.nothing)
        cv2.createTrackbar("H_Sat", "trackbars", 255, 255, self.nothing)
        cv2.createTrackbar("L_Sat", "trackbars", 0, 255, self.nothing)
        cv2.createTrackbar("H_Val", "trackbars", 255, 255, self.nothing)
        cv2.createTrackbar("L_Val", "trackbars", 0, 255, self.nothing)

    @staticmethod
    def return_trackbar_data():
        hh = cv2.getTrackbarPos("H_Hue", "trackbars")
        lh = cv2.getTrackbarPos("L_Hue", "trackbars")
        hs = cv2.getTrackbarPos("H_Sat", "trackbars")
        ls = cv2.getTrackbarPos("L_Sat", "trackbars")
        hv = cv2.getTrackbarPos("H_Val", "trackbars")
        lv = cv2.getTrackbarPos("L_Val", "trackbars")
        return hh, lh, hs, ls, hv, lv



