import cv2 as cv 

image=cv.imread("E:/python program/Open CV/Pictures/gettyimages-157482029-612x612.jpg")
# cv.imshow("original",image)

#converting RGB image to Gray image
'''
cv2.cvtColor(src, code[, dst[, dstCn]])
gray=cv.cvtColor(image,6)   #cv.COLOR_BGR2GRAY=6   convert between RGB/BGR and grayscale
cv.imshow("gray",gray)
'''
#Blur
'''
blur=cv.GaussianBlur(image,(3,3),cv.BORDER_REPLICATE)
cv.imshow("Gaussianblur",blur)
'''

#Edge Cascade
edge=cv.Canny(image,100,125)
cv.imshow("egde",edge)

#Dialation
dilated=cv.dilate(edge,(7,7),iterations=3)
cv.imshow("dilated",dilated)

#erosion to get back to the original image
eroded=cv.erode(dilated,(3,3),iterations=3)
cv.imshow("eroded",eroded)
cv.waitKey(0)
