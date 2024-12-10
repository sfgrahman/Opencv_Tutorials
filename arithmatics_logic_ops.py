import cv2
import numpy as np

input_path = "data/input/"

img1 = cv2.imread(input_path + "3D-Matplotlib.png")
img2 = cv2.imread(input_path + "mainlogo.png")
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
# addition operation
# img = img1 + img2
# img = cv2.add(img1, img2)
# img = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow("image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
