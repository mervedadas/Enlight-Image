import cv2
import numpy as np
size = 500
img = cv2.imread("assets/shapes.jpg")
img = cv2.resize(img, (size, size))
print(img)
print("-----------------------------------------------")
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_image)

print("-----------------------------------")
avg_s =img.mean()
print("hello im avg ", avg_s)
min=np.amin(img)
print("hello im min", min)
sum=0
cnt=0
for i in range(size):
    for j in range(size):
        for k in range(3):
            if(img[i][j])[k] == min:
                cnt += 1
                continue
            else:
                sum += (img[i][j])[k]
print("hello im cnt", cnt)
final_avg= sum/((size*size)-cnt)
print("im final", final_avg)
hsv_image[:, :, 0] = final_avg
out = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
cv2.imshow("images",  out)
cv2.imwrite("shapes1.jpg", out)
cv2.imshow('original', img)
row,col,channel = img.shape
roi = img[0:row, 0:col]
print(row, col, channel)
cv2.waitKey()
cv2.destroyAllWindows()

# print((img[0][1])[0])
