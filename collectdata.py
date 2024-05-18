import cv2,time, math
from cvzone.HandTrackingModule import HandDetector
import numpy as np 

cap= cv2.VideoCapture(0, cv2.CAP_DSHOW)
detect = HandDetector(maxHands=1)
offset = 50
counter = 0
im_size = 400
im_dir = 'data/hello/'

while True:
    succes, img = cap.read()
    hands,img = detect.findHands(img)
    if hands:
        hand= hands[0]
        x,w,y,h = hand ['bbox']

        imgWhite = np.ones((im_size, im_size, 3),np.uint8)*255

        imgcrop=img[y-offset: y+h+offset,x-offset:x+w+offset]
        imgcropshape=imgcrop.shape
        aspectrat= h/w

        if aspectrat > 1:
            k= im_size/h
            wcal = math.ceil(k*w)
            im_resize= cv2.resize(imgcrop,(wcal, im_size))
            im_resizeshape = im_resize.shape
            wgap= math.ceil((im_size-wcal)/2)
            imgWhite[:,wgap:wcal+wgap] = im_resize

        else:
            k =im_size/w
            hcal = math.ceil(k*h)
            im_resize= cv2.resize(imgcrop,(im_size,hcal))
            im_resizeshape = im_resize.shape
            hgap= math.ceil((im_size-hcal)/2)
            imgWhite[hgap:hcal+hgap,:] = im_resize
        
        cv2.imshow("ImageCrop", imgcrop)
        cv2.imshow("ImageWhite", imgWhite)
    
    cv2.imshow("Hand", img)
    wkey= cv2.waitKey(1)
    if wkey == ord('c'):
        counter +=1
        cv2.imwrite(f'{im_dir}Image_.{time.time()}+.jpg', imgWhite)
        print(counter)
    elif wkey == ord('q'):
        break
