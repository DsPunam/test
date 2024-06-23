import cv2
import numpy as np
import os

#showing image in a single array

img=cv2.imread("E:\python program\Open CV\Pictures\human_face.jpg")
h=np.hstack((img,img))
v=np.vstack((h,h))

#saving image in a specific directory

cv2.imwrite("merge.png",v)

# cv2.imshow("image",v)
cv2.waitKey(0)
cv2.destroyAllWindows()

#slidshow

image_name=os.listdir(r"E:\python program\Open CV\Pictures")
print(image_name)

for image in image_name:
    path="E:\\python program\\Open CV\\Pictures"
    img=path + "\\" + image
    i=cv2.imread(img)
    # resized=cv2.resize(i,(300,300))
    cv2.imshow("image",i)
    cv2.waitKey(1000)

cv2.destroyAllWindows()
