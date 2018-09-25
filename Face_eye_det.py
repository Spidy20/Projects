import numpy as np
import cv2
import requests
from urllib.request import  urlopen

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mobile_video="http://192.168.1.102:8080/shot.jpg"


while True:
    img_resp=urlopen(mobile_video)
    img_arr=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    img=cv2.imdecode(img_arr,-1)


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('android mobile capture',img)
    k = cv2.waitKey(1)
    if k == 27:
        break
#
# img.release()
# cv2.destroyAllWindows()