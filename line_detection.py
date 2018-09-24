import numpy as np
import  cv2

img=cv2.imread('images.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150)

lines=cv2.HoughLinesP(edges, 1, np.pi/180, 50)

for Line in lines:
    x1,y1,x2,y2=Line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv2.imshow("Edges",edges)
cv2.imshow("images",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
