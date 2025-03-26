import cv2 as cv
import close

img = cv.imread("/home/kotik2137/Images/RichG.jpg")
# cv.imshow("fox", img)

# Averaging

average = cv.blur(img, (3, 3))
#cv.imshow("Average", average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
#cv.imshow("Gaussian", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
#cv.imshow("Median", median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

close.it()
