import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('Harcascades\haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Harcascades\haarcascade_eye.xml')

def detect(gray, frame):
    face = face_classifier.detectMultiScale(gray, 1.3, 5)
    for x,y,w,h in face:
        cv2.rectangle(frame, (x,y), (x+w , y+h), (255,0,0) , 2)
        # For Eyes
        eye_gray  = gray[y:y+h , x:x+w] 
        eye_frame = frame[y:y+h , x:x+w]
        eyes = eye_classifier.detectMultiScale(gray, 1.1, 3)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(frame, (ex,ey), (ex+ew , ey+eh), (255,0,0) , 2)

    return frame

video_capture = cv2.VideoCapture(0)
while True:
    _ , frame_image = video_capture.read()
    gray_scale = cv2.cvtColor(frame_image, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray_scale, frame_image)
    cv2.putText(canvas, org = (100,100) , fontScale = 1, color = (255,0,0), thickness = 1,text = "Shree's Eyes Identified", fontFace = cv2.FONT_ITALIC)
    cv2.imshow(" Test Video Face Detection " , canvas)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
video_capture.release()
cv2.destroyAllWindows()