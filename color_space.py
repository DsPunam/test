import cv2 as cv 

image=cv.imread("E:/python program/Open CV/Pictures/gettyimages-157482029-612x612.jpg")

cv.imshow("original_image",image)

#converting to gray image
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("gray_image",gray)

#converting to HSV image
HSV=cv.cvtColor(image,cv.COLOR_BGR2HSV)
cv.imshow("HSV_image",HSV)

#converting to LAB image
LAB=cv.cvtColor(image,cv.COLOR_BGR2LAB)
cv.imshow("LAB_image",LAB)

#converting to RGB image
RGB=cv.cvtColor(image,cv.COLOR_BGR2RGB)
cv.imshow("RGB_image",RGB)

cv.waitKey(0)
'''
WE CAN NOT CONVERT A GRAY IMAGE TO HSV OR LAB DIRECTLY....FOR THIS WE HAVE TO FIRST CONVERT THE GRAY IMAGE
TO BGR THEN TO HSV..BECAUSE WE CAN CONVERT THE HSV TO BGR,LAB TO BGR AND RGB TO BGR..
'''