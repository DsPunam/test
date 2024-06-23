import cv2 as cv

'''
img=cv.imread("E:/python program/Open CV/Pictures/download.jpg")
width=int(img.shape[1]*0.75)
height=int(img.shape[0]*0.75)

resized_image=cv.resize(img,(width,height),interpolation=cv.INTER_LINEAR)
cv.imshow("image",resized_image)

cv.waitKey(0)
'''

capture=cv.VideoCapture("E:/python program/Open CV/Videos/(Hdvidz.in)_Dil-Kya-Kare-Jab-kisise-Kisiko-Pyar-Ho-Jaaye-Kabil-Movie-HD-Vid.mp4")
while True:
    isTrue,frame=capture.read()
    width=int(frame.shape[1]*0.75)
    height=int(frame.shape[0]*0.75)
    
    resized_video=cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)
    cv.imshow("video",resized_video)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

