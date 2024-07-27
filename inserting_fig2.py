import cv2
import numpy as np

# Events - Mouse Event 1

def event_mouse(event, x, y, flags, params):
        if event == 1:

            cv2.circle(img, center = (x,y), radius = 50, color = (255,0,0), thickness= -1)
    

cv2.namedWindow(winname = 'window')
cv2.setMouseCallback('window',event_mouse)

img = cv2.imread('shree_img.jpg')

while True:
    cv2.imshow('window',img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()