import  numpy as np
import  cv2
from urllib.request import  urlopen


mobile_video="http://192.168.1.101:8080/shot.jpg"

while True:
    img_resp = urlopen(mobile_video)
    img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    frame = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([10,90, 110])
    up_yellow = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, low_yellow, up_yellow)
    edges = cv2.Canny(mask, 75, 150)

    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=40)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    key = cv2.waitKey(25)
    if key == 27:
        break
img.release()
cv2.destroyAllWindows()