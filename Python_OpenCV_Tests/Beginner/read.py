import cv2 as cv
#
#img = cv.imread('/home/kotik2137/Images/1.8x.png')
#
#cv.imshow('Anime', img)
#
#cv.waitKey(0)

capture = cv.VideoCapture('/home/kotik2137/Downloads/test.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow("Test", frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
