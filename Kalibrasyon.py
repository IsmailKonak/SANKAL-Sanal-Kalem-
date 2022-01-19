# -*- coding: utf-8 -*-
# Coded By İsmail Konak
# Mail: i_konak@hotmail.com

import cv2
import numpy as np
from place import idread, hsvHwrite, hsvLwrite

def renk():
    def bos(x):
        pass

    barsWindow = 'Kalibrasyon'
    hl = 'H Min'
    hh = 'H Max'
    sl = 'S Min'
    sh = 'S Max'
    vl = 'V Min'
    vh = 'V Max'

    idreal = idread()
    cap = cv2.VideoCapture(int(idreal))

    cv2.namedWindow(barsWindow, flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow(barsWindow,(600,600))

    def ppp():
        print("hi")

    cv2.createTrackbar(hl, barsWindow, 0, 179, bos)
    cv2.createTrackbar(hh, barsWindow, 0, 179, bos)
    cv2.createTrackbar(sl, barsWindow, 0, 255, bos)
    cv2.createTrackbar(sh, barsWindow, 0, 255, bos)
    cv2.createTrackbar(vl, barsWindow, 0, 255, bos)
    cv2.createTrackbar(vh, barsWindow, 0, 255, bos)

    cv2.setTrackbarPos(hl, barsWindow, 0)
    cv2.setTrackbarPos(hh, barsWindow, 179)
    cv2.setTrackbarPos(sl, barsWindow, 0)
    cv2.setTrackbarPos(sh, barsWindow, 255)
    cv2.setTrackbarPos(vl, barsWindow, 0)
    cv2.setTrackbarPos(vh, barsWindow, 255)

    while (True):
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hul = cv2.getTrackbarPos(hl, barsWindow)
        huh = cv2.getTrackbarPos(hh, barsWindow)
        sal = cv2.getTrackbarPos(sl, barsWindow)
        sah = cv2.getTrackbarPos(sh, barsWindow)
        val = cv2.getTrackbarPos(vl, barsWindow)
        vah = cv2.getTrackbarPos(vh, barsWindow)

        HSVLOW = np.array([hul, sal, val])
        HSVHIGH = np.array([huh, sah, vah])

        mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
        maskedFrame = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Maskelenecek Alan', maskedFrame)
        hsvHwrite(f"{huh}, {sah}, {vah}")
        hsvLwrite(f"{hul}, {sal}, {val}")
        if cv2.waitKey(5) & 0xFF == ord('q'):

            break
    print("hi")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    renk()