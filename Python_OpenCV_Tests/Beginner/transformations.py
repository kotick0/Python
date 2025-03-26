import cv2 as cv
import numpy as np
import sys
import close

img = cv.imread('/home/kotik2137/Downloads/image.png')

#cv.imshow('Image', img)
#TRANSLATION
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# przy -x translacja na lewo 
# przy -y translacja na gory
# przy x translacja na prawo 
# przy y translacja w dol

translated = translate(img, -200, -200)
#cv.imshow('Translated', translated)
#close.it()

#ROTATING IMAGES
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]


    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -180)
#cv.imshow('Rotated', rotated)
rotated_rotated = rotate(rotated, -45)
#cv.imshow('2xrotated', rotated_rotated)
#close.it()

#RESIZING IMAGES
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#FLIPPING IMAGES
flip = cv.flip(img, 1)
#cv.imshow('xd', flip)
#close.it()

#CROPPING IMAGES
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)
close.it()
