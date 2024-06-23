import cv2 as cv 
import numpy as np 

image=cv.imread("E:/python program/Open CV/Pictures/png-transparent-beach-ball-ball-game-computer-wallpaper-sphere-thumbnail.png")
blank=np.zeros(image.shape[:2],dtype="uint8")
# cv.imshow("blank",blank)

rectangle=cv.rectangle(blank.copy(),(30,30),(100,100),255,-1)
# cv.imshow("rectangle",rectangle)

circle=cv.circle(blank.copy(),(100,100),50,255,-1)

masked=cv.bitwise_and(image,image,mask=circle)
cv.imshow("masked",masked)
cv.waitKey(0)