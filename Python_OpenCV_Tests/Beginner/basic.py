import cv2 as cv

img = cv.imread('/home/kotik2137/Downloads/image.png')
# cv.imshow('Image', img)

#GRAYSCALE IMAGES
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)


#BLUR IMAGES
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)
#cv.waitKey(0)

#EDGE CASCODE (Edge Recognition) najjjs
canny = cv.Canny(blur, 125,125)
#cv.imshow('Canny', canny)
#cv.waitKey(0)

#Dialating IMages
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)
#cv.waitKey(0)

#ERODING IMAGES
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Eroded', eroded)
#cv.waitKey(0)

#RESIZING IMAGES
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#CROPPING INAMGES
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
