import cv2 as cv
import close
import numpy as np


img = cv.imread('Images/man.jpg')
#cv.imshow('Man', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Man', gray)

# Laplacian (gradient method)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel (gradiant method)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("Combined Sobel", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)
close.it()
