import cv2

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0),5 )
            cv2.imshow('Face detection', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cam.release()
cv2.destroyAllWindows()