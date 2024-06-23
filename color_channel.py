import cv2 as cv 
import numpy as np 

image=cv.imread("E:/python program/Open CV/Pictures/gettyimages-157482029-612x612.jpg")

'''
Syntax: cv2.split(m[, mv])

Parameters:

m: Input multi-channel array
mv: Output vector of arrays
'''
b,g,r=cv.split(image)
blank=np.zeros(image.shape[:2],dtype="uint8")
# cv.imshow("blank",blank)

#blue image
blue=cv.merge([b,blank,blank])
cv.imshow("blue",blue)

#green image
green=cv.merge([blank,g,blank])
cv.imshow("green",green)

#red image
red=cv.merge([blank,blank,r])
cv.imshow("red",red)

#merged image
merged_image=cv.merge([b,g,r])
cv.imshow("merged_image",merged_image)

cv.waitKey(0)