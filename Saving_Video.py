import cv2
import numpy as np

# 

cap = cv2.VideoCapture(0)  # 0 - index rep your webcam

fourcc= cv2.VideoWriter_fourcc(*'XVID') # Format required by opencv while saving the video

out = cv2.VideoWriter('output.mp4', fourcc , 20.0 , (300,300)) # writing saved video takes the output file name, fourcc code , fps, and video size



while (True):
    ret , frame = cap.read()

    if ret == True:  # checks if the video is detected 

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('window', gray)
        out.write(gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # breaks the while Loop
    
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

