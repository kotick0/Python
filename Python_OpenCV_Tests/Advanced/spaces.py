# SWITCHING BETWEEN COLOR-SPACES
import close
import cv2 as cv

img = cv.imread("/home/kotik2137/Images/image.png")
# cv.imshow('fox', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# BGR to HSV (Hue)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

# BGR to l*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("RGB", rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv_bgr", hsv_bgr)

close.it()
