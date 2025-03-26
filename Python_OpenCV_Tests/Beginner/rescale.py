import cv2 as cv

img = cv.imread('/home/kotik2137/Images/1.8x.png')


def rescaleImage(img, scale=0.20):
    width=int(img.shape[1] * scale)
    height=int(img.shape[0] * scale)# 0 to wysokosc || 1 dlugosc
    dimensions=(width,height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

img_resized = rescaleImage(img)
cv.imshow('Anime', img_resized)
cv.waitKey(0)
