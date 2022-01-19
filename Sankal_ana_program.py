# -*- coding: utf-8 -*-
# Coded By İsmail Konak
# Mail: i_konak@hotmail.com

import cv2
import numpy as np
from place import idread
from place import hsvHread, hsvLread

def main():
    idreal = idread()
    cap = cv2.VideoCapture(int(idreal))


    def dondur(n, frame):
        if n == -1:
            cv2.flip(frame, -1)
        elif n == 1:
            cv2.flip(frame, 1)
        elif n == 0:
            cv2.flip(frame, 0)


    while True:
        ret, img = cap.read()
        dondur(1, img)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        Low = hsvLread()
        High = hsvHread()
        HSVLOW = np.array([int(Low[0]),int(Low[1]),int(Low[2])])
        HSVHIGH = np.array([np.array([int(High[0]),int(High[1]),int(High[2])])])
        mask = cv2.inRange(hsv, HSVLOW, HSVHIGH)
        ret, maskedFrame = cv2.threshold(mask, 127, 240, cv2.THRESH_BINARY_INV)
        cv2.imshow("Sanal Kalem", maskedFrame)
        k = cv2.waitKey(5)
        if k == ord("e"):
            break
    cv2.destroyAllWindows()
    cap.release()


if __name__ == '__main__':
    main()