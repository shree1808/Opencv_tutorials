# This program detects face and eyes from an image 

import cv2
import numpy as np

face_classifier  = cv2.CascadeClassifier('Harcascades\haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Harcascades\haarcascade_eye.xml')


face = cv2.imread('shree_img.jpg')

gray = cv2.cvtColor(face , cv2.COLOR_BGR2GRAY)

scale = face_classifier.detectMultiScale(gray, 1.3 , 5)

if scale is ():
    print('No face is detected')

for x,y,w,h in scale:
    cv2.rectangle(face, (x,y) , (x+w , y+h), (127,0,255), 2)
    cv2.imshow('img',face)
    cv2.waitKey(0)

    # To crop till the eye
    crop_gray = gray[y:y+h, x:x+w]
    crop_color = face[y:y+h, x:x+w]

    eye = eye_classifier.detectMultiScale(crop_gray)

    for x1, y1, w1, h1 in eye:
        cv2.rectangle(crop_color, (x1, y1), (x1+ w1 , y1 + h1), (255,255,0), 2)
        cv2.imshow('img', face)
        cv2.waitKey(0)

cv2.destroyAllWindows()