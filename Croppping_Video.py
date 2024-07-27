# Cropping while on Video capture mode.

import cv2
# Mouse click events
# Cropping with on-click and up-click , image h and w on left click event and channel info on right click
ix = -1
iy = -1
flag = False

def click_event(event, x, y, flags, params):
    
    global ix, iy , flag

    if event == cv2.EVENT_LBUTTONDOWN: # on-click
        flag = True
        ix = x
        iy = y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if flag == True:
            frame_copy = frame.copy()
            line_type = cv2.LINE_AA
            cv2.rectangle(frame_copy, (ix,iy) , (x,y) , (255,0,0) , 1 , line_type)
            cv2.imshow('window', frame_copy)


    elif event == cv2.EVENT_LBUTTONUP: # up-click
        flag = False
        cropped_image = frame[ix:x , iy:y]
        line_type = cv2.LINE_AA
        cv2.imshow('cropped_image', cropped_image)
        cv2.waitKey(0)      

    elif event == cv2.EVENT_RBUTTONDOWN:
        blue, green , red = frame[y,x,0] , frame[y,x,1] , frame[y,x,2]
        fontface = cv2.FONT_ITALIC
        text = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(frame, text, (x,y), fontface , 1, (44,97,144), cv2.LINE_AA)
        
cv2.namedWindow(winname = 'window')
event = cv2.setMouseCallback('window', click_event)

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        cv2.imshow('window', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()