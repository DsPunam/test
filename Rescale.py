import cv2 as cv

'''
Choice of Interpolation Method for Resizing:

cv2.INTER_AREA: This is used when we need to shrink an image.
cv2.INTER_CUBIC: This is slow but more efficient.
cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation 
technique in OpenCV.
'''
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

'''
capture=cv.VideoCapture('E:/python program/Open CV/Videos/(Hdvidz.in)_Dil-Kya-Kare-Jab-kisise-Kisiko-Pyar-Ho-Jaaye-Kabil-Movie-HD-Vid.mp4')
while True:
    isTrue,frame=capture.read()
    resized_frame=rescale(frame)

    cv.imshow("video",frame)
    cv.imshow("video",resized_frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
'''

image=cv.imread("E:/python program/Open CV/Pictures/image.jpg")
cv.imshow("resized_image",rescale(image))

cv.waitKey(0)

'''
If you are enlarging the image, you should prefer to use INTER_LINEAR or INTER_CUBIC interpolation. If you are shrinking the image, you should prefer to use INTER_AREA interpolation.

Cubic interpolation is computationally more complex, and hence slower than linear interpolation. However, the quality of the resulting image will be higher.
'''