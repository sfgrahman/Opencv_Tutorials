import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobel_x = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)  # Gradient in x-direction
    sobel_y = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)  # Gradient in y-direction
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow("original", frame)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("sobel_x", sobel_x)
    cv2.imshow("sobel_y", sobel_y)
    cv2.imshow("Canny", edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
