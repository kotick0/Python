import cv2 as cv
import close
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


img = cv.imread("/home/kotik2137/github/python-opencv-tests/Advanced/Images/people.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2], dtype="uint8")


mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow("Mask", mask)

cv.imshow("masked", masked)
# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title("Color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

colors = ("b", "g", "r")

for i, col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(color_hist, color=col)
    plt.xlim([0, 256])


# plt.figure()
# plt.title("Color histogram", color_hist)
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.xlim([0, 256])
plt.show()

close.it()
