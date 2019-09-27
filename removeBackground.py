import cv2
import numpy as np

img = cv2.imread("assets/shapes2.jpg")
img=cv2.resize(img,(400,400))
cv2.imshow("original",img)
img = cv2.resize(img, (400, 400))
# row,col,channel = img.shape
# roi = img[0:row, 0:col]
# print(row, col, channel)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert gray
cv2.imshow("Gray",imgGray)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(imgGray, cv2.MORPH_OPEN, kernel)  #erode + dilation
cv2.imshow("opening",opening)
ret, binary= cv2.threshold(opening,90, 255, cv2.THRESH_BINARY)    #binary thresholding
cv2.imshow("binary",binary)
blur = cv2.GaussianBlur(binary,(5,5),0)   #gaussian blur
cv2.imwrite("shapes3.jpg",blur)
cv2.imshow("blur",blur)
cv2.waitKey()
cv2.destroyAllWindows()



