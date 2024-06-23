import cv2 as cv

#For reading the pictures we use imread() method in opencv
img=cv.imread('E:/python program/Open CV/Pictures/download (1).jpg')

#for displaying image we use imshow() method
#cv.imshow("Books",img)

#cv.waitKey(0)
'''waitkey() function of Python OpenCV allows users to display a window 
for given milliseconds or until any key is pressed. It takes time in milliseconds 
as a parameter and waits for the given time to destroy the window, if 0 is passed in the 
argument it waits till any key is pressed.'''

#reading videos
capture=cv.VideoCapture('E:/python program/Open CV/Videos/(Hdvidz.in)_Dil-Kya-Kare-Jab-kisise-Kisiko-Pyar-Ho-Jaaye-Kabil-Movie-HD-Vid.mp4')

while True:
    isTrue, frame=capture.read()
    cv.imshow("Video", frame)
    #print(frame.shape[1])

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()