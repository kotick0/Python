#Module for closing windows with escape key
import cv2

def it(): 
    while True:
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            cv2.destroyAllWindows()
            break
