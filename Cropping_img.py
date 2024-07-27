import cv2
import numpy as np

img = cv2.imread('shree_img.jpg')
flag = False
ix = -1
iy = -1

def crop_detect(event, x ,y, flags, params):
    global flag, ix, iy

    if event == 1: ## OnClick
        flag = True
        ix= x
        iy =y

        
    if event == 4: ## UpClick
        fx = x
        fy = y
        flag = False
        cv2.rectangle(img, (ix,iy) , (x,y) , (0,0,0) , 1)
        cropped_image = img[iy:fy , ix:fx]
        cv2.imshow('Cropped_image', cropped_image)
        cv2.waitKey(0)


cv2.namedWindow(winname = 'window')
cv2.setMouseCallback('window',crop_detect)

while True:
    
    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()