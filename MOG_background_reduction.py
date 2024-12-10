import cv2
import numpy as np

input_path = "data/input/"
cap = cv2.VideoCapture(input_path + "people-walking.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow("fgmask", frame)
    cv2.imshow("frame", fgmask)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
