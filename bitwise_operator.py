import cv2 as cv 
import numpy as np 

# image=cv.imread("E:/python program/Open CV/Pictures/png-transparent-beach-ball-ball-game-computer-wallpaper-sphere-thumbnail.png")
blank=np.zeros((400,400),dtype="uint8")
# cv.imshow("blank",blank)

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
# cv.imshow("rectangle",rectangle)

circle=cv.circle(blank.copy(),(200,200),200,255,-1)
# cv.imshow("circle",circle)

#bitwise_add
'''
Syntax: cv2.bitwise_and(source1, source2, destination, mask)
Parameters: 
source1: First Input Image array(Single-channel, 8-bit or floating-point) 
source2: Second Input Image array(Single-channel, 8-bit or floating-point) 
dest: Output array (Similar to the dimensions and type of Input image array) 
mask: Operation mask, Input / output 8-bit single-channel mask 
'''

And=cv.bitwise_and(rectangle,circle)
# cv.imshow("And",And)

#bitwise_or
Or=cv.bitwise_or(rectangle,circle)
# cv.imshow("Or",Or)

#bitwise_xor
Xor=cv.bitwise_xor(rectangle,circle)
# cv.imshow("Xor",Xor)

#bitwise_not
Not=cv.bitwise_not(rectangle,circle)
cv.imshow("Not",Not)
cv.waitKey(0)