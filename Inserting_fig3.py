# Interesting program that lets you join data points you visit ( after 2 visits)

import cv2
import numpy as np

flag= False
ix = -1
iy = -1

def mouse_event_function(event, x, y, flags, params):

    global flag, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y) ,3, (255,34,134), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0,255,0), 5)
        cv2.imshow('window', img)


    elif event == cv2.EVENT_RBUTTONDOWN:
        flag = True
        ix = x
        iy = y

    elif event == cv2.EVENT_MOUSEMOVE:
        if flag == True:
            frame_copy = img.copy()
            cv2.rectangle(frame_copy, (ix,iy), (x,y), (25,67,45) ,1)
            cv2.imshow('window',frame_copy)

    elif event == cv2.EVENT_RBUTTONUP:
        flag = False
        xe = x
        ye = y
        cropped_img = img[ix:xe , iy:ye]
        cv2.imshow('cropped_window', cropped_img)
        cv2.waitKey(0)   

cv2.namedWindow(winname = 'window')
cv2.setMouseCallback('window' , mouse_event_function)

img = np.zeros((512,512,3), np.uint8)
points = []

while True:
    cv2.imshow('window', img)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()