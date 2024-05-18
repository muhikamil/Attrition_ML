import cv2
import os
import time
import uuid

img_dir='Tensorflow/images/collectedimages'

labels = ['hello','thanks','yes','no','iloveyou']
num = 15

for label in labels:
    os.mkdir ('RealTimeObjectDetection/Tensorflow/images/collectedimages\\'+label)
    cap= cv2.VideoCapture(0)
    print('Collecting image for: '.format(label))
    time.sleep(5)
    for imgnum in range(num):
        ret, frame = cap.read()
    imgname = os.path.join(img_dir, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
    cv2.imwrite(imgname, frame)
    cv2.imshow('frame',frame)
    time.sleep(2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows