import cv2
import numpy as np
import matplotlib.pyplot as plt

input_path = "data/input/watch.jpg"
output_path = "data/output"
img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([50, 100], [80, 100], "c", linewidth=5)
# plt.show()

cv2.imwrite(output_path + "/watchgray.png", img)
