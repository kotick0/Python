import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

#img = cv.imread('/home/kotik2137/Images/1.8x.png')
#cv.imshow('Anime', img)

#Kolorowanie (tutaj na zielono)
#blank[200:300, 300:400] = 98,86,78
#cv.imshow('Blank', blank)

# rysowanie kwadr.
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#cv.imshow('Blank', blank)
#
#cv.waitKey(0)

# Rysowanie kola lol
#cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
#cv.imshow('circle', blank)
#if 0xFF==ord('q') & cv.waitKey(0):
#    cv.destroyAllWindows()

#RYSOWANIE LINII
#cv.line(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (0,255,8), thickness=3)
#cv.imshow('linia', blank)
#cv.waitKey(0)

#PISANIE TEKSTU NA ZDJECIU
cv.putText(blank, 'Siema Eniu!', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('text', blank)
cv.waitKey(0)
