import cv2 as cv
import numpy as np
#cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)

image=cv.imread("E:/python program/Open CV/Pictures/image.jpg")
'''
In an affine transformation, the transformation matrix is a 2x3 matrix in which the first two 
columns represent the rotation and scaling components, and the third column represents the translation 
component.
cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)
'''
def translate(img):
    transmat=np.float32([[1,0,200],[0,1,200]])
    dimension=(image.shape[1],image.shape[0])
    return cv.warpAffine(img,transmat,dimension)

translate_image=translate(image)
# cv.imshow("image",translate_image)
# cv.waitKey(0)

#Rotation
#we can rotate an image by following ways
#number 1

# cv2.ROTATE_90_CLOCKWISE: Rotate the image 90 degrees clockwise.
# cv2.ROTATE_90_COUNTERCLOCKWISE: Rotate the image 90 degrees counterclockwise.
# cv2.ROTATE_180: Rotate the image 180 degrees.

rotate_image=cv.rotate(image,cv.ROTATE_180)
# cv.imshow("rotate_image",rotate_image)
# cv.waitKey(0)

#number 2

(height,weidth)=image.shape[:2]

#Define a rotation matrix to rotate the image by one's desired angle around the center.
#cv2.getRotationMatrix2D(center, angle, scale)

rotation_matrix=cv.getRotationMatrix2D((weidth//2,height//2),-45,1.0)

'''
This is a type of affine transformation. An affine transformation is transformation which preserves 
lines and parallelism. These transformation matrix are taken by warpaffine() function as parameter and 
the rotated image will be returned.
'''
rotated=cv.warpAffine(image,rotation_matrix,(height,weidth))
# cv.imshow("rotate_image",rotated)
# cv.waitKey(0)

#flipping

flip=cv.flip(image,0)   #0-->vertically flipping, 1-->horizontally flipping, -1-->both vertically and horizontally
cv.imshow("flip_image",flip)
cv.waitKey(0)