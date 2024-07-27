# Drawing a Rectangle while Dragging (Mouse Click Event)

# Onclick event - 1
# Upclick event - 4

import cv2
import numpy as np

img = np.zeros((512,512,3))
draw = False
ix = -1
iy = -1

def draw_rect(event, x, y, flags , params):
    global draw, ix, iy

    if event==1:
        draw = True
        ix = x
        iy =y

    if event == 0:
        if draw == True:
            cv2.rectangle(img, (ix,iy), (x,y), (255,255,0), -1)

    if event == 4:
        draw = False
        cv2.rectangle(img, (ix,iy), (x,y), (255,255,0), -1)


cv2.namedWindow(winname = 'window')
cv2.setMouseCallback('window', draw_rect)

while True:
    cv2.imshow('window', img)
    cv2.putText(img, org = (50,50) , fontScale = 1, color = (255,0,0), thickness = 1,text = "Test Crop", fontFace = cv2.FONT_ITALIC)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

    
cv2.destroyAllWindows()