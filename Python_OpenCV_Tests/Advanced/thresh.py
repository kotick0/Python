import cv2 as cv
import close

img = cv.imread('Images/man.jpg')
#cv.imshow('Man', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#Simple threshholding
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#cv.imshow('Simple Thresholded Inverted', thresh_inv)

# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 6)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

close.it()
